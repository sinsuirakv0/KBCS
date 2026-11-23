# v15.7.3 → v15.7.4 · 要調査の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-fac9ed16fe5da9ba3a4ffb3f39856eff"></a>

### [`00b7250c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7250c.md) → [`00b72550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72550.md) _ZNK8firebase4auth4User16DeleteLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7252c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7250c.md#insn-00b7252c) · [`00b72538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7250c.md#insn-00b72538) · [`00b72544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7250c.md#insn-00b72544)
- 新版 `00b72570`（命令位置の公開資料なし） · `00b7257c`（命令位置の公開資料なし） · `00b72588`（命令位置の公開資料なし）

~~~diff
- 00b7252c ["INT_ADD", "register:40f0:8", ["const:b7252c:8", "const:4:8"]]
- 00b7252c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72570 ["INT_ADD", "register:40f0:8", ["const:b72570:8", "const:4:8"]]
+ 00b72570 ["CALL", null, ["callee:00bddc20:8"]]
- 00b7252c bytes a9ad0194
+ 00b72570 bytes acad0194
- 00b72538 ["INT_ADD", "register:40f0:8", ["const:b72538:8", "const:4:8"]]
- 00b72538 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7257c ["INT_ADD", "register:40f0:8", ["const:b7257c:8", "const:4:8"]]
+ 00b7257c ["CALL", null, ["callee:00bddc30:8"]]
- 00b72538 bytes aaad0194
+ 00b7257c bytes adad0194
- 00b72544 ["INT_ADD", "register:40f0:8", ["const:b72544:8", "const:4:8"]]
- 00b72544 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72588 ["INT_ADD", "register:40f0:8", ["const:b72588:8", "const:4:8"]]
+ 00b72588 ["CALL", null, ["callee:00bdde10:8"]]
- 00b72544 bytes 1fae0194
+ 00b72588 bytes 22ae0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b0b7cd6f2639d078683a3d10fdbe32b"></a>

### [`00b7259c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7259c.md) → [`00b725e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b725e0.md) _ZNK8firebase4auth4User37UpdatePhoneNumberCredentialLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b725bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7259c.md#insn-00b725bc) · [`00b725c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7259c.md#insn-00b725c8) · [`00b725d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7259c.md#insn-00b725d4)
- 新版 `00b72600`（命令位置の公開資料なし） · `00b7260c`（命令位置の公開資料なし） · `00b72618`（命令位置の公開資料なし）

~~~diff
- 00b725bc ["INT_ADD", "register:40f0:8", ["const:b725bc:8", "const:4:8"]]
- 00b725bc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b72600 ["INT_ADD", "register:40f0:8", ["const:b72600:8", "const:4:8"]]
+ 00b72600 ["CALL", null, ["callee:00bddc20:8"]]
- 00b725bc bytes 85ad0194
+ 00b72600 bytes 88ad0194
- 00b725c8 ["INT_ADD", "register:40f0:8", ["const:b725c8:8", "const:4:8"]]
- 00b725c8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b7260c ["INT_ADD", "register:40f0:8", ["const:b7260c:8", "const:4:8"]]
+ 00b7260c ["CALL", null, ["callee:00bddc30:8"]]
- 00b725c8 bytes 86ad0194
+ 00b7260c bytes 89ad0194
- 00b725d4 ["INT_ADD", "register:40f0:8", ["const:b725d4:8", "const:4:8"]]
- 00b725d4 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b72618 ["INT_ADD", "register:40f0:8", ["const:b72618:8", "const:4:8"]]
+ 00b72618 ["CALL", null, ["callee:00bdde10:8"]]
- 00b725d4 bytes fbad0194
+ 00b72618 bytes fead0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe761c9dfedda38fca6111e5940b06ef"></a>

### [`00b7262c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7262c.md) → [`00b72670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72670.md) _ZN8firebase4auth4User18GetTokenThreadSafeEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbb0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc00.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7265c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7262c.md#insn-00b7265c) · [`00b72664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7262c.md#insn-00b72664) · [`00b72680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b7262c.md#insn-00b72680)
- 新版 `00b726a0`（命令位置の公開資料なし） · `00b726a8`（命令位置の公開資料なし） · `00b726c4`（命令位置の公開資料なし）

~~~diff
- 00b7265c ["INT_ADD", "register:40f0:8", ["const:b7265c:8", "const:4:8"]]
- 00b7265c ["CALL", null, ["callee:00bddc00:8"]]
+ 00b726a0 ["INT_ADD", "register:40f0:8", ["const:b726a0:8", "const:4:8"]]
+ 00b726a0 ["CALL", null, ["callee:00bddc00:8"]]
- 00b7265c bytes 55ad0194
+ 00b726a0 bytes 58ad0194
- 00b72664 ["INT_ADD", "register:40f0:8", ["const:b72664:8", "const:4:8"]]
- 00b72664 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b726a8 ["INT_ADD", "register:40f0:8", ["const:b726a8:8", "const:4:8"]]
+ 00b726a8 ["CALL", null, ["callee:00bddc20:8"]]
- 00b72664 bytes 5bad0194
+ 00b726a8 bytes 5ead0194
- 00b72680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b72680 ["INT_ADD", "register:40f0:8", ["const:b72680:8", "const:4:8"]]
- 00b72680 ["CALLIND", null, ["register:0:8"]]
+ 00b726c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b726c4 ["INT_ADD", "register:40f0:8", ["const:b726c4:8", "const:4:8"]]
+ 00b726c4 ["CALLIND", null, ["register:0:8"]]
- 00b72680 bytes 00013fd6
+ 00b726c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b413d6734ab972b7b7e9274666f985"></a>

### [`00b72874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72874.md) → [`00b728b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b728b8.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72874.md#insn-00b72884)
- 新版 `00b728c8`（命令位置の公開資料なし）

~~~diff
- 00b72884 ["INT_ADD", "register:40f0:8", ["const:b72884:8", "const:4:8"]]
- 00b72884 ["CALL", null, ["callee:00be0b80:8"]]
+ 00b728c8 ["INT_ADD", "register:40f0:8", ["const:b728c8:8", "const:4:8"]]
+ 00b728c8 ["CALL", null, ["callee:00be0b80:8"]]
- 00b72884 bytes abb80194
+ 00b728c8 bytes aeb80194
~~~


<a id="compare-8eb6b43820bc78e5c3bd3250271b91b0"></a>

### [`00b729ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b729ec.md) → [`00b72a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a30.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md) · 呼出先 1件 [`00be0eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md) · 呼出先 1件 [`00be0f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b729f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b729ec.md#insn-00b729f8)
- 新版 `00b72a3c`（命令位置の公開資料なし）

~~~diff
- 00b729f8 ["INT_ADD", "register:40f0:8", ["const:b729f8:8", "const:4:8"]]
- 00b729f8 ["CALL", null, ["callee:00be0f00:8"]]
+ 00b72a3c ["INT_ADD", "register:40f0:8", ["const:b72a3c:8", "const:4:8"]]
+ 00b72a3c ["CALL", null, ["callee:00be0f00:8"]]
- 00b729f8 bytes 2eb90194
+ 00b72a3c bytes 31b90194
~~~


<a id="compare-30968af258e90dee65b1d39868055235"></a>

