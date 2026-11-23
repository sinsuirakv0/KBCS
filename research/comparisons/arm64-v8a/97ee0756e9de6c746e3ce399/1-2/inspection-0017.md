# v15.7.3 → v15.7.4 · 要調査の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-c64df5c8760b304ecfa0dba46643d863"></a>

### [`00bab2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab2b0.md) → [`00bab2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab2f4.md) _ZNSt6__ndk17codecvtIcc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ad0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab2b0.md#insn-00bab2c4)
- 新版 `00bab308`（命令位置の公開資料なし）

~~~diff
- 00bab2c4 ["INT_ADD", "register:40f0:8", ["const:bab2c4:8", "const:4:8"]]
- 00bab2c4 ["CALL", null, ["callee:00be1b20:8"]]
+ 00bab308 ["INT_ADD", "register:40f0:8", ["const:bab308:8", "const:4:8"]]
+ 00bab308 ["CALL", null, ["callee:00be1b20:8"]]
- 00bab2c4 bytes 03da0094
+ 00bab308 bytes 06da0094
~~~


<a id="compare-c768c4363c65418d5fa73a1c5b0f0cfb"></a>

### [`00bab4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4d0.md) → [`00bab514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab514.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4d0.md#insn-00bab4e4)
- 新版 `00bab528`（命令位置の公開資料なし）

~~~diff
- 00bab4e4 ["INT_ADD", "register:40f0:8", ["const:bab4e4:8", "const:4:8"]]
- 00bab4e4 ["CALL", null, ["callee:00be1b30:8"]]
+ 00bab528 ["INT_ADD", "register:40f0:8", ["const:bab528:8", "const:4:8"]]
+ 00bab528 ["CALL", null, ["callee:00be1b30:8"]]
- 00bab4e4 bytes 7fd90094
+ 00bab528 bytes 82d90094
~~~


<a id="compare-eeeca747c5790ab81efd930bcb5fc88c"></a>

### [`00bab4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md) → [`00bab540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab540.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1af0.md) [`00be1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b40.md) [`00be1b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5b0) · [`00bab5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5d0) · [`00bab5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab4fc.md#insn-00bab5e0)
- 新版 `00bab5f4`（命令位置の公開資料なし） · `00bab614`（命令位置の公開資料なし） · `00bab624`（命令位置の公開資料なし）

~~~diff
- 00bab5b0 ["INT_ADD", "register:40f0:8", ["const:bab5b0:8", "const:4:8"]]
- 00bab5b0 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab5f4 ["INT_ADD", "register:40f0:8", ["const:bab5f4:8", "const:4:8"]]
+ 00bab5f4 ["CALL", null, ["callee:00be1580:8"]]
- 00bab5b0 bytes e0d70094
+ 00bab5f4 bytes e3d70094
- 00bab5d0 ["INT_ADD", "register:40f0:8", ["const:bab5d0:8", "const:4:8"]]
- 00bab5d0 ["CALL", null, ["callee:00be1b40:8"]]
+ 00bab614 ["INT_ADD", "register:40f0:8", ["const:bab614:8", "const:4:8"]]
+ 00bab614 ["CALL", null, ["callee:00be1b40:8"]]
- 00bab5d0 bytes 48d90094
+ 00bab614 bytes 4bd90094
- 00bab5e0 ["INT_ADD", "register:40f0:8", ["const:bab5e0:8", "const:4:8"]]
- 00bab5e0 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab624 ["INT_ADD", "register:40f0:8", ["const:bab624:8", "const:4:8"]]
+ 00bab624 ["CALL", null, ["callee:00be1580:8"]]
- 00bab5e0 bytes d4d70094
+ 00bab624 bytes d7d70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eee0c492bc7e94bf8364c272a3018bd"></a>

### [`00bab7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md) → [`00bab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab804.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE5do_inERS1_PKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b10.md) [`00be1b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b60.md) [`00be1b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bab860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab860) · [`00bab880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab880) · [`00bab890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab7c0.md#insn-00bab890)
- 新版 `00bab8a4`（命令位置の公開資料なし） · `00bab8c4`（命令位置の公開資料なし） · `00bab8d4`（命令位置の公開資料なし）

~~~diff
- 00bab860 ["INT_ADD", "register:40f0:8", ["const:bab860:8", "const:4:8"]]
- 00bab860 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab8a4 ["INT_ADD", "register:40f0:8", ["const:bab8a4:8", "const:4:8"]]
+ 00bab8a4 ["CALL", null, ["callee:00be1580:8"]]
- 00bab860 bytes 34d70094
+ 00bab8a4 bytes 37d70094
- 00bab880 ["INT_ADD", "register:40f0:8", ["const:bab880:8", "const:4:8"]]
- 00bab880 ["CALL", null, ["callee:00be1b60:8"]]
+ 00bab8c4 ["INT_ADD", "register:40f0:8", ["const:bab8c4:8", "const:4:8"]]
+ 00bab8c4 ["CALL", null, ["callee:00be1b60:8"]]
- 00bab880 bytes a4d80094
+ 00bab8c4 bytes a7d80094
- 00bab890 ["INT_ADD", "register:40f0:8", ["const:bab890:8", "const:4:8"]]
- 00bab890 ["CALL", null, ["callee:00be1580:8"]]
+ 00bab8d4 ["INT_ADD", "register:40f0:8", ["const:bab8d4:8", "const:4:8"]]
+ 00bab8d4 ["CALL", null, ["callee:00be1580:8"]]
- 00bab890 bytes 28d70094
+ 00bab8d4 bytes 2bd70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c52527a8b393cabfcecc8e421183ffe2"></a>

### [`00baba74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md) → [`00babab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babab8.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babaa0) · [`00babab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babab8) · [`00babac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md#insn-00babac8)
- 新版 `00babae4`（命令位置の公開資料なし） · `00babafc`（命令位置の公開資料なし） · `00babb0c`（命令位置の公開資料なし）

~~~diff
- 00babaa0 ["INT_ADD", "register:40f0:8", ["const:babaa0:8", "const:4:8"]]
- 00babaa0 ["CALL", null, ["callee:00be1580:8"]]
+ 00babae4 ["INT_ADD", "register:40f0:8", ["const:babae4:8", "const:4:8"]]
+ 00babae4 ["CALL", null, ["callee:00be1580:8"]]
- 00babaa0 bytes a4d60094
+ 00babae4 bytes a7d60094
- 00babab8 ["INT_ADD", "register:40f0:8", ["const:babab8:8", "const:4:8"]]
- 00babab8 ["CALL", null, ["callee:00be1b50:8"]]
+ 00babafc ["INT_ADD", "register:40f0:8", ["const:babafc:8", "const:4:8"]]
+ 00babafc ["CALL", null, ["callee:00be1b50:8"]]
- 00babab8 bytes 12d80094
+ 00babafc bytes 15d80094
- 00babac8 ["INT_ADD", "register:40f0:8", ["const:babac8:8", "const:4:8"]]
- 00babac8 ["CALL", null, ["callee:00be1580:8"]]
+ 00babb0c ["INT_ADD", "register:40f0:8", ["const:babb0c:8", "const:4:8"]]
+ 00babb0c ["CALL", null, ["callee:00be1580:8"]]
- 00babac8 bytes 9ad60094
+ 00babb0c bytes 9dd60094
~~~


<a id="compare-54be66eef88ef0cdafe83f70687b22a6"></a>

### [`00babb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md) → [`00babb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babb98.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b30.md) [`00be1b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b80.md) [`00be1b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb70) · [`00babb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb88) · [`00babb98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md#insn-00babb98)
- 新版 `00babbb4`（命令位置の公開資料なし） · `00babbcc`（命令位置の公開資料なし） · `00babbdc`（命令位置の公開資料なし）

~~~diff
- 00babb70 ["INT_ADD", "register:40f0:8", ["const:babb70:8", "const:4:8"]]
- 00babb70 ["CALL", null, ["callee:00be1580:8"]]
+ 00babbb4 ["INT_ADD", "register:40f0:8", ["const:babbb4:8", "const:4:8"]]
+ 00babbb4 ["CALL", null, ["callee:00be1580:8"]]
- 00babb70 bytes 70d60094
+ 00babbb4 bytes 73d60094
- 00babb88 ["INT_ADD", "register:40f0:8", ["const:babb88:8", "const:4:8"]]
- 00babb88 ["CALL", null, ["callee:00be1b80:8"]]
+ 00babbcc ["INT_ADD", "register:40f0:8", ["const:babbcc:8", "const:4:8"]]
+ 00babbcc ["CALL", null, ["callee:00be1b80:8"]]
- 00babb88 bytes ead70094
+ 00babbcc bytes edd70094
- 00babb98 ["INT_ADD", "register:40f0:8", ["const:babb98:8", "const:4:8"]]
- 00babb98 ["CALL", null, ["callee:00be1580:8"]]
+ 00babbdc ["INT_ADD", "register:40f0:8", ["const:babbdc:8", "const:4:8"]]
+ 00babbdc ["CALL", null, ["callee:00be1580:8"]]
- 00babb98 bytes 66d60094
+ 00babbdc bytes 69d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d4005b406b962f9f3a3a6360f7ca48"></a>

### [`00babc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md) → [`00babc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babc68.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babc78) · [`00babc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babc90) · [`00babca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md#insn-00babca0)
- 新版 `00babcbc`（命令位置の公開資料なし） · `00babcd4`（命令位置の公開資料なし） · `00babce4`（命令位置の公開資料なし）

~~~diff
- 00babc78 ["INT_ADD", "register:40f0:8", ["const:babc78:8", "const:4:8"]]
- 00babc78 ["CALL", null, ["callee:00be1580:8"]]
+ 00babcbc ["INT_ADD", "register:40f0:8", ["const:babcbc:8", "const:4:8"]]
+ 00babcbc ["CALL", null, ["callee:00be1580:8"]]
- 00babc78 bytes 2ed60094
+ 00babcbc bytes 31d60094
- 00babc90 ["INT_ADD", "register:40f0:8", ["const:babc90:8", "const:4:8"]]
- 00babc90 ["CALL", null, ["callee:00be1ba0:8"]]
+ 00babcd4 ["INT_ADD", "register:40f0:8", ["const:babcd4:8", "const:4:8"]]
+ 00babcd4 ["CALL", null, ["callee:00be1ba0:8"]]
- 00babc90 bytes b0d70094
+ 00babcd4 bytes b3d70094
- 00babca0 ["INT_ADD", "register:40f0:8", ["const:babca0:8", "const:4:8"]]
- 00babca0 ["CALL", null, ["callee:00be1580:8"]]
+ 00babce4 ["INT_ADD", "register:40f0:8", ["const:babce4:8", "const:4:8"]]
+ 00babce4 ["CALL", null, ["callee:00be1580:8"]]
- 00babca0 bytes 24d60094
+ 00babce4 bytes 27d60094
~~~


<a id="compare-41927b256c86cc8ce71faaec2b594c50"></a>

### [`00babd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md) → [`00babd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babd60.md) _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md) [`00be1b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd38) · [`00babd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd44) · [`00babd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd1c.md#insn-00babd54)
- 新版 `00babd7c`（命令位置の公開資料なし） · `00babd88`（命令位置の公開資料なし） · `00babd98`（命令位置の公開資料なし）

~~~diff
- 00babd38 ["INT_ADD", "register:40f0:8", ["const:babd38:8", "const:4:8"]]
- 00babd38 ["CALL", null, ["callee:00be1580:8"]]
+ 00babd7c ["INT_ADD", "register:40f0:8", ["const:babd7c:8", "const:4:8"]]
+ 00babd7c ["CALL", null, ["callee:00be1580:8"]]
- 00babd38 bytes fed50094
+ 00babd7c bytes 01d60094
- 00babd44 ["INT_ADD", "register:40f0:8", ["const:babd44:8", "const:4:8"]]
- 00babd44 ["CALL", null, ["callee:00be1b90:8"]]
+ 00babd88 ["INT_ADD", "register:40f0:8", ["const:babd88:8", "const:4:8"]]
+ 00babd88 ["CALL", null, ["callee:00be1b90:8"]]
- 00babd44 bytes 7fd70094
+ 00babd88 bytes 82d70094
- 00babd54 ["INT_ADD", "register:40f0:8", ["const:babd54:8", "const:4:8"]]
- 00babd54 ["CALL", null, ["callee:00be1580:8"]]
+ 00babd98 ["INT_ADD", "register:40f0:8", ["const:babd98:8", "const:4:8"]]
+ 00babd98 ["CALL", null, ["callee:00be1580:8"]]
- 00babd54 bytes f7d50094
+ 00babd98 bytes fad50094
~~~


<a id="compare-1315d20329ec41e7b6d92fd36e49f453"></a>

### [`00babd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd94.md) → [`00babdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md) _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babd94.md#insn-00babda8)
- 新版 `00babdec`（命令位置の公開資料なし）

~~~diff
- 00babda8 ["INT_ADD", "register:40f0:8", ["const:babda8:8", "const:4:8"]]
- 00babda8 ["CALL", null, ["callee:00be1bb0:8"]]
+ 00babdec ["INT_ADD", "register:40f0:8", ["const:babdec:8", "const:4:8"]]
+ 00babdec ["CALL", null, ["callee:00be1bb0:8"]]
- 00babda8 bytes 6ed70094
+ 00babdec bytes 71d70094
~~~


<a id="compare-27705d2c1f1d6ba37378baedae0d382e"></a>

### [`00babdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babdc0.md) → [`00babe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe04.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00babe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babdc0.md#insn-00babe04)
- 新版 `00babe48`（命令位置の公開資料なし）

~~~diff
- 00babe04 ["INT_ADD", "register:40f0:8", ["const:babe04:8", "const:4:8"]]
- 00babe04 ["CALL", null, ["callee:00babe6c:8"]]
+ 00babe48 ["INT_ADD", "register:40f0:8", ["const:babe48:8", "const:4:8"]]
+ 00babe48 ["CALL", null, ["callee:00babe6c:8"]]
- 00babe04 bytes 09000094
+ 00babe48 bytes 09000094
~~~


<a id="compare-8160602b5c463484e7cf8793e420da20"></a>

### [`00bac084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac084.md) → [`00bac0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac0c8.md) _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac084.md#insn-00bac0c8)
- 新版 `00bac10c`（命令位置の公開資料なし）

~~~diff
- 00bac0c8 ["INT_ADD", "register:40f0:8", ["const:bac0c8:8", "const:4:8"]]
- 00bac0c8 ["CALL", null, ["callee:00bac130:8"]]
+ 00bac10c ["INT_ADD", "register:40f0:8", ["const:bac10c:8", "const:4:8"]]
+ 00bac10c ["CALL", null, ["callee:00bac130:8"]]
- 00bac0c8 bytes 09000094
+ 00bac10c bytes 09000094
~~~


<a id="compare-7fcb4095d028c83eccc6874b85806be1"></a>

### [`00bac5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5d0.md) → [`00bac614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac614.md) _ZNSt6__ndk17codecvtIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5d0.md#insn-00bac5e4)
- 新版 `00bac628`（命令位置の公開資料なし）

~~~diff
- 00bac5e4 ["INT_ADD", "register:40f0:8", ["const:bac5e4:8", "const:4:8"]]
- 00bac5e4 ["CALL", null, ["callee:00be1bc0:8"]]
+ 00bac628 ["INT_ADD", "register:40f0:8", ["const:bac628:8", "const:4:8"]]
+ 00bac628 ["CALL", null, ["callee:00be1bc0:8"]]
- 00bac5e4 bytes 63d50094
+ 00bac628 bytes 66d50094
~~~


<a id="compare-d4d50d335b59a7fcafc5cc8cfddc4359"></a>

### [`00bac5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5fc.md) → [`00bac640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac640.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE6do_outERS1_PKDsS5_RS5_PDuS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac5fc.md#insn-00bac640)
- 新版 `00bac684`（命令位置の公開資料なし）

~~~diff
- 00bac640 ["INT_ADD", "register:40f0:8", ["const:bac640:8", "const:4:8"]]
- 00bac640 ["CALL", null, ["callee:00babe6c:8"]]
+ 00bac684 ["INT_ADD", "register:40f0:8", ["const:bac684:8", "const:4:8"]]
+ 00bac684 ["CALL", null, ["callee:00babe6c:8"]]
- 00bac640 bytes fafdff97
+ 00bac684 bytes fafdff97
~~~


<a id="compare-3f7554049cd659499fad5641388c0ad0"></a>

### [`00bac664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac664.md) → [`00bac6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac6a8.md) _ZNKSt6__ndk17codecvtIDsDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac664.md#insn-00bac6a8)
- 新版 `00bac6ec`（命令位置の公開資料なし）

~~~diff
- 00bac6a8 ["INT_ADD", "register:40f0:8", ["const:bac6a8:8", "const:4:8"]]
- 00bac6a8 ["CALL", null, ["callee:00bac130:8"]]
+ 00bac6ec ["INT_ADD", "register:40f0:8", ["const:bac6ec:8", "const:4:8"]]
+ 00bac6ec ["CALL", null, ["callee:00bac130:8"]]
- 00bac6a8 bytes 91feff97
+ 00bac6ec bytes 91feff97
~~~


<a id="compare-6d466a65866bdf3dc7e8f9a78a8cb974"></a>

### [`00bac71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac71c.md) → [`00bac760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac760.md) _ZNSt6__ndk17codecvtIDic9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bac730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac71c.md#insn-00bac730)
- 新版 `00bac774`（命令位置の公開資料なし）

~~~diff
- 00bac730 ["INT_ADD", "register:40f0:8", ["const:bac730:8", "const:4:8"]]
- 00bac730 ["CALL", null, ["callee:00be1bd0:8"]]
+ 00bac774 ["INT_ADD", "register:40f0:8", ["const:bac774:8", "const:4:8"]]
+ 00bac774 ["CALL", null, ["callee:00be1bd0:8"]]
- 00bac730 bytes 14d50094
+ 00bac774 bytes 17d50094
~~~


<a id="compare-4b880827b1d44e48eaf343efb8046057"></a>

### [`00bac9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac9f8.md) → [`00baca3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00baca3c.md) _ZNKSt6__ndk17codecvtIDic9mbstate_tE5do_inERS1_PKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac9f8.md#insn-00baca3c)
- 新版 `00baca80`（命令位置の公開資料なし）

~~~diff
- 00baca3c ["INT_ADD", "register:40f0:8", ["const:baca3c:8", "const:4:8"]]
- 00baca3c ["CALL", null, ["callee:00bacaa4:8"]]
+ 00baca80 ["INT_ADD", "register:40f0:8", ["const:baca80:8", "const:4:8"]]
+ 00baca80 ["CALL", null, ["callee:00bacaa4:8"]]
- 00baca3c bytes 09000094
+ 00baca80 bytes 09000094
~~~


<a id="compare-0daa33b754e063196d044e3e6bba0661"></a>

### [`00baced8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baced8.md) → [`00bacf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacf1c.md) _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1b90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baceec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baced8.md#insn-00baceec)
- 新版 `00bacf30`（命令位置の公開資料なし）

~~~diff
- 00baceec ["INT_ADD", "register:40f0:8", ["const:baceec:8", "const:4:8"]]
- 00baceec ["CALL", null, ["callee:00be1be0:8"]]
+ 00bacf30 ["INT_ADD", "register:40f0:8", ["const:bacf30:8", "const:4:8"]]
+ 00bacf30 ["CALL", null, ["callee:00be1be0:8"]]
- 00baceec bytes 29d30094
+ 00bacf30 bytes 2cd30094
~~~


<a id="compare-5b8bf427f6a49c1b387506d52c0fc71e"></a>

### [`00bad02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad02c.md) → [`00bad070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad070.md) _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE5do_inERS1_PKDuS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad02c.md#insn-00bad070)
- 新版 `00bad0b4`（命令位置の公開資料なし）

~~~diff
- 00bad070 ["INT_ADD", "register:40f0:8", ["const:bad070:8", "const:4:8"]]
- 00bad070 ["CALL", null, ["callee:00bacaa4:8"]]
+ 00bad0b4 ["INT_ADD", "register:40f0:8", ["const:bad0b4:8", "const:4:8"]]
+ 00bad0b4 ["CALL", null, ["callee:00bacaa4:8"]]
- 00bad070 bytes 7cfeff97
+ 00bad0b4 bytes 7cfeff97
~~~


<a id="compare-041a289d14b6e7538c862e7d9e5cef4b"></a>

### [`00bad0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad0e4.md) → [`00bad128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad128.md) _ZNKSt6__ndk114__codecvt_utf8IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac870.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac8b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad0e4.md#insn-00bad130)
- 新版 `00bad174`（命令位置の公開資料なし）

~~~diff
- 00bad130 ["INT_ADD", "register:40f0:8", ["const:bad130:8", "const:4:8"]]
- 00bad130 ["CALL", null, ["callee:00bac8b4:8"]]
+ 00bad174 ["INT_ADD", "register:40f0:8", ["const:bad174:8", "const:4:8"]]
+ 00bad174 ["CALL", null, ["callee:00bac8b4:8"]]
- 00bad130 bytes d0fdff97
+ 00bad174 bytes d0fdff97
~~~


<a id="compare-de4cac94643da60915fd7bdc2aed1138"></a>

### [`00bad154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad154.md) → [`00bad198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad198.md) _ZNKSt6__ndk114__codecvt_utf8IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad154.md#insn-00bad1a0)
- 新版 `00bad1e4`（命令位置の公開資料なし）

~~~diff
- 00bad1a0 ["INT_ADD", "register:40f0:8", ["const:bad1a0:8", "const:4:8"]]
- 00bad1a0 ["CALL", null, ["callee:00bacaa4:8"]]
+ 00bad1e4 ["INT_ADD", "register:40f0:8", ["const:bad1e4:8", "const:4:8"]]
+ 00bad1e4 ["CALL", null, ["callee:00bacaa4:8"]]
- 00bad1a0 bytes 30feff97
+ 00bad1e4 bytes 30feff97
~~~


<a id="compare-6c56814a96cf4ffb3151b3ce581be97a"></a>

### [`00bad674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad674.md) → [`00bad6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad6b8.md) _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac870.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac8b4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad674.md#insn-00bad6c0)
- 新版 `00bad704`（命令位置の公開資料なし）

~~~diff
- 00bad6c0 ["INT_ADD", "register:40f0:8", ["const:bad6c0:8", "const:4:8"]]
- 00bad6c0 ["CALL", null, ["callee:00bac8b4:8"]]
+ 00bad704 ["INT_ADD", "register:40f0:8", ["const:bad704:8", "const:4:8"]]
+ 00bad704 ["CALL", null, ["callee:00bac8b4:8"]]
- 00bad6c0 bytes 6cfcff97
+ 00bad704 bytes 6cfcff97
~~~


<a id="compare-eff99a4d7fee29aff2e4fb22e6826a68"></a>

### [`00bad6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad6e4.md) → [`00bad728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad728.md) _ZNKSt6__ndk114__codecvt_utf8IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00baca60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad6e4.md#insn-00bad730)
- 新版 `00bad774`（命令位置の公開資料なし）

~~~diff
- 00bad730 ["INT_ADD", "register:40f0:8", ["const:bad730:8", "const:4:8"]]
- 00bad730 ["CALL", null, ["callee:00bacaa4:8"]]
+ 00bad774 ["INT_ADD", "register:40f0:8", ["const:bad774:8", "const:4:8"]]
+ 00bad774 ["CALL", null, ["callee:00bacaa4:8"]]
- 00bad730 bytes ccfcff97
+ 00bad774 bytes ccfcff97
~~~


<a id="compare-cba090750b98e8291bdd1461b0d050e1"></a>

### [`00bae688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae688.md) → [`00bae6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae6cc.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae6f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae73c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae688.md#insn-00bae6d4)
- 新版 `00bae718`（命令位置の公開資料なし）

~~~diff
- 00bae6d4 ["INT_ADD", "register:40f0:8", ["const:bae6d4:8", "const:4:8"]]
- 00bae6d4 ["CALL", null, ["callee:00bae73c:8"]]
+ 00bae718 ["INT_ADD", "register:40f0:8", ["const:bae718:8", "const:4:8"]]
+ 00bae718 ["CALL", null, ["callee:00bae73c:8"]]
- 00bae6d4 bytes 09000094
+ 00bae718 bytes 09000094
~~~


<a id="compare-90bbf0d7ceb02aae11494a78616bd6f6"></a>

### [`00bae920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae920.md) → [`00bae964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae964.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae990.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae9d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae920.md#insn-00bae96c)
- 新版 `00bae9b0`（命令位置の公開資料なし）