### [`00b72a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md) → [`00b72a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a80.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ee0.md) · 呼出先 2件 [`00be0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ec0.md) [`00be0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ed0.md)
- 新版 呼出元 1件 [`00be0f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f30.md) · 呼出先 2件 [`00be0f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f10.md) [`00be0f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md#insn-00b72a64) · [`00b72a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a3c.md#insn-00b72a6c)
- 新版 `00b72aa8`（命令位置の公開資料なし） · `00b72ab0`（命令位置の公開資料なし）

~~~diff
- 00b72a64 ["INT_ADD", "register:40f0:8", ["const:b72a64:8", "const:4:8"]]
- 00b72a64 ["CALL", null, ["callee:00be0f20:8"]]
+ 00b72aa8 ["INT_ADD", "register:40f0:8", ["const:b72aa8:8", "const:4:8"]]
+ 00b72aa8 ["CALL", null, ["callee:00be0f20:8"]]
- 00b72a64 bytes 1bb90194
+ 00b72aa8 bytes 1eb90194
- 00b72a6c ["INT_ADD", "register:40f0:8", ["const:b72a6c:8", "const:4:8"]]
- 00b72a6c ["CALL", null, ["callee:00be0f10:8"]]
+ 00b72ab0 ["INT_ADD", "register:40f0:8", ["const:b72ab0:8", "const:4:8"]]
+ 00b72ab0 ["CALL", null, ["callee:00be0f10:8"]]
- 00b72a6c bytes 15b90194
+ 00b72ab0 bytes 18b90194
~~~


<a id="compare-b5054b5dfb5d1026bd6b96e4caece0f9"></a>

### [`00b72ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72ad4.md) → [`00b72b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b18.md) _ZSt17current_exceptionv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6c0.md) · 呼出先 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md)
- 新版 呼出元 1件 [`00bdb710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb710.md) · 呼出先 1件 [`00be0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72ad4.md#insn-00b72ae8)
- 新版 `00b72b2c`（命令位置の公開資料なし）

~~~diff
- 00b72ae8 ["INT_ADD", "register:40f0:8", ["const:b72ae8:8", "const:4:8"]]
- 00b72ae8 ["CALL", null, ["callee:00be0f40:8"]]
+ 00b72b2c ["INT_ADD", "register:40f0:8", ["const:b72b2c:8", "const:4:8"]]
+ 00b72b2c ["CALL", null, ["callee:00be0f40:8"]]
- 00b72ae8 bytes 02b90194
+ 00b72b2c bytes 05b90194
~~~


<a id="compare-7f3c46436c3b17969938c28ee5efa3fb"></a>

### [`00b72b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b18.md) → [`00b72b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b5c.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b18.md#insn-00b72b2c)
- 新版 `00b72b70`（命令位置の公開資料なし）

~~~diff
- 00b72b2c ["INT_ADD", "register:40f0:8", ["const:b72b2c:8", "const:4:8"]]
- 00b72b2c ["CALL", null, ["callee:00be0f50:8"]]
+ 00b72b70 ["INT_ADD", "register:40f0:8", ["const:b72b70:8", "const:4:8"]]
+ 00b72b70 ["CALL", null, ["callee:00be0f50:8"]]
- 00b72b2c bytes f5b80194
+ 00b72b70 bytes f8b80194
~~~


<a id="compare-5a8ba09bcdd448888dbbe9f17431ded0"></a>

### [`00b72b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md) → [`00b72b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b88.md) _ZNKSt16nested_exception14rethrow_nestedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md) [`00bdb620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb620.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md) [`00bdb670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md#insn-00b72b68) · [`00b72b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md#insn-00b72b70) · [`00b72b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md#insn-00b72b7c)
- 新版 `00b72bac`（命令位置の公開資料なし） · `00b72bb4`（命令位置の公開資料なし） · `00b72bc0`（命令位置の公開資料なし）

~~~diff
- 00b72b68 ["INT_ADD", "register:40f0:8", ["const:b72b68:8", "const:4:8"]]
- 00b72b68 ["CALL", null, ["callee:00bdb4a0:8"]]
+ 00b72bac ["INT_ADD", "register:40f0:8", ["const:b72bac:8", "const:4:8"]]
+ 00b72bac ["CALL", null, ["callee:00bdb4a0:8"]]
- 00b72b68 bytes 3aa20194
+ 00b72bac bytes 3da20194
- 00b72b70 ["INT_ADD", "register:40f0:8", ["const:b72b70:8", "const:4:8"]]
- 00b72b70 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00b72bb4 ["INT_ADD", "register:40f0:8", ["const:b72bb4:8", "const:4:8"]]
+ 00b72bb4 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00b72b70 bytes 84a10194
+ 00b72bb4 bytes 87a10194
- 00b72b7c ["INT_ADD", "register:40f0:8", ["const:b72b7c:8", "const:4:8"]]
- 00b72b7c ["CALL", null, ["callee:00bdb660:8"]]
+ 00b72bc0 ["INT_ADD", "register:40f0:8", ["const:b72bc0:8", "const:4:8"]]
+ 00b72bc0 ["CALL", null, ["callee:00bdb660:8"]]
- 00b72b7c bytes a5a20194
+ 00b72bc0 bytes a8a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9dcf031a04ee4cb4260490900915790"></a>

### [`00b72b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md) → [`00b72be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72be0.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb620.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be0f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f10.md)
- 新版 呼出元 1件 [`00bdb670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb670.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be0f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b72bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md#insn-00b72bac) · [`00b72bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b9c.md#insn-00b72bb0)
- 新版 `00b72bf0`（命令位置の公開資料なし） · `00b72bf4`（命令位置の公開資料なし）

~~~diff
- 00b72bac ["INT_ADD", "register:40f0:8", ["const:b72bac:8", "const:4:8"]]
- 00b72bac ["CALL", null, ["callee:00be0f60:8"]]
+ 00b72bf0 ["INT_ADD", "register:40f0:8", ["const:b72bf0:8", "const:4:8"]]
+ 00b72bf0 ["CALL", null, ["callee:00be0f60:8"]]
- 00b72bac bytes d9b80194
+ 00b72bf0 bytes dcb80194
- 00b72bb0 ["INT_ADD", "register:40f0:8", ["const:b72bb0:8", "const:4:8"]]
- 00b72bb0 ["CALL", null, ["callee:00bdb1d0:8"]]
+ 00b72bf4 ["INT_ADD", "register:40f0:8", ["const:b72bf4:8", "const:4:8"]]
+ 00b72bf4 ["CALL", null, ["callee:00bdb1d0:8"]]
- 00b72bb0 bytes 74a10194
+ 00b72bf4 bytes 77a10194
~~~


<a id="compare-964d5c7b29674e6c1fb634ea6e713e44"></a>

### [`00b72bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72bb4.md) → [`00b72bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd980.md) · 呼出先 1件 [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md)
- 新版 呼出元 1件 [`00bdd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9d0.md) · 呼出先 1件 [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b732d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72bb4.md#insn-00b732d0)
- 新版 `00b73314`（命令位置の公開資料なし）

~~~diff
- 00b732d0 ["INT_ADD", "register:40f0:8", ["const:b732d0:8", "const:4:8"]]
- 00b732d0 ["CALL", null, ["callee:00b73318:8"]]
+ 00b73314 ["INT_ADD", "register:40f0:8", ["const:b73314:8", "const:4:8"]]
+ 00b73314 ["CALL", null, ["callee:00b73318:8"]]
- 00b732d0 bytes 01000094
+ 00b73314 bytes 01000094
~~~


<a id="compare-3d98e0fb5c78070de072682980e0af26"></a>

### [`00b73368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73368.md) → [`00b733ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733ac.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd8f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7337c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73368.md#insn-00b7337c)
- 新版 `00b733c0`（命令位置の公開資料なし）

~~~diff
- 00b7337c ["INT_ADD", "register:40f0:8", ["const:b7337c:8", "const:4:8"]]
- 00b7337c ["CALL", null, ["callee:00bdd940:8"]]
+ 00b733c0 ["INT_ADD", "register:40f0:8", ["const:b733c0:8", "const:4:8"]]
+ 00b733c0 ["CALL", null, ["callee:00bdd940:8"]]
- 00b7337c bytes 5da90194
+ 00b733c0 bytes 60a90194
~~~


<a id="compare-6bc6d92edc0c4b0c49b9071e71f72c0c"></a>

### [`00b733bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733bc.md) → [`00b73400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73400.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b733d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733bc.md#insn-00b733d0)
- 新版 `00b73414`（命令位置の公開資料なし）

~~~diff
- 00b733d0 ["INT_ADD", "register:40f0:8", ["const:b733d0:8", "const:4:8"]]
- 00b733d0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00b73414 ["INT_ADD", "register:40f0:8", ["const:b73414:8", "const:4:8"]]
+ 00b73414 ["CALL", null, ["callee:00bd6e60:8"]]
- 00b733d0 bytes 948e0194
+ 00b73414 bytes 938e0194
~~~


<a id="compare-bd708673ddfd75d249c94a182bb1a2b8"></a>

### [`00b733e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md) → [`00b73424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73424.md) _ZNSt6__ndk114__shared_count16__release_sharedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b733fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md#insn-00b733fc) · [`00b73414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b733e0.md#insn-00b73414)
- 新版 `00b73440`（命令位置の公開資料なし） · `00b73458`（命令位置の公開資料なし）

~~~diff
- 00b733fc ["INT_ADD", "register:40f0:8", ["const:b733fc:8", "const:4:8"]]
- 00b733fc ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b73440 ["INT_ADD", "register:40f0:8", ["const:b73440:8", "const:4:8"]]
+ 00b73440 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b733fc bytes 958e0194
+ 00b73440 bytes 948e0194
- 00b73414 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b73414 ["INT_ADD", "register:40f0:8", ["const:b73414:8", "const:4:8"]]
- 00b73414 ["CALLIND", null, ["register:0:8"]]
+ 00b73458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b73458 ["INT_ADD", "register:40f0:8", ["const:b73458:8", "const:4:8"]]
+ 00b73458 ["CALLIND", null, ["register:0:8"]]
- 00b73414 bytes 00013fd6
+ 00b73458 bytes 00013fd6
~~~


<a id="compare-f27f216005b8fff7b645c9648bc6389c"></a>

### [`00b73430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73430.md) → [`00b73474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73474.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73430.md#insn-00b73444)
- 新版 `00b73488`（命令位置の公開資料なし）

~~~diff
- 00b73444 ["INT_ADD", "register:40f0:8", ["const:b73444:8", "const:4:8"]]
- 00b73444 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00b73488 ["INT_ADD", "register:40f0:8", ["const:b73488:8", "const:4:8"]]
+ 00b73488 ["CALL", null, ["callee:00bd6e60:8"]]
- 00b73444 bytes 778e0194
+ 00b73488 bytes 768e0194
~~~


<a id="compare-5fcc5e37ccb25d655fb5fc3531138baa"></a>

### [`00b73454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73454.md) → [`00b73498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73498.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73454.md#insn-00b73468)
- 新版 `00b734ac`（命令位置の公開資料なし）

~~~diff
- 00b73468 ["INT_ADD", "register:40f0:8", ["const:b73468:8", "const:4:8"]]
- 00b73468 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00b734ac ["INT_ADD", "register:40f0:8", ["const:b734ac:8", "const:4:8"]]
+ 00b734ac ["CALL", null, ["callee:00bd6e60:8"]]
- 00b73468 bytes 6e8e0194
+ 00b734ac bytes 6d8e0194
~~~


<a id="compare-3901201c987b3bc90cbb587e3c3051de"></a>

### [`00b73478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md) → [`00b734bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b734bc.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b73494) · [`00b734bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b734bc) · [`00b734d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73478.md#insn-00b734d0)
- 新版 `00b734d8`（命令位置の公開資料なし） · `00b73500`（命令位置の公開資料なし） · `00b73514`（命令位置の公開資料なし）

~~~diff
- 00b73494 ["INT_ADD", "register:40f0:8", ["const:b73494:8", "const:4:8"]]
- 00b73494 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b734d8 ["INT_ADD", "register:40f0:8", ["const:b734d8:8", "const:4:8"]]
+ 00b734d8 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b73494 bytes 6f8e0194
+ 00b734d8 bytes 6e8e0194
- 00b734bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b734bc ["INT_ADD", "register:40f0:8", ["const:b734bc:8", "const:4:8"]]
- 00b734bc ["CALLIND", null, ["register:0:8"]]
+ 00b73500 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b73500 ["INT_ADD", "register:40f0:8", ["const:b73500:8", "const:4:8"]]
+ 00b73500 ["CALLIND", null, ["register:0:8"]]
- 00b734bc bytes 00013fd6
+ 00b73500 bytes 00013fd6
- 00b734d0 ["INT_ADD", "register:40f0:8", ["const:b734d0:8", "const:4:8"]]
- 00b734d0 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b73514 ["INT_ADD", "register:40f0:8", ["const:b73514:8", "const:4:8"]]
+ 00b73514 ["CALL", null, ["callee:00bd6e90:8"]]
- 00b734d0 bytes 608e0194
+ 00b73514 bytes 5f8e0194
~~~


<a id="compare-6f67d3a9c3eeb1cfe6194e34d3eb7ff4"></a>

### [`00b734f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b734f4.md) → [`00b73538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73538.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b734f4.md#insn-00b73518)
- 新版 `00b7355c`（命令位置の公開資料なし）

~~~diff
- 00b73518 ["INT_ADD", "register:40f0:8", ["const:b73518:8", "const:4:8"]]
- 00b73518 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00b7355c ["INT_ADD", "register:40f0:8", ["const:b7355c:8", "const:4:8"]]
+ 00b7355c ["CALL", null, ["callee:00bd6e90:8"]]
- 00b73518 bytes 4e8e0194
+ 00b7355c bytes 4d8e0194
~~~


<a id="compare-8f1e5d808ce6572efa3939cea7c06cba"></a>

### [`00b7354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md) → [`00b73590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73590.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb650.md) · 呼出先 1件 [`00bd6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md)
- 新版 呼出元 1件 [`00bdb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6a0.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7357c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md#insn-00b7357c)
- 新版 `00b735c0`（命令位置の公開資料なし）

~~~diff
- 00b7357c ["INT_ADD", "register:40f0:8", ["const:b7357c:8", "const:4:8"]]
- 00b7357c ["CALL", null, ["callee:00bd6d90:8"]]
+ 00b735c0 ["INT_ADD", "register:40f0:8", ["const:b735c0:8", "const:4:8"]]
+ 00b735c0 ["CALL", null, ["callee:00bd6d90:8"]]
- 00b7357c bytes f58d0194
+ 00b735c0 bytes f48d0194
~~~


<a id="compare-a4fee1b0811e2719483306cd9c8e724f"></a>

### [`00b735b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735b8.md) → [`00b735fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b735fc.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b735c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735b8.md#insn-00b735c8)
- 新版 `00b7360c`（命令位置の公開資料なし）

~~~diff
- 00b735c8 ["INT_ADD", "register:40f0:8", ["const:b735c8:8", "const:4:8"]]
- 00b735c8 ["CALL", null, ["callee:00bde820:8"]]
+ 00b7360c ["INT_ADD", "register:40f0:8", ["const:b7360c:8", "const:4:8"]]
+ 00b7360c ["CALL", null, ["callee:00bde820:8"]]
- 00b735c8 bytes 82ac0194
+ 00b7360c bytes 85ac0194
~~~


<a id="compare-c6de2c8ca1ba83d273bbc072b9802a36"></a>

### [`00b735dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735dc.md) → [`00b73620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73620.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b735ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b735dc.md#insn-00b735ec)
- 新版 `00b73630`（命令位置の公開資料なし）

~~~diff
- 00b735ec ["INT_ADD", "register:40f0:8", ["const:b735ec:8", "const:4:8"]]
- 00b735ec ["CALL", null, ["callee:00bde830:8"]]
+ 00b73630 ["INT_ADD", "register:40f0:8", ["const:b73630:8", "const:4:8"]]
+ 00b73630 ["CALL", null, ["callee:00bde830:8"]]
- 00b735ec bytes 7dac0194
+ 00b73630 bytes 80ac0194
~~~


<a id="compare-fbd467399ccc1a0c899f3b512833b0ac"></a>

### [`00b73600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73600.md) → [`00b73644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73644.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

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
      "definition_site": "00b73690",
      "incomplete_value": true,
      "site": "00b73694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24808:8"
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
      "definition_site": "00b7364c",
      "incomplete_value": true,
      "site": "00b73650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c247b8:8"
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

- 旧版 [`00b73640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73600.md#insn-00b73640)
- 新版 `00b73684`（命令位置の公開資料なし）

~~~diff
- 00b73640 ["COPY", "register:4048:8", ["const:c247b8:8"]]
+ 00b73684 ["COPY", "register:4048:8", ["const:c24808:8"]]
- 00b73640 bytes c98b5810
+ 00b73684 bytes 298c5810
~~~


<a id="compare-95a846e2561b7547bca8a1abbe71e8e1"></a>

### [`00b73830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md) → [`00b73874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md#insn-00b73858) · [`00b73864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md#insn-00b73864) · [`00b73874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md#insn-00b73874)
- 新版 `00b7389c`（命令位置の公開資料なし） · `00b738a8`（命令位置の公開資料なし） · `00b738b8`（命令位置の公開資料なし）

~~~diff
- 00b73858 ["INT_ADD", "register:40f0:8", ["const:b73858:8", "const:4:8"]]
- 00b73858 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00b7389c ["INT_ADD", "register:40f0:8", ["const:b7389c:8", "const:4:8"]]
+ 00b7389c ["CALL", null, ["callee:00bd6e30:8"]]
- 00b73858 bytes 668d0194
+ 00b7389c bytes 658d0194
- 00b73864 ["INT_ADD", "register:40f0:8", ["const:b73864:8", "const:4:8"]]
- 00b73864 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00b738a8 ["INT_ADD", "register:40f0:8", ["const:b738a8:8", "const:4:8"]]
+ 00b738a8 ["CALL", null, ["callee:00bd6e30:8"]]
- 00b73864 bytes 638d0194
+ 00b738a8 bytes 628d0194
- 00b73874 ["INT_ADD", "register:40f0:8", ["const:b73874:8", "const:4:8"]]
- 00b73874 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b738b8 ["INT_ADD", "register:40f0:8", ["const:b738b8:8", "const:4:8"]]
+ 00b738b8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b73874 bytes e79d0194
+ 00b738b8 bytes ea9d0194
~~~


<a id="compare-75a4ce45bc8f8681550a942cef38a87d"></a>

### [`00b739e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md) → [`00b73a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a24.md) _ZNSt13runtime_erroraSERKS_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a08) · [`00b73a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a14) · [`00b73a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md#insn-00b73a24)
- 新版 `00b73a4c`（命令位置の公開資料なし） · `00b73a58`（命令位置の公開資料なし） · `00b73a68`（命令位置の公開資料なし）

~~~diff
- 00b73a08 ["INT_ADD", "register:40f0:8", ["const:b73a08:8", "const:4:8"]]
- 00b73a08 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00b73a4c ["INT_ADD", "register:40f0:8", ["const:b73a4c:8", "const:4:8"]]
+ 00b73a4c ["CALL", null, ["callee:00bd6e30:8"]]
- 00b73a08 bytes fa8c0194
+ 00b73a4c bytes f98c0194
- 00b73a14 ["INT_ADD", "register:40f0:8", ["const:b73a14:8", "const:4:8"]]
- 00b73a14 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00b73a58 ["INT_ADD", "register:40f0:8", ["const:b73a58:8", "const:4:8"]]
+ 00b73a58 ["CALL", null, ["callee:00bd6e30:8"]]
- 00b73a14 bytes f78c0194
+ 00b73a58 bytes f68c0194
- 00b73a24 ["INT_ADD", "register:40f0:8", ["const:b73a24:8", "const:4:8"]]
- 00b73a24 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b73a68 ["INT_ADD", "register:40f0:8", ["const:b73a68:8", "const:4:8"]]
+ 00b73a68 ["CALL", null, ["callee:00bdb060:8"]]
- 00b73a24 bytes 7b9d0194
+ 00b73a68 bytes 7e9d0194
~~~


<a id="compare-3d14a9165f65218beae35f95ee2acbde"></a>

### [`00b73a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a90.md) → [`00b73ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73ad4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md) · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)
- 新版 呼出元 1件 [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md) · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a90.md#insn-00b73b30) · [`00b73b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a90.md#insn-00b73b7c) · [`00b73b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a90.md#insn-00b73b8c)
- 新版 `00b73b74`（命令位置の公開資料なし） · `00b73bc0`（命令位置の公開資料なし） · `00b73bd0`（命令位置の公開資料なし）

~~~diff
- 00b73b30 ["INT_ADD", "register:40f0:8", ["const:b73b30:8", "const:4:8"]]
- 00b73b30 ["CALL", null, ["callee:00bde220:8"]]
+ 00b73b74 ["INT_ADD", "register:40f0:8", ["const:b73b74:8", "const:4:8"]]
+ 00b73b74 ["CALL", null, ["callee:00bde220:8"]]
- 00b73b30 bytes a8a90194
+ 00b73b74 bytes aba90194
- 00b73b7c ["INT_ADD", "register:40f0:8", ["const:b73b7c:8", "const:4:8"]]
- 00b73b7c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b73bc0 ["INT_ADD", "register:40f0:8", ["const:b73bc0:8", "const:4:8"]]
+ 00b73bc0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b73b7c bytes 499d0194
+ 00b73bc0 bytes 4c9d0194
- 00b73b8c ["INT_ADD", "register:40f0:8", ["const:b73b8c:8", "const:4:8"]]
- 00b73b8c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b73bd0 ["INT_ADD", "register:40f0:8", ["const:b73bd0:8", "const:4:8"]]
+ 00b73bd0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b73b8c bytes 459d0194
+ 00b73bd0 bytes 489d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57a109defbd53069f23ad5633c44d849"></a>

### [`00b73d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md) → [`00b73d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73d60.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73d78) · [`00b73d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73d9c) · [`00b73dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73d1c.md#insn-00b73dbc)
- 新版 `00b73dbc`（命令位置の公開資料なし） · `00b73de0`（命令位置の公開資料なし） · `00b73e00`（命令位置の公開資料なし）

~~~diff
- 00b73d78 ["INT_ADD", "register:40f0:8", ["const:b73d78:8", "const:4:8"]]
- 00b73d78 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b73dbc ["INT_ADD", "register:40f0:8", ["const:b73dbc:8", "const:4:8"]]
+ 00b73dbc ["CALL", null, ["callee:00bdb040:8"]]
- 00b73d78 bytes 9e9c0194
+ 00b73dbc bytes a19c0194
- 00b73d9c ["INT_ADD", "register:40f0:8", ["const:b73d9c:8", "const:4:8"]]
- 00b73d9c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b73de0 ["INT_ADD", "register:40f0:8", ["const:b73de0:8", "const:4:8"]]
+ 00b73de0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b73d9c bytes c19c0194
+ 00b73de0 bytes c49c0194
- 00b73dbc ["INT_ADD", "register:40f0:8", ["const:b73dbc:8", "const:4:8"]]
- 00b73dbc ["CALL", null, ["callee:00418c24:8"]]
+ 00b73e00 ["INT_ADD", "register:40f0:8", ["const:b73e00:8", "const:4:8"]]
+ 00b73e00 ["CALL", null, ["callee:00418c24:8"]]
- 00b73dbc bytes 9a93e297
+ 00b73e00 bytes 8993e297
~~~


<a id="compare-665bfa300a985178de91e1e19fa5e8ba"></a>

### [`00b73dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73dec.md) → [`00b73e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73e30.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1e0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00bdb230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb230.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73dec.md#insn-00b73e14)
- 新版 `00b73e58`（命令位置の公開資料なし）

~~~diff
- 00b73e14 ["INT_ADD", "register:40f0:8", ["const:b73e14:8", "const:4:8"]]
- 00b73e14 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b73e58 ["INT_ADD", "register:40f0:8", ["const:b73e58:8", "const:4:8"]]
+ 00b73e58 ["CALL", null, ["callee:00bdb190:8"]]
- 00b73e14 bytes cb9c0194
+ 00b73e58 bytes ce9c0194
~~~


<a id="compare-59a1a06426d75efa9fc21bf7241583ee"></a>

### [`00b73e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73e6c.md) → [`00b73eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73eb0.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73e6c.md#insn-00b73ec8)
- 新版 `00b73f0c`（命令位置の公開資料なし）

~~~diff
- 00b73ec8 ["INT_ADD", "register:40f0:8", ["const:b73ec8:8", "const:4:8"]]
- 00b73ec8 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b73f0c ["INT_ADD", "register:40f0:8", ["const:b73f0c:8", "const:4:8"]]
+ 00b73f0c ["CALL", null, ["callee:00bdb180:8"]]
- 00b73ec8 bytes 9a9c0194
+ 00b73f0c bytes 9d9c0194
~~~


<a id="compare-e3ca3df8ce091f4383b87c0b5f134ef2"></a>

### [`00b73f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f04.md) → [`00b73f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73f48.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b73f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f04.md#insn-00b73f58)
- 新版 `00b73f9c`（命令位置の公開資料なし）

~~~diff
- 00b73f58 ["INT_ADD", "register:40f0:8", ["const:b73f58:8", "const:4:8"]]
- 00b73f58 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b73f9c ["INT_ADD", "register:40f0:8", ["const:b73f9c:8", "const:4:8"]]
+ 00b73f9c ["CALL", null, ["callee:00bdb180:8"]]
- 00b73f58 bytes 769c0194
+ 00b73f9c bytes 799c0194
~~~


<a id="compare-b8bfa69b302c298a35cfc32a7455b222"></a>

### [`00b73f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f90.md) → [`00b73fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73fd4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f90.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be0fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fe0.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f90.md#insn-00b74074) · [`00b740a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f90.md#insn-00b740a0) · [`00b740b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f90.md#insn-00b740b8)
- 新版 `00b740b8`（命令位置の公開資料なし） · `00b740e4`（命令位置の公開資料なし） · `00b740fc`（命令位置の公開資料なし）

~~~diff
- 00b74074 ["INT_ADD", "register:40f0:8", ["const:b74074:8", "const:4:8"]]
- 00b74074 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b740b8 ["INT_ADD", "register:40f0:8", ["const:b740b8:8", "const:4:8"]]
+ 00b740b8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74074 bytes 0b9c0194
+ 00b740b8 bytes 0e9c0194
- 00b740a0 ["INT_ADD", "register:40f0:8", ["const:b740a0:8", "const:4:8"]]
- 00b740a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b740e4 ["INT_ADD", "register:40f0:8", ["const:b740e4:8", "const:4:8"]]
+ 00b740e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b740a0 bytes d49b0194
+ 00b740e4 bytes d79b0194
- 00b740b8 ["INT_ADD", "register:40f0:8", ["const:b740b8:8", "const:4:8"]]
- 00b740b8 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b740fc ["INT_ADD", "register:40f0:8", ["const:b740fc:8", "const:4:8"]]
+ 00b740fc ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b740b8 bytes fa9b0194
+ 00b740fc bytes fd9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa65f2c1537c8ebc3757af05e487ae0"></a>

### [`00b74150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md) → [`00b74194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) FUN_00b74194

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b74418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00b7445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b741fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md#insn-00b741fc) · [`00b74214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md#insn-00b74214) · [`00b74234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md#insn-00b74234)
- 新版 `00b74240`（命令位置の公開資料なし） · `00b74258`（命令位置の公開資料なし） · `00b74278`（命令位置の公開資料なし）

~~~diff
- 00b741fc ["INT_ADD", "register:40f0:8", ["const:b741fc:8", "const:4:8"]]
- 00b741fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74240 ["INT_ADD", "register:40f0:8", ["const:b74240:8", "const:4:8"]]
+ 00b74240 ["CALL", null, ["callee:00bdb040:8"]]
- 00b741fc bytes 7d9b0194
+ 00b74240 bytes 809b0194
- 00b74214 ["INT_ADD", "register:40f0:8", ["const:b74214:8", "const:4:8"]]
- 00b74214 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74258 ["INT_ADD", "register:40f0:8", ["const:b74258:8", "const:4:8"]]
+ 00b74258 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74214 bytes a39b0194
+ 00b74258 bytes a69b0194
- 00b74234 ["INT_ADD", "register:40f0:8", ["const:b74234:8", "const:4:8"]]
- 00b74234 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74278 ["INT_ADD", "register:40f0:8", ["const:b74278:8", "const:4:8"]]
+ 00b74278 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74234 bytes 9b9b0194
+ 00b74278 bytes 9e9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e118c2c56368b4e6ecc4cdb7e134043"></a>

### [`00b742b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b742b8.md) → [`00b742fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b742fc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b742b8.md#insn-00b74314) · [`00b74334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b742b8.md#insn-00b74334) · [`00b74354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b742b8.md#insn-00b74354)
- 新版 `00b74358`（命令位置の公開資料なし） · `00b74378`（命令位置の公開資料なし） · `00b74398`（命令位置の公開資料なし）

~~~diff
- 00b74314 ["INT_ADD", "register:40f0:8", ["const:b74314:8", "const:4:8"]]
- 00b74314 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74358 ["INT_ADD", "register:40f0:8", ["const:b74358:8", "const:4:8"]]
+ 00b74358 ["CALL", null, ["callee:00bdb040:8"]]
- 00b74314 bytes 379b0194
+ 00b74358 bytes 3a9b0194
- 00b74334 ["INT_ADD", "register:40f0:8", ["const:b74334:8", "const:4:8"]]
- 00b74334 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74378 ["INT_ADD", "register:40f0:8", ["const:b74378:8", "const:4:8"]]
+ 00b74378 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74334 bytes 5b9b0194
+ 00b74378 bytes 5e9b0194
- 00b74354 ["INT_ADD", "register:40f0:8", ["const:b74354:8", "const:4:8"]]
- 00b74354 ["CALL", null, ["callee:00418c24:8"]]
+ 00b74398 ["INT_ADD", "register:40f0:8", ["const:b74398:8", "const:4:8"]]
+ 00b74398 ["CALL", null, ["callee:00418c24:8"]]
- 00b74354 bytes 3492e297
+ 00b74398 bytes 2392e297
~~~


<a id="compare-dfb61c5aa2cb8377cce5e93a2e096aff"></a>

### [`00b74358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74358.md) → [`00b7439c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7439c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74358.md#insn-00b74398)
- 新版 `00b743dc`（命令位置の公開資料なし）

~~~diff
- 00b74398 ["INT_ADD", "register:40f0:8", ["const:b74398:8", "const:4:8"]]
- 00b74398 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b743dc ["INT_ADD", "register:40f0:8", ["const:b743dc:8", "const:4:8"]]
+ 00b743dc ["CALL", null, ["callee:0041fddc:8"]]
- 00b74398 bytes 91aee297
+ 00b743dc bytes 80aee297
~~~


<a id="compare-fbca21026521e06a815ab6362fd0285f"></a>

### [`00b74418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md) → [`00b7445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b74150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b744b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744b0) · [`00b744e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744e8) · [`00b744fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md#insn-00b744fc)
- 新版 `00b744f4`（命令位置の公開資料なし） · `00b7452c`（命令位置の公開資料なし） · `00b74540`（命令位置の公開資料なし）

~~~diff
- 00b744b0 ["INT_ADD", "register:40f0:8", ["const:b744b0:8", "const:4:8"]]
- 00b744b0 ["CALL", null, ["callee:00b74194:8"]]
+ 00b744f4 ["INT_ADD", "register:40f0:8", ["const:b744f4:8", "const:4:8"]]
+ 00b744f4 ["CALL", null, ["callee:00b74194:8"]]
- 00b744b0 bytes 28ffff97
+ 00b744f4 bytes 28ffff97
- 00b744e8 ["INT_ADD", "register:40f0:8", ["const:b744e8:8", "const:4:8"]]
- 00b744e8 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b7452c ["INT_ADD", "register:40f0:8", ["const:b7452c:8", "const:4:8"]]
+ 00b7452c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b744e8 bytes ee9a0194
+ 00b7452c bytes f19a0194
- 00b744fc ["INT_ADD", "register:40f0:8", ["const:b744fc:8", "const:4:8"]]
- 00b744fc ["CALL", null, ["callee:00bdb240:8"]]
+ 00b74540 ["INT_ADD", "register:40f0:8", ["const:b74540:8", "const:4:8"]]
+ 00b74540 ["CALL", null, ["callee:00bdb240:8"]]
- 00b744fc bytes 3d9b0194
+ 00b74540 bytes 409b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9003a027fe239f9b1cac45d9129c26b2"></a>

### [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md) → [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md) FUN_00b74590

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b74698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74698.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00b746dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b746dc.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b745fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md#insn-00b745fc) · [`00b7463c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md#insn-00b7463c) · [`00b7464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md#insn-00b7464c)
- 新版 `00b74640`（命令位置の公開資料なし） · `00b74680`（命令位置の公開資料なし） · `00b74690`（命令位置の公開資料なし）

~~~diff
- 00b745fc ["INT_ADD", "register:40f0:8", ["const:b745fc:8", "const:4:8"]]
- 00b745fc ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74640 ["INT_ADD", "register:40f0:8", ["const:b74640:8", "const:4:8"]]
+ 00b74640 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b745fc bytes a99a0194
+ 00b74640 bytes ac9a0194
- 00b7463c ["INT_ADD", "register:40f0:8", ["const:b7463c:8", "const:4:8"]]
- 00b7463c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74680 ["INT_ADD", "register:40f0:8", ["const:b74680:8", "const:4:8"]]
+ 00b74680 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7463c bytes 6d9a0194
+ 00b74680 bytes 709a0194
- 00b7464c ["INT_ADD", "register:40f0:8", ["const:b7464c:8", "const:4:8"]]
- 00b7464c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b74690 ["INT_ADD", "register:40f0:8", ["const:b74690:8", "const:4:8"]]
+ 00b74690 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b7464c bytes c59a0194
+ 00b74690 bytes c89a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07bfa17b19a4c43adcdd16fbac35fc15"></a>

### [`00b74698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74698.md) → [`00b746dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b746dc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b746e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74698.md#insn-00b746e4)
- 新版 `00b74728`（命令位置の公開資料なし）

~~~diff
- 00b746e4 ["INT_ADD", "register:40f0:8", ["const:b746e4:8", "const:4:8"]]
- 00b746e4 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74728 ["INT_ADD", "register:40f0:8", ["const:b74728:8", "const:4:8"]]
+ 00b74728 ["CALL", null, ["callee:0041fddc:8"]]
- 00b746e4 bytes beade297
+ 00b74728 bytes adade297
~~~


<a id="compare-040e40c477a97c45690edd1ee8281a24"></a>

### [`00b746e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b746e8.md) → [`00b7472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7472c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b746e8.md#insn-00b7473c) · [`00b74754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b746e8.md#insn-00b74754)
- 新版 `00b74780`（命令位置の公開資料なし） · `00b74798`（命令位置の公開資料なし）

~~~diff
- 00b7473c ["INT_ADD", "register:40f0:8", ["const:b7473c:8", "const:4:8"]]
- 00b7473c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74780 ["INT_ADD", "register:40f0:8", ["const:b74780:8", "const:4:8"]]
+ 00b74780 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7473c bytes 599a0194
+ 00b74780 bytes 5c9a0194
- 00b74754 ["INT_ADD", "register:40f0:8", ["const:b74754:8", "const:4:8"]]
- 00b74754 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74798 ["INT_ADD", "register:40f0:8", ["const:b74798:8", "const:4:8"]]
+ 00b74798 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74754 bytes a2ade297
+ 00b74798 bytes 91ade297
~~~


<a id="compare-b5222982f880c7d976d2302ff8434d20"></a>

### [`00b74758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74758.md) → [`00b7479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7479c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b747e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74758.md#insn-00b747e4) · [`00b74804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74758.md#insn-00b74804) · [`00b74828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74758.md#insn-00b74828)
- 新版 `00b74828`（命令位置の公開資料なし） · `00b74848`（命令位置の公開資料なし） · `00b7486c`（命令位置の公開資料なし）

~~~diff
- 00b747e4 ["INT_ADD", "register:40f0:8", ["const:b747e4:8", "const:4:8"]]
- 00b747e4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74828 ["INT_ADD", "register:40f0:8", ["const:b74828:8", "const:4:8"]]
+ 00b74828 ["CALL", null, ["callee:00bdb040:8"]]
- 00b747e4 bytes 039a0194
+ 00b74828 bytes 069a0194
- 00b74804 ["INT_ADD", "register:40f0:8", ["const:b74804:8", "const:4:8"]]
- 00b74804 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74848 ["INT_ADD", "register:40f0:8", ["const:b74848:8", "const:4:8"]]
+ 00b74848 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74804 bytes 279a0194
+ 00b74848 bytes 2a9a0194
- 00b74828 ["INT_ADD", "register:40f0:8", ["const:b74828:8", "const:4:8"]]
- 00b74828 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b7486c ["INT_ADD", "register:40f0:8", ["const:b7486c:8", "const:4:8"]]
+ 00b7486c ["CALL", null, ["callee:0041fddc:8"]]
- 00b74828 bytes 6dade297
+ 00b7486c bytes 5cade297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af361f39f52b6df7b500dadebdb35dd4"></a>

### [`00b74834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74834.md) → [`00b74878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74878.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb730.md) · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00bdb780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb780.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7487c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74834.md#insn-00b7487c)
- 新版 `00b748c0`（命令位置の公開資料なし）

~~~diff
- 00b7487c ["INT_ADD", "register:40f0:8", ["const:b7487c:8", "const:4:8"]]
- 00b7487c ["CALL", null, ["callee:00bdb180:8"]]
+ 00b748c0 ["INT_ADD", "register:40f0:8", ["const:b748c0:8", "const:4:8"]]
+ 00b748c0 ["CALL", null, ["callee:00bdb180:8"]]
- 00b7487c bytes 2d9a0194
+ 00b748c0 bytes 309a0194
~~~


<a id="compare-86d83eaf4766f924f418d58d3ff5d81c"></a>

### [`00b748a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md) → [`00b748e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b748e8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74900) · [`00b74920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74920) · [`00b74940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b748a4.md#insn-00b74940)
- 新版 `00b74944`（命令位置の公開資料なし） · `00b74964`（命令位置の公開資料なし） · `00b74984`（命令位置の公開資料なし）

~~~diff
- 00b74900 ["INT_ADD", "register:40f0:8", ["const:b74900:8", "const:4:8"]]
- 00b74900 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74944 ["INT_ADD", "register:40f0:8", ["const:b74944:8", "const:4:8"]]
+ 00b74944 ["CALL", null, ["callee:00bdb040:8"]]
- 00b74900 bytes bc990194
+ 00b74944 bytes bf990194
- 00b74920 ["INT_ADD", "register:40f0:8", ["const:b74920:8", "const:4:8"]]
- 00b74920 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b74964 ["INT_ADD", "register:40f0:8", ["const:b74964:8", "const:4:8"]]
+ 00b74964 ["CALL", null, ["callee:00bdb240:8"]]
- 00b74920 bytes 349a0194
+ 00b74964 bytes 379a0194
- 00b74940 ["INT_ADD", "register:40f0:8", ["const:b74940:8", "const:4:8"]]
- 00b74940 ["CALL", null, ["callee:00418c24:8"]]
+ 00b74984 ["INT_ADD", "register:40f0:8", ["const:b74984:8", "const:4:8"]]
+ 00b74984 ["CALL", null, ["callee:00418c24:8"]]
- 00b74940 bytes b990e297
+ 00b74984 bytes a890e297
~~~


<a id="compare-ee8979925dd3ca983657bc7e11d455a9"></a>

### [`00b74944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74944.md) → [`00b74988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74988.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74944.md#insn-00b74968)
- 新版 `00b749ac`（命令位置の公開資料なし）

~~~diff
- 00b74968 ["INT_ADD", "register:40f0:8", ["const:b74968:8", "const:4:8"]]
- 00b74968 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b749ac ["INT_ADD", "register:40f0:8", ["const:b749ac:8", "const:4:8"]]
+ 00b749ac ["CALL", null, ["callee:00bdb190:8"]]
- 00b74968 bytes f6990194
+ 00b749ac bytes f9990194
~~~


<a id="compare-0828b65f6bc0247a7c821c8bed702052"></a>

### [`00b74990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74990.md) → [`00b749d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b749d4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b749ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74990.md#insn-00b749ec)
- 新版 `00b74a30`（命令位置の公開資料なし）

~~~diff
- 00b749ec ["INT_ADD", "register:40f0:8", ["const:b749ec:8", "const:4:8"]]
- 00b749ec ["CALL", null, ["callee:00bdb180:8"]]
+ 00b74a30 ["INT_ADD", "register:40f0:8", ["const:b74a30:8", "const:4:8"]]
+ 00b74a30 ["CALL", null, ["callee:00bdb180:8"]]
- 00b749ec bytes d1990194
+ 00b74a30 bytes d4990194
~~~


<a id="compare-4d222777b08dee37b0b13084850d8fc1"></a>

### [`00b74a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md) → [`00b74a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74a5c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb760.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74ae4) · [`00b74af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74af4) · [`00b74b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74a18.md#insn-00b74b04)
- 新版 `00b74b28`（命令位置の公開資料なし） · `00b74b38`（命令位置の公開資料なし） · `00b74b48`（命令位置の公開資料なし）

~~~diff
- 00b74ae4 ["INT_ADD", "register:40f0:8", ["const:b74ae4:8", "const:4:8"]]
- 00b74ae4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74b28 ["INT_ADD", "register:40f0:8", ["const:b74b28:8", "const:4:8"]]
+ 00b74b28 ["CALL", null, ["callee:00bdb040:8"]]
- 00b74ae4 bytes 43990194
+ 00b74b28 bytes 46990194
- 00b74af4 ["INT_ADD", "register:40f0:8", ["const:b74af4:8", "const:4:8"]]
- 00b74af4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74b38 ["INT_ADD", "register:40f0:8", ["const:b74b38:8", "const:4:8"]]
+ 00b74b38 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74af4 bytes 6b990194
+ 00b74b38 bytes 6e990194
- 00b74b04 ["INT_ADD", "register:40f0:8", ["const:b74b04:8", "const:4:8"]]
- 00b74b04 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b74b48 ["INT_ADD", "register:40f0:8", ["const:b74b48:8", "const:4:8"]]
+ 00b74b48 ["CALL", null, ["callee:00bdb060:8"]]
- 00b74b04 bytes 43990194
+ 00b74b48 bytes 46990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6d07c816f595e4a1a01c9da30bcd51"></a>

### [`00b74b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md) → [`00b74be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74be0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd840.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdd890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd890.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74c78) · [`00b74c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74c88) · [`00b74ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74b9c.md#insn-00b74ca4)
- 新版 `00b74cbc`（命令位置の公開資料なし） · `00b74ccc`（命令位置の公開資料なし） · `00b74ce8`（命令位置の公開資料なし）

~~~diff
- 00b74c78 ["INT_ADD", "register:40f0:8", ["const:b74c78:8", "const:4:8"]]
- 00b74c78 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b74cbc ["INT_ADD", "register:40f0:8", ["const:b74cbc:8", "const:4:8"]]
+ 00b74cbc ["CALL", null, ["callee:00bdb040:8"]]
- 00b74c78 bytes de980194
+ 00b74cbc bytes e1980194
- 00b74c88 ["INT_ADD", "register:40f0:8", ["const:b74c88:8", "const:4:8"]]
- 00b74c88 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b74ccc ["INT_ADD", "register:40f0:8", ["const:b74ccc:8", "const:4:8"]]
+ 00b74ccc ["CALL", null, ["callee:00bdb060:8"]]
- 00b74c88 bytes e2980194
+ 00b74ccc bytes e5980194
- 00b74ca4 ["INT_ADD", "register:40f0:8", ["const:b74ca4:8", "const:4:8"]]
- 00b74ca4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b74ce8 ["INT_ADD", "register:40f0:8", ["const:b74ce8:8", "const:4:8"]]
+ 00b74ce8 ["CALL", null, ["callee:00bdb240:8"]]
- 00b74ca4 bytes 53990194
+ 00b74ce8 bytes 56990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d8fb1418b4a7a36b4959d9e10db17b"></a>

### [`00b74ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md) → [`00b74d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca90.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b74d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md)
- 新版 呼出元 1件 [`00bdcae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcae0.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md#insn-00b74d18) · [`00b74d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md#insn-00b74d54)
- 新版 `00b74d5c`（命令位置の公開資料なし） · `00b74d98`（命令位置の公開資料なし）

~~~diff
- 00b74d18 ["INT_ADD", "register:40f0:8", ["const:b74d18:8", "const:4:8"]]
- 00b74d18 ["CALL", null, ["callee:00b74d9c:8"]]
+ 00b74d5c ["INT_ADD", "register:40f0:8", ["const:b74d5c:8", "const:4:8"]]
+ 00b74d5c ["CALL", null, ["callee:00b74d9c:8"]]
- 00b74d18 bytes 10000094
+ 00b74d5c bytes 10000094
- 00b74d54 ["INT_ADD", "register:40f0:8", ["const:b74d54:8", "const:4:8"]]
- 00b74d54 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74d98 ["INT_ADD", "register:40f0:8", ["const:b74d98:8", "const:4:8"]]
+ 00b74d98 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74d54 bytes 22ace297
+ 00b74d98 bytes 11ace297
~~~


<a id="compare-8c579e8ebbe956be61193a45e5b4043e"></a>

### [`00b74d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md) → [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md) FUN_00b74d9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b74ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md) [`00bb9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9204.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`00b74d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md) [`00bb9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md#insn-00b74db0)
- 新版 `00b74df4`（命令位置の公開資料なし）

~~~diff
- 00b74db0 ["INT_ADD", "register:40f0:8", ["const:b74db0:8", "const:4:8"]]
- 00b74db0 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74df4 ["INT_ADD", "register:40f0:8", ["const:b74df4:8", "const:4:8"]]
+ 00b74df4 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74db0 bytes bc980194
+ 00b74df4 bytes bf980194
~~~


<a id="compare-eb14c9578c3fc55374916081a3f988da"></a>

### [`00b74dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md) → [`00b74e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74e30.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74e88) · [`00b74eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74eb0) · [`00b74ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74dec.md#insn-00b74ef0)
- 新版 `00b74ecc`（命令位置の公開資料なし） · `00b74ef4`（命令位置の公開資料なし） · `00b74f34`（命令位置の公開資料なし）

~~~diff
- 00b74e88 ["INT_ADD", "register:40f0:8", ["const:b74e88:8", "const:4:8"]]
- 00b74e88 ["CALL", null, ["callee:00bde220:8"]]
+ 00b74ecc ["INT_ADD", "register:40f0:8", ["const:b74ecc:8", "const:4:8"]]
+ 00b74ecc ["CALL", null, ["callee:00bde220:8"]]
- 00b74e88 bytes d2a40194
+ 00b74ecc bytes d5a40194
- 00b74eb0 ["INT_ADD", "register:40f0:8", ["const:b74eb0:8", "const:4:8"]]
- 00b74eb0 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b74ef4 ["INT_ADD", "register:40f0:8", ["const:b74ef4:8", "const:4:8"]]
+ 00b74ef4 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b74eb0 bytes 7c980194
+ 00b74ef4 bytes 7f980194
- 00b74ef0 ["INT_ADD", "register:40f0:8", ["const:b74ef0:8", "const:4:8"]]
- 00b74ef0 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74f34 ["INT_ADD", "register:40f0:8", ["const:b74f34:8", "const:4:8"]]
+ 00b74f34 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74ef0 bytes bbabe297
+ 00b74f34 bytes aaabe297
~~~


<a id="compare-b0e7f69a8c724a57942a5154681b0639"></a>

### [`00b74ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md) → [`00b74f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74f38.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f10) · [`00b74f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f4c) · [`00b74f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ef4.md#insn-00b74f6c)
- 新版 `00b74f54`（命令位置の公開資料なし） · `00b74f90`（命令位置の公開資料なし） · `00b74fb0`（命令位置の公開資料なし）

~~~diff
- 00b74f10 ["INT_ADD", "register:40f0:8", ["const:b74f10:8", "const:4:8"]]
- 00b74f10 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b74f54 ["INT_ADD", "register:40f0:8", ["const:b74f54:8", "const:4:8"]]
+ 00b74f54 ["CALL", null, ["callee:00bdb190:8"]]
- 00b74f10 bytes 8c980194
+ 00b74f54 bytes 8f980194
- 00b74f4c ["INT_ADD", "register:40f0:8", ["const:b74f4c:8", "const:4:8"]]
- 00b74f4c ["CALL", null, ["callee:00bdb200:8"]]
+ 00b74f90 ["INT_ADD", "register:40f0:8", ["const:b74f90:8", "const:4:8"]]
+ 00b74f90 ["CALL", null, ["callee:00bdb200:8"]]
- 00b74f4c bytes 99980194
+ 00b74f90 bytes 9c980194
- 00b74f6c ["INT_ADD", "register:40f0:8", ["const:b74f6c:8", "const:4:8"]]
- 00b74f6c ["CALL", null, ["callee:0041fddc:8"]]
+ 00b74fb0 ["INT_ADD", "register:40f0:8", ["const:b74fb0:8", "const:4:8"]]
+ 00b74fb0 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74f6c bytes 9cabe297
+ 00b74fb0 bytes 8babe297
~~~


<a id="compare-f7647bdfca9459d06d971d586abccca2"></a>

### [`00b74f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md) → [`00b74fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74fb8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b74fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md#insn-00b74fd4) · [`00b74ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74f74.md#insn-00b74ff0)
- 新版 `00b75018`（命令位置の公開資料なし） · `00b75034`（命令位置の公開資料なし）

~~~diff
- 00b74fd4 ["INT_ADD", "register:40f0:8", ["const:b74fd4:8", "const:4:8"]]
- 00b74fd4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b75018 ["INT_ADD", "register:40f0:8", ["const:b75018:8", "const:4:8"]]
+ 00b75018 ["CALL", null, ["callee:00bdb200:8"]]
- 00b74fd4 bytes 77980194
+ 00b75018 bytes 7a980194
- 00b74ff0 ["INT_ADD", "register:40f0:8", ["const:b74ff0:8", "const:4:8"]]
- 00b74ff0 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b75034 ["INT_ADD", "register:40f0:8", ["const:b75034:8", "const:4:8"]]
+ 00b75034 ["CALL", null, ["callee:0041fddc:8"]]
- 00b74ff0 bytes 7babe297
+ 00b75034 bytes 6aabe297
~~~


<a id="compare-8670b7753168bbd150dd2b083d33bacd"></a>

### [`00b74ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ff4.md) → [`00b75038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75038.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7501c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ff4.md#insn-00b7501c) · [`00b75070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ff4.md#insn-00b75070) · [`00b75094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ff4.md#insn-00b75094)
- 新版 `00b75060`（命令位置の公開資料なし） · `00b750b4`（命令位置の公開資料なし） · `00b750d8`（命令位置の公開資料なし）

~~~diff
- 00b7501c ["INT_ADD", "register:40f0:8", ["const:b7501c:8", "const:4:8"]]
- 00b7501c ["CALL", null, ["callee:00bdb190:8"]]
+ 00b75060 ["INT_ADD", "register:40f0:8", ["const:b75060:8", "const:4:8"]]
+ 00b75060 ["CALL", null, ["callee:00bdb190:8"]]
- 00b7501c bytes 49980194
+ 00b75060 bytes 4c980194
- 00b75070 ["INT_ADD", "register:40f0:8", ["const:b75070:8", "const:4:8"]]
- 00b75070 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b750b4 ["INT_ADD", "register:40f0:8", ["const:b750b4:8", "const:4:8"]]
+ 00b750b4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b75070 bytes 50980194
+ 00b750b4 bytes 53980194
- 00b75094 ["INT_ADD", "register:40f0:8", ["const:b75094:8", "const:4:8"]]
- 00b75094 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b750d8 ["INT_ADD", "register:40f0:8", ["const:b750d8:8", "const:4:8"]]
+ 00b750d8 ["CALL", null, ["callee:0041fddc:8"]]
- 00b75094 bytes 52abe297
+ 00b750d8 bytes 41abe297
~~~


<a id="compare-ed90d6ad8b17077aa59e2e001bb02161"></a>

### [`00b75098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75098.md) → [`00b750dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b750dc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b750d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75098.md#insn-00b750d8)
- 新版 `00b7511c`（命令位置の公開資料なし）

~~~diff
- 00b750d8 ["INT_ADD", "register:40f0:8", ["const:b750d8:8", "const:4:8"]]
- 00b750d8 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b7511c ["INT_ADD", "register:40f0:8", ["const:b7511c:8", "const:4:8"]]
+ 00b7511c ["CALL", null, ["callee:0041fddc:8"]]
- 00b750d8 bytes 41abe297
+ 00b7511c bytes 30abe297
~~~


<a id="compare-069411b1d21db8438f801cc4428e5b9a"></a>

### [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) → [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) FUN_00b75128

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00b750dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750dc.md) [`00baf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md) [`00baf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md) [`00bb3bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3bbc.md) [`00bb5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md) · 呼出先 2件 [`00b7454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b7454c.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 8件 [`00b75120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75120.md) [`00baf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf3b8.md) [`00baf7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf7b4.md) [`00bb3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb3c00.md) [`00bb5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5c14.md) · 呼出先 2件 [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md#insn-00b75100)
- 新版 `00b75144`（命令位置の公開資料なし）

~~~diff
- 00b75100 ["INT_ADD", "register:40f0:8", ["const:b75100:8", "const:4:8"]]
- 00b75100 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b75144 ["INT_ADD", "register:40f0:8", ["const:b75144:8", "const:4:8"]]
+ 00b75144 ["CALL", null, ["callee:00bdb190:8"]]
- 00b75100 bytes 10980194
+ 00b75144 bytes 13980194
~~~


<a id="compare-91ba33cff6413da13ffbc3a86a100733"></a>

### [`00b75120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75120.md) → [`00b75164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75164.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b751c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75120.md#insn-00b751c0) · [`00b751d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75120.md#insn-00b751d4)
- 新版 `00b75204`（命令位置の公開資料なし） · `00b75218`（命令位置の公開資料なし）

~~~diff
- 00b751c0 ["INT_ADD", "register:40f0:8", ["const:b751c0:8", "const:4:8"]]
- 00b751c0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00b75204 ["INT_ADD", "register:40f0:8", ["const:b75204:8", "const:4:8"]]
+ 00b75204 ["CALL", null, ["callee:00bdb180:8"]]
- 00b751c0 bytes dc970194
+ 00b75204 bytes df970194
- 00b751d4 ["INT_ADD", "register:40f0:8", ["const:b751d4:8", "const:4:8"]]
- 00b751d4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b75218 ["INT_ADD", "register:40f0:8", ["const:b75218:8", "const:4:8"]]
+ 00b75218 ["CALL", null, ["callee:00bdb200:8"]]
- 00b751d4 bytes f7970194
+ 00b75218 bytes fa970194
~~~


<a id="compare-a4f0d69e87b9ee42e1254ecf65c4fbda"></a>

### [`00b752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md) → [`00b75338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md) FUN_00b75338

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b752a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752a0.md) [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00b752e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b752e4.md) [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md#insn-00b75334) · [`00b75360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md#insn-00b75360) · [`00b75370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md#insn-00b75370)
- 新版 `00b75378`（命令位置の公開資料なし） · `00b753a4`（命令位置の公開資料なし） · `00b753b4`（命令位置の公開資料なし）

~~~diff
- 00b75334 ["INT_ADD", "register:40f0:8", ["const:b75334:8", "const:4:8"]]
- 00b75334 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75378 ["INT_ADD", "register:40f0:8", ["const:b75378:8", "const:4:8"]]
+ 00b75378 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b75334 bytes 5b970194
+ 00b75378 bytes 5e970194
- 00b75360 ["INT_ADD", "register:40f0:8", ["const:b75360:8", "const:4:8"]]
- 00b75360 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b753a4 ["INT_ADD", "register:40f0:8", ["const:b753a4:8", "const:4:8"]]
+ 00b753a4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b75360 bytes 24970194
+ 00b753a4 bytes 27970194
- 00b75370 ["INT_ADD", "register:40f0:8", ["const:b75370:8", "const:4:8"]]
- 00b75370 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b753b4 ["INT_ADD", "register:40f0:8", ["const:b753b4:8", "const:4:8"]]
+ 00b753b4 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b75370 bytes 7c970194
+ 00b753b4 bytes 7f970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c39682fe839e6aed47aa46eab6239b"></a>

### [`00b753a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md) → [`00b753ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b753ec.md) FUN_00b753ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b752a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752a0.md) [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00b752e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b752e4.md) [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b753ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md#insn-00b753ec) · [`00b75474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md#insn-00b75474) · [`00b7548c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md#insn-00b7548c)
- 新版 `00b75430`（命令位置の公開資料なし） · `00b754b8`（命令位置の公開資料なし） · `00b754d0`（命令位置の公開資料なし）

~~~diff
- 00b753ec ["INT_ADD", "register:40f0:8", ["const:b753ec:8", "const:4:8"]]
- 00b753ec ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75430 ["INT_ADD", "register:40f0:8", ["const:b75430:8", "const:4:8"]]
+ 00b75430 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b753ec bytes 2d970194
+ 00b75430 bytes 30970194
- 00b75474 ["INT_ADD", "register:40f0:8", ["const:b75474:8", "const:4:8"]]
- 00b75474 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b754b8 ["INT_ADD", "register:40f0:8", ["const:b754b8:8", "const:4:8"]]
+ 00b754b8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b75474 bytes df960194
+ 00b754b8 bytes e2960194
- 00b7548c ["INT_ADD", "register:40f0:8", ["const:b7548c:8", "const:4:8"]]
- 00b7548c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b754d0 ["INT_ADD", "register:40f0:8", ["const:b754d0:8", "const:4:8"]]
+ 00b754d0 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b7548c bytes 35970194
+ 00b754d0 bytes 38970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf37dcf33cfd2123d2ce883f11b443b0"></a>

### [`00b754cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b754cc.md) → [`00b75510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75510.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)
- 新版 呼出元 1件 [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) · 呼出先 3件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b754f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b754cc.md#insn-00b754f0) · [`00b7554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b754cc.md#insn-00b7554c) · [`00b75570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b754cc.md#insn-00b75570)
- 新版 `00b75534`（命令位置の公開資料なし） · `00b75590`（命令位置の公開資料なし） · `00b755b4`（命令位置の公開資料なし）

~~~diff
- 00b754f0 ["INT_ADD", "register:40f0:8", ["const:b754f0:8", "const:4:8"]]
- 00b754f0 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b75534 ["INT_ADD", "register:40f0:8", ["const:b75534:8", "const:4:8"]]
+ 00b75534 ["CALL", null, ["callee:00bdb190:8"]]
- 00b754f0 bytes 14970194
+ 00b75534 bytes 17970194
- 00b7554c ["INT_ADD", "register:40f0:8", ["const:b7554c:8", "const:4:8"]]
- 00b7554c ["CALL", null, ["callee:00bde220:8"]]
+ 00b75590 ["INT_ADD", "register:40f0:8", ["const:b75590:8", "const:4:8"]]
+ 00b75590 ["CALL", null, ["callee:00bde220:8"]]
- 00b7554c bytes 21a30194
+ 00b75590 bytes 24a30194
- 00b75570 ["INT_ADD", "register:40f0:8", ["const:b75570:8", "const:4:8"]]
- 00b75570 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b755b4 ["INT_ADD", "register:40f0:8", ["const:b755b4:8", "const:4:8"]]
+ 00b755b4 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b75570 bytes cc960194
+ 00b755b4 bytes cf960194
~~~


<a id="compare-a12251d9d69fd17ebe64dff1d3655fe2"></a>

### [`00b755b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b755b0.md) → [`00b755f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b755f4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b755fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b755b0.md#insn-00b755fc)
- 新版 `00b75640`（命令位置の公開資料なし）

~~~diff
- 00b755fc ["INT_ADD", "register:40f0:8", ["const:b755fc:8", "const:4:8"]]
- 00b755fc ["CALL", null, ["callee:0041fddc:8"]]
+ 00b75640 ["INT_ADD", "register:40f0:8", ["const:b75640:8", "const:4:8"]]
+ 00b75640 ["CALL", null, ["callee:0041fddc:8"]]
- 00b755fc bytes f8a9e297
+ 00b75640 bytes e7a9e297
~~~


<a id="compare-4ab85e0367a491c067f249ce1d54332e"></a>

### [`00b75600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75600.md) → [`00b75644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75644.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertENS_11__wrap_iterIPKcEEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b756c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75600.md#insn-00b756c4) · [`00b756f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75600.md#insn-00b756f0) · [`00b75710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75600.md#insn-00b75710)
- 新版 `00b75708`（命令位置の公開資料なし） · `00b75734`（命令位置の公開資料なし） · `00b75754`（命令位置の公開資料なし）

~~~diff
- 00b756c4 ["INT_ADD", "register:40f0:8", ["const:b756c4:8", "const:4:8"]]
- 00b756c4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75708 ["INT_ADD", "register:40f0:8", ["const:b75708:8", "const:4:8"]]
+ 00b75708 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b756c4 bytes 77960194
+ 00b75708 bytes 7a960194
- 00b756f0 ["INT_ADD", "register:40f0:8", ["const:b756f0:8", "const:4:8"]]
- 00b756f0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b75734 ["INT_ADD", "register:40f0:8", ["const:b75734:8", "const:4:8"]]
+ 00b75734 ["CALL", null, ["callee:00bdb040:8"]]
- 00b756f0 bytes 40960194
+ 00b75734 bytes 43960194
- 00b75710 ["INT_ADD", "register:40f0:8", ["const:b75710:8", "const:4:8"]]
- 00b75710 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b75754 ["INT_ADD", "register:40f0:8", ["const:b75754:8", "const:4:8"]]
+ 00b75754 ["CALL", null, ["callee:00bdb060:8"]]
- 00b75710 bytes 40960194
+ 00b75754 bytes 43960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ae57c2ccf8db7f2729261b8740de26"></a>

### [`00b757fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b757fc.md) → [`00b75840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75840.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b757fc.md#insn-00b75848)
- 新版 `00b7588c`（命令位置の公開資料なし）

~~~diff
- 00b75848 ["INT_ADD", "register:40f0:8", ["const:b75848:8", "const:4:8"]]
- 00b75848 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b7588c ["INT_ADD", "register:40f0:8", ["const:b7588c:8", "const:4:8"]]
+ 00b7588c ["CALL", null, ["callee:0041fddc:8"]]
- 00b75848 bytes 65a9e297
+ 00b7588c bytes 54a9e297
~~~


<a id="compare-2064376df8a1761fcd3279207514b36e"></a>

### [`00b7584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md) → [`00b75890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75890.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00be0ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ff0.md) · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b758ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md#insn-00b758ec) · [`00b7593c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md#insn-00b7593c) · [`00b7594c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b7584c.md#insn-00b7594c)
- 新版 `00b75930`（命令位置の公開資料なし） · `00b75980`（命令位置の公開資料なし） · `00b75990`（命令位置の公開資料なし）

~~~diff
- 00b758ec ["INT_ADD", "register:40f0:8", ["const:b758ec:8", "const:4:8"]]
- 00b758ec ["CALL", null, ["callee:00be1000:8"]]
+ 00b75930 ["INT_ADD", "register:40f0:8", ["const:b75930:8", "const:4:8"]]
+ 00b75930 ["CALL", null, ["callee:00be1000:8"]]
- 00b758ec bytes b1ad0194
+ 00b75930 bytes b4ad0194
- 00b7593c ["INT_ADD", "register:40f0:8", ["const:b7593c:8", "const:4:8"]]
- 00b7593c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75980 ["INT_ADD", "register:40f0:8", ["const:b75980:8", "const:4:8"]]
+ 00b75980 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7593c bytes d9950194
+ 00b75980 bytes dc950194
- 00b7594c ["INT_ADD", "register:40f0:8", ["const:b7594c:8", "const:4:8"]]
- 00b7594c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75990 ["INT_ADD", "register:40f0:8", ["const:b75990:8", "const:4:8"]]
+ 00b75990 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7594c bytes d5950194
+ 00b75990 bytes d8950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d917620bcfb77f791cad29f62c30d764"></a>

### [`00b75a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a3c.md) → [`00b75a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a80.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a3c.md#insn-00b75b08) · [`00b75b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a3c.md#insn-00b75b24) · [`00b75b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a3c.md#insn-00b75b38)
- 新版 `00b75b4c`（命令位置の公開資料なし） · `00b75b68`（命令位置の公開資料なし） · `00b75b7c`（命令位置の公開資料なし）

~~~diff
- 00b75b08 ["INT_ADD", "register:40f0:8", ["const:b75b08:8", "const:4:8"]]
- 00b75b08 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b75b4c ["INT_ADD", "register:40f0:8", ["const:b75b4c:8", "const:4:8"]]
+ 00b75b4c ["CALL", null, ["callee:00bdb040:8"]]
- 00b75b08 bytes 3a950194
+ 00b75b4c bytes 3d950194
- 00b75b24 ["INT_ADD", "register:40f0:8", ["const:b75b24:8", "const:4:8"]]
- 00b75b24 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75b68 ["INT_ADD", "register:40f0:8", ["const:b75b68:8", "const:4:8"]]
+ 00b75b68 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b75b24 bytes 5f950194
+ 00b75b68 bytes 62950194
- 00b75b38 ["INT_ADD", "register:40f0:8", ["const:b75b38:8", "const:4:8"]]
- 00b75b38 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b75b7c ["INT_ADD", "register:40f0:8", ["const:b75b7c:8", "const:4:8"]]
+ 00b75b7c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b75b38 bytes 8a950194
+ 00b75b7c bytes 8d950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-795752d591d1d2aa26bb4cea5e851eed"></a>

### [`00b75c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75c80.md) → [`00b75cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75cc4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75c80.md#insn-00b75cc4) · [`00b75d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75c80.md#insn-00b75d0c) · [`00b75d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75c80.md#insn-00b75d30)
- 新版 `00b75d08`（命令位置の公開資料なし） · `00b75d50`（命令位置の公開資料なし） · `00b75d74`（命令位置の公開資料なし）

~~~diff
- 00b75cc4 ["INT_ADD", "register:40f0:8", ["const:b75cc4:8", "const:4:8"]]
- 00b75cc4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b75d08 ["INT_ADD", "register:40f0:8", ["const:b75d08:8", "const:4:8"]]
+ 00b75d08 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b75cc4 bytes f7940194
+ 00b75d08 bytes fa940194
- 00b75d0c ["INT_ADD", "register:40f0:8", ["const:b75d0c:8", "const:4:8"]]
- 00b75d0c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b75d50 ["INT_ADD", "register:40f0:8", ["const:b75d50:8", "const:4:8"]]
+ 00b75d50 ["CALL", null, ["callee:00bdb040:8"]]
- 00b75d0c bytes b9940194
+ 00b75d50 bytes bc940194
- 00b75d30 ["INT_ADD", "register:40f0:8", ["const:b75d30:8", "const:4:8"]]
- 00b75d30 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b75d74 ["INT_ADD", "register:40f0:8", ["const:b75d74:8", "const:4:8"]]
+ 00b75d74 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b75d30 bytes dddeec97
+ 00b75d74 bytes ccdeec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18cadd3c59a3eb0594b3757f76fb81f8"></a>

### [`00b75d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75d64.md) → [`00b75da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75da8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ff0.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75d64.md#insn-00b75d8c)
- 新版 `00b75dd0`（命令位置の公開資料なし）

~~~diff
- 00b75d8c ["INT_ADD", "register:40f0:8", ["const:b75d8c:8", "const:4:8"]]
- 00b75d8c ["CALL", null, ["callee:00be1010:8"]]
+ 00b75dd0 ["INT_ADD", "register:40f0:8", ["const:b75dd0:8", "const:4:8"]]
+ 00b75dd0 ["CALL", null, ["callee:00be1010:8"]]
- 00b75d8c bytes 8dac0194
+ 00b75dd0 bytes 90ac0194
~~~


<a id="compare-9cbddda3738e37a219bc21c9d149f6bc"></a>

### [`00b75de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75de4.md) → [`00b75e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75e28.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE16find_last_not_ofEPKwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75de4.md#insn-00b75e48)
- 新版 `00b75e8c`（命令位置の公開資料なし）

~~~diff
- 00b75e48 ["INT_ADD", "register:40f0:8", ["const:b75e48:8", "const:4:8"]]
- 00b75e48 ["CALL", null, ["callee:00bdb600:8"]]
+ 00b75e8c ["INT_ADD", "register:40f0:8", ["const:b75e8c:8", "const:4:8"]]
+ 00b75e8c ["CALL", null, ["callee:00bdb600:8"]]
- 00b75e48 bytes da950194
+ 00b75e8c bytes dd950194
~~~


<a id="compare-e83fca5eeee7a28bd79db6bdd29ac841"></a>

### [`00b75e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e8c.md) → [`00b75ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75ed0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e8c.md#insn-00b75eec)
- 新版 `00b75f30`（命令位置の公開資料なし）

~~~diff
- 00b75eec ["INT_ADD", "register:40f0:8", ["const:b75eec:8", "const:4:8"]]
- 00b75eec ["CALL", null, ["callee:00bdb600:8"]]
+ 00b75f30 ["INT_ADD", "register:40f0:8", ["const:b75f30:8", "const:4:8"]]
+ 00b75f30 ["CALL", null, ["callee:00bdb600:8"]]
- 00b75eec bytes b1950194
+ 00b75f30 bytes b4950194
~~~


<a id="compare-eb24f8e9a2cc18cb9eb728763e215b3e"></a>

### [`00b75f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md) → [`00b75f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fd0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 1件 [`00be1020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1020.md) · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md#insn-00b75fac) · [`00b75fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md#insn-00b75fec) · [`00b7607c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md#insn-00b7607c)
- 新版 `00b75ff0`（命令位置の公開資料なし） · `00b76030`（命令位置の公開資料なし） · `00b760c0`（命令位置の公開資料なし）

~~~diff
- 00b75fac ["INT_ADD", "register:40f0:8", ["const:b75fac:8", "const:4:8"]]
- 00b75fac ["CALL", null, ["callee:00bdda50:8"]]
+ 00b75ff0 ["INT_ADD", "register:40f0:8", ["const:b75ff0:8", "const:4:8"]]
+ 00b75ff0 ["CALL", null, ["callee:00bdda50:8"]]
- 00b75fac bytes 959e0194
+ 00b75ff0 bytes 989e0194
- 00b75fec ["INT_ADD", "register:40f0:8", ["const:b75fec:8", "const:4:8"]]
- 00b75fec ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76030 ["INT_ADD", "register:40f0:8", ["const:b76030:8", "const:4:8"]]
+ 00b76030 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b75fec bytes 2d940194
+ 00b76030 bytes 30940194
- 00b7607c ["INT_ADD", "register:40f0:8", ["const:b7607c:8", "const:4:8"]]
- 00b7607c ["CALL", null, ["callee:00b75a68:8"]]
+ 00b760c0 ["INT_ADD", "register:40f0:8", ["const:b760c0:8", "const:4:8"]]
+ 00b760c0 ["CALL", null, ["callee:00b75a68:8"]]
- 00b7607c bytes 6afeff97
+ 00b760c0 bytes 6afeff97
~~~


<a id="compare-39ad2ef452cde2cd98e96c97bd08db02"></a>

### [`00b760b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b760b4.md) → [`00b760f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b760f8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b760b4.md#insn-00b76120) · [`00b76140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b760b4.md#insn-00b76140) · [`00b76160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b760b4.md#insn-00b76160)
- 新版 `00b76164`（命令位置の公開資料なし） · `00b76184`（命令位置の公開資料なし） · `00b761a4`（命令位置の公開資料なし）

~~~diff
- 00b76120 ["INT_ADD", "register:40f0:8", ["const:b76120:8", "const:4:8"]]
- 00b76120 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b76164 ["INT_ADD", "register:40f0:8", ["const:b76164:8", "const:4:8"]]
+ 00b76164 ["CALL", null, ["callee:00bdb040:8"]]
- 00b76120 bytes b4930194
+ 00b76164 bytes b7930194
- 00b76140 ["INT_ADD", "register:40f0:8", ["const:b76140:8", "const:4:8"]]
- 00b76140 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76184 ["INT_ADD", "register:40f0:8", ["const:b76184:8", "const:4:8"]]
+ 00b76184 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76140 bytes d8930194
+ 00b76184 bytes db930194
- 00b76160 ["INT_ADD", "register:40f0:8", ["const:b76160:8", "const:4:8"]]
- 00b76160 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b761a4 ["INT_ADD", "register:40f0:8", ["const:b761a4:8", "const:4:8"]]
+ 00b761a4 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b76160 bytes d1ddec97
+ 00b761a4 bytes c0ddec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-737fa9cb42299e04d2171fbf6535e7da"></a>

### [`00b76168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76168.md) → [`00b761ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761ac.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b761ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76168.md#insn-00b761ac)
- 新版 `00b761f0`（命令位置の公開資料なし）

~~~diff
- 00b761ac ["INT_ADD", "register:40f0:8", ["const:b761ac:8", "const:4:8"]]
- 00b761ac ["CALL", null, ["callee:00b75a68:8"]]
+ 00b761f0 ["INT_ADD", "register:40f0:8", ["const:b761f0:8", "const:4:8"]]
+ 00b761f0 ["CALL", null, ["callee:00b75a68:8"]]
- 00b761ac bytes 1efeff97
+ 00b761f0 bytes 1efeff97
~~~


<a id="compare-c0b87618b31f0542d02195f4995e5ad6"></a>

### [`00b761b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md) → [`00b761f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761f4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00be1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1030.md) · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md#insn-00b76234) · [`00b7627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md#insn-00b7627c) · [`00b7628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b761b0.md#insn-00b7628c)
- 新版 `00b76278`（命令位置の公開資料なし） · `00b762c0`（命令位置の公開資料なし） · `00b762d0`（命令位置の公開資料なし）

~~~diff
- 00b76234 ["INT_ADD", "register:40f0:8", ["const:b76234:8", "const:4:8"]]
- 00b76234 ["CALL", null, ["callee:00be1000:8"]]
+ 00b76278 ["INT_ADD", "register:40f0:8", ["const:b76278:8", "const:4:8"]]
+ 00b76278 ["CALL", null, ["callee:00be1000:8"]]
- 00b76234 bytes 5fab0194
+ 00b76278 bytes 62ab0194
- 00b7627c ["INT_ADD", "register:40f0:8", ["const:b7627c:8", "const:4:8"]]
- 00b7627c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b762c0 ["INT_ADD", "register:40f0:8", ["const:b762c0:8", "const:4:8"]]
+ 00b762c0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7627c bytes 89930194
+ 00b762c0 bytes 8c930194
- 00b7628c ["INT_ADD", "register:40f0:8", ["const:b7628c:8", "const:4:8"]]
- 00b7628c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b762d0 ["INT_ADD", "register:40f0:8", ["const:b762d0:8", "const:4:8"]]
+ 00b762d0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7628c bytes 85930194
+ 00b762d0 bytes 88930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fffd779c288d8e4ba6d09bd0d60cf1cd"></a>

### [`00b7635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md) → [`00b763a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b763a0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b763f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md#insn-00b763f0) · [`00b76444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md#insn-00b76444) · [`00b764e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md#insn-00b764e0)
- 新版 `00b76434`（命令位置の公開資料なし） · `00b76488`（命令位置の公開資料なし） · `00b76524`（命令位置の公開資料なし）

~~~diff
- 00b763f0 ["INT_ADD", "register:40f0:8", ["const:b763f0:8", "const:4:8"]]
- 00b763f0 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b76434 ["INT_ADD", "register:40f0:8", ["const:b76434:8", "const:4:8"]]
+ 00b76434 ["CALL", null, ["callee:00bdda50:8"]]
- 00b763f0 bytes 849d0194
+ 00b76434 bytes 879d0194
- 00b76444 ["INT_ADD", "register:40f0:8", ["const:b76444:8", "const:4:8"]]
- 00b76444 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76488 ["INT_ADD", "register:40f0:8", ["const:b76488:8", "const:4:8"]]
+ 00b76488 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76444 bytes 17930194
+ 00b76488 bytes 1a930194
- 00b764e0 ["INT_ADD", "register:40f0:8", ["const:b764e0:8", "const:4:8"]]
- 00b764e0 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b76524 ["INT_ADD", "register:40f0:8", ["const:b76524:8", "const:4:8"]]
+ 00b76524 ["CALL", null, ["callee:00b75a68:8"]]
- 00b764e0 bytes 51fdff97
+ 00b76524 bytes 51fdff97
~~~


<a id="compare-55d03cdd71e49d8120ac494f2b1c1697"></a>

### [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md) → [`00b76530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md) FUN_00b76530

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00b764e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764e4.md) [`00b7686c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md) [`00b77540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md) [`00bb00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb00e0.md) [`00bb0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0b74.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 5件 [`00b76528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76528.md) [`00b768b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b768b0.md) [`00b77584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77584.md) [`00bb0124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0124.md) [`00bb0bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0bb8.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md#insn-00b76554) · [`00b7657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md#insn-00b7657c)
- 新版 `00b76598`（命令位置の公開資料なし） · `00b765c0`（命令位置の公開資料なし）

~~~diff
- 00b76554 ["INT_ADD", "register:40f0:8", ["const:b76554:8", "const:4:8"]]
- 00b76554 ["CALL", null, ["callee:00be1000:8"]]
+ 00b76598 ["INT_ADD", "register:40f0:8", ["const:b76598:8", "const:4:8"]]
+ 00b76598 ["CALL", null, ["callee:00be1000:8"]]
- 00b76554 bytes 97aa0194
+ 00b76598 bytes 9aaa0194
- 00b7657c ["INT_ADD", "register:40f0:8", ["const:b7657c:8", "const:4:8"]]
- 00b7657c ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b765c0 ["INT_ADD", "register:40f0:8", ["const:b765c0:8", "const:4:8"]]
+ 00b765c0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b7657c bytes c9920194
+ 00b765c0 bytes cc920194
~~~


<a id="compare-09f578479317742c50e241aa9d13b684"></a>

### [`00b765b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md) → [`00b765f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b765f8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b76650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b76694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7664c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md#insn-00b7664c)
- 新版 `00b76690`（命令位置の公開資料なし）

~~~diff
- 00b7664c ["INT_ADD", "register:40f0:8", ["const:b7664c:8", "const:4:8"]]
- 00b7664c ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b76690 ["INT_ADD", "register:40f0:8", ["const:b76690:8", "const:4:8"]]
+ 00b76690 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b7664c bytes 96dcec97
+ 00b76690 bytes 85dcec97
~~~


<a id="compare-95e20b4ec8c126efed33173e25782f3c"></a>

### [`00b76650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md) → [`00b76694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md) FUN_00b76694

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b765b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b765b4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00b765f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b765f8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b766c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md#insn-00b766c0) · [`00b766ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md#insn-00b766ec) · [`00b76710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76650.md#insn-00b76710)
- 新版 `00b76704`（命令位置の公開資料なし） · `00b76730`（命令位置の公開資料なし） · `00b76754`（命令位置の公開資料なし）

~~~diff
- 00b766c0 ["INT_ADD", "register:40f0:8", ["const:b766c0:8", "const:4:8"]]
- 00b766c0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b76704 ["INT_ADD", "register:40f0:8", ["const:b76704:8", "const:4:8"]]
+ 00b76704 ["CALL", null, ["callee:00bdb040:8"]]
- 00b766c0 bytes 4c920194
+ 00b76704 bytes 4f920194
- 00b766ec ["INT_ADD", "register:40f0:8", ["const:b766ec:8", "const:4:8"]]
- 00b766ec ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76730 ["INT_ADD", "register:40f0:8", ["const:b76730:8", "const:4:8"]]
+ 00b76730 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b766ec bytes 6d920194
+ 00b76730 bytes 70920194
- 00b76710 ["INT_ADD", "register:40f0:8", ["const:b76710:8", "const:4:8"]]
- 00b76710 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b76754 ["INT_ADD", "register:40f0:8", ["const:b76754:8", "const:4:8"]]
+ 00b76754 ["CALL", null, ["callee:00bdb060:8"]]
- 00b76710 bytes 40920194
+ 00b76754 bytes 43920194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf943e99b705543db01235ed9f833030"></a>

### [`00b76794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76794.md) → [`00b767d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b767d8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda10.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00bdda60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda60.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76794.md#insn-00b76808) · [`00b76830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76794.md#insn-00b76830)
- 新版 `00b7684c`（命令位置の公開資料なし） · `00b76874`（命令位置の公開資料なし）

~~~diff
- 00b76808 ["INT_ADD", "register:40f0:8", ["const:b76808:8", "const:4:8"]]
- 00b76808 ["CALL", null, ["callee:00be1000:8"]]
+ 00b7684c ["INT_ADD", "register:40f0:8", ["const:b7684c:8", "const:4:8"]]
+ 00b7684c ["CALL", null, ["callee:00be1000:8"]]
- 00b76808 bytes eaa90194
+ 00b7684c bytes eda90194
- 00b76830 ["INT_ADD", "register:40f0:8", ["const:b76830:8", "const:4:8"]]
- 00b76830 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76874 ["INT_ADD", "register:40f0:8", ["const:b76874:8", "const:4:8"]]
+ 00b76874 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76830 bytes 1c920194
+ 00b76874 bytes 1f920194
~~~


<a id="compare-507c4b2250aed7a73d0b4a7a84b90b23"></a>

### [`00b7686c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md) → [`00b768b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b768b0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignERKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00b76530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b768bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7686c.md#insn-00b768bc)
- 新版 `00b76900`（命令位置の公開資料なし）

~~~diff
- 00b768bc ["INT_ADD", "register:40f0:8", ["const:b768bc:8", "const:4:8"]]
- 00b768bc ["CALL", null, ["callee:00b75a68:8"]]
+ 00b76900 ["INT_ADD", "register:40f0:8", ["const:b76900:8", "const:4:8"]]
+ 00b76900 ["CALL", null, ["callee:00b75a68:8"]]
- 00b768bc bytes 5afcff97
+ 00b76900 bytes 5afcff97
~~~


<a id="compare-11641e49445834fc59961e969a45122e"></a>

### [`00b768c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md) → [`00b76904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76904.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md#insn-00b76918) · [`00b76930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b768c0.md#insn-00b76930)
- 新版 `00b7695c`（命令位置の公開資料なし） · `00b76974`（命令位置の公開資料なし）

~~~diff
- 00b76918 ["INT_ADD", "register:40f0:8", ["const:b76918:8", "const:4:8"]]
- 00b76918 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b7695c ["INT_ADD", "register:40f0:8", ["const:b7695c:8", "const:4:8"]]
+ 00b7695c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76918 bytes e2910194
+ 00b7695c bytes e5910194
- 00b76930 ["INT_ADD", "register:40f0:8", ["const:b76930:8", "const:4:8"]]
- 00b76930 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b76974 ["INT_ADD", "register:40f0:8", ["const:b76974:8", "const:4:8"]]
+ 00b76974 ["CALL", null, ["callee:00b75a68:8"]]
- 00b76930 bytes 3dfcff97
+ 00b76974 bytes 3dfcff97
~~~


<a id="compare-eaa0ba6b5727933a810fde0c36de6691"></a>

### [`00b76934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md) → [`00b76978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76978.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda70.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bddac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddac0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b769d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b769d4) · [`00b769f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b769f4) · [`00b76a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76934.md#insn-00b76a18)
- 新版 `00b76a18`（命令位置の公開資料なし） · `00b76a38`（命令位置の公開資料なし） · `00b76a5c`（命令位置の公開資料なし）

~~~diff
- 00b769d4 ["INT_ADD", "register:40f0:8", ["const:b769d4:8", "const:4:8"]]
- 00b769d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b76a18 ["INT_ADD", "register:40f0:8", ["const:b76a18:8", "const:4:8"]]
+ 00b76a18 ["CALL", null, ["callee:00bdb040:8"]]
- 00b769d4 bytes 87910194
+ 00b76a18 bytes 8a910194
- 00b769f4 ["INT_ADD", "register:40f0:8", ["const:b769f4:8", "const:4:8"]]
- 00b769f4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76a38 ["INT_ADD", "register:40f0:8", ["const:b76a38:8", "const:4:8"]]
+ 00b76a38 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b769f4 bytes ab910194
+ 00b76a38 bytes ae910194
- 00b76a18 ["INT_ADD", "register:40f0:8", ["const:b76a18:8", "const:4:8"]]
- 00b76a18 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b76a5c ["INT_ADD", "register:40f0:8", ["const:b76a5c:8", "const:4:8"]]
+ 00b76a5c ["CALL", null, ["callee:00b75a68:8"]]
- 00b76a18 bytes 03fcff97
+ 00b76a5c bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f017ed61ae6fea78e2aa88908fc1b744"></a>

### [`00b76a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a28.md) → [`00b76a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76a6c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a28.md#insn-00b76a70)
- 新版 `00b76ab4`（命令位置の公開資料なし）

~~~diff
- 00b76a70 ["INT_ADD", "register:40f0:8", ["const:b76a70:8", "const:4:8"]]
- 00b76a70 ["CALL", null, ["callee:00bdb600:8"]]
+ 00b76ab4 ["INT_ADD", "register:40f0:8", ["const:b76ab4:8", "const:4:8"]]
+ 00b76ab4 ["CALL", null, ["callee:00bdb600:8"]]
- 00b76a70 bytes d0920194
+ 00b76ab4 bytes d3920194
~~~


<a id="compare-a8e6f751eb26b489ffab22d3bd03131c"></a>

### [`00b76a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a9c.md) → [`00b76ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ae0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a9c.md#insn-00b76b08) · [`00b76b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a9c.md#insn-00b76b84) · [`00b76b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a9c.md#insn-00b76b88)
- 新版 `00b76b4c`（命令位置の公開資料なし） · `00b76bc8`（命令位置の公開資料なし） · `00b76bcc`（命令位置の公開資料なし）

~~~diff
- 00b76b08 ["INT_ADD", "register:40f0:8", ["const:b76b08:8", "const:4:8"]]
- 00b76b08 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b76b4c ["INT_ADD", "register:40f0:8", ["const:b76b4c:8", "const:4:8"]]
+ 00b76b4c ["CALL", null, ["callee:00bdb040:8"]]
- 00b76b08 bytes 3a910194
+ 00b76b4c bytes 3d910194
- 00b76b84 ["INT_ADD", "register:40f0:8", ["const:b76b84:8", "const:4:8"]]
- 00b76b84 ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b76bc8 ["INT_ADD", "register:40f0:8", ["const:b76bc8:8", "const:4:8"]]
+ 00b76bc8 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b76b84 bytes 48dbec97
+ 00b76bc8 bytes 37dbec97
- 00b76b88 ["INT_ADD", "register:40f0:8", ["const:b76b88:8", "const:4:8"]]
- 00b76b88 ["CALL", null, ["callee:0041e380:8"]]
+ 00b76bcc ["INT_ADD", "register:40f0:8", ["const:b76bcc:8", "const:4:8"]]
+ 00b76bcc ["CALL", null, ["callee:0041e380:8"]]
- 00b76b88 bytes fe9de297
+ 00b76bcc bytes ed9de297
~~~


<a id="compare-d9b1f7976685c1f9f07f298de59913e6"></a>

### [`00b76b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76b8c.md) → [`00b76bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76bd0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be0fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) [`00be1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76b8c.md#insn-00b76bb0)
- 新版 `00b76bf4`（命令位置の公開資料なし）

~~~diff
- 00b76bb0 ["INT_ADD", "register:40f0:8", ["const:b76bb0:8", "const:4:8"]]
- 00b76bb0 ["CALL", null, ["callee:00be1010:8"]]
+ 00b76bf4 ["INT_ADD", "register:40f0:8", ["const:b76bf4:8", "const:4:8"]]
+ 00b76bf4 ["CALL", null, ["callee:00be1010:8"]]
- 00b76bb0 bytes 04a90194
+ 00b76bf4 bytes 07a90194
~~~


<a id="compare-2018b66fee3bc65e048b2aaf16cea803"></a>

### [`00b76bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76bd8.md) → [`00b76c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76c1c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76bd8.md#insn-00b76c40)
- 新版 `00b76c84`（命令位置の公開資料なし）

~~~diff
- 00b76c40 ["INT_ADD", "register:40f0:8", ["const:b76c40:8", "const:4:8"]]
- 00b76c40 ["CALL", null, ["callee:00bdb600:8"]]
+ 00b76c84 ["INT_ADD", "register:40f0:8", ["const:b76c84:8", "const:4:8"]]
+ 00b76c84 ["CALL", null, ["callee:00bdb600:8"]]
- 00b76c40 bytes 5c920194
+ 00b76c84 bytes 5f920194
~~~


<a id="compare-9c5dccba67bb595313e5471244bc455e"></a>

### [`00b76c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76c74.md) → [`00b76cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76cb8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76c74.md#insn-00b76d28) · [`00b76d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76c74.md#insn-00b76d44) · [`00b76d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76c74.md#insn-00b76d68)
- 新版 `00b76d6c`（命令位置の公開資料なし） · `00b76d88`（命令位置の公開資料なし） · `00b76dac`（命令位置の公開資料なし）

~~~diff
- 00b76d28 ["INT_ADD", "register:40f0:8", ["const:b76d28:8", "const:4:8"]]
- 00b76d28 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b76d6c ["INT_ADD", "register:40f0:8", ["const:b76d6c:8", "const:4:8"]]
+ 00b76d6c ["CALL", null, ["callee:00bdb040:8"]]
- 00b76d28 bytes b2900194
+ 00b76d6c bytes b5900194
- 00b76d44 ["INT_ADD", "register:40f0:8", ["const:b76d44:8", "const:4:8"]]
- 00b76d44 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76d88 ["INT_ADD", "register:40f0:8", ["const:b76d88:8", "const:4:8"]]
+ 00b76d88 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76d44 bytes d7900194
+ 00b76d88 bytes da900194
- 00b76d68 ["INT_ADD", "register:40f0:8", ["const:b76d68:8", "const:4:8"]]
- 00b76d68 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b76dac ["INT_ADD", "register:40f0:8", ["const:b76dac:8", "const:4:8"]]
+ 00b76dac ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b76d68 bytes ce900194
+ 00b76dac bytes d1900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6a302953078631c36a656d0449ffcba"></a>

### [`00b76db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76db4.md) → [`00b76df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76df8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9push_backEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ff0.md) · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 1件 [`00be1040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1040.md) · 呼出先 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76db4.md#insn-00b76e18)
- 新版 `00b76e5c`（命令位置の公開資料なし）

~~~diff
- 00b76e18 ["INT_ADD", "register:40f0:8", ["const:b76e18:8", "const:4:8"]]
- 00b76e18 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b76e5c ["INT_ADD", "register:40f0:8", ["const:b76e5c:8", "const:4:8"]]
+ 00b76e5c ["CALL", null, ["callee:00bdda50:8"]]
- 00b76e18 bytes fa9a0194
+ 00b76e5c bytes fd9a0194
~~~


<a id="compare-e4b600f3723da2b10b35a467f033ca82"></a>

### [`00b76e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76e5c.md) → [`00b76ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ea0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76e5c.md#insn-00b76ed4)
- 新版 `00b76f18`（命令位置の公開資料なし）

~~~diff
- 00b76ed4 ["INT_ADD", "register:40f0:8", ["const:b76ed4:8", "const:4:8"]]
- 00b76ed4 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b76f18 ["INT_ADD", "register:40f0:8", ["const:b76f18:8", "const:4:8"]]
+ 00b76f18 ["CALL", null, ["callee:00bdda50:8"]]
- 00b76ed4 bytes cb9a0194
+ 00b76f18 bytes ce9a0194
~~~


<a id="compare-25db143cfa808bf33bc09202d737eaca"></a>

### [`00b76fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76fdc.md) → [`00b77020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77020.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignEmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76fdc.md#insn-00b77040)
- 新版 `00b77084`（命令位置の公開資料なし）

~~~diff
- 00b77040 ["INT_ADD", "register:40f0:8", ["const:b77040:8", "const:4:8"]]
- 00b77040 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b77084 ["INT_ADD", "register:40f0:8", ["const:b77084:8", "const:4:8"]]
+ 00b77084 ["CALL", null, ["callee:00bdda50:8"]]
- 00b77040 bytes 709a0194
+ 00b77084 bytes 739a0194
~~~


<a id="compare-ba48ef7eb7d67038abe6799831c82c67"></a>

### [`00b770f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md) → [`00b77138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77138.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00b7716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00b771b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b771b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7712c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md#insn-00b7712c) · [`00b77168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md#insn-00b77168)
- 新版 `00b77170`（命令位置の公開資料なし） · `00b771ac`（命令位置の公開資料なし）

~~~diff
- 00b7712c ["INT_ADD", "register:40f0:8", ["const:b7712c:8", "const:4:8"]]
- 00b7712c ["CALL", null, ["callee:00b771b0:8"]]
+ 00b77170 ["INT_ADD", "register:40f0:8", ["const:b77170:8", "const:4:8"]]
+ 00b77170 ["CALL", null, ["callee:00b771b0:8"]]
- 00b7712c bytes 10000094
+ 00b77170 bytes 10000094
- 00b77168 ["INT_ADD", "register:40f0:8", ["const:b77168:8", "const:4:8"]]
- 00b77168 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b771ac ["INT_ADD", "register:40f0:8", ["const:b771ac:8", "const:4:8"]]
+ 00b771ac ["CALL", null, ["callee:00b75a68:8"]]
- 00b77168 bytes 2ffaff97
+ 00b771ac bytes 2ffaff97
~~~


<a id="compare-6985582d7eafa4a2944add0978245f7f"></a>

### [`00b7716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md) → [`00b771b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b771b0.md) FUN_00b771b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b770f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md) [`00bb925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb925c.md) · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`00b77138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77138.md) [`00bb92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b771cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md#insn-00b771cc)
- 新版 `00b77210`（命令位置の公開資料なし）

~~~diff
- 00b771cc ["INT_ADD", "register:40f0:8", ["const:b771cc:8", "const:4:8"]]
- 00b771cc ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b77210 ["INT_ADD", "register:40f0:8", ["const:b77210:8", "const:4:8"]]
+ 00b77210 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b771cc bytes b58f0194
+ 00b77210 bytes b88f0194
~~~


<a id="compare-2395b7ecde23741982a850c562543f68"></a>

### [`00b77208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77208.md) → [`00b7724c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7724c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b772a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77208.md#insn-00b772a4) · [`00b772d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77208.md#insn-00b772d0) · [`00b77310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77208.md#insn-00b77310)
- 新版 `00b772e8`（命令位置の公開資料なし） · `00b77314`（命令位置の公開資料なし） · `00b77354`（命令位置の公開資料なし）

~~~diff
- 00b772a4 ["INT_ADD", "register:40f0:8", ["const:b772a4:8", "const:4:8"]]
- 00b772a4 ["CALL", null, ["callee:00be1000:8"]]
+ 00b772e8 ["INT_ADD", "register:40f0:8", ["const:b772e8:8", "const:4:8"]]
+ 00b772e8 ["CALL", null, ["callee:00be1000:8"]]
- 00b772a4 bytes 43a70194
+ 00b772e8 bytes 46a70194
- 00b772d0 ["INT_ADD", "register:40f0:8", ["const:b772d0:8", "const:4:8"]]
- 00b772d0 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b77314 ["INT_ADD", "register:40f0:8", ["const:b77314:8", "const:4:8"]]
+ 00b77314 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b772d0 bytes 748f0194
+ 00b77314 bytes 778f0194
- 00b77310 ["INT_ADD", "register:40f0:8", ["const:b77310:8", "const:4:8"]]
- 00b77310 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77354 ["INT_ADD", "register:40f0:8", ["const:b77354:8", "const:4:8"]]
+ 00b77354 ["CALL", null, ["callee:00b75a68:8"]]
- 00b77310 bytes c5f9ff97
+ 00b77354 bytes c5f9ff97
~~~


<a id="compare-9d2076f1bdf2fc054c7723d7642d6698"></a>

### [`00b77314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77314.md) → [`00b77358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77358.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77314.md#insn-00b77334) · [`00b77378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77314.md#insn-00b77378) · [`00b773a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77314.md#insn-00b773a4)
- 新版 `00b77378`（命令位置の公開資料なし） · `00b773bc`（命令位置の公開資料なし） · `00b773e8`（命令位置の公開資料なし）

~~~diff
- 00b77334 ["INT_ADD", "register:40f0:8", ["const:b77334:8", "const:4:8"]]
- 00b77334 ["CALL", null, ["callee:00be1010:8"]]
+ 00b77378 ["INT_ADD", "register:40f0:8", ["const:b77378:8", "const:4:8"]]
+ 00b77378 ["CALL", null, ["callee:00be1010:8"]]
- 00b77334 bytes 23a70194
+ 00b77378 bytes 26a70194
- 00b77378 ["INT_ADD", "register:40f0:8", ["const:b77378:8", "const:4:8"]]
- 00b77378 ["CALL", null, ["callee:00be1050:8"]]
+ 00b773bc ["INT_ADD", "register:40f0:8", ["const:b773bc:8", "const:4:8"]]
+ 00b773bc ["CALL", null, ["callee:00be1050:8"]]
- 00b77378 bytes 22a70194
+ 00b773bc bytes 25a70194
- 00b773a4 ["INT_ADD", "register:40f0:8", ["const:b773a4:8", "const:4:8"]]
- 00b773a4 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b773e8 ["INT_ADD", "register:40f0:8", ["const:b773e8:8", "const:4:8"]]
+ 00b773e8 ["CALL", null, ["callee:00b75a68:8"]]
- 00b773a4 bytes a0f9ff97
+ 00b773e8 bytes a0f9ff97
~~~


<a id="compare-a7bc63b61358f99ca9eaa6cf32f52323"></a>

### [`00b773ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b773ac.md) → [`00b773f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b773f0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b773ac.md#insn-00b77410) · [`00b77434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b773ac.md#insn-00b77434)
- 新版 `00b77454`（命令位置の公開資料なし） · `00b77478`（命令位置の公開資料なし）

~~~diff
- 00b77410 ["INT_ADD", "register:40f0:8", ["const:b77410:8", "const:4:8"]]
- 00b77410 ["CALL", null, ["callee:00be1050:8"]]
+ 00b77454 ["INT_ADD", "register:40f0:8", ["const:b77454:8", "const:4:8"]]
+ 00b77454 ["CALL", null, ["callee:00be1050:8"]]
- 00b77410 bytes fca60194
+ 00b77454 bytes ffa60194
- 00b77434 ["INT_ADD", "register:40f0:8", ["const:b77434:8", "const:4:8"]]
- 00b77434 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77478 ["INT_ADD", "register:40f0:8", ["const:b77478:8", "const:4:8"]]
+ 00b77478 ["CALL", null, ["callee:00b75a68:8"]]
- 00b77434 bytes 7cf9ff97
+ 00b77478 bytes 7cf9ff97
~~~


<a id="compare-8cc953b8c59d377bd03caabf3a10680a"></a>

### [`00b77438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77438.md) → [`00b7747c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7747c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77438.md#insn-00b77464) · [`00b774bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77438.md#insn-00b774bc) · [`00b774ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77438.md#insn-00b774ec)
- 新版 `00b774a8`（命令位置の公開資料なし） · `00b77500`（命令位置の公開資料なし） · `00b77530`（命令位置の公開資料なし）

~~~diff
- 00b77464 ["INT_ADD", "register:40f0:8", ["const:b77464:8", "const:4:8"]]
- 00b77464 ["CALL", null, ["callee:00be1010:8"]]
+ 00b774a8 ["INT_ADD", "register:40f0:8", ["const:b774a8:8", "const:4:8"]]
+ 00b774a8 ["CALL", null, ["callee:00be1010:8"]]
- 00b77464 bytes d7a60194
+ 00b774a8 bytes daa60194
- 00b774bc ["INT_ADD", "register:40f0:8", ["const:b774bc:8", "const:4:8"]]
- 00b774bc ["CALL", null, ["callee:00be1050:8"]]
+ 00b77500 ["INT_ADD", "register:40f0:8", ["const:b77500:8", "const:4:8"]]
+ 00b77500 ["CALL", null, ["callee:00be1050:8"]]
- 00b774bc bytes d1a60194
+ 00b77500 bytes d4a60194
- 00b774ec ["INT_ADD", "register:40f0:8", ["const:b774ec:8", "const:4:8"]]
- 00b774ec ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77530 ["INT_ADD", "register:40f0:8", ["const:b77530:8", "const:4:8"]]
+ 00b77530 ["CALL", null, ["callee:00b75a68:8"]]
- 00b774ec bytes 4ef9ff97
+ 00b77530 bytes 4ef9ff97
~~~


<a id="compare-507c41fd4a9b922799526663358023f4"></a>

### [`00b774f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b774f0.md) → [`00b77534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77534.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b774f0.md#insn-00b77534)
- 新版 `00b77578`（命令位置の公開資料なし）

~~~diff
- 00b77534 ["INT_ADD", "register:40f0:8", ["const:b77534:8", "const:4:8"]]
- 00b77534 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77578 ["INT_ADD", "register:40f0:8", ["const:b77578:8", "const:4:8"]]
+ 00b77578 ["CALL", null, ["callee:00b75a68:8"]]
- 00b77534 bytes 3cf9ff97
+ 00b77578 bytes 3cf9ff97
~~~


<a id="compare-d5763b332a9c89c59df1b4d181683eb3"></a>

### [`00b77540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md) → [`00b77584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77584.md) FUN_00b77584

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b77538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77538.md) · 呼出先 2件 [`00b764ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b764ec.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)
- 新版 呼出元 1件 [`00b7757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7757c.md) · 呼出先 2件 [`00b76530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76530.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7755c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77540.md#insn-00b7755c)
- 新版 `00b775a0`（命令位置の公開資料なし）

~~~diff
- 00b7755c ["INT_ADD", "register:40f0:8", ["const:b7755c:8", "const:4:8"]]
- 00b7755c ["CALL", null, ["callee:00be1010:8"]]
+ 00b775a0 ["INT_ADD", "register:40f0:8", ["const:b775a0:8", "const:4:8"]]
+ 00b775a0 ["CALL", null, ["callee:00be1010:8"]]
- 00b7755c bytes 99a60194
+ 00b775a0 bytes 9ca60194
~~~


<a id="compare-7c295a4e3b27a4329f9a02d6c126b290"></a>

### [`00b7757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7757c.md) → [`00b775c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b775c0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEPKwmm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7757c.md#insn-00b77628) · [`00b7763c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7757c.md#insn-00b7763c)
- 新版 `00b7766c`（命令位置の公開資料なし） · `00b77680`（命令位置の公開資料なし）

~~~diff
- 00b77628 ["INT_ADD", "register:40f0:8", ["const:b77628:8", "const:4:8"]]
- 00b77628 ["CALL", null, ["callee:00bdb600:8"]]
+ 00b7766c ["INT_ADD", "register:40f0:8", ["const:b7766c:8", "const:4:8"]]
+ 00b7766c ["CALL", null, ["callee:00bdb600:8"]]
- 00b77628 bytes e28f0194
+ 00b7766c bytes e58f0194
- 00b7763c ["INT_ADD", "register:40f0:8", ["const:b7763c:8", "const:4:8"]]
- 00b7763c ["CALL", null, ["callee:00be1050:8"]]
+ 00b77680 ["INT_ADD", "register:40f0:8", ["const:b77680:8", "const:4:8"]]
+ 00b77680 ["CALL", null, ["callee:00be1050:8"]]
- 00b7763c bytes 71a60194
+ 00b77680 bytes 74a60194
~~~


<a id="compare-d136225c8ed602200cba196278971aa8"></a>

### [`00b7776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md) → [`00b777b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b777b0.md) FUN_00b777b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b77714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77714.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b77758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77758.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b777ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md#insn-00b777ac) · [`00b777f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md#insn-00b777f4) · [`00b77804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md#insn-00b77804)
- 新版 `00b777f0`（命令位置の公開資料なし） · `00b77838`（命令位置の公開資料なし） · `00b77848`（命令位置の公開資料なし）

~~~diff
- 00b777ac ["INT_ADD", "register:40f0:8", ["const:b777ac:8", "const:4:8"]]
- 00b777ac ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b777f0 ["INT_ADD", "register:40f0:8", ["const:b777f0:8", "const:4:8"]]
+ 00b777f0 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b777ac bytes 3d8e0194
+ 00b777f0 bytes 408e0194
- 00b777f4 ["INT_ADD", "register:40f0:8", ["const:b777f4:8", "const:4:8"]]
- 00b777f4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b77838 ["INT_ADD", "register:40f0:8", ["const:b77838:8", "const:4:8"]]
+ 00b77838 ["CALL", null, ["callee:00bdb040:8"]]
- 00b777f4 bytes ff8d0194
+ 00b77838 bytes 028e0194
- 00b77804 ["INT_ADD", "register:40f0:8", ["const:b77804:8", "const:4:8"]]
- 00b77804 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b77848 ["INT_ADD", "register:40f0:8", ["const:b77848:8", "const:4:8"]]
+ 00b77848 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b77804 bytes 578e0194
+ 00b77848 bytes 5a8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-457d2bc632f1b72f504b0a71ee756c67"></a>

### [`00b77840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md) → [`00b77884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77884.md) FUN_00b77884

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b77714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77714.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00b77758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77758.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md#insn-00b77888) · [`00b778b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md#insn-00b778b4)
- 新版 `00b778cc`（命令位置の公開資料なし） · `00b778f8`（命令位置の公開資料なし）

~~~diff
- 00b77888 ["INT_ADD", "register:40f0:8", ["const:b77888:8", "const:4:8"]]
- 00b77888 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b778cc ["INT_ADD", "register:40f0:8", ["const:b778cc:8", "const:4:8"]]
+ 00b778cc ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b77888 bytes 068e0194
+ 00b778cc bytes 098e0194
- 00b778b4 ["INT_ADD", "register:40f0:8", ["const:b778b4:8", "const:4:8"]]
- 00b778b4 ["CALL", null, ["callee:00be1000:8"]]
+ 00b778f8 ["INT_ADD", "register:40f0:8", ["const:b778f8:8", "const:4:8"]]
+ 00b778f8 ["CALL", null, ["callee:00be1000:8"]]
- 00b778b4 bytes bfa50194
+ 00b778f8 bytes c2a50194
~~~


<a id="compare-685a8becccb69a1176a7ed32b701a6a9"></a>

### [`00b778d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b778d0.md) → [`00b77914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77914.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b778f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b778d0.md#insn-00b778f4) · [`00b77950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b778d0.md#insn-00b77950) · [`00b77978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b778d0.md#insn-00b77978)
- 新版 `00b77938`（命令位置の公開資料なし） · `00b77994`（命令位置の公開資料なし） · `00b779bc`（命令位置の公開資料なし）

~~~diff
- 00b778f4 ["INT_ADD", "register:40f0:8", ["const:b778f4:8", "const:4:8"]]
- 00b778f4 ["CALL", null, ["callee:00be1010:8"]]
+ 00b77938 ["INT_ADD", "register:40f0:8", ["const:b77938:8", "const:4:8"]]
+ 00b77938 ["CALL", null, ["callee:00be1010:8"]]
- 00b778f4 bytes b3a50194
+ 00b77938 bytes b6a50194
- 00b77950 ["INT_ADD", "register:40f0:8", ["const:b77950:8", "const:4:8"]]
- 00b77950 ["CALL", null, ["callee:00be1000:8"]]
+ 00b77994 ["INT_ADD", "register:40f0:8", ["const:b77994:8", "const:4:8"]]
+ 00b77994 ["CALL", null, ["callee:00be1000:8"]]
- 00b77950 bytes 98a50194
+ 00b77994 bytes 9ba50194
- 00b77978 ["INT_ADD", "register:40f0:8", ["const:b77978:8", "const:4:8"]]
- 00b77978 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b779bc ["INT_ADD", "register:40f0:8", ["const:b779bc:8", "const:4:8"]]
+ 00b779bc ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b77978 bytes ca8d0194
+ 00b779bc bytes cd8d0194
~~~


<a id="compare-c93c253de16ddd4c55966acdb738e32a"></a>

### [`00b779b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b779b8.md) → [`00b779fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b779fc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be0ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b779b8.md#insn-00b77a04)
- 新版 `00b77a48`（命令位置の公開資料なし）

~~~diff
- 00b77a04 ["INT_ADD", "register:40f0:8", ["const:b77a04:8", "const:4:8"]]
- 00b77a04 ["CALL", null, ["callee:00b75a68:8"]]
+ 00b77a48 ["INT_ADD", "register:40f0:8", ["const:b77a48:8", "const:4:8"]]
+ 00b77a48 ["CALL", null, ["callee:00b75a68:8"]]
- 00b77a04 bytes 08f8ff97
+ 00b77a48 bytes 08f8ff97
~~~


<a id="compare-d09ff3f0c4eaa8337842303c59138ccb"></a>

### [`00b77a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md) → [`00b77a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77a4c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md#insn-00b77a88) · [`00b77ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77a08.md#insn-00b77ab8)
- 新版 `00b77acc`（命令位置の公開資料なし） · `00b77afc`（命令位置の公開資料なし）

~~~diff
- 00b77a88 ["INT_ADD", "register:40f0:8", ["const:b77a88:8", "const:4:8"]]
- 00b77a88 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b77acc ["INT_ADD", "register:40f0:8", ["const:b77acc:8", "const:4:8"]]
+ 00b77acc ["CALL", null, ["callee:00bdda50:8"]]
- 00b77a88 bytes de970194
+ 00b77acc bytes e1970194
- 00b77ab8 ["INT_ADD", "register:40f0:8", ["const:b77ab8:8", "const:4:8"]]
- 00b77ab8 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b77afc ["INT_ADD", "register:40f0:8", ["const:b77afc:8", "const:4:8"]]
+ 00b77afc ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b77ab8 bytes 7a8d0194
+ 00b77afc bytes 7d8d0194
~~~


<a id="compare-183d85987e20f35c615692ecee9d0292"></a>

### [`00b77b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77b0c.md) → [`00b77b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77b50.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9f0.md) · 呼出先 1件 [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)
- 新版 呼出元 1件 [`00bdda40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda40.md) · 呼出先 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b77b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77b0c.md#insn-00b77b90)
- 新版 `00b77bd4`（命令位置の公開資料なし）

~~~diff
- 00b77b90 ["INT_ADD", "register:40f0:8", ["const:b77b90:8", "const:4:8"]]
- 00b77b90 ["CALL", null, ["callee:00bdda50:8"]]
+ 00b77bd4 ["INT_ADD", "register:40f0:8", ["const:b77bd4:8", "const:4:8"]]
+ 00b77bd4 ["CALL", null, ["callee:00bdda50:8"]]
- 00b77b90 bytes 9c970194
+ 00b77bd4 bytes 9f970194
~~~