~~~diff
- 00bae96c ["INT_ADD", "register:40f0:8", ["const:bae96c:8", "const:4:8"]]
- 00bae96c ["CALL", null, ["callee:00bae9d4:8"]]
+ 00bae9b0 ["INT_ADD", "register:40f0:8", ["const:bae9b0:8", "const:4:8"]]
+ 00bae9b0 ["CALL", null, ["callee:00bae9d4:8"]]
- 00bae96c bytes 09000094
+ 00bae9b0 bytes 09000094
~~~


<a id="compare-9a631378855808fdf319a89a83878455"></a>

### [`00baec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md) → [`00baecc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baecc4.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babe28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00babe6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe6c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baeccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baec80.md#insn-00baeccc)
- 新版 `00baed10`（命令位置の公開資料なし）

~~~diff
- 00baeccc ["INT_ADD", "register:40f0:8", ["const:baeccc:8", "const:4:8"]]
- 00baeccc ["CALL", null, ["callee:00babe6c:8"]]
+ 00baed10 ["INT_ADD", "register:40f0:8", ["const:baed10:8", "const:4:8"]]
+ 00baed10 ["CALL", null, ["callee:00babe6c:8"]]
- 00baeccc bytes 57f4ff97
+ 00baed10 bytes 57f4ff97
~~~


<a id="compare-fb456dbad5e44024fcfa0c35e7d0dac3"></a>

### [`00baecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baecf0.md) → [`00baed34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baed34.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac0ec.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bac130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baed3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baecf0.md#insn-00baed3c)
- 新版 `00baed80`（命令位置の公開資料なし）

~~~diff
- 00baed3c ["INT_ADD", "register:40f0:8", ["const:baed3c:8", "const:4:8"]]
- 00baed3c ["CALL", null, ["callee:00bac130:8"]]
+ 00baed80 ["INT_ADD", "register:40f0:8", ["const:baed80:8", "const:4:8"]]
+ 00baed80 ["CALL", null, ["callee:00bac130:8"]]
- 00baed3c bytes ecf4ff97
+ 00baed80 bytes ecf4ff97
~~~


<a id="compare-a4542958aa72bca5627f27a847ad51e4"></a>

### [`00baedc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baedc4.md) → [`00baee08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee08.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae6f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae73c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baee10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baedc4.md#insn-00baee10)
- 新版 `00baee54`（命令位置の公開資料なし）

~~~diff
- 00baee10 ["INT_ADD", "register:40f0:8", ["const:baee10:8", "const:4:8"]]
- 00baee10 ["CALL", null, ["callee:00bae73c:8"]]
+ 00baee54 ["INT_ADD", "register:40f0:8", ["const:baee54:8", "const:4:8"]]
+ 00baee54 ["CALL", null, ["callee:00bae73c:8"]]
- 00baee10 bytes 3afeff97
+ 00baee54 bytes 3afeff97
~~~


<a id="compare-59510c0aae0271b24cb46d515d5e7508"></a>

### [`00baee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baee34.md) → [`00baee78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee78.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00bae990.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bae9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae9d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baee80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baee34.md#insn-00baee80)
- 新版 `00baeec4`（命令位置の公開資料なし）

~~~diff
- 00baee80 ["INT_ADD", "register:40f0:8", ["const:baee80:8", "const:4:8"]]
- 00baee80 ["CALL", null, ["callee:00bae9d4:8"]]
+ 00baeec4 ["INT_ADD", "register:40f0:8", ["const:baeec4:8", "const:4:8"]]
+ 00baeec4 ["CALL", null, ["callee:00bae9d4:8"]]
- 00baee80 bytes c4feff97
+ 00baeec4 bytes c4feff97
~~~


<a id="compare-97cc70bc22ebcc3ac3bd30d3306acfd9"></a>

### [`00baef08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef08.md) → [`00baef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef4c.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ba0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baef1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef08.md#insn-00baef1c)
- 新版 `00baef60`（命令位置の公開資料なし）

~~~diff
- 00baef1c ["INT_ADD", "register:40f0:8", ["const:baef1c:8", "const:4:8"]]
- 00baef1c ["CALL", null, ["callee:00be1bf0:8"]]
+ 00baef60 ["INT_ADD", "register:40f0:8", ["const:baef60:8", "const:4:8"]]
+ 00baef60 ["CALL", null, ["callee:00be1bf0:8"]]
- 00baef1c bytes 21cb0094
+ 00baef60 bytes 24cb0094
~~~


<a id="compare-06b72a8933b5bba5d0112f64e5285081"></a>

### [`00baef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef34.md) → [`00baef78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef78.md) _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baef48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef34.md#insn-00baef48)
- 新版 `00baef8c`（命令位置の公開資料なし）

~~~diff
- 00baef48 ["INT_ADD", "register:40f0:8", ["const:baef48:8", "const:4:8"]]
- 00baef48 ["CALL", null, ["callee:00be1c00:8"]]
+ 00baef8c ["INT_ADD", "register:40f0:8", ["const:baef8c:8", "const:4:8"]]
+ 00baef8c ["CALL", null, ["callee:00be1c00:8"]]
- 00baef48 bytes 1acb0094
+ 00baef8c bytes 1dcb0094
~~~


<a id="compare-eda7f43ff1cb97f0e61663c075c3e653"></a>

### [`00baef60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef60.md) → [`00baefa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baefa4.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baef74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef60.md#insn-00baef74)
- 新版 `00baefb8`（命令位置の公開資料なし）

~~~diff
- 00baef74 ["INT_ADD", "register:40f0:8", ["const:baef74:8", "const:4:8"]]
- 00baef74 ["CALL", null, ["callee:00be1c10:8"]]
+ 00baefb8 ["INT_ADD", "register:40f0:8", ["const:baefb8:8", "const:4:8"]]
+ 00baefb8 ["CALL", null, ["callee:00be1c10:8"]]
- 00baef74 bytes 13cb0094
+ 00baefb8 bytes 16cb0094
~~~


<a id="compare-0c31384379fae309822bb9d859da2f67"></a>

### [`00baef8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef8c.md) → [`00baefd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baefd0.md) _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef8c.md#insn-00baefa0)
- 新版 `00baefe4`（命令位置の公開資料なし）

~~~diff
- 00baefa0 ["INT_ADD", "register:40f0:8", ["const:baefa0:8", "const:4:8"]]
- 00baefa0 ["CALL", null, ["callee:00be1c20:8"]]
+ 00baefe4 ["INT_ADD", "register:40f0:8", ["const:baefe4:8", "const:4:8"]]
+ 00baefe4 ["CALL", null, ["callee:00be1c20:8"]]
- 00baefa0 bytes 0ccb0094
+ 00baefe4 bytes 0fcb0094
~~~


<a id="compare-140563288dea158a2d5e3d7004246aa0"></a>

### [`00baf064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf064.md) → [`00baf0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf0a8.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1bf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf064.md#insn-00baf078)
- 新版 `00baf0bc`（命令位置の公開資料なし）

~~~diff
- 00baf078 ["INT_ADD", "register:40f0:8", ["const:baf078:8", "const:4:8"]]
- 00baf078 ["CALL", null, ["callee:00be1c40:8"]]
+ 00baf0bc ["INT_ADD", "register:40f0:8", ["const:baf0bc:8", "const:4:8"]]
+ 00baf0bc ["CALL", null, ["callee:00be1c40:8"]]
- 00baf078 bytes deca0094
+ 00baf0bc bytes e1ca0094
~~~


<a id="compare-3c1335488af55e65f40caafa9c34bf28"></a>

### [`00baf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf0e0.md) → [`00baf124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf124.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf0e0.md#insn-00baf0f4)
- 新版 `00baf138`（命令位置の公開資料なし）

~~~diff
- 00baf0f4 ["INT_ADD", "register:40f0:8", ["const:baf0f4:8", "const:4:8"]]
- 00baf0f4 ["CALL", null, ["callee:00be1c60:8"]]
+ 00baf138 ["INT_ADD", "register:40f0:8", ["const:baf138:8", "const:4:8"]]
+ 00baf138 ["CALL", null, ["callee:00be1c60:8"]]
- 00baf0f4 bytes c7ca0094
+ 00baf138 bytes caca0094
~~~


<a id="compare-c058a6cb19212a9c8aba69ac5b3fc94c"></a>

### [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) → [`00baf224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf224.md) FUN_00baf224

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00bb13a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md) [`00bb14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md) [`00bb15bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md) [`00bb16c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)
- 新版 呼出元 4件 [`00bb13e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb13e8.md) [`00bb14f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb14f4.md) [`00bb1600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1600.md) [`00bb170c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb170c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md#insn-00baf200) · [`00baf254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md#insn-00baf254) · [`00baf274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md#insn-00baf274)
- 新版 `00baf244`（命令位置の公開資料なし） · `00baf298`（命令位置の公開資料なし） · `00baf2b8`（命令位置の公開資料なし）

~~~diff
- 00baf200 ["INT_ADD", "register:40f0:8", ["const:baf200:8", "const:4:8"]]
- 00baf200 ["CALL", null, ["callee:00be1010:8"]]
+ 00baf244 ["INT_ADD", "register:40f0:8", ["const:baf244:8", "const:4:8"]]
+ 00baf244 ["CALL", null, ["callee:00be1010:8"]]
- 00baf200 bytes 70c70094
+ 00baf244 bytes 73c70094
- 00baf254 ["INT_ADD", "register:40f0:8", ["const:baf254:8", "const:4:8"]]
- 00baf254 ["CALL", null, ["callee:00bdb040:8"]]
+ 00baf298 ["INT_ADD", "register:40f0:8", ["const:baf298:8", "const:4:8"]]
+ 00baf298 ["CALL", null, ["callee:00bdb040:8"]]
- 00baf254 bytes 67af0094
+ 00baf298 bytes 6aaf0094
- 00baf274 ["INT_ADD", "register:40f0:8", ["const:baf274:8", "const:4:8"]]
- 00baf274 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00baf2b8 ["INT_ADD", "register:40f0:8", ["const:baf2b8:8", "const:4:8"]]
+ 00baf2b8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00baf274 bytes 8baf0094
+ 00baf2b8 bytes 8eaf0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d67f9bc48d986e2f044dffa35031155"></a>

### [`00baf2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf2c0.md) → [`00baf304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf304.md) _ZNKSt6__ndk18numpunctIwE12do_falsenameEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf2c0.md#insn-00baf2d8)
- 新版 `00baf31c`（命令位置の公開資料なし）

~~~diff
- 00baf2d8 ["INT_ADD", "register:40f0:8", ["const:baf2d8:8", "const:4:8"]]
- 00baf2d8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00baf31c ["INT_ADD", "register:40f0:8", ["const:baf31c:8", "const:4:8"]]
+ 00baf31c ["CALL", null, ["callee:00bdb040:8"]]
- 00baf2d8 bytes 46af0094
+ 00baf31c bytes 49af0094
~~~


<a id="compare-378ef66a7ec1c7b48e3f2aa627b718a3"></a>

### [`00baf6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6b8.md) → [`00baf6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf6fc.md) _ZNSt6__ndk115numpunct_bynameIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6b8.md#insn-00baf6cc)
- 新版 `00baf710`（命令位置の公開資料なし）

~~~diff
- 00baf6cc ["INT_ADD", "register:40f0:8", ["const:baf6cc:8", "const:4:8"]]
- 00baf6cc ["CALL", null, ["callee:00be1c90:8"]]
+ 00baf710 ["INT_ADD", "register:40f0:8", ["const:baf710:8", "const:4:8"]]
+ 00baf710 ["CALL", null, ["callee:00be1c90:8"]]
- 00baf6cc bytes 5dc90094
+ 00baf710 bytes 60c90094
~~~


<a id="compare-a3fbad7a702fe4bf03eef046050ee6a8"></a>

### [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md) → [`00baf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md) FUN_00baf728

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00baf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md) [`00bb68cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md) [`00bb75c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md) · 呼出先 1件 [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 3件 [`00baf7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf7b4.md) [`00bb6910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6910.md) [`00bb760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb760c.md) · 呼出先 1件 [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baf6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md#insn-00baf6f8)
- 新版 `00baf73c`（命令位置の公開資料なし）

~~~diff
- 00baf6f8 ["INT_ADD", "register:40f0:8", ["const:baf6f8:8", "const:4:8"]]
- 00baf6f8 ["CALL", null, ["callee:00be1930:8"]]
+ 00baf73c ["INT_ADD", "register:40f0:8", ["const:baf73c:8", "const:4:8"]]
+ 00baf73c ["CALL", null, ["callee:00be1930:8"]]
- 00baf6f8 bytes 7ac80094
+ 00baf73c bytes 7dc80094
~~~


<a id="compare-65ca6880019db13e8342bc7e3ce29cdd"></a>

### [`00baf9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf9f0.md) → [`00bafa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa34.md) _ZNSt6__ndk115numpunct_bynameIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bafa04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf9f0.md#insn-00bafa04)
- 新版 `00bafa48`（命令位置の公開資料なし）

~~~diff
- 00bafa04 ["INT_ADD", "register:40f0:8", ["const:bafa04:8", "const:4:8"]]
- 00bafa04 ["CALL", null, ["callee:00be1cb0:8"]]
+ 00bafa48 ["INT_ADD", "register:40f0:8", ["const:bafa48:8", "const:4:8"]]
+ 00bafa48 ["CALL", null, ["callee:00be1cb0:8"]]
- 00bafa04 bytes 97c80094
+ 00bafa48 bytes 9ac80094
~~~


<a id="compare-8a7e0553364d38b2893c505cab3d2b39"></a>

### [`00bb18cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18cc.md) → [`00bb1910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1910.md) _ZNSt6__ndk110__time_getD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be1c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c90.md) · 呼出先 1件 [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 1件 [`00be1ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ce0.md) · 呼出先 1件 [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb18dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18cc.md#insn-00bb18dc)
- 新版 `00bb1920`（命令位置の公開資料なし）

~~~diff
- 00bb18dc ["INT_ADD", "register:40f0:8", ["const:bb18dc:8", "const:4:8"]]
- 00bb18dc ["CALL", null, ["callee:00be1930:8"]]
+ 00bb1920 ["INT_ADD", "register:40f0:8", ["const:bb1920:8", "const:4:8"]]
+ 00bb1920 ["CALL", null, ["callee:00be1930:8"]]
- 00bb18dc bytes 01c00094
+ 00bb1920 bytes 04c00094
~~~


<a id="compare-dff7b52f419a81554cc8781066891780"></a>

### [`00bb18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18f0.md) → [`00bb1934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1934.md) _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ca0.md) · 呼出先 3件 [`00bb1ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1ed8.md) [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md) [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md)
- 新版 呼出元 1件 [`00be1cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cf0.md) · 呼出先 3件 [`00bb1f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1f1c.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md) [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18f0.md#insn-00bb1978) · [`00bb19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18f0.md#insn-00bb19f4) · [`00bb1a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18f0.md#insn-00bb1a0c)
- 新版 `00bb19bc`（命令位置の公開資料なし） · `00bb1a38`（命令位置の公開資料なし） · `00bb1a50`（命令位置の公開資料なし）

~~~diff
- 00bb1978 ["INT_ADD", "register:40f0:8", ["const:bb1978:8", "const:4:8"]]
- 00bb1978 ["CALL", null, ["callee:00be1670:8"]]
+ 00bb19bc ["INT_ADD", "register:40f0:8", ["const:bb19bc:8", "const:4:8"]]
+ 00bb19bc ["CALL", null, ["callee:00be1670:8"]]
- 00bb1978 bytes 2abf0094
+ 00bb19bc bytes 2dbf0094
- 00bb19f4 ["INT_ADD", "register:40f0:8", ["const:bb19f4:8", "const:4:8"]]
- 00bb19f4 ["CALL", null, ["callee:00bb1f1c:8"]]
+ 00bb1a38 ["INT_ADD", "register:40f0:8", ["const:bb1a38:8", "const:4:8"]]
+ 00bb1a38 ["CALL", null, ["callee:00bb1f1c:8"]]
- 00bb19f4 bytes 39010094
+ 00bb1a38 bytes 39010094
- 00bb1a0c ["INT_ADD", "register:40f0:8", ["const:bb1a0c:8", "const:4:8"]]
- 00bb1a0c ["CALL", null, ["callee:00bdb7b0:8"]]
+ 00bb1a50 ["INT_ADD", "register:40f0:8", ["const:bb1a50:8", "const:4:8"]]
+ 00bb1a50 ["CALL", null, ["callee:00bdb7b0:8"]]
- 00bb1a0c bytes 55a70094
+ 00bb1a50 bytes 58a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10b199588300cf1e1aa67d207f9abb2"></a>

### [`00bb1ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1ed8.md) → [`00bb1f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1f1c.md) FUN_00bb1f1c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bb18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb18f0.md) · 呼出先 3件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md)
- 新版 呼出元 1件 [`00bb1934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1934.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb1f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1ed8.md#insn-00bb1f38) · [`00bb1f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1ed8.md#insn-00bb1f48) · [`00bb1fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1ed8.md#insn-00bb1fdc)
- 新版 `00bb1f7c`（命令位置の公開資料なし） · `00bb1f8c`（命令位置の公開資料なし） · `00bb2020`（命令位置の公開資料なし）

~~~diff
- 00bb1f38 ["INT_ADD", "register:40f0:8", ["const:bb1f38:8", "const:4:8"]]
- 00bb1f38 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bb1f7c ["INT_ADD", "register:40f0:8", ["const:bb1f7c:8", "const:4:8"]]
+ 00bb1f7c ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bb1f38 bytes 92ac0094
+ 00bb1f7c bytes 95ac0094
- 00bb1f48 ["INT_ADD", "register:40f0:8", ["const:bb1f48:8", "const:4:8"]]
- 00bb1f48 ["CALL", null, ["callee:00be0f80:8"]]
+ 00bb1f8c ["INT_ADD", "register:40f0:8", ["const:bb1f8c:8", "const:4:8"]]
+ 00bb1f8c ["CALL", null, ["callee:00be0f80:8"]]
- 00bb1f48 bytes fabb0094
+ 00bb1f8c bytes fdbb0094
- 00bb1fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1fdc ["INT_ADD", "register:40f0:8", ["const:bb1fdc:8", "const:4:8"]]
- 00bb1fdc ["CALLIND", null, ["register:0:8"]]
+ 00bb2020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb2020 ["INT_ADD", "register:40f0:8", ["const:bb2020:8", "const:4:8"]]
+ 00bb2020 ["CALLIND", null, ["register:0:8"]]
- 00bb1fdc bytes 00013fd6
+ 00bb2020 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcf5625074ba52e74bd1511b6c9a36cb"></a>

### [`00bb21e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb2/00bb21e8.md) → [`00bb222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb2/00bb222c.md) _ZNSt6__ndk118__time_get_storageIwE9__analyzeEcRKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cb0.md) · 呼出先 8件 [`00bb3890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3890.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be1d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d00.md) · 呼出先 8件 [`00bb38d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb38d4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb226c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb2/00bb21e8.md#insn-00bb226c) · [`00bb2278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb2/00bb21e8.md#insn-00bb2278) · [`00bb2294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb2/00bb21e8.md#insn-00bb2294)
- 新版 `00bb22b0`（命令位置の公開資料なし） · `00bb22bc`（命令位置の公開資料なし） · `00bb22d8`（命令位置の公開資料なし）

~~~diff
- 00bb226c ["INT_ADD", "register:40f0:8", ["const:bb226c:8", "const:4:8"]]
- 00bb226c ["CALL", null, ["callee:00be1670:8"]]
+ 00bb22b0 ["INT_ADD", "register:40f0:8", ["const:bb22b0:8", "const:4:8"]]
+ 00bb22b0 ["CALL", null, ["callee:00be1670:8"]]
- 00bb226c bytes edbc0094
+ 00bb22b0 bytes f0bc0094
- 00bb2278 ["INT_ADD", "register:40f0:8", ["const:bb2278:8", "const:4:8"]]
- 00bb2278 ["CALL", null, ["callee:00be1580:8"]]
+ 00bb22bc ["INT_ADD", "register:40f0:8", ["const:bb22bc:8", "const:4:8"]]
+ 00bb22bc ["CALL", null, ["callee:00be1580:8"]]
- 00bb2278 bytes aebc0094
+ 00bb22bc bytes b1bc0094
- 00bb2294 ["INT_ADD", "register:40f0:8", ["const:bb2294:8", "const:4:8"]]
- 00bb2294 ["CALL", null, ["callee:00be1690:8"]]
+ 00bb22d8 ["INT_ADD", "register:40f0:8", ["const:bb22d8:8", "const:4:8"]]
+ 00bb22d8 ["CALL", null, ["callee:00be1690:8"]]
- 00bb2294 bytes ebbc0094
+ 00bb22d8 bytes eebc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c7e3be99125a508311be6a09c671898"></a>

### [`00bb3890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3890.md) → [`00bb38d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb38d4.md) FUN_00bb38d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bb21e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb2/00bb21e8.md) · 呼出先 3件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md)
- 新版 呼出元 1件 [`00bb222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb2/00bb222c.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb38f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3890.md#insn-00bb38f0) · [`00bb3900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3890.md#insn-00bb3900) · [`00bb39a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3890.md#insn-00bb39a8)
- 新版 `00bb3934`（命令位置の公開資料なし） · `00bb3944`（命令位置の公開資料なし） · `00bb39ec`（命令位置の公開資料なし）

~~~diff
- 00bb38f0 ["INT_ADD", "register:40f0:8", ["const:bb38f0:8", "const:4:8"]]
- 00bb38f0 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00bb3934 ["INT_ADD", "register:40f0:8", ["const:bb3934:8", "const:4:8"]]
+ 00bb3934 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00bb38f0 bytes 24a60094
+ 00bb3934 bytes 27a60094
- 00bb3900 ["INT_ADD", "register:40f0:8", ["const:bb3900:8", "const:4:8"]]
- 00bb3900 ["CALL", null, ["callee:00be0f80:8"]]
+ 00bb3944 ["INT_ADD", "register:40f0:8", ["const:bb3944:8", "const:4:8"]]
+ 00bb3944 ["CALL", null, ["callee:00be0f80:8"]]
- 00bb3900 bytes 8cb50094
+ 00bb3944 bytes 8fb50094
- 00bb39a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb39a8 ["INT_ADD", "register:40f0:8", ["const:bb39a8:8", "const:4:8"]]
- 00bb39a8 ["CALLIND", null, ["register:0:8"]]
+ 00bb39ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb39ec ["INT_ADD", "register:40f0:8", ["const:bb39ec:8", "const:4:8"]]
+ 00bb39ec ["CALLIND", null, ["register:0:8"]]
- 00bb39a8 bytes 00013fd6
+ 00bb39ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba0e64f0e001b03f4ef130bb193658d"></a>

### [`00bb5fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5fb8.md) → [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) FUN_00bb5ffc

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bb5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md) [`00bb64e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md) · 呼出先 4件 [`00bb9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md) [`00be0f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f90.md)
- 新版 呼出元 2件 [`00bb5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5c14.md) [`00bb6528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6528.md) · 呼出先 4件 [`00bb9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md) [`00be0fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb6068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5fb8.md#insn-00bb6068) · [`00bb63c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5fb8.md#insn-00bb63c8)
- 新版 `00bb60ac`（命令位置の公開資料なし） · `00bb640c`（命令位置の公開資料なし）

~~~diff
- 00bb6068 ["INT_ADD", "register:40f0:8", ["const:bb6068:8", "const:4:8"]]
- 00bb6068 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bb60ac ["INT_ADD", "register:40f0:8", ["const:bb60ac:8", "const:4:8"]]
+ 00bb60ac ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bb6068 bytes 0e940094
+ 00bb60ac bytes 11940094
- 00bb63c8 ["INT_ADD", "register:40f0:8", ["const:bb63c8:8", "const:4:8"]]
- 00bb63c8 ["CALL", null, ["callee:00be0fe0:8"]]
+ 00bb640c ["INT_ADD", "register:40f0:8", ["const:bb640c:8", "const:4:8"]]
+ 00bb640c ["CALL", null, ["callee:00be0fe0:8"]]
- 00bb63c8 bytes f2aa0094
+ 00bb640c bytes f5aa0094
~~~


<a id="compare-f0c9d99df00b1827ae2b7f35f276d138"></a>

### [`00bb7080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7080.md) → [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) FUN_00bb70c4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bb68cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md) [`00bb75c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md) · 呼出先 4件 [`00bb925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fd0.md) [`00be0ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ff0.md)
- 新版 呼出元 2件 [`00bb6910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6910.md) [`00bb760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb760c.md) · 呼出先 4件 [`00bb92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1020.md) [`00be1040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7080.md#insn-00bb7138) · [`00bb74a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7080.md#insn-00bb74a8)
- 新版 `00bb717c`（命令位置の公開資料なし） · `00bb74ec`（命令位置の公開資料なし）

~~~diff
- 00bb7138 ["INT_ADD", "register:40f0:8", ["const:bb7138:8", "const:4:8"]]
- 00bb7138 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bb717c ["INT_ADD", "register:40f0:8", ["const:bb717c:8", "const:4:8"]]
+ 00bb717c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bb7138 bytes da8f0094
+ 00bb717c bytes dd8f0094
- 00bb74a8 ["INT_ADD", "register:40f0:8", ["const:bb74a8:8", "const:4:8"]]
- 00bb74a8 ["CALL", null, ["callee:00be1020:8"]]
+ 00bb74ec ["INT_ADD", "register:40f0:8", ["const:bb74ec:8", "const:4:8"]]
+ 00bb74ec ["CALL", null, ["callee:00be1020:8"]]
- 00bb74a8 bytes caa60094
+ 00bb74ec bytes cda60094
~~~


<a id="compare-6836697c2464b9216fd6e24b7009d249"></a>

### [`00bb7d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7d7c.md) → [`00bb7dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dc0.md) FUN_00bb7dc0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7d7c.md#insn-00bb7d90)
- 新版 `00bb7dd4`（命令位置の公開資料なし）

~~~diff
- 00bb7d90 ["INT_ADD", "register:40f0:8", ["const:bb7d90:8", "const:4:8"]]
- 00bb7d90 ["CALL", null, ["callee:00bdda30:8"]]
+ 00bb7dd4 ["INT_ADD", "register:40f0:8", ["const:bb7dd4:8", "const:4:8"]]
+ 00bb7dd4 ["CALL", null, ["callee:00bdda30:8"]]
- 00bb7d90 bytes 14970094
+ 00bb7dd4 bytes 17970094
~~~


<a id="compare-c0e04f1e7b76cf322019ba1b152fb133"></a>

### [`00bb7da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7da8.md) → [`00bb7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dec.md) FUN_00bb7dec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7da8.md#insn-00bb7dbc)
- 新版 `00bb7e00`（命令位置の公開資料なし）

~~~diff
- 00bb7dbc ["INT_ADD", "register:40f0:8", ["const:bb7dbc:8", "const:4:8"]]
- 00bb7dbc ["CALL", null, ["callee:00be1770:8"]]
+ 00bb7e00 ["INT_ADD", "register:40f0:8", ["const:bb7e00:8", "const:4:8"]]
+ 00bb7e00 ["CALL", null, ["callee:00be1770:8"]]
- 00bb7dbc bytes 59a60094
+ 00bb7e00 bytes 5ca60094
~~~


<a id="compare-1347c968dd61e3aa9faa238a45ae260f"></a>

### [`00bb7dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7dd4.md) → [`00bb7e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e18.md) FUN_00bb7e18

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7dd4.md#insn-00bb7de8)
- 新版 `00bb7e2c`（命令位置の公開資料なし）

~~~diff
- 00bb7de8 ["INT_ADD", "register:40f0:8", ["const:bb7de8:8", "const:4:8"]]
- 00bb7de8 ["CALL", null, ["callee:00be1790:8"]]
+ 00bb7e2c ["INT_ADD", "register:40f0:8", ["const:bb7e2c:8", "const:4:8"]]
+ 00bb7e2c ["CALL", null, ["callee:00be1790:8"]]
- 00bb7de8 bytes 56a60094
+ 00bb7e2c bytes 59a60094
~~~


<a id="compare-dce45d84622acaeb411677a95ad2fb42"></a>

### [`00bb7e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e00.md) → [`00bb7e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e44.md) FUN_00bb7e44

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e00.md#insn-00bb7e14)
- 新版 `00bb7e58`（命令位置の公開資料なし）

~~~diff
- 00bb7e14 ["INT_ADD", "register:40f0:8", ["const:bb7e14:8", "const:4:8"]]
- 00bb7e14 ["CALL", null, ["callee:00bdda30:8"]]
+ 00bb7e58 ["INT_ADD", "register:40f0:8", ["const:bb7e58:8", "const:4:8"]]
+ 00bb7e58 ["CALL", null, ["callee:00bdda30:8"]]
- 00bb7e14 bytes f3960094
+ 00bb7e58 bytes f6960094
~~~


<a id="compare-fb996e3cb31083dd8151d734fccedb66"></a>

### [`00bb7e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e2c.md) → [`00bb7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e70.md) FUN_00bb7e70

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e2c.md#insn-00bb7e40)
- 新版 `00bb7e84`（命令位置の公開資料なし）

~~~diff
- 00bb7e40 ["INT_ADD", "register:40f0:8", ["const:bb7e40:8", "const:4:8"]]
- 00bb7e40 ["CALL", null, ["callee:00bdda30:8"]]
+ 00bb7e84 ["INT_ADD", "register:40f0:8", ["const:bb7e84:8", "const:4:8"]]
+ 00bb7e84 ["CALL", null, ["callee:00bdda30:8"]]
- 00bb7e40 bytes e8960094
+ 00bb7e84 bytes eb960094
~~~


<a id="compare-e5b56d6ee7aa534e990a9ffc49e4d7e8"></a>

### [`00bb7e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e58.md) → [`00bb7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e9c.md) FUN_00bb7e9c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e58.md#insn-00bb7e6c)
- 新版 `00bb7eb0`（命令位置の公開資料なし）

~~~diff
- 00bb7e6c ["INT_ADD", "register:40f0:8", ["const:bb7e6c:8", "const:4:8"]]
- 00bb7e6c ["CALL", null, ["callee:00be1770:8"]]
+ 00bb7eb0 ["INT_ADD", "register:40f0:8", ["const:bb7eb0:8", "const:4:8"]]
+ 00bb7eb0 ["CALL", null, ["callee:00be1770:8"]]
- 00bb7e6c bytes 2da60094
+ 00bb7eb0 bytes 30a60094
~~~


<a id="compare-74cc082698a5df01e7546fa874f4650e"></a>

### [`00bb7e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e84.md) → [`00bb7ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ec8.md) FUN_00bb7ec8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7e84.md#insn-00bb7e98)
- 新版 `00bb7edc`（命令位置の公開資料なし）

~~~diff
- 00bb7e98 ["INT_ADD", "register:40f0:8", ["const:bb7e98:8", "const:4:8"]]
- 00bb7e98 ["CALL", null, ["callee:00be1770:8"]]
+ 00bb7edc ["INT_ADD", "register:40f0:8", ["const:bb7edc:8", "const:4:8"]]
+ 00bb7edc ["CALL", null, ["callee:00be1770:8"]]
- 00bb7e98 bytes 22a60094
+ 00bb7edc bytes 25a60094
~~~


<a id="compare-6394f27cba8e6b84f4b1635b6000f0fd"></a>

### [`00bb7eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7eb0.md) → [`00bb7ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7ef4.md) FUN_00bb7ef4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7eb0.md#insn-00bb7ec4)
- 新版 `00bb7f08`（命令位置の公開資料なし）

~~~diff
- 00bb7ec4 ["INT_ADD", "register:40f0:8", ["const:bb7ec4:8", "const:4:8"]]
- 00bb7ec4 ["CALL", null, ["callee:00be1790:8"]]
+ 00bb7f08 ["INT_ADD", "register:40f0:8", ["const:bb7f08:8", "const:4:8"]]
+ 00bb7f08 ["CALL", null, ["callee:00be1790:8"]]
- 00bb7ec4 bytes 1fa60094
+ 00bb7f08 bytes 22a60094
~~~


<a id="compare-f446729b8146b91d7f4249f8fda243ac"></a>

### [`00bb7edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7edc.md) → [`00bb7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f20.md) FUN_00bb7f20

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7edc.md#insn-00bb7ef0)
- 新版 `00bb7f34`（命令位置の公開資料なし）

~~~diff
- 00bb7ef0 ["INT_ADD", "register:40f0:8", ["const:bb7ef0:8", "const:4:8"]]
- 00bb7ef0 ["CALL", null, ["callee:00be1790:8"]]
+ 00bb7f34 ["INT_ADD", "register:40f0:8", ["const:bb7f34:8", "const:4:8"]]
+ 00bb7f34 ["CALL", null, ["callee:00be1790:8"]]
- 00bb7ef0 bytes 14a60094
+ 00bb7f34 bytes 17a60094
~~~


<a id="compare-ee78f97f1e9787ded64032a2f9eda7fc"></a>

### [`00bb7fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7fc8.md) → [`00bb800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb800c.md) FUN_00bb800c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7fc8.md#insn-00bb7fdc)
- 新版 `00bb8020`（命令位置の公開資料なし）

~~~diff
- 00bb7fdc ["INT_ADD", "register:40f0:8", ["const:bb7fdc:8", "const:4:8"]]
- 00bb7fdc ["CALL", null, ["callee:00bdda30:8"]]
+ 00bb8020 ["INT_ADD", "register:40f0:8", ["const:bb8020:8", "const:4:8"]]
+ 00bb8020 ["CALL", null, ["callee:00bdda30:8"]]
- 00bb7fdc bytes 81960094
+ 00bb8020 bytes 84960094
~~~


<a id="compare-d4d94616733be82590872b14e62ade3f"></a>

### [`00bb7ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7ff4.md) → [`00bb8038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8038.md) FUN_00bb8038

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1740.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7ff4.md#insn-00bb8008)
- 新版 `00bb804c`（命令位置の公開資料なし）

~~~diff
- 00bb8008 ["INT_ADD", "register:40f0:8", ["const:bb8008:8", "const:4:8"]]
- 00bb8008 ["CALL", null, ["callee:00be1790:8"]]
+ 00bb804c ["INT_ADD", "register:40f0:8", ["const:bb804c:8", "const:4:8"]]
+ 00bb804c ["CALL", null, ["callee:00be1790:8"]]
- 00bb8008 bytes cea50094
+ 00bb804c bytes d1a50094
~~~


<a id="compare-5edf5b7f97913593a70ac083afca6b6a"></a>

### [`00bb8020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8020.md) → [`00bb8064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8064.md) FUN_00bb8064

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8020.md#insn-00bb8034)
- 新版 `00bb8078`（命令位置の公開資料なし）

~~~diff
- 00bb8034 ["INT_ADD", "register:40f0:8", ["const:bb8034:8", "const:4:8"]]
- 00bb8034 ["CALL", null, ["callee:00be1770:8"]]
+ 00bb8078 ["INT_ADD", "register:40f0:8", ["const:bb8078:8", "const:4:8"]]
+ 00bb8078 ["CALL", null, ["callee:00be1770:8"]]
- 00bb8034 bytes bba50094
+ 00bb8078 bytes bea50094
~~~


<a id="compare-8fb068b9251c94f3c6e9f5286b171634"></a>

### [`00bb804c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb804c.md) → [`00bb8090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8090.md) FUN_00bb8090

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb804c.md#insn-00bb8060)
- 新版 `00bb80a4`（命令位置の公開資料なし）

~~~diff
- 00bb8060 ["INT_ADD", "register:40f0:8", ["const:bb8060:8", "const:4:8"]]
- 00bb8060 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb80a4 ["INT_ADD", "register:40f0:8", ["const:bb80a4:8", "const:4:8"]]
+ 00bb80a4 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8060 bytes 008d0094
+ 00bb80a4 bytes 038d0094
~~~


<a id="compare-67bbfb9c13385341906267de76b21046"></a>

### [`00bb8078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8078.md) → [`00bb80bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80bc.md) FUN_00bb80bc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb808c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8078.md#insn-00bb808c)
- 新版 `00bb80d0`（命令位置の公開資料なし）

~~~diff
- 00bb808c ["INT_ADD", "register:40f0:8", ["const:bb808c:8", "const:4:8"]]
- 00bb808c ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb80d0 ["INT_ADD", "register:40f0:8", ["const:bb80d0:8", "const:4:8"]]
+ 00bb80d0 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb808c bytes f58c0094
+ 00bb80d0 bytes f88c0094
~~~


<a id="compare-df4c26d6fae529a5c08c4cef6e81233a"></a>

### [`00bb80a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb80a4.md) → [`00bb80e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb80e8.md) FUN_00bb80e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb80b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb80a4.md#insn-00bb80b8)
- 新版 `00bb80fc`（命令位置の公開資料なし）

~~~diff
- 00bb80b8 ["INT_ADD", "register:40f0:8", ["const:bb80b8:8", "const:4:8"]]
- 00bb80b8 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb80fc ["INT_ADD", "register:40f0:8", ["const:bb80fc:8", "const:4:8"]]
+ 00bb80fc ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb80b8 bytes ea8c0094
+ 00bb80fc bytes ed8c0094
~~~


<a id="compare-bf4d5e9eaef3249f6f473759dc69dfcc"></a>

### [`00bb80d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb80d0.md) → [`00bb8114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8114.md) FUN_00bb8114

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb80e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb80d0.md#insn-00bb80e4)
- 新版 `00bb8128`（命令位置の公開資料なし）

~~~diff
- 00bb80e4 ["INT_ADD", "register:40f0:8", ["const:bb80e4:8", "const:4:8"]]
- 00bb80e4 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8128 ["INT_ADD", "register:40f0:8", ["const:bb8128:8", "const:4:8"]]
+ 00bb8128 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb80e4 bytes df8c0094
+ 00bb8128 bytes e28c0094
~~~


<a id="compare-9df68fce3dda5fd5f5eef9bb1d268b82"></a>

### [`00bb8104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8104.md) → [`00bb8148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8148.md) FUN_00bb8148

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8104.md#insn-00bb8118)
- 新版 `00bb815c`（命令位置の公開資料なし）

~~~diff
- 00bb8118 ["INT_ADD", "register:40f0:8", ["const:bb8118:8", "const:4:8"]]
- 00bb8118 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb815c ["INT_ADD", "register:40f0:8", ["const:bb815c:8", "const:4:8"]]
+ 00bb815c ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8118 bytes d28c0094
+ 00bb815c bytes d58c0094
~~~


<a id="compare-63f583314dceae91c0acd125726be040"></a>

### [`00bb8138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8138.md) → [`00bb817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb817c.md) FUN_00bb817c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb814c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8138.md#insn-00bb814c)
- 新版 `00bb8190`（命令位置の公開資料なし）

~~~diff
- 00bb814c ["INT_ADD", "register:40f0:8", ["const:bb814c:8", "const:4:8"]]
- 00bb814c ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8190 ["INT_ADD", "register:40f0:8", ["const:bb8190:8", "const:4:8"]]
+ 00bb8190 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb814c bytes c58c0094
+ 00bb8190 bytes c88c0094
~~~


<a id="compare-4beb5ead432cc299ce50a12b8a7bb120"></a>

### [`00bb8164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8164.md) → [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) FUN_00bb81a8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb9d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb9ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ddc.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8164.md#insn-00bb817c)
- 新版 `00bb81c0`（命令位置の公開資料なし）

~~~diff
- 00bb817c ["INT_ADD", "register:40f0:8", ["const:bb817c:8", "const:4:8"]]
- 00bb817c ["CALL", null, ["callee:00bb9ddc:8"]]
+ 00bb81c0 ["INT_ADD", "register:40f0:8", ["const:bb81c0:8", "const:4:8"]]
+ 00bb81c0 ["CALL", null, ["callee:00bb9ddc:8"]]
- 00bb817c bytes 07070094
+ 00bb81c0 bytes 07070094
~~~


<a id="compare-919769e5772484d5f9afd22c450dd803"></a>

### [`00bb8194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8194.md) → [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) FUN_00bb81d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb9d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb9ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ddc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb81ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8194.md#insn-00bb81ac) · [`00bb81b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8194.md#insn-00bb81b4)
- 新版 `00bb81f0`（命令位置の公開資料なし） · `00bb81f8`（命令位置の公開資料なし）

~~~diff
- 00bb81ac ["INT_ADD", "register:40f0:8", ["const:bb81ac:8", "const:4:8"]]
- 00bb81ac ["CALL", null, ["callee:00bb9ddc:8"]]
+ 00bb81f0 ["INT_ADD", "register:40f0:8", ["const:bb81f0:8", "const:4:8"]]
+ 00bb81f0 ["CALL", null, ["callee:00bb9ddc:8"]]
- 00bb81ac bytes fb060094
+ 00bb81f0 bytes fb060094
- 00bb81b4 ["INT_ADD", "register:40f0:8", ["const:bb81b4:8", "const:4:8"]]
- 00bb81b4 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb81f8 ["INT_ADD", "register:40f0:8", ["const:bb81f8:8", "const:4:8"]]
+ 00bb81f8 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb81b4 bytes ab8c0094
+ 00bb81f8 bytes ae8c0094
~~~


<a id="compare-3d5c33389143b79010bbef235c01d813"></a>

### [`00bb8280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8280.md) → [`00bb82c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82c4.md) FUN_00bb82c4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb9fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bba00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8280.md#insn-00bb8298)
- 新版 `00bb82dc`（命令位置の公開資料なし）

~~~diff
- 00bb8298 ["INT_ADD", "register:40f0:8", ["const:bb8298:8", "const:4:8"]]
- 00bb8298 ["CALL", null, ["callee:00bba00c:8"]]
+ 00bb82dc ["INT_ADD", "register:40f0:8", ["const:bb82dc:8", "const:4:8"]]
+ 00bb82dc ["CALL", null, ["callee:00bba00c:8"]]
- 00bb8298 bytes 4c070094
+ 00bb82dc bytes 4c070094
~~~


<a id="compare-fe136297ec39e9a4003a69c0d5df32e6"></a>

### [`00bb82b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb82b0.md) → [`00bb82f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82f4.md) FUN_00bb82f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb9fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bba00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb82c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb82b0.md#insn-00bb82c8) · [`00bb82d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb82b0.md#insn-00bb82d0)
- 新版 `00bb830c`（命令位置の公開資料なし） · `00bb8314`（命令位置の公開資料なし）

~~~diff
- 00bb82c8 ["INT_ADD", "register:40f0:8", ["const:bb82c8:8", "const:4:8"]]
- 00bb82c8 ["CALL", null, ["callee:00bba00c:8"]]
+ 00bb830c ["INT_ADD", "register:40f0:8", ["const:bb830c:8", "const:4:8"]]
+ 00bb830c ["CALL", null, ["callee:00bba00c:8"]]
- 00bb82c8 bytes 40070094
+ 00bb830c bytes 40070094
- 00bb82d0 ["INT_ADD", "register:40f0:8", ["const:bb82d0:8", "const:4:8"]]
- 00bb82d0 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8314 ["INT_ADD", "register:40f0:8", ["const:bb8314:8", "const:4:8"]]
+ 00bb8314 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb82d0 bytes 648c0094
+ 00bb8314 bytes 678c0094
~~~


<a id="compare-4a70874c3f13d7eabb32fdaa651ff4ac"></a>

### [`00bb839c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb839c.md) → [`00bb83e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb83e0.md) FUN_00bb83e0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb83b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb839c.md#insn-00bb83b4) · [`00bb83bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb839c.md#insn-00bb83bc)
- 新版 `00bb83f8`（命令位置の公開資料なし） · `00bb8400`（命令位置の公開資料なし）

~~~diff
- 00bb83b4 ["INT_ADD", "register:40f0:8", ["const:bb83b4:8", "const:4:8"]]
- 00bb83b4 ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb83f8 ["INT_ADD", "register:40f0:8", ["const:bb83f8:8", "const:4:8"]]
+ 00bb83f8 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb83b4 bytes 5ba60094
+ 00bb83f8 bytes 5ea60094
- 00bb83bc ["INT_ADD", "register:40f0:8", ["const:bb83bc:8", "const:4:8"]]
- 00bb83bc ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8400 ["INT_ADD", "register:40f0:8", ["const:bb8400:8", "const:4:8"]]
+ 00bb8400 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb83bc bytes 298c0094
+ 00bb8400 bytes 2c8c0094
~~~


<a id="compare-e46314671c85ebf3110790de11d02e93"></a>

### [`00bb83d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb83d4.md) → [`00bb8418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8418.md) FUN_00bb8418

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb83ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb83d4.md#insn-00bb83ec) · [`00bb83f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb83d4.md#insn-00bb83f4)
- 新版 `00bb8430`（命令位置の公開資料なし） · `00bb8438`（命令位置の公開資料なし）

~~~diff
- 00bb83ec ["INT_ADD", "register:40f0:8", ["const:bb83ec:8", "const:4:8"]]
- 00bb83ec ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb8430 ["INT_ADD", "register:40f0:8", ["const:bb8430:8", "const:4:8"]]
+ 00bb8430 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb83ec bytes 4da60094
+ 00bb8430 bytes 50a60094
- 00bb83f4 ["INT_ADD", "register:40f0:8", ["const:bb83f4:8", "const:4:8"]]
- 00bb83f4 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8438 ["INT_ADD", "register:40f0:8", ["const:bb8438:8", "const:4:8"]]
+ 00bb8438 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb83f4 bytes 1b8c0094
+ 00bb8438 bytes 1e8c0094
~~~


<a id="compare-43bdcbea3daa8b89c2386f0430873147"></a>

### [`00bb840c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb840c.md) → [`00bb8450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8450.md) FUN_00bb8450

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb840c.md#insn-00bb8424)
- 新版 `00bb8468`（命令位置の公開資料なし）

~~~diff
- 00bb8424 ["INT_ADD", "register:40f0:8", ["const:bb8424:8", "const:4:8"]]
- 00bb8424 ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb8468 ["INT_ADD", "register:40f0:8", ["const:bb8468:8", "const:4:8"]]
+ 00bb8468 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb8424 bytes 3fa60094
+ 00bb8468 bytes 42a60094
~~~


<a id="compare-cc860d58c63a9c9a4710dd9ca18fe7a2"></a>

### [`00bb843c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb843c.md) → [`00bb8480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8480.md) FUN_00bb8480

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb843c.md#insn-00bb8454) · [`00bb845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb843c.md#insn-00bb845c)
- 新版 `00bb8498`（命令位置の公開資料なし） · `00bb84a0`（命令位置の公開資料なし）

~~~diff
- 00bb8454 ["INT_ADD", "register:40f0:8", ["const:bb8454:8", "const:4:8"]]
- 00bb8454 ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb8498 ["INT_ADD", "register:40f0:8", ["const:bb8498:8", "const:4:8"]]
+ 00bb8498 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb8454 bytes 33a60094
+ 00bb8498 bytes 36a60094
- 00bb845c ["INT_ADD", "register:40f0:8", ["const:bb845c:8", "const:4:8"]]
- 00bb845c ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb84a0 ["INT_ADD", "register:40f0:8", ["const:bb84a0:8", "const:4:8"]]
+ 00bb84a0 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb845c bytes 018c0094
+ 00bb84a0 bytes 048c0094
~~~


<a id="compare-9c14e5a589a0316bb6c734912a236de3"></a>

### [`00bb8474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8474.md) → [`00bb84b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb84b8.md) FUN_00bb84b8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb848c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8474.md#insn-00bb848c)
- 新版 `00bb84d0`（命令位置の公開資料なし）

~~~diff
- 00bb848c ["INT_ADD", "register:40f0:8", ["const:bb848c:8", "const:4:8"]]
- 00bb848c ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb84d0 ["INT_ADD", "register:40f0:8", ["const:bb84d0:8", "const:4:8"]]
+ 00bb84d0 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb848c bytes 25a60094
+ 00bb84d0 bytes 28a60094
~~~


<a id="compare-5a088830665679d8e955073f1acb51eb"></a>

### [`00bb84a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb84a4.md) → [`00bb84e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb84e8.md) FUN_00bb84e8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb84bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb84a4.md#insn-00bb84bc) · [`00bb84c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb84a4.md#insn-00bb84c4)
- 新版 `00bb8500`（命令位置の公開資料なし） · `00bb8508`（命令位置の公開資料なし）

~~~diff
- 00bb84bc ["INT_ADD", "register:40f0:8", ["const:bb84bc:8", "const:4:8"]]
- 00bb84bc ["CALL", null, ["callee:00be1d70:8"]]
+ 00bb8500 ["INT_ADD", "register:40f0:8", ["const:bb8500:8", "const:4:8"]]
+ 00bb8500 ["CALL", null, ["callee:00be1d70:8"]]
- 00bb84bc bytes 19a60094
+ 00bb8500 bytes 1ca60094
- 00bb84c4 ["INT_ADD", "register:40f0:8", ["const:bb84c4:8", "const:4:8"]]
- 00bb84c4 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8508 ["INT_ADD", "register:40f0:8", ["const:bb8508:8", "const:4:8"]]
+ 00bb8508 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb84c4 bytes e78b0094
+ 00bb8508 bytes ea8b0094
~~~


<a id="compare-26fcf400f19514a08358040bbfd4adaf"></a>

### [`00bb84dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb84dc.md) → [`00bb8520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8520.md) FUN_00bb8520

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb84f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb84dc.md#insn-00bb84f0)
- 新版 `00bb8534`（命令位置の公開資料なし）

~~~diff
- 00bb84f0 ["INT_ADD", "register:40f0:8", ["const:bb84f0:8", "const:4:8"]]
- 00bb84f0 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8534 ["INT_ADD", "register:40f0:8", ["const:bb8534:8", "const:4:8"]]
+ 00bb8534 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb84f0 bytes dc8b0094
+ 00bb8534 bytes df8b0094
~~~


<a id="compare-36c7fde3a7d3b275b0647c06aedd4cf4"></a>

### [`00bb8508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8508.md) → [`00bb854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb854c.md) FUN_00bb854c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb851c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8508.md#insn-00bb851c)
- 新版 `00bb8560`（命令位置の公開資料なし）

~~~diff
- 00bb851c ["INT_ADD", "register:40f0:8", ["const:bb851c:8", "const:4:8"]]
- 00bb851c ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8560 ["INT_ADD", "register:40f0:8", ["const:bb8560:8", "const:4:8"]]
+ 00bb8560 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb851c bytes d18b0094
+ 00bb8560 bytes d48b0094
~~~


<a id="compare-681898719d1ec1cc5799b521f89627e9"></a>

### [`00bb8534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8534.md) → [`00bb8578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8578.md) FUN_00bb8578

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8534.md#insn-00bb8548)
- 新版 `00bb858c`（命令位置の公開資料なし）

~~~diff
- 00bb8548 ["INT_ADD", "register:40f0:8", ["const:bb8548:8", "const:4:8"]]
- 00bb8548 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb858c ["INT_ADD", "register:40f0:8", ["const:bb858c:8", "const:4:8"]]
+ 00bb858c ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8548 bytes c68b0094
+ 00bb858c bytes c98b0094
~~~


<a id="compare-b5cd9101e1c3509483443837b8c71024"></a>

### [`00bb8560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8560.md) → [`00bb85a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb85a4.md) FUN_00bb85a4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8560.md#insn-00bb8574)
- 新版 `00bb85b8`（命令位置の公開資料なし）

~~~diff
- 00bb8574 ["INT_ADD", "register:40f0:8", ["const:bb8574:8", "const:4:8"]]
- 00bb8574 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb85b8 ["INT_ADD", "register:40f0:8", ["const:bb85b8:8", "const:4:8"]]
+ 00bb85b8 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8574 bytes bb8b0094
+ 00bb85b8 bytes be8b0094
~~~


<a id="compare-2a5abb98f5526e30cb152a2284b00562"></a>

### [`00bb8620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8620.md) → [`00bb8664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8664.md) FUN_00bb8664

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb85d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb85d0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8620.md#insn-00bb8634)
- 新版 `00bb8678`（命令位置の公開資料なし）

~~~diff
- 00bb8634 ["INT_ADD", "register:40f0:8", ["const:bb8634:8", "const:4:8"]]
- 00bb8634 ["CALL", null, ["callee:00bb85d0:8"]]
+ 00bb8678 ["INT_ADD", "register:40f0:8", ["const:bb8678:8", "const:4:8"]]
+ 00bb8678 ["CALL", null, ["callee:00bb85d0:8"]]
- 00bb8634 bytes d6ffff97
+ 00bb8678 bytes d6ffff97
~~~


<a id="compare-b790b6b01d719659519aaf726e183b22"></a>

### [`00bb86e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb86e0.md) → [`00bb8724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md) FUN_00bb8724

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb8690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8690.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb86f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb86e0.md#insn-00bb86f4)
- 新版 `00bb8738`（命令位置の公開資料なし）

~~~diff
- 00bb86f4 ["INT_ADD", "register:40f0:8", ["const:bb86f4:8", "const:4:8"]]
- 00bb86f4 ["CALL", null, ["callee:00bb8690:8"]]
+ 00bb8738 ["INT_ADD", "register:40f0:8", ["const:bb8738:8", "const:4:8"]]
+ 00bb8738 ["CALL", null, ["callee:00bb8690:8"]]
- 00bb86f4 bytes d6ffff97
+ 00bb8738 bytes d6ffff97
~~~


<a id="compare-e8972adfae50d1424eb8930a5417e991"></a>

### [`00bb87a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87a0.md) → [`00bb87e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md) FUN_00bb87e4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb870c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb8750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8750.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb87b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87a0.md#insn-00bb87b4)
- 新版 `00bb87f8`（命令位置の公開資料なし）

~~~diff
- 00bb87b4 ["INT_ADD", "register:40f0:8", ["const:bb87b4:8", "const:4:8"]]
- 00bb87b4 ["CALL", null, ["callee:00bb8750:8"]]
+ 00bb87f8 ["INT_ADD", "register:40f0:8", ["const:bb87f8:8", "const:4:8"]]
+ 00bb87f8 ["CALL", null, ["callee:00bb8750:8"]]
- 00bb87b4 bytes d6ffff97
+ 00bb87f8 bytes d6ffff97
~~~


<a id="compare-4c6a1c5ff483a8f639a7f7a73614a8c0"></a>

### [`00bb8860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8860.md) → [`00bb88a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88a4.md) FUN_00bb88a4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb87cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb8810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8860.md#insn-00bb8874)
- 新版 `00bb88b8`（命令位置の公開資料なし）

~~~diff
- 00bb8874 ["INT_ADD", "register:40f0:8", ["const:bb8874:8", "const:4:8"]]
- 00bb8874 ["CALL", null, ["callee:00bb8810:8"]]
+ 00bb88b8 ["INT_ADD", "register:40f0:8", ["const:bb88b8:8", "const:4:8"]]
+ 00bb88b8 ["CALL", null, ["callee:00bb8810:8"]]
- 00bb8874 bytes d6ffff97
+ 00bb88b8 bytes d6ffff97
~~~


<a id="compare-e68afdb9deac7687db001b6fec2b6b94"></a>

### [`00bb888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb888c.md) → [`00bb88d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88d0.md) FUN_00bb88d0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb88a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb888c.md#insn-00bb88a0)
- 新版 `00bb88e4`（命令位置の公開資料なし）

~~~diff
- 00bb88a0 ["INT_ADD", "register:40f0:8", ["const:bb88a0:8", "const:4:8"]]
- 00bb88a0 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb88e4 ["INT_ADD", "register:40f0:8", ["const:bb88e4:8", "const:4:8"]]
+ 00bb88e4 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb88a0 bytes f08a0094
+ 00bb88e4 bytes f38a0094
~~~


<a id="compare-0271e4a6e307fb338127d4165c2f26b1"></a>

### [`00bb88b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb88b8.md) → [`00bb88fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88fc.md) FUN_00bb88fc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb88cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb88b8.md#insn-00bb88cc)
- 新版 `00bb8910`（命令位置の公開資料なし）

~~~diff
- 00bb88cc ["INT_ADD", "register:40f0:8", ["const:bb88cc:8", "const:4:8"]]
- 00bb88cc ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8910 ["INT_ADD", "register:40f0:8", ["const:bb8910:8", "const:4:8"]]
+ 00bb8910 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb88cc bytes e58a0094
+ 00bb8910 bytes e88a0094
~~~


<a id="compare-eaee5a85fea6cb0a5021cb935c4acfe7"></a>

### [`00bb88e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb88e4.md) → [`00bb8928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8928.md) FUN_00bb8928

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb88f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb88e4.md#insn-00bb88f8)
- 新版 `00bb893c`（命令位置の公開資料なし）

~~~diff
- 00bb88f8 ["INT_ADD", "register:40f0:8", ["const:bb88f8:8", "const:4:8"]]
- 00bb88f8 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb893c ["INT_ADD", "register:40f0:8", ["const:bb893c:8", "const:4:8"]]
+ 00bb893c ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb88f8 bytes da8a0094
+ 00bb893c bytes dd8a0094
~~~


<a id="compare-fa58b984ca4ac7e3f2519a454ec98e57"></a>

### [`00bb8910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8910.md) → [`00bb8954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8954.md) FUN_00bb8954

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8910.md#insn-00bb8924)
- 新版 `00bb8968`（命令位置の公開資料なし）

~~~diff
- 00bb8924 ["INT_ADD", "register:40f0:8", ["const:bb8924:8", "const:4:8"]]
- 00bb8924 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8968 ["INT_ADD", "register:40f0:8", ["const:bb8968:8", "const:4:8"]]
+ 00bb8968 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8924 bytes cf8a0094
+ 00bb8968 bytes d28a0094
~~~


<a id="compare-2a05a2ab4b94a2bed34a2d13ffb4332f"></a>

### [`00bb893c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb893c.md) → [`00bb8980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8980.md) FUN_00bb8980

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb893c.md#insn-00bb8950)
- 新版 `00bb8994`（命令位置の公開資料なし）

~~~diff
- 00bb8950 ["INT_ADD", "register:40f0:8", ["const:bb8950:8", "const:4:8"]]
- 00bb8950 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8994 ["INT_ADD", "register:40f0:8", ["const:bb8994:8", "const:4:8"]]
+ 00bb8994 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb8950 bytes c48a0094
+ 00bb8994 bytes c78a0094
~~~


<a id="compare-8b03488f1ec2e5bdab799fc38aa92870"></a>

### [`00bb8968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8968.md) → [`00bb89ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb89ac.md) FUN_00bb89ac

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb897c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8968.md#insn-00bb897c)
- 新版 `00bb89c0`（命令位置の公開資料なし）

~~~diff
- 00bb897c ["INT_ADD", "register:40f0:8", ["const:bb897c:8", "const:4:8"]]
- 00bb897c ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb89c0 ["INT_ADD", "register:40f0:8", ["const:bb89c0:8", "const:4:8"]]
+ 00bb89c0 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb897c bytes b98a0094
+ 00bb89c0 bytes bc8a0094
~~~


<a id="compare-ddb0e7f9c4b7020f51d47df300f45825"></a>

### [`00bb8994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8994.md) → [`00bb89d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb89d8.md) FUN_00bb89d8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb89a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8994.md#insn-00bb89a8)
- 新版 `00bb89ec`（命令位置の公開資料なし）

~~~diff
- 00bb89a8 ["INT_ADD", "register:40f0:8", ["const:bb89a8:8", "const:4:8"]]
- 00bb89a8 ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb89ec ["INT_ADD", "register:40f0:8", ["const:bb89ec:8", "const:4:8"]]
+ 00bb89ec ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb89a8 bytes ae8a0094
+ 00bb89ec bytes b18a0094
~~~


<a id="compare-aec178278e95a96036e073a57cfd6e09"></a>

### [`00bb89c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb89c8.md) → [`00bb8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a0c.md) FUN_00bb8a0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb89dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb89c8.md#insn-00bb89dc)
- 新版 `00bb8a20`（命令位置の公開資料なし）

~~~diff
- 00bb89dc ["INT_ADD", "register:40f0:8", ["const:bb89dc:8", "const:4:8"]]
- 00bb89dc ["CALL", null, ["callee:00bdb4b0:8"]]
+ 00bb8a20 ["INT_ADD", "register:40f0:8", ["const:bb8a20:8", "const:4:8"]]
+ 00bb8a20 ["CALL", null, ["callee:00bdb4b0:8"]]
- 00bb89dc bytes a18a0094
+ 00bb8a20 bytes a48a0094
~~~


<a id="compare-3ba2beca210887d083181b897ab7ffed"></a>

### [`00bb89f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb89f4.md) → [`00bb8a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a38.md) FUN_00bb8a38

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb89f4.md#insn-00bb8a08)
- 新版 `00bb8a4c`（命令位置の公開資料なし）

~~~diff
- 00bb8a08 ["INT_ADD", "register:40f0:8", ["const:bb8a08:8", "const:4:8"]]
- 00bb8a08 ["CALL", null, ["callee:00be1580:8"]]
+ 00bb8a4c ["INT_ADD", "register:40f0:8", ["const:bb8a4c:8", "const:4:8"]]
+ 00bb8a4c ["CALL", null, ["callee:00be1580:8"]]
- 00bb8a08 bytes caa20094
+ 00bb8a4c bytes cda20094
~~~


<a id="compare-e85a037d93a456e2e9c6143ba76088df"></a>

### [`00bb8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md) → [`00bb8a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a78.md) FUN_00bb8a78

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) · 呼出先 4件 [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 4件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) [`00ba7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7a64.md) · 呼出先 4件 [`00bb8a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md#insn-00bb8a84) · [`00bb8ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md#insn-00bb8ab4) · [`00bb8b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md#insn-00bb8b40)
- 新版 `00bb8ac8`（命令位置の公開資料なし） · `00bb8af8`（命令位置の公開資料なし） · `00bb8b84`（命令位置の公開資料なし）

~~~diff
- 00bb8a84 ["INT_ADD", "register:40f0:8", ["const:bb8a84:8", "const:4:8"]]
- 00bb8a84 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb8ac8 ["INT_ADD", "register:40f0:8", ["const:bb8ac8:8", "const:4:8"]]
+ 00bb8ac8 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb8a84 bytes 63890094
+ 00bb8ac8 bytes 66890094
- 00bb8ab4 ["INT_ADD", "register:40f0:8", ["const:bb8ab4:8", "const:4:8"]]
- 00bb8ab4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00bb8af8 ["INT_ADD", "register:40f0:8", ["const:bb8af8:8", "const:4:8"]]
+ 00bb8af8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00bb8ab4 bytes 7b890094
+ 00bb8af8 bytes 7e890094
- 00bb8b40 ["INT_ADD", "register:40f0:8", ["const:bb8b40:8", "const:4:8"]]
- 00bb8b40 ["CALL", null, ["callee:00bdb040:8"]]
+ 00bb8b84 ["INT_ADD", "register:40f0:8", ["const:bb8b84:8", "const:4:8"]]
+ 00bb8b84 ["CALL", null, ["callee:00bdb040:8"]]
- 00bb8b40 bytes 2c890094
+ 00bb8b84 bytes 2f890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eb702130d9f53908a2b529f96426b8c"></a>

### [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) → [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) FUN_00bb8bd4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`00ba07e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba07e8.md) [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) [`00ba30a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 54件 [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bb8a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md#insn-00bb8c30) · [`00bb8c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md#insn-00bb8c58) · [`00bb8c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md#insn-00bb8c78)
- 新版 `00bb8c74`（命令位置の公開資料なし） · `00bb8c9c`（命令位置の公開資料なし） · `00bb8cbc`（命令位置の公開資料なし）

~~~diff
- 00bb8c30 ["INT_ADD", "register:40f0:8", ["const:bb8c30:8", "const:4:8"]]
- 00bb8c30 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb8c74 ["INT_ADD", "register:40f0:8", ["const:bb8c74:8", "const:4:8"]]
+ 00bb8c74 ["CALL", null, ["callee:00bdb240:8"]]
- 00bb8c30 bytes 70890094
+ 00bb8c74 bytes 73890094
- 00bb8c58 ["INT_ADD", "register:40f0:8", ["const:bb8c58:8", "const:4:8"]]
- 00bb8c58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00bb8c9c ["INT_ADD", "register:40f0:8", ["const:bb8c9c:8", "const:4:8"]]
+ 00bb8c9c ["CALL", null, ["callee:00bdb040:8"]]
- 00bb8c58 bytes e6880094
+ 00bb8c9c bytes e9880094
- 00bb8c78 ["INT_ADD", "register:40f0:8", ["const:bb8c78:8", "const:4:8"]]
- 00bb8c78 ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb8cbc ["INT_ADD", "register:40f0:8", ["const:bb8cbc:8", "const:4:8"]]
+ 00bb8cbc ["CALL", null, ["callee:00bdb240:8"]]
- 00bb8c78 bytes 5e890094
+ 00bb8cbc bytes 61890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31884935d766a4a03f039e9505ae81ec"></a>

### [`00bb9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md) → [`00bb9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md) FUN_00bb9248

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb5fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5fb8.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b74d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md)
- 新版 呼出元 1件 [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb9240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md#insn-00bb9240) · [`00bb9258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md#insn-00bb9258)
- 新版 `00bb9284`（命令位置の公開資料なし） · `00bb929c`（命令位置の公開資料なし）

~~~diff
- 00bb9240 ["INT_ADD", "register:40f0:8", ["const:bb9240:8", "const:4:8"]]
- 00bb9240 ["CALL", null, ["callee:00b74d9c:8"]]
+ 00bb9284 ["INT_ADD", "register:40f0:8", ["const:bb9284:8", "const:4:8"]]
+ 00bb9284 ["CALL", null, ["callee:00b74d9c:8"]]
- 00bb9240 bytes c6eefe97
+ 00bb9284 bytes c6eefe97
- 00bb9258 ["INT_ADD", "register:40f0:8", ["const:bb9258:8", "const:4:8"]]
- 00bb9258 ["CALL", null, ["callee:0041fddc:8"]]
+ 00bb929c ["INT_ADD", "register:40f0:8", ["const:bb929c:8", "const:4:8"]]
+ 00bb929c ["CALL", null, ["callee:0041fddc:8"]]
- 00bb9258 bytes e19ae197
+ 00bb929c bytes d09ae197
~~~


<a id="compare-43de180d8d3a79771e343d025d33dc2b"></a>

### [`00bb925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md) → [`00bb92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md) FUN_00bb92a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb7080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7080.md) · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00b7716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md)
- 新版 呼出元 1件 [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00b771b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b771b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb929c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md#insn-00bb929c) · [`00bb92b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md#insn-00bb92b4)
- 新版 `00bb92e0`（命令位置の公開資料なし） · `00bb92f8`（命令位置の公開資料なし）

~~~diff
- 00bb929c ["INT_ADD", "register:40f0:8", ["const:bb929c:8", "const:4:8"]]
- 00bb929c ["CALL", null, ["callee:00b771b0:8"]]
+ 00bb92e0 ["INT_ADD", "register:40f0:8", ["const:bb92e0:8", "const:4:8"]]
+ 00bb92e0 ["CALL", null, ["callee:00b771b0:8"]]
- 00bb929c bytes b4f7fe97
+ 00bb92e0 bytes b4f7fe97
- 00bb92b4 ["INT_ADD", "register:40f0:8", ["const:bb92b4:8", "const:4:8"]]
- 00bb92b4 ["CALL", null, ["callee:00b75a68:8"]]
+ 00bb92f8 ["INT_ADD", "register:40f0:8", ["const:bb92f8:8", "const:4:8"]]
+ 00bb92f8 ["CALL", null, ["callee:00b75a68:8"]]
- 00bb92b4 bytes dcf1fe97
+ 00bb92f8 bytes dcf1fe97
~~~


<a id="compare-9baa5ec5ac0cc5b1bb467db5d26833f9"></a>

### [`00bb9d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md) → [`00bb9ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ddc.md) FUN_00bb9ddc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bb8164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8164.md) [`00bb8194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8194.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 2件 [`00bb81a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81a8.md) [`00bb81d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb81d8.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb9de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md#insn-00bb9de0) · [`00bb9e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md#insn-00bb9e04) · [`00bb9e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9d98.md#insn-00bb9e80)
- 新版 `00bb9e24`（命令位置の公開資料なし） · `00bb9e48`（命令位置の公開資料なし） · `00bb9ec4`（命令位置の公開資料なし）

~~~diff
- 00bb9de0 ["INT_ADD", "register:40f0:8", ["const:bb9de0:8", "const:4:8"]]
- 00bb9de0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb9e24 ["INT_ADD", "register:40f0:8", ["const:bb9e24:8", "const:4:8"]]
+ 00bb9e24 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb9de0 bytes 8c840094
+ 00bb9e24 bytes 8f840094
- 00bb9e04 ["INT_ADD", "register:40f0:8", ["const:bb9e04:8", "const:4:8"]]
- 00bb9e04 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb9e48 ["INT_ADD", "register:40f0:8", ["const:bb9e48:8", "const:4:8"]]
+ 00bb9e48 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb9e04 bytes 83840094
+ 00bb9e48 bytes 86840094
- 00bb9e80 ["INT_ADD", "register:40f0:8", ["const:bb9e80:8", "const:4:8"]]
- 00bb9e80 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bb9ec4 ["INT_ADD", "register:40f0:8", ["const:bb9ec4:8", "const:4:8"]]
+ 00bb9ec4 ["CALL", null, ["callee:00bdb060:8"]]
- 00bb9e80 bytes 64840094
+ 00bb9ec4 bytes 67840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6896c701c66c69a153fce83ce37258"></a>

### [`00bb9fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md) → [`00bba00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md) FUN_00bba00c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bb8280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8280.md) [`00bb82b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb82b0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 2件 [`00bb82c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82c4.md) [`00bb82f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82f4.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bba010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md#insn-00bba010) · [`00bba034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md#insn-00bba034) · [`00bba0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9fc8.md#insn-00bba0b0)
- 新版 `00bba054`（命令位置の公開資料なし） · `00bba078`（命令位置の公開資料なし） · `00bba0f4`（命令位置の公開資料なし）

~~~diff
- 00bba010 ["INT_ADD", "register:40f0:8", ["const:bba010:8", "const:4:8"]]
- 00bba010 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bba054 ["INT_ADD", "register:40f0:8", ["const:bba054:8", "const:4:8"]]
+ 00bba054 ["CALL", null, ["callee:00bdb060:8"]]
- 00bba010 bytes 00840094
+ 00bba054 bytes 03840094
- 00bba034 ["INT_ADD", "register:40f0:8", ["const:bba034:8", "const:4:8"]]
- 00bba034 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bba078 ["INT_ADD", "register:40f0:8", ["const:bba078:8", "const:4:8"]]
+ 00bba078 ["CALL", null, ["callee:00bdb060:8"]]
- 00bba034 bytes f7830094
+ 00bba078 bytes fa830094
- 00bba0b0 ["INT_ADD", "register:40f0:8", ["const:bba0b0:8", "const:4:8"]]
- 00bba0b0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00bba0f4 ["INT_ADD", "register:40f0:8", ["const:bba0f4:8", "const:4:8"]]
+ 00bba0f4 ["CALL", null, ["callee:00bdb060:8"]]
- 00bba0b0 bytes d8830094
+ 00bba0f4 bytes db830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60db946b6a5acfcdb76f048b7c3e4b18"></a>

### [`00bba3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3dc.md) → [`00bba420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md) _ZNSt6__ndk111regex_errorD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bba3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3dc.md#insn-00bba3f0)
- 新版 `00bba434`（命令位置の公開資料なし）

~~~diff
- 00bba3f0 ["INT_ADD", "register:40f0:8", ["const:bba3f0:8", "const:4:8"]]
- 00bba3f0 ["CALL", null, ["callee:00bdd970:8"]]
+ 00bba434 ["INT_ADD", "register:40f0:8", ["const:bba434:8", "const:4:8"]]
+ 00bba434 ["CALL", null, ["callee:00bdd970:8"]]
- 00bba3f0 bytes 4c8d0094
+ 00bba434 bytes 4f8d0094
~~~


<a id="compare-946509a7de19d4689cd42a1bb71ff964"></a>

### [`00bbacc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacc0.md) → [`00bbad04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad04.md) __cxa_pure_virtual

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbacd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacc0.md#insn-00bbacd4)
- 新版 `00bbad18`（命令位置の公開資料なし）

~~~diff
- 00bbacd4 ["INT_ADD", "register:40f0:8", ["const:bbacd4:8", "const:4:8"]]
- 00bbacd4 ["CALL", null, ["callee:00bbb19c:8"]]
+ 00bbad18 ["INT_ADD", "register:40f0:8", ["const:bbad18:8", "const:4:8"]]
+ 00bbad18 ["CALL", null, ["callee:00bbb19c:8"]]
- 00bbacd4 bytes 21010094
+ 00bbad18 bytes 21010094
~~~


<a id="compare-c4ccec6db878d90ad1d5ab078291a010"></a>

### [`00bbacf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf8.md) → [`00bbad3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad3c.md) _ZNSt9exceptionD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1df0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbad0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf8.md#insn-00bbad0c)
- 新版 `00bbad50`（命令位置の公開資料なし）

~~~diff
- 00bbad0c ["INT_ADD", "register:40f0:8", ["const:bbad0c:8", "const:4:8"]]
- 00bbad0c ["CALL", null, ["callee:00be1e40:8"]]
+ 00bbad50 ["INT_ADD", "register:40f0:8", ["const:bbad50:8", "const:4:8"]]
+ 00bbad50 ["CALL", null, ["callee:00be1e40:8"]]
- 00bbad0c bytes 399c0094
+ 00bbad50 bytes 3c9c0094
~~~


