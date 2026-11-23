# v15.7.3 → v15.7.4 · 要調査の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-3280fead06211cdc05209a396d065310"></a>

### [`00b81534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81534.md) → [`00b81578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81534.md#insn-00b81574) · [`00b81584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81534.md#insn-00b81584) · [`00b815d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81534.md#insn-00b815d8)
- 新版 [`00b815b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b815b8) · [`00b815c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b815c8) · [`00b8161c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b8161c)

~~~diff
- 00b81574 ["INT_ADD", "register:40f0:8", ["const:b81574:8", "const:4:8"]]
- 00b81574 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b815b8 ["INT_ADD", "register:40f0:8", ["const:b815b8:8", "const:4:8"]]
+ 00b815b8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b81574 bytes a3670194
+ 00b815b8 bytes a6670194
- 00b81584 ["INT_ADD", "register:40f0:8", ["const:b81584:8", "const:4:8"]]
- 00b81584 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b815c8 ["INT_ADD", "register:40f0:8", ["const:b815c8:8", "const:4:8"]]
+ 00b815c8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b81584 bytes 6b6e0194
+ 00b815c8 bytes 6e6e0194
- 00b815d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b815d8 ["INT_ADD", "register:40f0:8", ["const:b815d8:8", "const:4:8"]]
- 00b815d8 ["CALLIND", null, ["register:0:8"]]
+ 00b8161c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8161c ["INT_ADD", "register:40f0:8", ["const:b8161c:8", "const:4:8"]]
+ 00b8161c ["CALLIND", null, ["register:0:8"]]
- 00b815d8 bytes 00013fd6
+ 00b8161c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e64e7484d66c369d3e97353f735494e1"></a>

### [`00b81668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81668.md) → [`00b816ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b816a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81668.md#insn-00b816a4) · [`00b816b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81668.md#insn-00b816b4) · [`00b81700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81668.md#insn-00b81700)
- 新版 [`00b816e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md#insn-00b816e8) · [`00b816f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md#insn-00b816f8) · [`00b81744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md#insn-00b81744)

~~~diff
- 00b816a4 ["INT_ADD", "register:40f0:8", ["const:b816a4:8", "const:4:8"]]
- 00b816a4 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b816e8 ["INT_ADD", "register:40f0:8", ["const:b816e8:8", "const:4:8"]]
+ 00b816e8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b816a4 bytes 57670194
+ 00b816e8 bytes 5a670194
- 00b816b4 ["INT_ADD", "register:40f0:8", ["const:b816b4:8", "const:4:8"]]
- 00b816b4 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b816f8 ["INT_ADD", "register:40f0:8", ["const:b816f8:8", "const:4:8"]]
+ 00b816f8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b816b4 bytes 1f6e0194
+ 00b816f8 bytes 226e0194
- 00b81700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81700 ["INT_ADD", "register:40f0:8", ["const:b81700:8", "const:4:8"]]
- 00b81700 ["CALLIND", null, ["register:0:8"]]
+ 00b81744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81744 ["INT_ADD", "register:40f0:8", ["const:b81744:8", "const:4:8"]]
+ 00b81744 ["CALLIND", null, ["register:0:8"]]
- 00b81700 bytes 00013fd6
+ 00b81744 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb31d9adb9b50de082f273187f9ef5f"></a>

### [`00b81790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81790.md) → [`00b817d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b817b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81790.md#insn-00b817b4) · [`00b817dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81790.md#insn-00b817dc) · [`00b81800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81790.md#insn-00b81800)
- 新版 [`00b817f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b817f8) · [`00b81820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b81820) · [`00b81844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b81844)

~~~diff
- 00b817b4 ["INT_ADD", "register:40f0:8", ["const:b817b4:8", "const:4:8"]]
- 00b817b4 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b817f8 ["INT_ADD", "register:40f0:8", ["const:b817f8:8", "const:4:8"]]
+ 00b817f8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b817b4 bytes df6d0194
+ 00b817f8 bytes e26d0194
- 00b817dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b817dc ["INT_ADD", "register:40f0:8", ["const:b817dc:8", "const:4:8"]]
- 00b817dc ["CALLIND", null, ["register:0:8"]]
+ 00b81820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81820 ["INT_ADD", "register:40f0:8", ["const:b81820:8", "const:4:8"]]
+ 00b81820 ["CALLIND", null, ["register:0:8"]]
- 00b817dc bytes 00013fd6
+ 00b81820 bytes 00013fd6
- 00b81800 ["INT_ADD", "register:40f0:8", ["const:b81800:8", "const:4:8"]]
- 00b81800 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b81844 ["INT_ADD", "register:40f0:8", ["const:b81844:8", "const:4:8"]]
+ 00b81844 ["CALL", null, ["callee:00bdb450:8"]]
- 00b81800 bytes 00670194
+ 00b81844 bytes 03670194
~~~


<a id="compare-98687b4aa5432ab523239fdb30d0824d"></a>

### [`00b81880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81880.md) → [`00b818c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc960.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00bdc9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9b0.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b818bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81880.md#insn-00b818bc) · [`00b818cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81880.md#insn-00b818cc) · [`00b818fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81880.md#insn-00b818fc)
- 新版 [`00b81900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b81900) · [`00b81910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b81910) · [`00b81940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b81940)

~~~diff
- 00b818bc ["INT_ADD", "register:40f0:8", ["const:b818bc:8", "const:4:8"]]
- 00b818bc ["CALL", null, ["callee:00bdb450:8"]]
+ 00b81900 ["INT_ADD", "register:40f0:8", ["const:b81900:8", "const:4:8"]]
+ 00b81900 ["CALL", null, ["callee:00bdb450:8"]]
- 00b818bc bytes d1660194
+ 00b81900 bytes d4660194
- 00b818cc ["INT_ADD", "register:40f0:8", ["const:b818cc:8", "const:4:8"]]
- 00b818cc ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b81910 ["INT_ADD", "register:40f0:8", ["const:b81910:8", "const:4:8"]]
+ 00b81910 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b818cc bytes 996d0194
+ 00b81910 bytes 9c6d0194
- 00b818fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b818fc ["INT_ADD", "register:40f0:8", ["const:b818fc:8", "const:4:8"]]
- 00b818fc ["CALLIND", null, ["register:0:8"]]
+ 00b81940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81940 ["INT_ADD", "register:40f0:8", ["const:b81940:8", "const:4:8"]]
+ 00b81940 ["CALLIND", null, ["register:0:8"]]
- 00b818fc bytes 00013fd6
+ 00b81940 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14f58ab4c6e896041ee8dc98cba9f7e"></a>

### [`00b81990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81990.md) → [`00b819d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b819c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81990.md#insn-00b819c8)
- 新版 [`00b81a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md#insn-00b81a0c)

~~~diff
- 00b819c8 ["INT_ADD", "register:40f0:8", ["const:b819c8:8", "const:4:8"]]
- 00b819c8 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b81a0c ["INT_ADD", "register:40f0:8", ["const:b81a0c:8", "const:4:8"]]
+ 00b81a0c ["CALL", null, ["callee:00bdb390:8"]]
- 00b819c8 bytes 5e660194
+ 00b81a0c bytes 61660194
~~~


<a id="compare-52473a8e7fe7d5eca6419c39858f6a6c"></a>

### [`00b81a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81a5c.md) → [`00b81aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81a5c.md#insn-00b81a8c)
- 新版 [`00b81ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md#insn-00b81ad0)

~~~diff
- 00b81a8c ["INT_ADD", "register:40f0:8", ["const:b81a8c:8", "const:4:8"]]
- 00b81a8c ["CALL", null, ["callee:00be1320:8"]]
+ 00b81ad0 ["INT_ADD", "register:40f0:8", ["const:b81ad0:8", "const:4:8"]]
+ 00b81ad0 ["CALL", null, ["callee:00be1320:8"]]
- 00b81a8c bytes 117e0194
+ 00b81ad0 bytes 147e0194
~~~


<a id="compare-b1a9b84bfb26bd877101deb665728a5b"></a>

### [`00b81ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81ac0.md) → [`00b81b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) · 呼出先 1件 [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)
- 新版 呼出元 1件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) · 呼出先 1件 [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81ac0.md#insn-00b81b04)
- 新版 [`00b81b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md#insn-00b81b48)

~~~diff
- 00b81b04 ["INT_ADD", "register:40f0:8", ["const:b81b04:8", "const:4:8"]]
- 00b81b04 ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b81b48 ["INT_ADD", "register:40f0:8", ["const:b81b48:8", "const:4:8"]]
+ 00b81b48 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b81b04 bytes 53690194
+ 00b81b48 bytes 56690194
~~~


<a id="compare-12bb42676451df56db211fcde555ccf3"></a>

### [`00b81b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81b24.md) → [`00b81b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)
- 新版 呼出元 1件 [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81b24.md#insn-00b81b60) · [`00b81b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81b24.md#insn-00b81b84) · [`00b81ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81b24.md#insn-00b81ba8)
- 新版 [`00b81ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81ba4) · [`00b81bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81bc8) · [`00b81bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b68.md#insn-00b81bec)

~~~diff
- 00b81b60 ["INT_ADD", "register:40f0:8", ["const:b81b60:8", "const:4:8"]]
- 00b81b60 ["CALL", null, ["callee:00be01f0:8"]]
+ 00b81ba4 ["INT_ADD", "register:40f0:8", ["const:b81ba4:8", "const:4:8"]]
+ 00b81ba4 ["CALL", null, ["callee:00be01f0:8"]]
- 00b81b60 bytes 90790194
+ 00b81ba4 bytes 93790194
- 00b81b84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81b84 ["INT_ADD", "register:40f0:8", ["const:b81b84:8", "const:4:8"]]
- 00b81b84 ["CALLIND", null, ["register:0:8"]]
+ 00b81bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b81bc8 ["INT_ADD", "register:40f0:8", ["const:b81bc8:8", "const:4:8"]]
+ 00b81bc8 ["CALLIND", null, ["register:0:8"]]
- 00b81b84 bytes 00013fd6
+ 00b81bc8 bytes 00013fd6
- 00b81ba8 ["INT_ADD", "register:40f0:8", ["const:b81ba8:8", "const:4:8"]]
- 00b81ba8 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b81bec ["INT_ADD", "register:40f0:8", ["const:b81bec:8", "const:4:8"]]
+ 00b81bec ["CALL", null, ["callee:00bdb450:8"]]
- 00b81ba8 bytes 16660194
+ 00b81bec bytes 19660194
~~~


<a id="compare-ff312892b430a220b486163924ca58f5"></a>

### [`00b81bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81bd8.md) → [`00b81c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c1c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_9basic_iosIcS2_EES6_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81bd8.md#insn-00b81bf8)
- 新版 [`00b81c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c1c.md#insn-00b81c3c)

~~~diff
- 00b81bf8 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81bf8 ["INT_ADD", "register:40f0:8", ["const:b81bf8:8", "const:4:8"]]
- 00b81bf8 ["CALLIND", null, ["register:0:8"]]
+ 00b81c3c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b81c3c ["INT_ADD", "register:40f0:8", ["const:b81c3c:8", "const:4:8"]]
+ 00b81c3c ["CALLIND", null, ["register:0:8"]]
- 00b81bf8 bytes 20003fd6
+ 00b81c3c bytes 20003fd6
~~~


<a id="compare-473228698fb0b7389feebd1bffabde4f"></a>

### [`00b81c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c10.md) → [`00b81c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c54.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c10.md#insn-00b81c30)
- 新版 [`00b81c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c54.md#insn-00b81c74)

~~~diff
- 00b81c30 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b81c30 ["INT_ADD", "register:40f0:8", ["const:b81c30:8", "const:4:8"]]
- 00b81c30 ["CALLIND", null, ["register:0:8"]]
+ 00b81c74 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b81c74 ["INT_ADD", "register:40f0:8", ["const:b81c74:8", "const:4:8"]]
+ 00b81c74 ["CALLIND", null, ["register:0:8"]]
- 00b81c30 bytes 20003fd6
+ 00b81c74 bytes 20003fd6
~~~


<a id="compare-c09bb85c71873aff7a47e45fbee9f98f"></a>

### [`00b825b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b825b0.md) → [`00b825f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b825d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b825b0.md#insn-00b825d4) · [`00b8261c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b825b0.md#insn-00b8261c) · [`00b8263c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b825b0.md#insn-00b8263c)
- 新版 [`00b82618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md#insn-00b82618) · [`00b82660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md#insn-00b82660) · [`00b82680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md#insn-00b82680)

~~~diff
- 00b825d4 ["INT_ADD", "register:40f0:8", ["const:b825d4:8", "const:4:8"]]
- 00b825d4 ["CALL", null, ["callee:00bdb410:8"]]
+ 00b82618 ["INT_ADD", "register:40f0:8", ["const:b82618:8", "const:4:8"]]
+ 00b82618 ["CALL", null, ["callee:00bdb410:8"]]
- 00b825d4 bytes 7b630194
+ 00b82618 bytes 7e630194
- 00b8261c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8261c ["INT_ADD", "register:40f0:8", ["const:b8261c:8", "const:4:8"]]
- 00b8261c ["CALLIND", null, ["register:0:8"]]
+ 00b82660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b82660 ["INT_ADD", "register:40f0:8", ["const:b82660:8", "const:4:8"]]
+ 00b82660 ["CALLIND", null, ["register:0:8"]]
- 00b8261c bytes 00013fd6
+ 00b82660 bytes 00013fd6
- 00b8263c ["INT_ADD", "register:40f0:8", ["const:b8263c:8", "const:4:8"]]
- 00b8263c ["CALL", null, ["callee:00bdb450:8"]]
+ 00b82680 ["INT_ADD", "register:40f0:8", ["const:b82680:8", "const:4:8"]]
+ 00b82680 ["CALL", null, ["callee:00bdb450:8"]]
- 00b8263c bytes 71630194
+ 00b82680 bytes 74630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a38dbfa565a8a2b9bef79bec6b21b57"></a>

### [`00b826a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b826a8.md) → [`00b826ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b826f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b826a8.md#insn-00b826f8)
- 新版 [`00b8273c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md#insn-00b8273c)

~~~diff
- 00b826f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b826f8 ["INT_ADD", "register:40f0:8", ["const:b826f8:8", "const:4:8"]]
- 00b826f8 ["CALLIND", null, ["register:0:8"]]
+ 00b8273c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8273c ["INT_ADD", "register:40f0:8", ["const:b8273c:8", "const:4:8"]]
+ 00b8273c ["CALLIND", null, ["register:0:8"]]
- 00b826f8 bytes 00013fd6
+ 00b8273c bytes 00013fd6
~~~


<a id="compare-49f2330a20c5f1c89166491a35e70802"></a>

### [`00b82708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82708.md) → [`00b8274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82708.md#insn-00b82734) · [`00b8276c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82708.md#insn-00b8276c) · [`00b8278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82708.md#insn-00b8278c)
- 新版 [`00b82778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b82778) · [`00b827b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b827b0) · [`00b827d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b827d0)

~~~diff
- 00b82734 ["INT_ADD", "register:40f0:8", ["const:b82734:8", "const:4:8"]]
- 00b82734 ["CALL", null, ["callee:00bdb410:8"]]
+ 00b82778 ["INT_ADD", "register:40f0:8", ["const:b82778:8", "const:4:8"]]
+ 00b82778 ["CALL", null, ["callee:00bdb410:8"]]
- 00b82734 bytes 23630194
+ 00b82778 bytes 26630194
- 00b8276c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8276c ["INT_ADD", "register:40f0:8", ["const:b8276c:8", "const:4:8"]]
- 00b8276c ["CALLIND", null, ["register:0:8"]]
+ 00b827b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b827b0 ["INT_ADD", "register:40f0:8", ["const:b827b0:8", "const:4:8"]]
+ 00b827b0 ["CALLIND", null, ["register:0:8"]]
- 00b8276c bytes 00013fd6
+ 00b827b0 bytes 00013fd6
- 00b8278c ["INT_ADD", "register:40f0:8", ["const:b8278c:8", "const:4:8"]]
- 00b8278c ["CALL", null, ["callee:00bdb450:8"]]
+ 00b827d0 ["INT_ADD", "register:40f0:8", ["const:b827d0:8", "const:4:8"]]
+ 00b827d0 ["CALL", null, ["callee:00bdb450:8"]]
- 00b8278c bytes 1d630194
+ 00b827d0 bytes 20630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217ceb98c24528606161e84e7c922813"></a>

### [`00b827cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b827cc.md) → [`00b82810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b827f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b827cc.md#insn-00b827f8) · [`00b82830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b827cc.md#insn-00b82830) · [`00b82850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b827cc.md#insn-00b82850)
- 新版 [`00b8283c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b8283c) · [`00b82874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b82874) · [`00b82894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b82894)

~~~diff
- 00b827f8 ["INT_ADD", "register:40f0:8", ["const:b827f8:8", "const:4:8"]]
- 00b827f8 ["CALL", null, ["callee:00bdb410:8"]]
+ 00b8283c ["INT_ADD", "register:40f0:8", ["const:b8283c:8", "const:4:8"]]
+ 00b8283c ["CALL", null, ["callee:00bdb410:8"]]
- 00b827f8 bytes f2620194
+ 00b8283c bytes f5620194
- 00b82830 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82830 ["INT_ADD", "register:40f0:8", ["const:b82830:8", "const:4:8"]]
- 00b82830 ["CALLIND", null, ["register:0:8"]]
+ 00b82874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b82874 ["INT_ADD", "register:40f0:8", ["const:b82874:8", "const:4:8"]]
+ 00b82874 ["CALLIND", null, ["register:0:8"]]
- 00b82830 bytes 00013fd6
+ 00b82874 bytes 00013fd6
- 00b82850 ["INT_ADD", "register:40f0:8", ["const:b82850:8", "const:4:8"]]
- 00b82850 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b82894 ["INT_ADD", "register:40f0:8", ["const:b82894:8", "const:4:8"]]
+ 00b82894 ["CALL", null, ["callee:00bdb450:8"]]
- 00b82850 bytes ec620194
+ 00b82894 bytes ef620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd436d772cca3f709fce18a7526b17f9"></a>

### [`00b82890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82890.md) → [`00b828d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b828d4.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b828d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82890.md#insn-00b828d8)
- 新版 [`00b8291c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b828d4.md#insn-00b8291c)

~~~diff
- 00b828d8 ["INT_ADD", "register:40f0:8", ["const:b828d8:8", "const:4:8"]]
- 00b828d8 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b8291c ["INT_ADD", "register:40f0:8", ["const:b8291c:8", "const:4:8"]]
+ 00b8291c ["CALL", null, ["callee:00bdb390:8"]]
- 00b828d8 bytes 9a620194
+ 00b8291c bytes 9d620194
~~~


<a id="compare-ca0115f462eb2c1a38d84edb21c3b7fb"></a>

### [`00b829f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b829f0.md) → [`00b82a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b829f0.md#insn-00b82a08)
- 新版 [`00b82a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md#insn-00b82a4c)

~~~diff
- 00b82a08 ["INT_ADD", "register:40f0:8", ["const:b82a08:8", "const:4:8"]]
- 00b82a08 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b82a4c ["INT_ADD", "register:40f0:8", ["const:b82a4c:8", "const:4:8"]]
+ 00b82a4c ["CALL", null, ["callee:00be01e0:8"]]
- 00b82a08 bytes e2750194
+ 00b82a4c bytes e5750194
~~~


<a id="compare-f3ea907a224d33cfc97790844d18d570"></a>

### [`00b82a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a20.md) → [`00b82a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a64.md) _ZThn16_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a20.md#insn-00b82a38)
- 新版 [`00b82a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a64.md#insn-00b82a7c)

~~~diff
- 00b82a38 ["INT_ADD", "register:40f0:8", ["const:b82a38:8", "const:4:8"]]
- 00b82a38 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b82a7c ["INT_ADD", "register:40f0:8", ["const:b82a7c:8", "const:4:8"]]
+ 00b82a7c ["CALL", null, ["callee:00be01e0:8"]]
- 00b82a38 bytes d6750194
+ 00b82a7c bytes d9750194
~~~


<a id="compare-588e324c141944de2258d23beab40c5e"></a>

### [`00b82a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a50.md) → [`00b82a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a94.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a50.md#insn-00b82a70)
- 新版 [`00b82ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a94.md#insn-00b82ab4)

~~~diff
- 00b82a70 ["INT_ADD", "register:40f0:8", ["const:b82a70:8", "const:4:8"]]
- 00b82a70 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b82ab4 ["INT_ADD", "register:40f0:8", ["const:b82ab4:8", "const:4:8"]]
+ 00b82ab4 ["CALL", null, ["callee:00be01e0:8"]]
- 00b82a70 bytes c8750194
+ 00b82ab4 bytes cb750194
~~~


<a id="compare-43136b6ff6a8a78adbcdce18b94642de"></a>

### [`00b82a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a88.md) → [`00b82acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a88.md#insn-00b82ac0)
- 新版 [`00b82b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md#insn-00b82b04)

~~~diff
- 00b82ac0 ["INT_ADD", "register:40f0:8", ["const:b82ac0:8", "const:4:8"]]
- 00b82ac0 ["CALL", null, ["callee:00be1320:8"]]
+ 00b82b04 ["INT_ADD", "register:40f0:8", ["const:b82b04:8", "const:4:8"]]
+ 00b82b04 ["CALL", null, ["callee:00be1320:8"]]
- 00b82ac0 bytes 047a0194
+ 00b82b04 bytes 077a0194
~~~


<a id="compare-bacb119f8ab68512b3a7c0f4a1cb05df"></a>

### [`00b82afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82afc.md) → [`00b82b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b40.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82afc.md#insn-00b82b10)
- 新版 [`00b82b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b40.md#insn-00b82b54)

~~~diff
- 00b82b10 ["INT_ADD", "register:40f0:8", ["const:b82b10:8", "const:4:8"]]
- 00b82b10 ["CALL", null, ["callee:00be13b0:8"]]
+ 00b82b54 ["INT_ADD", "register:40f0:8", ["const:b82b54:8", "const:4:8"]]
+ 00b82b54 ["CALL", null, ["callee:00be13b0:8"]]
- 00b82b10 bytes 147a0194
+ 00b82b54 bytes 177a0194
~~~


<a id="compare-cba67c103ca5a655472baae400fb21f4"></a>

### [`00b82b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82b28.md) → [`00b82b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be12d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12d0.md) [`00be1310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1310.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82b28.md#insn-00b82b50) · [`00b82b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82b28.md#insn-00b82b5c) · [`00b82b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82b28.md#insn-00b82b78)
- 新版 [`00b82b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82b94) · [`00b82ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82ba0) · [`00b82bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b6c.md#insn-00b82bbc)

~~~diff
- 00b82b50 ["INT_ADD", "register:40f0:8", ["const:b82b50:8", "const:4:8"]]
- 00b82b50 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b82b94 ["INT_ADD", "register:40f0:8", ["const:b82b94:8", "const:4:8"]]
+ 00b82b94 ["CALL", null, ["callee:00be12d0:8"]]
- 00b82b50 bytes cc790194
+ 00b82b94 bytes cf790194
- 00b82b5c ["INT_ADD", "register:40f0:8", ["const:b82b5c:8", "const:4:8"]]
- 00b82b5c ["CALL", null, ["callee:00be1310:8"]]
+ 00b82ba0 ["INT_ADD", "register:40f0:8", ["const:b82ba0:8", "const:4:8"]]
+ 00b82ba0 ["CALL", null, ["callee:00be1310:8"]]
- 00b82b5c bytes d9790194
+ 00b82ba0 bytes dc790194
- 00b82b78 ["INT_ADD", "register:40f0:8", ["const:b82b78:8", "const:4:8"]]
- 00b82b78 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b82bbc ["INT_ADD", "register:40f0:8", ["const:b82bbc:8", "const:4:8"]]
+ 00b82bbc ["CALL", null, ["callee:00be12d0:8"]]
- 00b82b78 bytes c2790194
+ 00b82bbc bytes c5790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2661ce4b3c716b4ad68627607e0df5aa"></a>

### [`00b82bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82bbc.md) → [`00b82c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c00.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82bbc.md#insn-00b82bd0)
- 新版 [`00b82c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c00.md#insn-00b82c14)

~~~diff
- 00b82bd0 ["INT_ADD", "register:40f0:8", ["const:b82bd0:8", "const:4:8"]]
- 00b82bd0 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b82c14 ["INT_ADD", "register:40f0:8", ["const:b82c14:8", "const:4:8"]]
+ 00b82c14 ["CALL", null, ["callee:00be13d0:8"]]
- 00b82bd0 bytes ec790194
+ 00b82c14 bytes ef790194
~~~


<a id="compare-48607fb8a090e124d4ef535e366a7582"></a>

### [`00b82be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82be8.md) → [`00b82c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82be8.md#insn-00b82c10) · [`00b82c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82be8.md#insn-00b82c1c)
- 新版 [`00b82c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md#insn-00b82c54) · [`00b82c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c2c.md#insn-00b82c60)

~~~diff
- 00b82c10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b82c10 ["INT_ADD", "register:40f0:8", ["const:b82c10:8", "const:4:8"]]
- 00b82c10 ["CALLIND", null, ["register:0:8"]]
+ 00b82c54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b82c54 ["INT_ADD", "register:40f0:8", ["const:b82c54:8", "const:4:8"]]
+ 00b82c54 ["CALLIND", null, ["register:0:8"]]
- 00b82c10 bytes 20013fd6
+ 00b82c54 bytes 20013fd6
- 00b82c1c ["INT_ADD", "register:40f0:8", ["const:b82c1c:8", "const:4:8"]]
- 00b82c1c ["CALL", null, ["callee:00bdd980:8"]]
+ 00b82c60 ["INT_ADD", "register:40f0:8", ["const:b82c60:8", "const:4:8"]]
+ 00b82c60 ["CALL", null, ["callee:00bdd980:8"]]
- 00b82c1c bytes 456b0194
+ 00b82c60 bytes 486b0194
~~~


<a id="compare-0fc66db3fc6975b4f11975e0068a3f81"></a>

### [`00b82cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82cb4.md) → [`00b82cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82cf8.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82cb4.md#insn-00b82d00)
- 新版 [`00b82d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82cf8.md#insn-00b82d44)

~~~diff
- 00b82d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82d00 ["INT_ADD", "register:40f0:8", ["const:b82d00:8", "const:4:8"]]
- 00b82d00 ["CALLIND", null, ["register:0:8"]]
+ 00b82d44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b82d44 ["INT_ADD", "register:40f0:8", ["const:b82d44:8", "const:4:8"]]
+ 00b82d44 ["CALLIND", null, ["register:0:8"]]
- 00b82d00 bytes 00013fd6
+ 00b82d44 bytes 00013fd6
~~~


<a id="compare-11e5ec5540f581e1944ac6a2106addd1"></a>

### [`00b82ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82ef0.md) → [`00b82f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f34.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82ef0.md#insn-00b82f10)
- 新版 [`00b82f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f34.md#insn-00b82f54)

~~~diff
- 00b82f10 ["INT_ADD", "register:40f0:8", ["const:b82f10:8", "const:4:8"]]
- 00b82f10 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b82f54 ["INT_ADD", "register:40f0:8", ["const:b82f54:8", "const:4:8"]]
+ 00b82f54 ["CALL", null, ["callee:00be12e0:8"]]
- 00b82f10 bytes e0780194
+ 00b82f54 bytes e3780194
~~~


<a id="compare-0af3d62ddc6b4b86fde9b0197eae03eb"></a>

### [`00b82f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82f40.md) → [`00b82f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82f40.md#insn-00b82f64) · [`00b82f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82f40.md#insn-00b82f70) · [`00b82f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82f40.md#insn-00b82f7c)
- 新版 [`00b82fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fa8) · [`00b82fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fb4) · [`00b82fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fc0)

~~~diff
- 00b82f64 ["INT_ADD", "register:40f0:8", ["const:b82f64:8", "const:4:8"]]
- 00b82f64 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b82fa8 ["INT_ADD", "register:40f0:8", ["const:b82fa8:8", "const:4:8"]]
+ 00b82fa8 ["CALL", null, ["callee:00bdd980:8"]]
- 00b82f64 bytes 736a0194
+ 00b82fa8 bytes 766a0194
- 00b82f70 ["INT_ADD", "register:40f0:8", ["const:b82f70:8", "const:4:8"]]
- 00b82f70 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b82fb4 ["INT_ADD", "register:40f0:8", ["const:b82fb4:8", "const:4:8"]]
+ 00b82fb4 ["CALL", null, ["callee:00be12e0:8"]]
- 00b82f70 bytes c8780194
+ 00b82fb4 bytes cb780194
- 00b82f7c ["INT_ADD", "register:40f0:8", ["const:b82f7c:8", "const:4:8"]]
- 00b82f7c ["CALL", null, ["callee:00be12e0:8"]]
+ 00b82fc0 ["INT_ADD", "register:40f0:8", ["const:b82fc0:8", "const:4:8"]]
+ 00b82fc0 ["CALL", null, ["callee:00be12e0:8"]]
- 00b82f7c bytes c5780194
+ 00b82fc0 bytes c8780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc0fcbc540c2367591b5d6fe8ea9f15"></a>

### [`00b8308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8308c.md) → [`00b830d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8308c.md#insn-00b83110) · [`00b83128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8308c.md#insn-00b83128)
- 新版 [`00b83154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md#insn-00b83154) · [`00b8316c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b830d0.md#insn-00b8316c)

~~~diff
- 00b83110 ["INT_ADD", "register:40f0:8", ["const:b83110:8", "const:4:8"]]
- 00b83110 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b83154 ["INT_ADD", "register:40f0:8", ["const:b83154:8", "const:4:8"]]
+ 00b83154 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b83110 bytes e45f0194
+ 00b83154 bytes e75f0194
- 00b83128 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83128 ["INT_ADD", "register:40f0:8", ["const:b83128:8", "const:4:8"]]
- 00b83128 ["CALLIND", null, ["register:0:8"]]
+ 00b8316c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8316c ["INT_ADD", "register:40f0:8", ["const:b8316c:8", "const:4:8"]]
+ 00b8316c ["CALLIND", null, ["register:0:8"]]
- 00b83128 bytes 00013fd6
+ 00b8316c bytes 00013fd6
~~~


<a id="compare-d7969eb0263d8166ed9c3350137bb2a3"></a>

### [`00b8316c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8316c.md) → [`00b831b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b831b0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b8316c.md#insn-00b83188)
- 新版 [`00b831cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b831b0.md#insn-00b831cc)

~~~diff
- 00b83188 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83188 ["INT_ADD", "register:40f0:8", ["const:b83188:8", "const:4:8"]]
- 00b83188 ["CALLIND", null, ["register:0:8"]]
+ 00b831cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b831cc ["INT_ADD", "register:40f0:8", ["const:b831cc:8", "const:4:8"]]
+ 00b831cc ["CALLIND", null, ["register:0:8"]]
- 00b83188 bytes 00013fd6
+ 00b831cc bytes 00013fd6
~~~


<a id="compare-dccaf36bb4867ea35f4bd9bb518dfa14"></a>

### [`00b831bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b831bc.md) → [`00b83200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b831bc.md#insn-00b83238) · [`00b83254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b831bc.md#insn-00b83254)
- 新版 [`00b8327c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md#insn-00b8327c) · [`00b83298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83200.md#insn-00b83298)

~~~diff
- 00b83238 ["INT_ADD", "register:40f0:8", ["const:b83238:8", "const:4:8"]]
- 00b83238 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b8327c ["INT_ADD", "register:40f0:8", ["const:b8327c:8", "const:4:8"]]
+ 00b8327c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b83238 bytes 9a5f0194
+ 00b8327c bytes 9d5f0194
- 00b83254 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83254 ["INT_ADD", "register:40f0:8", ["const:b83254:8", "const:4:8"]]
- 00b83254 ["CALLIND", null, ["register:0:8"]]
+ 00b83298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83298 ["INT_ADD", "register:40f0:8", ["const:b83298:8", "const:4:8"]]
+ 00b83298 ["CALLIND", null, ["register:0:8"]]
- 00b83254 bytes 00013fd6
+ 00b83298 bytes 00013fd6
~~~


<a id="compare-fcb4336d3d88dd2b02a35ae6267be6f2"></a>

### [`00b832a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832a0.md) → [`00b832e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b832e4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b832dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832a0.md#insn-00b832dc)
- 新版 [`00b83320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b832e4.md#insn-00b83320)

~~~diff
- 00b832dc ["INT_ADD", "register:40f0:8", ["const:b832dc:8", "const:4:8"]]
- 00b832dc ["CALL", null, ["callee:00bdb390:8"]]
+ 00b83320 ["INT_ADD", "register:40f0:8", ["const:b83320:8", "const:4:8"]]
+ 00b83320 ["CALL", null, ["callee:00bdb390:8"]]
- 00b832dc bytes 19600194
+ 00b83320 bytes 1c600194
~~~


<a id="compare-2d87572843eadba03fcd62115def9984"></a>

### [`00b83394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83394.md) → [`00b833d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b833d8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b833ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83394.md#insn-00b833ac)
- 新版 [`00b833f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b833d8.md#insn-00b833f0)

~~~diff
- 00b833ac ["INT_ADD", "register:40f0:8", ["const:b833ac:8", "const:4:8"]]
- 00b833ac ["CALL", null, ["callee:00be01e0:8"]]
+ 00b833f0 ["INT_ADD", "register:40f0:8", ["const:b833f0:8", "const:4:8"]]
+ 00b833f0 ["CALL", null, ["callee:00be01e0:8"]]
- 00b833ac bytes 79730194
+ 00b833f0 bytes 7c730194
~~~


<a id="compare-1b2628650bfbfaba6bb3f0a3aa9cb47b"></a>

### [`00b833c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833c4.md) → [`00b83408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83408.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b833e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833c4.md#insn-00b833e4)
- 新版 [`00b83428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83408.md#insn-00b83428)

~~~diff
- 00b833e4 ["INT_ADD", "register:40f0:8", ["const:b833e4:8", "const:4:8"]]
- 00b833e4 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b83428 ["INT_ADD", "register:40f0:8", ["const:b83428:8", "const:4:8"]]
+ 00b83428 ["CALL", null, ["callee:00be01e0:8"]]
- 00b833e4 bytes 6b730194
+ 00b83428 bytes 6e730194
~~~


<a id="compare-99bd1a6b48351c917d23e25536264b39"></a>

### [`00b833fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833fc.md) → [`00b83440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83440.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b833fc.md#insn-00b83434)
- 新版 [`00b83478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83440.md#insn-00b83478)

~~~diff
- 00b83434 ["INT_ADD", "register:40f0:8", ["const:b83434:8", "const:4:8"]]
- 00b83434 ["CALL", null, ["callee:00be1320:8"]]
+ 00b83478 ["INT_ADD", "register:40f0:8", ["const:b83478:8", "const:4:8"]]
+ 00b83478 ["CALL", null, ["callee:00be1320:8"]]
- 00b83434 bytes a7770194
+ 00b83478 bytes aa770194
~~~


<a id="compare-a4dc21dbae599d6fe31f49955f9501c8"></a>

### [`00b83658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83658.md) → [`00b8369c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 1件 [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8368c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83658.md#insn-00b8368c) · [`00b836b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83658.md#insn-00b836b0) · [`00b836d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83658.md#insn-00b836d0)
- 新版 [`00b836d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b836d0) · [`00b836f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b836f4) · [`00b83714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b83714)

~~~diff
- 00b8368c ["INT_ADD", "register:40f0:8", ["const:b8368c:8", "const:4:8"]]
- 00b8368c ["CALL", null, ["callee:00be1400:8"]]
+ 00b836d0 ["INT_ADD", "register:40f0:8", ["const:b836d0:8", "const:4:8"]]
+ 00b836d0 ["CALL", null, ["callee:00be1400:8"]]
- 00b8368c bytes 49770194
+ 00b836d0 bytes 4c770194
- 00b836b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b836b0 ["INT_ADD", "register:40f0:8", ["const:b836b0:8", "const:4:8"]]
- 00b836b0 ["CALLIND", null, ["register:0:8"]]
+ 00b836f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b836f4 ["INT_ADD", "register:40f0:8", ["const:b836f4:8", "const:4:8"]]
+ 00b836f4 ["CALLIND", null, ["register:0:8"]]
- 00b836b0 bytes 00013fd6
+ 00b836f4 bytes 00013fd6
- 00b836d0 ["INT_ADD", "register:40f0:8", ["const:b836d0:8", "const:4:8"]]
- 00b836d0 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b83714 ["INT_ADD", "register:40f0:8", ["const:b83714:8", "const:4:8"]]
+ 00b83714 ["CALL", null, ["callee:00bdb450:8"]]
- 00b836d0 bytes 4c5f0194
+ 00b83714 bytes 4f5f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0072f88e1806846651ce0dca43db182"></a>

### [`00b83748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83748.md) → [`00b8378c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8378c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b83768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83748.md#insn-00b83768)
- 新版 [`00b837ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8378c.md#insn-00b837ac)

~~~diff
- 00b83768 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b83768 ["INT_ADD", "register:40f0:8", ["const:b83768:8", "const:4:8"]]
- 00b83768 ["CALLIND", null, ["register:0:8"]]
+ 00b837ac ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b837ac ["INT_ADD", "register:40f0:8", ["const:b837ac:8", "const:4:8"]]
+ 00b837ac ["CALLIND", null, ["register:0:8"]]
- 00b83768 bytes 20003fd6
+ 00b837ac bytes 20003fd6
~~~


<a id="compare-fd5964649fdf107baa4040a45946cb7d"></a>

### [`00b83780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83780.md) → [`00b837c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837c4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b837a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83780.md#insn-00b837a0)
- 新版 [`00b837e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837c4.md#insn-00b837e4)

~~~diff
- 00b837a0 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b837a0 ["INT_ADD", "register:40f0:8", ["const:b837a0:8", "const:4:8"]]
- 00b837a0 ["CALLIND", null, ["register:0:8"]]
+ 00b837e4 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b837e4 ["INT_ADD", "register:40f0:8", ["const:b837e4:8", "const:4:8"]]
+ 00b837e4 ["CALLIND", null, ["register:0:8"]]
- 00b837a0 bytes 20003fd6
+ 00b837e4 bytes 20003fd6
~~~


<a id="compare-d65ec36e449fe80e5e34c0e412491818"></a>

### [`00b837b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b837b8.md) → [`00b837fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b837e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b837b8.md#insn-00b837e8) · [`00b8384c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b837b8.md#insn-00b8384c) · [`00b83880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b837b8.md#insn-00b83880)
- 新版 [`00b8382c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b8382c) · [`00b83890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b83890) · [`00b838c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b837fc.md#insn-00b838c4)

~~~diff
- 00b837e8 ["INT_ADD", "register:40f0:8", ["const:b837e8:8", "const:4:8"]]
- 00b837e8 ["CALL", null, ["callee:00be1420:8"]]
+ 00b8382c ["INT_ADD", "register:40f0:8", ["const:b8382c:8", "const:4:8"]]
+ 00b8382c ["CALL", null, ["callee:00be1420:8"]]
- 00b837e8 bytes fa760194
+ 00b8382c bytes fd760194
- 00b8384c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8384c ["INT_ADD", "register:40f0:8", ["const:b8384c:8", "const:4:8"]]
- 00b8384c ["CALLIND", null, ["register:0:8"]]
+ 00b83890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b83890 ["INT_ADD", "register:40f0:8", ["const:b83890:8", "const:4:8"]]
+ 00b83890 ["CALLIND", null, ["register:0:8"]]
- 00b8384c bytes 00013fd6
+ 00b83890 bytes 00013fd6
- 00b83880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b83880 ["INT_ADD", "register:40f0:8", ["const:b83880:8", "const:4:8"]]
- 00b83880 ["CALLIND", null, ["register:0:8"]]
+ 00b838c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b838c4 ["INT_ADD", "register:40f0:8", ["const:b838c4:8", "const:4:8"]]
+ 00b838c4 ["CALLIND", null, ["register:0:8"]]
- 00b83880 bytes 00013fd6
+ 00b838c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bf383e9b0e0e34815d11cd1b7f9553f"></a>

### [`00b849c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b849c4.md) → [`00b84a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13e0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00be1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1430.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b849ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b849c4.md#insn-00b849ec) · [`00b84a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b849c4.md#insn-00b84a44) · [`00b84a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b849c4.md#insn-00b84a6c)
- 新版 [`00b84a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84a30) · [`00b84a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84a88) · [`00b84ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84a08.md#insn-00b84ab0)

~~~diff
- 00b849ec ["INT_ADD", "register:40f0:8", ["const:b849ec:8", "const:4:8"]]
- 00b849ec ["CALL", null, ["callee:00be1420:8"]]
+ 00b84a30 ["INT_ADD", "register:40f0:8", ["const:b84a30:8", "const:4:8"]]
+ 00b84a30 ["CALL", null, ["callee:00be1420:8"]]
- 00b849ec bytes 79720194
+ 00b84a30 bytes 7c720194
- 00b84a44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84a44 ["INT_ADD", "register:40f0:8", ["const:b84a44:8", "const:4:8"]]
- 00b84a44 ["CALLIND", null, ["register:0:8"]]
+ 00b84a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84a88 ["INT_ADD", "register:40f0:8", ["const:b84a88:8", "const:4:8"]]
+ 00b84a88 ["CALLIND", null, ["register:0:8"]]
- 00b84a44 bytes 00013fd6
+ 00b84a88 bytes 00013fd6
- 00b84a6c ["INT_ADD", "register:40f0:8", ["const:b84a6c:8", "const:4:8"]]
- 00b84a6c ["CALL", null, ["callee:00bdb450:8"]]
+ 00b84ab0 ["INT_ADD", "register:40f0:8", ["const:b84ab0:8", "const:4:8"]]
+ 00b84ab0 ["CALL", null, ["callee:00bdb450:8"]]
- 00b84a6c bytes 655a0194
+ 00b84ab0 bytes 685a0194
~~~


<a id="compare-20699fdd0df30ff1db5da5f138d11694"></a>

### [`00b84adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84adc.md) → [`00b84b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b20.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84adc.md#insn-00b84af4)
- 新版 [`00b84b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b20.md#insn-00b84b38)

~~~diff
- 00b84af4 ["INT_ADD", "register:40f0:8", ["const:b84af4:8", "const:4:8"]]
- 00b84af4 ["CALL", null, ["callee:00be1430:8"]]
+ 00b84b38 ["INT_ADD", "register:40f0:8", ["const:b84b38:8", "const:4:8"]]
+ 00b84b38 ["CALL", null, ["callee:00be1430:8"]]
- 00b84af4 bytes 3b720194
+ 00b84b38 bytes 3e720194
~~~


<a id="compare-b7fbd3138b2fc9f7353c2d68ea8aad1f"></a>

### [`00b84bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84bbc.md) → [`00b84c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13f0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00be1440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1440.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84bbc.md#insn-00b84bf8) · [`00b84c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84bbc.md#insn-00b84c70) · [`00b84cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84bbc.md#insn-00b84cac)
- 新版 [`00b84c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84c3c) · [`00b84cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84cb4) · [`00b84cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84cf0)

~~~diff
- 00b84bf8 ["INT_ADD", "register:40f0:8", ["const:b84bf8:8", "const:4:8"]]
- 00b84bf8 ["CALL", null, ["callee:00be1420:8"]]
+ 00b84c3c ["INT_ADD", "register:40f0:8", ["const:b84c3c:8", "const:4:8"]]
+ 00b84c3c ["CALL", null, ["callee:00be1420:8"]]
- 00b84bf8 bytes f6710194
+ 00b84c3c bytes f9710194
- 00b84c70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84c70 ["INT_ADD", "register:40f0:8", ["const:b84c70:8", "const:4:8"]]
- 00b84c70 ["CALLIND", null, ["register:0:8"]]
+ 00b84cb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84cb4 ["INT_ADD", "register:40f0:8", ["const:b84cb4:8", "const:4:8"]]
+ 00b84cb4 ["CALLIND", null, ["register:0:8"]]
- 00b84c70 bytes 00013fd6
+ 00b84cb4 bytes 00013fd6
- 00b84cac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84cac ["INT_ADD", "register:40f0:8", ["const:b84cac:8", "const:4:8"]]
- 00b84cac ["CALLIND", null, ["register:0:8"]]
+ 00b84cf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84cf0 ["INT_ADD", "register:40f0:8", ["const:b84cf0:8", "const:4:8"]]
+ 00b84cf0 ["CALLIND", null, ["register:0:8"]]
- 00b84cac bytes 00013fd6
+ 00b84cf0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0dc69d3ec0374756b31c59ac5952f86"></a>

### [`00b84e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84e20.md) → [`00b84e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1400.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00be1450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1450.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b84e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84e20.md#insn-00b84e54) · [`00b84eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84e20.md#insn-00b84eb4) · [`00b84ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84e20.md#insn-00b84ef0)
- 新版 [`00b84e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84e98) · [`00b84ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84ef8) · [`00b84f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84e64.md#insn-00b84f34)

~~~diff
- 00b84e54 ["INT_ADD", "register:40f0:8", ["const:b84e54:8", "const:4:8"]]
- 00b84e54 ["CALL", null, ["callee:00be1420:8"]]
+ 00b84e98 ["INT_ADD", "register:40f0:8", ["const:b84e98:8", "const:4:8"]]
+ 00b84e98 ["CALL", null, ["callee:00be1420:8"]]
- 00b84e54 bytes 5f710194
+ 00b84e98 bytes 62710194
- 00b84eb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84eb4 ["INT_ADD", "register:40f0:8", ["const:b84eb4:8", "const:4:8"]]
- 00b84eb4 ["CALLIND", null, ["register:0:8"]]
+ 00b84ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84ef8 ["INT_ADD", "register:40f0:8", ["const:b84ef8:8", "const:4:8"]]
+ 00b84ef8 ["CALLIND", null, ["register:0:8"]]
- 00b84eb4 bytes 00013fd6
+ 00b84ef8 bytes 00013fd6
- 00b84ef0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b84ef0 ["INT_ADD", "register:40f0:8", ["const:b84ef0:8", "const:4:8"]]
- 00b84ef0 ["CALLIND", null, ["register:0:8"]]
+ 00b84f34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b84f34 ["INT_ADD", "register:40f0:8", ["const:b84f34:8", "const:4:8"]]
+ 00b84f34 ["CALLIND", null, ["register:0:8"]]
- 00b84ef0 bytes 00013fd6
+ 00b84f34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-735cfd17323a915d5e8857e2361d0270"></a>

### [`00b85028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85028.md) → [`00b8506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1410.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00be1460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1460.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85028.md#insn-00b85068) · [`00b850c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85028.md#insn-00b850c0) · [`00b85108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85028.md#insn-00b85108)
- 新版 [`00b850ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md#insn-00b850ac) · [`00b85104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md#insn-00b85104) · [`00b8514c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md#insn-00b8514c)

~~~diff
- 00b85068 ["INT_ADD", "register:40f0:8", ["const:b85068:8", "const:4:8"]]
- 00b85068 ["CALL", null, ["callee:00be1420:8"]]
+ 00b850ac ["INT_ADD", "register:40f0:8", ["const:b850ac:8", "const:4:8"]]
+ 00b850ac ["CALL", null, ["callee:00be1420:8"]]
- 00b85068 bytes da700194
+ 00b850ac bytes dd700194
- 00b850c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b850c0 ["INT_ADD", "register:40f0:8", ["const:b850c0:8", "const:4:8"]]
- 00b850c0 ["CALLIND", null, ["register:0:8"]]
+ 00b85104 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85104 ["INT_ADD", "register:40f0:8", ["const:b85104:8", "const:4:8"]]
+ 00b85104 ["CALLIND", null, ["register:0:8"]]
- 00b850c0 bytes 00013fd6
+ 00b85104 bytes 00013fd6
- 00b85108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85108 ["INT_ADD", "register:40f0:8", ["const:b85108:8", "const:4:8"]]
- 00b85108 ["CALLIND", null, ["register:0:8"]]
+ 00b8514c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8514c ["INT_ADD", "register:40f0:8", ["const:b8514c:8", "const:4:8"]]
+ 00b8514c ["CALLIND", null, ["register:0:8"]]
- 00b85108 bytes 00013fd6
+ 00b8514c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffc94cad4a651c93c04dbb3a0afcdc1e"></a>

### [`00b85264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85264.md) → [`00b852a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85264.md#insn-00b85298) · [`00b852f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85264.md#insn-00b852f0) · [`00b85358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85264.md#insn-00b85358)
- 新版 [`00b852dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md#insn-00b852dc) · [`00b85334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md#insn-00b85334) · [`00b8539c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md#insn-00b8539c)

~~~diff
- 00b85298 ["INT_ADD", "register:40f0:8", ["const:b85298:8", "const:4:8"]]
- 00b85298 ["CALL", null, ["callee:00be1420:8"]]
+ 00b852dc ["INT_ADD", "register:40f0:8", ["const:b852dc:8", "const:4:8"]]
+ 00b852dc ["CALL", null, ["callee:00be1420:8"]]
- 00b85298 bytes 4e700194
+ 00b852dc bytes 51700194
- 00b852f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b852f0 ["INT_ADD", "register:40f0:8", ["const:b852f0:8", "const:4:8"]]
- 00b852f0 ["CALLIND", null, ["register:0:8"]]
+ 00b85334 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b85334 ["INT_ADD", "register:40f0:8", ["const:b85334:8", "const:4:8"]]
+ 00b85334 ["CALLIND", null, ["register:0:8"]]
- 00b852f0 bytes 20013fd6
+ 00b85334 bytes 20013fd6
- 00b85358 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85358 ["INT_ADD", "register:40f0:8", ["const:b85358:8", "const:4:8"]]
- 00b85358 ["CALLIND", null, ["register:0:8"]]
+ 00b8539c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b8539c ["INT_ADD", "register:40f0:8", ["const:b8539c:8", "const:4:8"]]
+ 00b8539c ["CALLIND", null, ["register:0:8"]]
- 00b85358 bytes 20013fd6
+ 00b8539c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ed7b1d39492beb0e0b2d8be619896e"></a>

### [`00b85418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85418.md) → [`00b8545c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85418.md#insn-00b85440) · [`00b85480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85418.md#insn-00b85480) · [`00b854a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85418.md#insn-00b854a8)
- 新版 [`00b85484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md#insn-00b85484) · [`00b854c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md#insn-00b854c4) · [`00b854ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md#insn-00b854ec)

~~~diff
- 00b85440 ["INT_ADD", "register:40f0:8", ["const:b85440:8", "const:4:8"]]
- 00b85440 ["CALL", null, ["callee:00be1420:8"]]
+ 00b85484 ["INT_ADD", "register:40f0:8", ["const:b85484:8", "const:4:8"]]
+ 00b85484 ["CALL", null, ["callee:00be1420:8"]]
- 00b85440 bytes e46f0194
+ 00b85484 bytes e76f0194
- 00b85480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85480 ["INT_ADD", "register:40f0:8", ["const:b85480:8", "const:4:8"]]
- 00b85480 ["CALLIND", null, ["register:0:8"]]
+ 00b854c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b854c4 ["INT_ADD", "register:40f0:8", ["const:b854c4:8", "const:4:8"]]
+ 00b854c4 ["CALLIND", null, ["register:0:8"]]
- 00b85480 bytes 00013fd6
+ 00b854c4 bytes 00013fd6
- 00b854a8 ["INT_ADD", "register:40f0:8", ["const:b854a8:8", "const:4:8"]]
- 00b854a8 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b854ec ["INT_ADD", "register:40f0:8", ["const:b854ec:8", "const:4:8"]]
+ 00b854ec ["CALL", null, ["callee:00bdb450:8"]]
- 00b854a8 bytes d6570194
+ 00b854ec bytes d9570194
~~~


<a id="compare-d3ffda6e01e79f8477feb9aeafd08ef8"></a>

### [`00b85518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85518.md) → [`00b8555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85518.md#insn-00b85548) · [`00b85574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85518.md#insn-00b85574) · [`00b855a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85518.md#insn-00b855a4)
- 新版 [`00b8558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b8558c) · [`00b855b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b855b8) · [`00b855e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8555c.md#insn-00b855e8)

~~~diff
- 00b85548 ["INT_ADD", "register:40f0:8", ["const:b85548:8", "const:4:8"]]
- 00b85548 ["CALL", null, ["callee:00be1420:8"]]
+ 00b8558c ["INT_ADD", "register:40f0:8", ["const:b8558c:8", "const:4:8"]]
+ 00b8558c ["CALL", null, ["callee:00be1420:8"]]
- 00b85548 bytes a26f0194
+ 00b8558c bytes a56f0194
- 00b85574 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85574 ["INT_ADD", "register:40f0:8", ["const:b85574:8", "const:4:8"]]
- 00b85574 ["CALLIND", null, ["register:0:8"]]
+ 00b855b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b855b8 ["INT_ADD", "register:40f0:8", ["const:b855b8:8", "const:4:8"]]
+ 00b855b8 ["CALLIND", null, ["register:0:8"]]
- 00b85574 bytes 00013fd6
+ 00b855b8 bytes 00013fd6
- 00b855a4 ["INT_ADD", "register:40f0:8", ["const:b855a4:8", "const:4:8"]]
- 00b855a4 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b855e8 ["INT_ADD", "register:40f0:8", ["const:b855e8:8", "const:4:8"]]
+ 00b855e8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b855a4 bytes 97570194
+ 00b855e8 bytes 9a570194
~~~


<a id="compare-0754c6a8fadb33fe6692ab5ba0cbc670"></a>

### [`00b85610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85610.md) → [`00b85654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85610.md#insn-00b85640) · [`00b85684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85610.md#insn-00b85684) · [`00b856d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85610.md#insn-00b856d0)
- 新版 [`00b85684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b85684) · [`00b856c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b856c8) · [`00b85714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85654.md#insn-00b85714)

~~~diff
- 00b85640 ["INT_ADD", "register:40f0:8", ["const:b85640:8", "const:4:8"]]
- 00b85640 ["CALL", null, ["callee:00be1420:8"]]
+ 00b85684 ["INT_ADD", "register:40f0:8", ["const:b85684:8", "const:4:8"]]
+ 00b85684 ["CALL", null, ["callee:00be1420:8"]]
- 00b85640 bytes 646f0194
+ 00b85684 bytes 676f0194
- 00b85684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85684 ["INT_ADD", "register:40f0:8", ["const:b85684:8", "const:4:8"]]
- 00b85684 ["CALLIND", null, ["register:0:8"]]
+ 00b856c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b856c8 ["INT_ADD", "register:40f0:8", ["const:b856c8:8", "const:4:8"]]
+ 00b856c8 ["CALLIND", null, ["register:0:8"]]
- 00b85684 bytes 00013fd6
+ 00b856c8 bytes 00013fd6
- 00b856d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b856d0 ["INT_ADD", "register:40f0:8", ["const:b856d0:8", "const:4:8"]]
- 00b856d0 ["CALLIND", null, ["register:0:8"]]
+ 00b85714 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b85714 ["INT_ADD", "register:40f0:8", ["const:b85714:8", "const:4:8"]]
+ 00b85714 ["CALLIND", null, ["register:0:8"]]
- 00b856d0 bytes 20013fd6
+ 00b85714 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4f05d2d32cb0772d554888a955468c8"></a>

### [`00b85764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85764.md) → [`00b857a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b857a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85764.md#insn-00b857a4) · [`00b857b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85764.md#insn-00b857b4) · [`00b85810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85764.md#insn-00b85810)
- 新版 [`00b857e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b857e8) · [`00b857f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b857f8) · [`00b85854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b857a8.md#insn-00b85854)

~~~diff
- 00b857a4 ["INT_ADD", "register:40f0:8", ["const:b857a4:8", "const:4:8"]]
- 00b857a4 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b857e8 ["INT_ADD", "register:40f0:8", ["const:b857e8:8", "const:4:8"]]
+ 00b857e8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b857a4 bytes 17570194
+ 00b857e8 bytes 1a570194
- 00b857b4 ["INT_ADD", "register:40f0:8", ["const:b857b4:8", "const:4:8"]]
- 00b857b4 ["CALL", null, ["callee:00be1420:8"]]
+ 00b857f8 ["INT_ADD", "register:40f0:8", ["const:b857f8:8", "const:4:8"]]
+ 00b857f8 ["CALL", null, ["callee:00be1420:8"]]
- 00b857b4 bytes 076f0194
+ 00b857f8 bytes 0a6f0194
- 00b85810 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85810 ["INT_ADD", "register:40f0:8", ["const:b85810:8", "const:4:8"]]
- 00b85810 ["CALLIND", null, ["register:0:8"]]
+ 00b85854 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85854 ["INT_ADD", "register:40f0:8", ["const:b85854:8", "const:4:8"]]
+ 00b85854 ["CALLIND", null, ["register:0:8"]]
- 00b85810 bytes 00013fd6
+ 00b85854 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a07897d28f6ed07e0919b2e581a8070e"></a>

### [`00b858a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b858a4.md) → [`00b858e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b858e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b858a4.md#insn-00b858e0) · [`00b858f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b858a4.md#insn-00b858f0) · [`00b85944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b858a4.md#insn-00b85944)
- 新版 [`00b85924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85924) · [`00b85934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85934) · [`00b85988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b858e8.md#insn-00b85988)

~~~diff
- 00b858e0 ["INT_ADD", "register:40f0:8", ["const:b858e0:8", "const:4:8"]]
- 00b858e0 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b85924 ["INT_ADD", "register:40f0:8", ["const:b85924:8", "const:4:8"]]
+ 00b85924 ["CALL", null, ["callee:00bdb450:8"]]
- 00b858e0 bytes c8560194
+ 00b85924 bytes cb560194
- 00b858f0 ["INT_ADD", "register:40f0:8", ["const:b858f0:8", "const:4:8"]]
- 00b858f0 ["CALL", null, ["callee:00be1420:8"]]
+ 00b85934 ["INT_ADD", "register:40f0:8", ["const:b85934:8", "const:4:8"]]
+ 00b85934 ["CALL", null, ["callee:00be1420:8"]]
- 00b858f0 bytes b86e0194
+ 00b85934 bytes bb6e0194
- 00b85944 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85944 ["INT_ADD", "register:40f0:8", ["const:b85944:8", "const:4:8"]]
- 00b85944 ["CALLIND", null, ["register:0:8"]]
+ 00b85988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85988 ["INT_ADD", "register:40f0:8", ["const:b85988:8", "const:4:8"]]
+ 00b85988 ["CALLIND", null, ["register:0:8"]]
- 00b85944 bytes 00013fd6
+ 00b85988 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2cbc3a5ada421f0e99cd79b1c4295c"></a>

### [`00b859d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b859d8.md) → [`00b85a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b859fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b859d8.md#insn-00b859fc) · [`00b85a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b859d8.md#insn-00b85a24) · [`00b85a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b859d8.md#insn-00b85a48)
- 新版 [`00b85a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a40) · [`00b85a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a68) · [`00b85a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85a1c.md#insn-00b85a8c)

~~~diff
- 00b859fc ["INT_ADD", "register:40f0:8", ["const:b859fc:8", "const:4:8"]]
- 00b859fc ["CALL", null, ["callee:00be1420:8"]]
+ 00b85a40 ["INT_ADD", "register:40f0:8", ["const:b85a40:8", "const:4:8"]]
+ 00b85a40 ["CALL", null, ["callee:00be1420:8"]]
- 00b859fc bytes 756e0194
+ 00b85a40 bytes 786e0194
- 00b85a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85a24 ["INT_ADD", "register:40f0:8", ["const:b85a24:8", "const:4:8"]]
- 00b85a24 ["CALLIND", null, ["register:0:8"]]
+ 00b85a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85a68 ["INT_ADD", "register:40f0:8", ["const:b85a68:8", "const:4:8"]]
+ 00b85a68 ["CALLIND", null, ["register:0:8"]]
- 00b85a24 bytes 00013fd6
+ 00b85a68 bytes 00013fd6
- 00b85a48 ["INT_ADD", "register:40f0:8", ["const:b85a48:8", "const:4:8"]]
- 00b85a48 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b85a8c ["INT_ADD", "register:40f0:8", ["const:b85a8c:8", "const:4:8"]]
+ 00b85a8c ["CALL", null, ["callee:00bdb450:8"]]
- 00b85a48 bytes 6e560194
+ 00b85a8c bytes 71560194
~~~


<a id="compare-70ed44a87cad2380e39ed12af2a48344"></a>

### [`00b85ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ac8.md) → [`00b85b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ac8.md#insn-00b85aec) · [`00b85b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ac8.md#insn-00b85b1c) · [`00b85b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ac8.md#insn-00b85b40)
- 新版 [`00b85b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b30) · [`00b85b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b60) · [`00b85b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b84)

~~~diff
- 00b85aec ["INT_ADD", "register:40f0:8", ["const:b85aec:8", "const:4:8"]]
- 00b85aec ["CALL", null, ["callee:00be1420:8"]]
+ 00b85b30 ["INT_ADD", "register:40f0:8", ["const:b85b30:8", "const:4:8"]]
+ 00b85b30 ["CALL", null, ["callee:00be1420:8"]]
- 00b85aec bytes 396e0194
+ 00b85b30 bytes 3c6e0194
- 00b85b1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85b1c ["INT_ADD", "register:40f0:8", ["const:b85b1c:8", "const:4:8"]]
- 00b85b1c ["CALLIND", null, ["register:0:8"]]
+ 00b85b60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85b60 ["INT_ADD", "register:40f0:8", ["const:b85b60:8", "const:4:8"]]
+ 00b85b60 ["CALLIND", null, ["register:0:8"]]
- 00b85b1c bytes 00013fd6
+ 00b85b60 bytes 00013fd6
- 00b85b40 ["INT_ADD", "register:40f0:8", ["const:b85b40:8", "const:4:8"]]
- 00b85b40 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b85b84 ["INT_ADD", "register:40f0:8", ["const:b85b84:8", "const:4:8"]]
+ 00b85b84 ["CALL", null, ["callee:00bdb450:8"]]
- 00b85b40 bytes 30560194
+ 00b85b84 bytes 33560194
~~~


<a id="compare-791673c1539b0e095250fe0494e81648"></a>

### [`00b85bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85bc4.md) → [`00b85c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85bc4.md#insn-00b85c00) · [`00b85c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85bc4.md#insn-00b85c10) · [`00b85c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85bc4.md#insn-00b85c40)
- 新版 [`00b85c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c44) · [`00b85c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c54) · [`00b85c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85c08.md#insn-00b85c84)

~~~diff
- 00b85c00 ["INT_ADD", "register:40f0:8", ["const:b85c00:8", "const:4:8"]]
- 00b85c00 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b85c44 ["INT_ADD", "register:40f0:8", ["const:b85c44:8", "const:4:8"]]
+ 00b85c44 ["CALL", null, ["callee:00bdb450:8"]]
- 00b85c00 bytes 00560194
+ 00b85c44 bytes 03560194
- 00b85c10 ["INT_ADD", "register:40f0:8", ["const:b85c10:8", "const:4:8"]]
- 00b85c10 ["CALL", null, ["callee:00be1420:8"]]
+ 00b85c54 ["INT_ADD", "register:40f0:8", ["const:b85c54:8", "const:4:8"]]
+ 00b85c54 ["CALL", null, ["callee:00be1420:8"]]
- 00b85c10 bytes f06d0194
+ 00b85c54 bytes f36d0194
- 00b85c40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85c40 ["INT_ADD", "register:40f0:8", ["const:b85c40:8", "const:4:8"]]
- 00b85c40 ["CALLIND", null, ["register:0:8"]]
+ 00b85c84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85c84 ["INT_ADD", "register:40f0:8", ["const:b85c84:8", "const:4:8"]]
+ 00b85c84 ["CALLIND", null, ["register:0:8"]]
- 00b85c40 bytes 00013fd6
+ 00b85c84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a261c43da2f77fd281392472677ce5"></a>

### [`00b85cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85cd4.md) → [`00b85d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85cd4.md#insn-00b85d10) · [`00b85d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85cd4.md#insn-00b85d20) · [`00b85d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85cd4.md#insn-00b85d50)
- 新版 [`00b85d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d54) · [`00b85d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d64) · [`00b85d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d94)

~~~diff
- 00b85d10 ["INT_ADD", "register:40f0:8", ["const:b85d10:8", "const:4:8"]]
- 00b85d10 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b85d54 ["INT_ADD", "register:40f0:8", ["const:b85d54:8", "const:4:8"]]
+ 00b85d54 ["CALL", null, ["callee:00bdb450:8"]]
- 00b85d10 bytes bc550194
+ 00b85d54 bytes bf550194
- 00b85d20 ["INT_ADD", "register:40f0:8", ["const:b85d20:8", "const:4:8"]]
- 00b85d20 ["CALL", null, ["callee:00be1420:8"]]
+ 00b85d64 ["INT_ADD", "register:40f0:8", ["const:b85d64:8", "const:4:8"]]
+ 00b85d64 ["CALL", null, ["callee:00be1420:8"]]
- 00b85d20 bytes ac6d0194
+ 00b85d64 bytes af6d0194
- 00b85d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85d50 ["INT_ADD", "register:40f0:8", ["const:b85d50:8", "const:4:8"]]
- 00b85d50 ["CALLIND", null, ["register:0:8"]]
+ 00b85d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85d94 ["INT_ADD", "register:40f0:8", ["const:b85d94:8", "const:4:8"]]
+ 00b85d94 ["CALLIND", null, ["register:0:8"]]
- 00b85d50 bytes 00013fd6
+ 00b85d94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a0977f4ed9ecae7ba92ac24203640b"></a>

### [`00b85de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85de4.md) → [`00b85e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e28.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85de4.md#insn-00b85e1c)
- 新版 [`00b85e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e28.md#insn-00b85e60)

~~~diff
- 00b85e1c ["INT_ADD", "register:40f0:8", ["const:b85e1c:8", "const:4:8"]]
- 00b85e1c ["CALL", null, ["callee:00bdb390:8"]]
+ 00b85e60 ["INT_ADD", "register:40f0:8", ["const:b85e60:8", "const:4:8"]]
+ 00b85e60 ["CALL", null, ["callee:00bdb390:8"]]
- 00b85e1c bytes 49550194
+ 00b85e60 bytes 4c550194
~~~


<a id="compare-ad4f59f25f6b6242d2f77681bf330359"></a>

### [`00b85ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ed4.md) → [`00b85f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f18.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ed4.md#insn-00b85eec)
- 新版 [`00b85f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f18.md#insn-00b85f30)

~~~diff
- 00b85eec ["INT_ADD", "register:40f0:8", ["const:b85eec:8", "const:4:8"]]
- 00b85eec ["CALL", null, ["callee:00be01e0:8"]]
+ 00b85f30 ["INT_ADD", "register:40f0:8", ["const:b85f30:8", "const:4:8"]]
+ 00b85f30 ["CALL", null, ["callee:00be01e0:8"]]
- 00b85eec bytes a9680194
+ 00b85f30 bytes ac680194
~~~


<a id="compare-fef2eda33f73c75a22ef3e1f3f4b294a"></a>

### [`00b85f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f04.md) → [`00b85f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f48.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f04.md#insn-00b85f24)
- 新版 [`00b85f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f48.md#insn-00b85f68)

~~~diff
- 00b85f24 ["INT_ADD", "register:40f0:8", ["const:b85f24:8", "const:4:8"]]
- 00b85f24 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b85f68 ["INT_ADD", "register:40f0:8", ["const:b85f68:8", "const:4:8"]]
+ 00b85f68 ["CALL", null, ["callee:00be01e0:8"]]
- 00b85f24 bytes 9b680194
+ 00b85f68 bytes 9e680194
~~~


<a id="compare-9c793930c971075bd0b20bae05d4d916"></a>

### [`00b85f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f3c.md) → [`00b85f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f80.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f3c.md#insn-00b85f6c)
- 新版 [`00b85fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f80.md#insn-00b85fb0)

~~~diff
- 00b85f6c ["INT_ADD", "register:40f0:8", ["const:b85f6c:8", "const:4:8"]]
- 00b85f6c ["CALL", null, ["callee:00be1320:8"]]
+ 00b85fb0 ["INT_ADD", "register:40f0:8", ["const:b85fb0:8", "const:4:8"]]
+ 00b85fb0 ["CALL", null, ["callee:00be1320:8"]]
- 00b85f6c bytes d96c0194
+ 00b85fb0 bytes dc6c0194
~~~


<a id="compare-c9f0ae37817fa7b8ddb27a0c4140dcf9"></a>

### [`00b85fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85fa0.md) → [`00b85fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85fe4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) · 呼出先 1件 [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md)
- 新版 呼出元 1件 [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) · 呼出先 1件 [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85fa0.md#insn-00b85fe4)
- 新版 [`00b86028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85fe4.md#insn-00b86028)

~~~diff
- 00b85fe4 ["INT_ADD", "register:40f0:8", ["const:b85fe4:8", "const:4:8"]]
- 00b85fe4 ["CALL", null, ["callee:00be13f0:8"]]
+ 00b86028 ["INT_ADD", "register:40f0:8", ["const:b86028:8", "const:4:8"]]
+ 00b86028 ["CALL", null, ["callee:00be13f0:8"]]
- 00b85fe4 bytes ef6c0194
+ 00b86028 bytes f26c0194
~~~


<a id="compare-dd352c39d7fab655d0f2f2e9476ed1f5"></a>

### [`00b86004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86004.md) → [`00b86048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md) · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)
- 新版 呼出元 1件 [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86004.md#insn-00b86040) · [`00b86064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86004.md#insn-00b86064) · [`00b86088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86004.md#insn-00b86088)
- 新版 [`00b86084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b86084) · [`00b860a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b860a8) · [`00b860cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86048.md#insn-00b860cc)

~~~diff
- 00b86040 ["INT_ADD", "register:40f0:8", ["const:b86040:8", "const:4:8"]]
- 00b86040 ["CALL", null, ["callee:00be01f0:8"]]
+ 00b86084 ["INT_ADD", "register:40f0:8", ["const:b86084:8", "const:4:8"]]
+ 00b86084 ["CALL", null, ["callee:00be01f0:8"]]
- 00b86040 bytes 58680194
+ 00b86084 bytes 5b680194
- 00b86064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b86064 ["INT_ADD", "register:40f0:8", ["const:b86064:8", "const:4:8"]]
- 00b86064 ["CALLIND", null, ["register:0:8"]]
+ 00b860a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b860a8 ["INT_ADD", "register:40f0:8", ["const:b860a8:8", "const:4:8"]]
+ 00b860a8 ["CALLIND", null, ["register:0:8"]]
- 00b86064 bytes 00013fd6
+ 00b860a8 bytes 00013fd6
- 00b86088 ["INT_ADD", "register:40f0:8", ["const:b86088:8", "const:4:8"]]
- 00b86088 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b860cc ["INT_ADD", "register:40f0:8", ["const:b860cc:8", "const:4:8"]]
+ 00b860cc ["CALL", null, ["callee:00bdb450:8"]]
- 00b86088 bytes de540194
+ 00b860cc bytes e1540194
~~~


<a id="compare-2f76074eeac18a92a0621a53cc6b69cf"></a>

### [`00b860b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860b8.md) → [`00b860fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b860fc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b860d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860b8.md#insn-00b860d8)
- 新版 [`00b8611c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b860fc.md#insn-00b8611c)

~~~diff
- 00b860d8 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b860d8 ["INT_ADD", "register:40f0:8", ["const:b860d8:8", "const:4:8"]]
- 00b860d8 ["CALLIND", null, ["register:0:8"]]
+ 00b8611c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b8611c ["INT_ADD", "register:40f0:8", ["const:b8611c:8", "const:4:8"]]
+ 00b8611c ["CALLIND", null, ["register:0:8"]]
- 00b860d8 bytes 20003fd6
+ 00b8611c bytes 20003fd6
~~~


<a id="compare-f92188883d98e573525c530032452c75"></a>

### [`00b860f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860f0.md) → [`00b86134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86134.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b86110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b860f0.md#insn-00b86110)
- 新版 [`00b86154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86134.md#insn-00b86154)

~~~diff
- 00b86110 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b86110 ["INT_ADD", "register:40f0:8", ["const:b86110:8", "const:4:8"]]
- 00b86110 ["CALLIND", null, ["register:0:8"]]
+ 00b86154 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00b86154 ["INT_ADD", "register:40f0:8", ["const:b86154:8", "const:4:8"]]
+ 00b86154 ["CALLIND", null, ["register:0:8"]]
- 00b86110 bytes 20003fd6
+ 00b86154 bytes 20003fd6
~~~


<a id="compare-9870bfca4da4649b437bb9c6d93289a0"></a>

### [`00b875d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b875d8.md) → [`00b8761c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b875d8.md#insn-00b87600) · [`00b87654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b875d8.md#insn-00b87654) · [`00b87680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b875d8.md#insn-00b87680)
- 新版 [`00b87644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b87644) · [`00b87698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b87698) · [`00b876c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b876c4)

~~~diff
- 00b87600 ["INT_ADD", "register:40f0:8", ["const:b87600:8", "const:4:8"]]
- 00b87600 ["CALL", null, ["callee:00be1400:8"]]
+ 00b87644 ["INT_ADD", "register:40f0:8", ["const:b87644:8", "const:4:8"]]
+ 00b87644 ["CALL", null, ["callee:00be1400:8"]]
- 00b87600 bytes 6c670194
+ 00b87644 bytes 6f670194
- 00b87654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87654 ["INT_ADD", "register:40f0:8", ["const:b87654:8", "const:4:8"]]
- 00b87654 ["CALLIND", null, ["register:0:8"]]
+ 00b87698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87698 ["INT_ADD", "register:40f0:8", ["const:b87698:8", "const:4:8"]]
+ 00b87698 ["CALLIND", null, ["register:0:8"]]
- 00b87654 bytes 00013fd6
+ 00b87698 bytes 00013fd6
- 00b87680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87680 ["INT_ADD", "register:40f0:8", ["const:b87680:8", "const:4:8"]]
- 00b87680 ["CALLIND", null, ["register:0:8"]]
+ 00b876c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b876c4 ["INT_ADD", "register:40f0:8", ["const:b876c4:8", "const:4:8"]]
+ 00b876c4 ["CALLIND", null, ["register:0:8"]]
- 00b87680 bytes 00013fd6
+ 00b876c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f56d71963cca5c50b3eb27ff1f8d18d"></a>

### [`00b877a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b877a4.md) → [`00b877e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE3putEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b877c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b877a4.md#insn-00b877c8) · [`00b87814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b877a4.md#insn-00b87814) · [`00b87838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b877a4.md#insn-00b87838)
- 新版 [`00b8780c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b8780c) · [`00b87858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b87858) · [`00b8787c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b8787c)

~~~diff
- 00b877c8 ["INT_ADD", "register:40f0:8", ["const:b877c8:8", "const:4:8"]]
- 00b877c8 ["CALL", null, ["callee:00be1400:8"]]
+ 00b8780c ["INT_ADD", "register:40f0:8", ["const:b8780c:8", "const:4:8"]]
+ 00b8780c ["CALL", null, ["callee:00be1400:8"]]
- 00b877c8 bytes fa660194
+ 00b8780c bytes fd660194
- 00b87814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87814 ["INT_ADD", "register:40f0:8", ["const:b87814:8", "const:4:8"]]
- 00b87814 ["CALLIND", null, ["register:0:8"]]
+ 00b87858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87858 ["INT_ADD", "register:40f0:8", ["const:b87858:8", "const:4:8"]]
+ 00b87858 ["CALLIND", null, ["register:0:8"]]
- 00b87814 bytes 00013fd6
+ 00b87858 bytes 00013fd6
- 00b87838 ["INT_ADD", "register:40f0:8", ["const:b87838:8", "const:4:8"]]
- 00b87838 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b8787c ["INT_ADD", "register:40f0:8", ["const:b8787c:8", "const:4:8"]]
+ 00b8787c ["CALL", null, ["callee:00bdb450:8"]]
- 00b87838 bytes f24e0194
+ 00b8787c bytes f54e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279bebee7d8c8b98d60e9ca5af19fca9"></a>

### [`00b878a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b878a4.md) → [`00b878e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5writeEPKwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b878d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b878a4.md#insn-00b878d0) · [`00b87900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b878a4.md#insn-00b87900) · [`00b87920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b878a4.md#insn-00b87920)
- 新版 [`00b87914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b87914) · [`00b87944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b87944) · [`00b87964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b87964)

~~~diff
- 00b878d0 ["INT_ADD", "register:40f0:8", ["const:b878d0:8", "const:4:8"]]
- 00b878d0 ["CALL", null, ["callee:00be1400:8"]]
+ 00b87914 ["INT_ADD", "register:40f0:8", ["const:b87914:8", "const:4:8"]]
+ 00b87914 ["CALL", null, ["callee:00be1400:8"]]
- 00b878d0 bytes b8660194
+ 00b87914 bytes bb660194
- 00b87900 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87900 ["INT_ADD", "register:40f0:8", ["const:b87900:8", "const:4:8"]]
- 00b87900 ["CALLIND", null, ["register:0:8"]]
+ 00b87944 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87944 ["INT_ADD", "register:40f0:8", ["const:b87944:8", "const:4:8"]]
+ 00b87944 ["CALLIND", null, ["register:0:8"]]
- 00b87900 bytes 00013fd6
+ 00b87944 bytes 00013fd6
- 00b87920 ["INT_ADD", "register:40f0:8", ["const:b87920:8", "const:4:8"]]
- 00b87920 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b87964 ["INT_ADD", "register:40f0:8", ["const:b87964:8", "const:4:8"]]
+ 00b87964 ["CALL", null, ["callee:00bdb450:8"]]
- 00b87920 bytes b84e0194
+ 00b87964 bytes bb4e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef0261518122105fde4572d97da1d183"></a>

### [`00b87990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87990.md) → [`00b879d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b879d4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5tellpEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b879e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87990.md#insn-00b879e0)
- 新版 [`00b87a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b879d4.md#insn-00b87a24)

~~~diff
- 00b879e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b879e0 ["INT_ADD", "register:40f0:8", ["const:b879e0:8", "const:4:8"]]
- 00b879e0 ["CALLIND", null, ["register:0:8"]]
+ 00b87a24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87a24 ["INT_ADD", "register:40f0:8", ["const:b87a24:8", "const:4:8"]]
+ 00b87a24 ["CALLIND", null, ["register:0:8"]]
- 00b879e0 bytes 00013fd6
+ 00b87a24 bytes 00013fd6
~~~


<a id="compare-0abab12706485c2b1964be239a17eb1f"></a>

### [`00b879f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b879f0.md) → [`00b87a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b879f0.md#insn-00b87a1c) · [`00b87a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b879f0.md#insn-00b87a54) · [`00b87a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b879f0.md#insn-00b87a74)
- 新版 [`00b87a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87a60) · [`00b87a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87a98) · [`00b87ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87ab8)

~~~diff
- 00b87a1c ["INT_ADD", "register:40f0:8", ["const:b87a1c:8", "const:4:8"]]
- 00b87a1c ["CALL", null, ["callee:00be1400:8"]]
+ 00b87a60 ["INT_ADD", "register:40f0:8", ["const:b87a60:8", "const:4:8"]]
+ 00b87a60 ["CALL", null, ["callee:00be1400:8"]]
- 00b87a1c bytes 65660194
+ 00b87a60 bytes 68660194
- 00b87a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87a54 ["INT_ADD", "register:40f0:8", ["const:b87a54:8", "const:4:8"]]
- 00b87a54 ["CALLIND", null, ["register:0:8"]]
+ 00b87a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87a98 ["INT_ADD", "register:40f0:8", ["const:b87a98:8", "const:4:8"]]
+ 00b87a98 ["CALLIND", null, ["register:0:8"]]
- 00b87a54 bytes 00013fd6
+ 00b87a98 bytes 00013fd6
- 00b87a74 ["INT_ADD", "register:40f0:8", ["const:b87a74:8", "const:4:8"]]
- 00b87a74 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b87ab8 ["INT_ADD", "register:40f0:8", ["const:b87ab8:8", "const:4:8"]]
+ 00b87ab8 ["CALL", null, ["callee:00bdb450:8"]]
- 00b87a74 bytes 634e0194
+ 00b87ab8 bytes 664e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f201cdd9c8beb7f536179846efb0577"></a>

### [`00b87ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ab4.md) → [`00b87af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ab4.md#insn-00b87ae0) · [`00b87b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ab4.md#insn-00b87b18) · [`00b87b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ab4.md#insn-00b87b38)
- 新版 [`00b87b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b24) · [`00b87b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b5c) · [`00b87b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b7c)

~~~diff
- 00b87ae0 ["INT_ADD", "register:40f0:8", ["const:b87ae0:8", "const:4:8"]]
- 00b87ae0 ["CALL", null, ["callee:00be1400:8"]]
+ 00b87b24 ["INT_ADD", "register:40f0:8", ["const:b87b24:8", "const:4:8"]]
+ 00b87b24 ["CALL", null, ["callee:00be1400:8"]]
- 00b87ae0 bytes 34660194
+ 00b87b24 bytes 37660194
- 00b87b18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87b18 ["INT_ADD", "register:40f0:8", ["const:b87b18:8", "const:4:8"]]
- 00b87b18 ["CALLIND", null, ["register:0:8"]]
+ 00b87b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87b5c ["INT_ADD", "register:40f0:8", ["const:b87b5c:8", "const:4:8"]]
+ 00b87b5c ["CALLIND", null, ["register:0:8"]]
- 00b87b18 bytes 00013fd6
+ 00b87b5c bytes 00013fd6
- 00b87b38 ["INT_ADD", "register:40f0:8", ["const:b87b38:8", "const:4:8"]]
- 00b87b38 ["CALL", null, ["callee:00bdb450:8"]]
+ 00b87b7c ["INT_ADD", "register:40f0:8", ["const:b87b7c:8", "const:4:8"]]
+ 00b87b7c ["CALL", null, ["callee:00bdb450:8"]]
- 00b87b38 bytes 324e0194
+ 00b87b7c bytes 354e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b8f78a5443a7a0dfa887227835abffc"></a>

### [`00b87c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md) → [`00b87c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md) FUN_00b87c68

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b87b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87b78.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 1件 [`00b87bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md#insn-00b87cdc) · [`00b87d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md#insn-00b87d80) · [`00b87d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87c24.md#insn-00b87d94)
- 新版 [`00b87d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md#insn-00b87d20) · [`00b87dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md#insn-00b87dc4) · [`00b87dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md#insn-00b87dd8)

~~~diff
- 00b87cdc ["INT_ADD", "register:40f0:8", ["const:b87cdc:8", "const:4:8"]]
- 00b87cdc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b87d20 ["INT_ADD", "register:40f0:8", ["const:b87d20:8", "const:4:8"]]
+ 00b87d20 ["CALL", null, ["callee:00bdb060:8"]]
- 00b87cdc bytes cd4c0194
+ 00b87d20 bytes d04c0194
- 00b87d80 ["INT_ADD", "register:40f0:8", ["const:b87d80:8", "const:4:8"]]
- 00b87d80 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b87dc4 ["INT_ADD", "register:40f0:8", ["const:b87dc4:8", "const:4:8"]]
+ 00b87dc4 ["CALL", null, ["callee:00bdd980:8"]]
- 00b87d80 bytes ec560194
+ 00b87dc4 bytes ef560194
- 00b87d94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87d94 ["INT_ADD", "register:40f0:8", ["const:b87d94:8", "const:4:8"]]
- 00b87d94 ["CALLIND", null, ["register:0:8"]]
+ 00b87dd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87dd8 ["INT_ADD", "register:40f0:8", ["const:b87dd8:8", "const:4:8"]]
+ 00b87dd8 ["CALLIND", null, ["register:0:8"]]
- 00b87d94 bytes 00013fd6
+ 00b87dd8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41156e511915c5143d95c44cbd9a555e"></a>

### [`00b87df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87df8.md) → [`00b87e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 1件 [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b87eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87df8.md#insn-00b87eb0) · [`00b87f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87df8.md#insn-00b87f78) · [`00b87f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87df8.md#insn-00b87f8c)
- 新版 [`00b87ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87ef4) · [`00b87fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87fbc) · [`00b87fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87fd0)

~~~diff
- 00b87eb0 ["INT_ADD", "register:40f0:8", ["const:b87eb0:8", "const:4:8"]]
- 00b87eb0 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b87ef4 ["INT_ADD", "register:40f0:8", ["const:b87ef4:8", "const:4:8"]]
+ 00b87ef4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b87eb0 bytes 584c0194
+ 00b87ef4 bytes 5b4c0194
- 00b87f78 ["INT_ADD", "register:40f0:8", ["const:b87f78:8", "const:4:8"]]
- 00b87f78 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b87fbc ["INT_ADD", "register:40f0:8", ["const:b87fbc:8", "const:4:8"]]
+ 00b87fbc ["CALL", null, ["callee:00bdd980:8"]]
- 00b87f78 bytes 6e560194
+ 00b87fbc bytes 71560194
- 00b87f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87f8c ["INT_ADD", "register:40f0:8", ["const:b87f8c:8", "const:4:8"]]
- 00b87f8c ["CALLIND", null, ["register:0:8"]]
+ 00b87fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b87fd0 ["INT_ADD", "register:40f0:8", ["const:b87fd0:8", "const:4:8"]]
+ 00b87fd0 ["CALLIND", null, ["register:0:8"]]
- 00b87f8c bytes 00013fd6
+ 00b87fd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496846ed006cdc64eb6274134f8a8491"></a>

### [`00b87ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ff4.md) → [`00b88038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4swapERS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ff4.md#insn-00b88228) · [`00b88234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ff4.md#insn-00b88234) · [`00b88248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b87/00b87ff4.md#insn-00b88248)
- 新版 [`00b8826c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b8826c) · [`00b88278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b88278) · [`00b8828c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b8828c)

~~~diff
- 00b88228 ["INT_ADD", "register:40f0:8", ["const:b88228:8", "const:4:8"]]
- 00b88228 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b8826c ["INT_ADD", "register:40f0:8", ["const:b8826c:8", "const:4:8"]]
+ 00b8826c ["CALL", null, ["callee:00bdd980:8"]]
- 00b88228 bytes c2550194
+ 00b8826c bytes c5550194
- 00b88234 ["INT_ADD", "register:40f0:8", ["const:b88234:8", "const:4:8"]]
- 00b88234 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b88278 ["INT_ADD", "register:40f0:8", ["const:b88278:8", "const:4:8"]]
+ 00b88278 ["CALL", null, ["callee:00bdd980:8"]]
- 00b88234 bytes bf550194
+ 00b88278 bytes c2550194
- 00b88248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88248 ["INT_ADD", "register:40f0:8", ["const:b88248:8", "const:4:8"]]
- 00b88248 ["CALLIND", null, ["register:0:8"]]
+ 00b8828c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8828c ["INT_ADD", "register:40f0:8", ["const:b8828c:8", "const:4:8"]]
+ 00b8828c ["CALLIND", null, ["register:0:8"]]
- 00b88248 bytes 00013fd6
+ 00b8828c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9428d669e230c3caa8e9b79230c3cb5"></a>

### [`00b882cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md) → [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00b752f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b752f4.md) [`00b753a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b753a8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00b75338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md) [`00b753ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b753ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md#insn-00b88328) · [`00b88340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b882cc.md#insn-00b88340)
- 新版 [`00b8836c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md#insn-00b8836c) · [`00b88384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md#insn-00b88384)

~~~diff
- 00b88328 ["INT_ADD", "register:40f0:8", ["const:b88328:8", "const:4:8"]]
- 00b88328 ["CALL", null, ["callee:00b753ec:8"]]
+ 00b8836c ["INT_ADD", "register:40f0:8", ["const:b8836c:8", "const:4:8"]]
+ 00b8836c ["CALL", null, ["callee:00b753ec:8"]]
- 00b88328 bytes 20b4ff97
+ 00b8836c bytes 20b4ff97
- 00b88340 ["INT_ADD", "register:40f0:8", ["const:b88340:8", "const:4:8"]]
- 00b88340 ["CALL", null, ["callee:00b75338:8"]]
+ 00b88384 ["INT_ADD", "register:40f0:8", ["const:b88384:8", "const:4:8"]]
+ 00b88384 ["CALL", null, ["callee:00b75338:8"]]
- 00b88340 bytes edb3ff97
+ 00b88384 bytes edb3ff97
~~~


<a id="compare-55c642db5a1c8004e452cfb7729d0847"></a>

### [`00b88358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88358.md) → [`00b8839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md) _ZNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8839c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88358.md#insn-00b8839c) · [`00b883c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88358.md#insn-00b883c8)
- 新版 [`00b883e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md#insn-00b883e0) · [`00b8840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md#insn-00b8840c)

~~~diff
- 00b8839c ["INT_ADD", "register:40f0:8", ["const:b8839c:8", "const:4:8"]]
- 00b8839c ["CALL", null, ["callee:00be1320:8"]]
+ 00b883e0 ["INT_ADD", "register:40f0:8", ["const:b883e0:8", "const:4:8"]]
+ 00b883e0 ["CALL", null, ["callee:00be1320:8"]]
- 00b8839c bytes cd630194
+ 00b883e0 bytes d0630194
- 00b883c8 ["INT_ADD", "register:40f0:8", ["const:b883c8:8", "const:4:8"]]
- 00b883c8 ["CALL", null, ["callee:00be1470:8"]]
+ 00b8840c ["INT_ADD", "register:40f0:8", ["const:b8840c:8", "const:4:8"]]
+ 00b8840c ["CALL", null, ["callee:00be1470:8"]]
- 00b883c8 bytes 16640194
+ 00b8840c bytes 19640194
~~~


<a id="compare-e42455b4c42e141afcb9263f8c92f476"></a>

### [`00b883e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b883e4.md) → [`00b88428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md) _ZNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b883e4.md#insn-00b88428) · [`00b88454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b883e4.md#insn-00b88454)
- 新版 [`00b8846c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md#insn-00b8846c) · [`00b88498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md#insn-00b88498)

~~~diff
- 00b88428 ["INT_ADD", "register:40f0:8", ["const:b88428:8", "const:4:8"]]
- 00b88428 ["CALL", null, ["callee:00be1320:8"]]
+ 00b8846c ["INT_ADD", "register:40f0:8", ["const:b8846c:8", "const:4:8"]]
+ 00b8846c ["CALL", null, ["callee:00be1320:8"]]
- 00b88428 bytes aa630194
+ 00b8846c bytes ad630194
- 00b88454 ["INT_ADD", "register:40f0:8", ["const:b88454:8", "const:4:8"]]
- 00b88454 ["CALL", null, ["callee:00be1470:8"]]
+ 00b88498 ["INT_ADD", "register:40f0:8", ["const:b88498:8", "const:4:8"]]
+ 00b88498 ["CALL", null, ["callee:00be1470:8"]]
- 00b88454 bytes f3630194
+ 00b88498 bytes f6630194
~~~


<a id="compare-2fe71ce30b2c46cf50af324fb5b6c926"></a>

### [`00b88474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88474.md) → [`00b884b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md) _ZNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b884b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88474.md#insn-00b884b8) · [`00b884e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88474.md#insn-00b884e4)
- 新版 [`00b884fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md#insn-00b884fc) · [`00b88528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b884b8.md#insn-00b88528)

~~~diff
- 00b884b8 ["INT_ADD", "register:40f0:8", ["const:b884b8:8", "const:4:8"]]
- 00b884b8 ["CALL", null, ["callee:00be1320:8"]]
+ 00b884fc ["INT_ADD", "register:40f0:8", ["const:b884fc:8", "const:4:8"]]
+ 00b884fc ["CALL", null, ["callee:00be1320:8"]]
- 00b884b8 bytes 86630194
+ 00b884fc bytes 89630194
- 00b884e4 ["INT_ADD", "register:40f0:8", ["const:b884e4:8", "const:4:8"]]
- 00b884e4 ["CALL", null, ["callee:00be1470:8"]]
+ 00b88528 ["INT_ADD", "register:40f0:8", ["const:b88528:8", "const:4:8"]]
+ 00b88528 ["CALL", null, ["callee:00be1470:8"]]
- 00b884e4 bytes cf630194
+ 00b88528 bytes d2630194
~~~


<a id="compare-0e365243535ccc50a51e55aa414eecc2"></a>

### [`00b88500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md) → [`00b88544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md#insn-00b88558) · [`00b88568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md#insn-00b88568) · [`00b88584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88500.md#insn-00b88584)
- 新版 [`00b8859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b8859c) · [`00b885ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b885ac) · [`00b885c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md#insn-00b885c8)

~~~diff
- 00b88558 ["INT_ADD", "register:40f0:8", ["const:b88558:8", "const:4:8"]]
- 00b88558 ["CALL", null, ["callee:00b88f5c:8"]]
+ 00b8859c ["INT_ADD", "register:40f0:8", ["const:b8859c:8", "const:4:8"]]
+ 00b8859c ["CALL", null, ["callee:00b88f5c:8"]]
- 00b88558 bytes 70020094
+ 00b8859c bytes 70020094
- 00b88568 ["INT_ADD", "register:40f0:8", ["const:b88568:8", "const:4:8"]]
- 00b88568 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b885ac ["INT_ADD", "register:40f0:8", ["const:b885ac:8", "const:4:8"]]
+ 00b885ac ["CALL", null, ["callee:00bdd240:8"]]
- 00b88568 bytes 22530194
+ 00b885ac bytes 25530194
- 00b88584 ["INT_ADD", "register:40f0:8", ["const:b88584:8", "const:4:8"]]
- 00b88584 ["CALL", null, ["callee:00bdd210:8"]]
+ 00b885c8 ["INT_ADD", "register:40f0:8", ["const:b885c8:8", "const:4:8"]]
+ 00b885c8 ["CALL", null, ["callee:00bdd210:8"]]
- 00b88584 bytes 0f530194
+ 00b885c8 bytes 12530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a4e0a0b044e363413ae90175340218"></a>

### [`00b885b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md) → [`00b885f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md#insn-00b88614) · [`00b88624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md#insn-00b88624) · [`00b88640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md#insn-00b88640)
- 新版 [`00b88658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md#insn-00b88658) · [`00b88668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md#insn-00b88668) · [`00b88684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md#insn-00b88684)

~~~diff
- 00b88614 ["INT_ADD", "register:40f0:8", ["const:b88614:8", "const:4:8"]]
- 00b88614 ["CALL", null, ["callee:00b88f5c:8"]]
+ 00b88658 ["INT_ADD", "register:40f0:8", ["const:b88658:8", "const:4:8"]]
+ 00b88658 ["CALL", null, ["callee:00b88f5c:8"]]
- 00b88614 bytes 41020094
+ 00b88658 bytes 41020094
- 00b88624 ["INT_ADD", "register:40f0:8", ["const:b88624:8", "const:4:8"]]
- 00b88624 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b88668 ["INT_ADD", "register:40f0:8", ["const:b88668:8", "const:4:8"]]
+ 00b88668 ["CALL", null, ["callee:00bdd240:8"]]
- 00b88624 bytes f3520194
+ 00b88668 bytes f6520194
- 00b88640 ["INT_ADD", "register:40f0:8", ["const:b88640:8", "const:4:8"]]
- 00b88640 ["CALL", null, ["callee:00bdd210:8"]]
+ 00b88684 ["INT_ADD", "register:40f0:8", ["const:b88684:8", "const:4:8"]]
+ 00b88684 ["CALL", null, ["callee:00bdd210:8"]]
- 00b88640 bytes e0520194
+ 00b88684 bytes e3520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9b024cef7da26a45c849d63d479af8"></a>

### [`00b8866c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8866c.md) → [`00b886b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b886c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8866c.md#insn-00b886c4) · [`00b886d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8866c.md#insn-00b886d4) · [`00b886f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8866c.md#insn-00b886f0)
- 新版 [`00b88708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88708) · [`00b88718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88718) · [`00b88734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88734)

~~~diff
- 00b886c4 ["INT_ADD", "register:40f0:8", ["const:b886c4:8", "const:4:8"]]
- 00b886c4 ["CALL", null, ["callee:00b88f5c:8"]]
+ 00b88708 ["INT_ADD", "register:40f0:8", ["const:b88708:8", "const:4:8"]]
+ 00b88708 ["CALL", null, ["callee:00b88f5c:8"]]
- 00b886c4 bytes 15020094
+ 00b88708 bytes 15020094
- 00b886d4 ["INT_ADD", "register:40f0:8", ["const:b886d4:8", "const:4:8"]]
- 00b886d4 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b88718 ["INT_ADD", "register:40f0:8", ["const:b88718:8", "const:4:8"]]
+ 00b88718 ["CALL", null, ["callee:00bdd240:8"]]
- 00b886d4 bytes c7520194
+ 00b88718 bytes ca520194
- 00b886f0 ["INT_ADD", "register:40f0:8", ["const:b886f0:8", "const:4:8"]]
- 00b886f0 ["CALL", null, ["callee:00bdd210:8"]]
+ 00b88734 ["INT_ADD", "register:40f0:8", ["const:b88734:8", "const:4:8"]]
+ 00b88734 ["CALL", null, ["callee:00bdd210:8"]]
- 00b886f0 bytes b4520194
+ 00b88734 bytes b7520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5701cb988883400764b29957026f43"></a>

### [`00b8871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8871c.md) → [`00b88760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8871c.md#insn-00b88780) · [`00b88790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8871c.md#insn-00b88790) · [`00b887ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b8871c.md#insn-00b887ac)
- 新版 [`00b887c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887c4) · [`00b887d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887d4) · [`00b887f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md#insn-00b887f0)

~~~diff
- 00b88780 ["INT_ADD", "register:40f0:8", ["const:b88780:8", "const:4:8"]]
- 00b88780 ["CALL", null, ["callee:00b88f5c:8"]]
+ 00b887c4 ["INT_ADD", "register:40f0:8", ["const:b887c4:8", "const:4:8"]]
+ 00b887c4 ["CALL", null, ["callee:00b88f5c:8"]]
- 00b88780 bytes e6010094
+ 00b887c4 bytes e6010094
- 00b88790 ["INT_ADD", "register:40f0:8", ["const:b88790:8", "const:4:8"]]
- 00b88790 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b887d4 ["INT_ADD", "register:40f0:8", ["const:b887d4:8", "const:4:8"]]
+ 00b887d4 ["CALL", null, ["callee:00bdd240:8"]]
- 00b88790 bytes 98520194
+ 00b887d4 bytes 9b520194
- 00b887ac ["INT_ADD", "register:40f0:8", ["const:b887ac:8", "const:4:8"]]
- 00b887ac ["CALL", null, ["callee:00bdd210:8"]]
+ 00b887f0 ["INT_ADD", "register:40f0:8", ["const:b887f0:8", "const:4:8"]]
+ 00b887f0 ["CALL", null, ["callee:00bdd210:8"]]
- 00b887ac bytes 85520194
+ 00b887f0 bytes 88520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0f6fc363ecc9dcee12c12e824d24e8"></a>

### [`00b88b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88b64.md) → [`00b88ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE5closeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88b64.md#insn-00b88b8c) · [`00b88b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88b64.md#insn-00b88b98) · [`00b88bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88b64.md#insn-00b88bc0)
- 新版 [`00b88bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88bd0) · [`00b88bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88bdc) · [`00b88c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ba8.md#insn-00b88c04)

~~~diff
- 00b88b8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88b8c ["INT_ADD", "register:40f0:8", ["const:b88b8c:8", "const:4:8"]]
- 00b88b8c ["CALLIND", null, ["register:0:8"]]
+ 00b88bd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b88bd0 ["INT_ADD", "register:40f0:8", ["const:b88bd0:8", "const:4:8"]]
+ 00b88bd0 ["CALLIND", null, ["register:0:8"]]
- 00b88b8c bytes 00013fd6
+ 00b88bd0 bytes 00013fd6
- 00b88b98 ["INT_ADD", "register:40f0:8", ["const:b88b98:8", "const:4:8"]]
- 00b88b98 ["CALL", null, ["callee:00bdd1b0:8"]]
+ 00b88bdc ["INT_ADD", "register:40f0:8", ["const:b88bdc:8", "const:4:8"]]
+ 00b88bdc ["CALL", null, ["callee:00bdd1b0:8"]]
- 00b88b98 bytes 72510194
+ 00b88bdc bytes 75510194
- 00b88bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b88bc0 ["INT_ADD", "register:40f0:8", ["const:b88bc0:8", "const:4:8"]]
- 00b88bc0 ["CALLIND", null, ["register:0:8"]]
+ 00b88c04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b88c04 ["INT_ADD", "register:40f0:8", ["const:b88c04:8", "const:4:8"]]
+ 00b88c04 ["CALLIND", null, ["register:0:8"]]
- 00b88bc0 bytes 00013fd6
+ 00b88c04 bytes 00013fd6
~~~


<a id="compare-f06dce76002e793751c3a81c4202c221"></a>

### [`00b88bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88bf0.md) → [`00b88c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md) FUN_00b88c34

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdc080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88bf0.md#insn-00b88c04)
- 新版 [`00b88c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md#insn-00b88c48)

~~~diff
- 00b88c04 ["INT_ADD", "register:40f0:8", ["const:b88c04:8", "const:4:8"]]
- 00b88c04 ["CALL", null, ["callee:00bdc0d0:8"]]
+ 00b88c48 ["INT_ADD", "register:40f0:8", ["const:b88c48:8", "const:4:8"]]
+ 00b88c48 ["CALL", null, ["callee:00bdc0d0:8"]]
- 00b88c04 bytes 1f4d0194
+ 00b88c48 bytes 224d0194
~~~


<a id="compare-24963dca26e235f22aa85205301843de"></a>

### [`00b88c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88c1c.md) → [`00b88c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b88c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88c1c.md#insn-00b88c40) · [`00b88c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88c1c.md#insn-00b88c4c) · [`00b88c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88c1c.md#insn-00b88c58)
- 新版 [`00b88c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88c84) · [`00b88c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88c90) · [`00b88c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88c9c)

~~~diff
- 00b88c40 ["INT_ADD", "register:40f0:8", ["const:b88c40:8", "const:4:8"]]
- 00b88c40 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b88c84 ["INT_ADD", "register:40f0:8", ["const:b88c84:8", "const:4:8"]]
+ 00b88c84 ["CALL", null, ["callee:00bdd980:8"]]
- 00b88c40 bytes 3c530194
+ 00b88c84 bytes 3f530194
- 00b88c4c ["INT_ADD", "register:40f0:8", ["const:b88c4c:8", "const:4:8"]]
- 00b88c4c ["CALL", null, ["callee:00be12e0:8"]]
+ 00b88c90 ["INT_ADD", "register:40f0:8", ["const:b88c90:8", "const:4:8"]]
+ 00b88c90 ["CALL", null, ["callee:00be12e0:8"]]
- 00b88c4c bytes 91610194
+ 00b88c90 bytes 94610194
- 00b88c58 ["INT_ADD", "register:40f0:8", ["const:b88c58:8", "const:4:8"]]
- 00b88c58 ["CALL", null, ["callee:00be12e0:8"]]
+ 00b88c9c ["INT_ADD", "register:40f0:8", ["const:b88c9c:8", "const:4:8"]]
+ 00b88c9c ["CALL", null, ["callee:00be12e0:8"]]
- 00b88c58 bytes 8e610194
+ 00b88c9c bytes 91610194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae192803a2eb42243a2ce5a58084c924"></a>

### [`00b8995c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b8995c.md) → [`00b899a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899a0.md) FUN_00b899a0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b8995c.md#insn-00b89970)
- 新版 [`00b899b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899a0.md#insn-00b899b4)

~~~diff
- 00b89970 ["INT_ADD", "register:40f0:8", ["const:b89970:8", "const:4:8"]]
- 00b89970 ["CALL", null, ["callee:00bdb150:8"]]
+ 00b899b4 ["INT_ADD", "register:40f0:8", ["const:b899b4:8", "const:4:8"]]
+ 00b899b4 ["CALL", null, ["callee:00bdb150:8"]]
- 00b89970 bytes e4450194
+ 00b899b4 bytes e7450194
~~~


<a id="compare-623b0b3d0684bc5f87b5ffd86d99a773"></a>

### [`00b89a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a20.md) → [`00b89a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md) FUN_00b89a64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a20.md#insn-00b89a60) · [`00b89ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a20.md#insn-00b89ac0) · [`00b89b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a20.md#insn-00b89b0c)
- 新版 [`00b89aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md#insn-00b89aa4) · [`00b89b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md#insn-00b89b04) · [`00b89b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md#insn-00b89b50)

~~~diff
- 00b89a60 ["INT_ADD", "register:40f0:8", ["const:b89a60:8", "const:4:8"]]
- 00b89a60 ["CALL", null, ["callee:00be14a0:8"]]
+ 00b89aa4 ["INT_ADD", "register:40f0:8", ["const:b89aa4:8", "const:4:8"]]
+ 00b89aa4 ["CALL", null, ["callee:00be14a0:8"]]
- 00b89a60 bytes 7c5e0194
+ 00b89aa4 bytes 7f5e0194
- 00b89ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89ac0 ["INT_ADD", "register:40f0:8", ["const:b89ac0:8", "const:4:8"]]
- 00b89ac0 ["CALLIND", null, ["register:0:8"]]
+ 00b89b04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89b04 ["INT_ADD", "register:40f0:8", ["const:b89b04:8", "const:4:8"]]
+ 00b89b04 ["CALLIND", null, ["register:0:8"]]
- 00b89ac0 bytes 00013fd6
+ 00b89b04 bytes 00013fd6
- 00b89b0c ["INT_ADD", "register:40f0:8", ["const:b89b0c:8", "const:4:8"]]
- 00b89b0c ["CALL", null, ["callee:00be14a0:8"]]
+ 00b89b50 ["INT_ADD", "register:40f0:8", ["const:b89b50:8", "const:4:8"]]
+ 00b89b50 ["CALL", null, ["callee:00be14a0:8"]]
- 00b89b0c bytes 515e0194
+ 00b89b50 bytes 545e0194
~~~


<a id="compare-55d08e03b44d771e8de6291ccb0410bb"></a>

### [`00b89b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89b48.md) → [`00b89b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md) FUN_00b89b8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b89a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a08.md) [`00b89a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89a14.md) · 呼出先 2件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md) [`00be1460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1460.md)
- 新版 呼出元 2件 [`00b89a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a4c.md) [`00b89a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a58.md) · 呼出先 2件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89b48.md#insn-00b89b98) · [`00b89bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89b48.md#insn-00b89bcc) · [`00b89c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89b48.md#insn-00b89c18)
- 新版 [`00b89bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89bdc) · [`00b89c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89c10) · [`00b89c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89c5c)

~~~diff
- 00b89b98 ["INT_ADD", "register:40f0:8", ["const:b89b98:8", "const:4:8"]]
- 00b89b98 ["CALL", null, ["callee:00be14b0:8"]]
+ 00b89bdc ["INT_ADD", "register:40f0:8", ["const:b89bdc:8", "const:4:8"]]
+ 00b89bdc ["CALL", null, ["callee:00be14b0:8"]]
- 00b89b98 bytes 325e0194
+ 00b89bdc bytes 355e0194
- 00b89bcc ["INT_ADD", "register:40f0:8", ["const:b89bcc:8", "const:4:8"]]
- 00b89bcc ["CALL", null, ["callee:00be14b0:8"]]
+ 00b89c10 ["INT_ADD", "register:40f0:8", ["const:b89c10:8", "const:4:8"]]
+ 00b89c10 ["CALL", null, ["callee:00be14b0:8"]]
- 00b89bcc bytes 255e0194
+ 00b89c10 bytes 285e0194
- 00b89c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89c18 ["INT_ADD", "register:40f0:8", ["const:b89c18:8", "const:4:8"]]
- 00b89c18 ["CALLIND", null, ["register:0:8"]]
+ 00b89c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89c5c ["INT_ADD", "register:40f0:8", ["const:b89c5c:8", "const:4:8"]]
+ 00b89c5c ["CALLIND", null, ["register:0:8"]]
- 00b89c18 bytes 00013fd6
+ 00b89c5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e0d82a89a1f83bfbddcdde4dbfabe79"></a>

### [`00b89cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89cf0.md) → [`00b89d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d34.md) FUN_00b89d34

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89cf0.md#insn-00b89d04)
- 新版 [`00b89d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d34.md#insn-00b89d48)

~~~diff
- 00b89d04 ["INT_ADD", "register:40f0:8", ["const:b89d04:8", "const:4:8"]]
- 00b89d04 ["CALL", null, ["callee:00bdb150:8"]]
+ 00b89d48 ["INT_ADD", "register:40f0:8", ["const:b89d48:8", "const:4:8"]]
+ 00b89d48 ["CALL", null, ["callee:00bdb150:8"]]
- 00b89d04 bytes ff440194
+ 00b89d48 bytes 02450194
~~~


<a id="compare-f2e3b5671e646987351dbae2b556d425"></a>

### [`00b89d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d78.md) → [`00b89dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md) FUN_00b89dbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d78.md#insn-00b89db0) · [`00b89dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d78.md#insn-00b89dd0) · [`00b89df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89d78.md#insn-00b89df8)
- 新版 [`00b89df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89df4) · [`00b89e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89e14) · [`00b89e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89dbc.md#insn-00b89e3c)

~~~diff
- 00b89db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89db0 ["INT_ADD", "register:40f0:8", ["const:b89db0:8", "const:4:8"]]
- 00b89db0 ["CALLIND", null, ["register:0:8"]]
+ 00b89df4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89df4 ["INT_ADD", "register:40f0:8", ["const:b89df4:8", "const:4:8"]]
+ 00b89df4 ["CALLIND", null, ["register:0:8"]]
- 00b89db0 bytes 00013fd6
+ 00b89df4 bytes 00013fd6
- 00b89dd0 ["INT_ADD", "register:40f0:8", ["const:b89dd0:8", "const:4:8"]]
- 00b89dd0 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b89e14 ["INT_ADD", "register:40f0:8", ["const:b89e14:8", "const:4:8"]]
+ 00b89e14 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b89dd0 bytes 6c4d0194
+ 00b89e14 bytes 6f4d0194
- 00b89df8 ["INT_ADD", "register:40f0:8", ["const:b89df8:8", "const:4:8"]]
- 00b89df8 ["CALL", null, ["callee:00bdd360:8"]]
+ 00b89e3c ["INT_ADD", "register:40f0:8", ["const:b89e3c:8", "const:4:8"]]
+ 00b89e3c ["CALL", null, ["callee:00bdd360:8"]]
- 00b89df8 bytes 464d0194
+ 00b89e3c bytes 494d0194
~~~


<a id="compare-61851eeda583992ac0e43644e3223b57"></a>

### [`00b89e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89e1c.md) → [`00b89e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89e60.md) FUN_00b89e60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89e1c.md#insn-00b89e84)
- 新版 [`00b89ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89e60.md#insn-00b89ec8)

~~~diff
- 00b89e84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89e84 ["INT_ADD", "register:40f0:8", ["const:b89e84:8", "const:4:8"]]
- 00b89e84 ["CALLIND", null, ["register:0:8"]]
+ 00b89ec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89ec8 ["INT_ADD", "register:40f0:8", ["const:b89ec8:8", "const:4:8"]]
+ 00b89ec8 ["CALLIND", null, ["register:0:8"]]
- 00b89e84 bytes 00013fd6
+ 00b89ec8 bytes 00013fd6
~~~


<a id="compare-03dbc549423559c7987ba84e8ec0ac4c"></a>

### [`00b89ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ec0.md) → [`00b89f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md) FUN_00b89f04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b89f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ec0.md#insn-00b89f0c) · [`00b89f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ec0.md#insn-00b89f58) · [`00b89f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ec0.md#insn-00b89f94)
- 新版 [`00b89f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89f50) · [`00b89f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89f9c) · [`00b89fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89f04.md#insn-00b89fd8)

~~~diff
- 00b89f0c ["INT_ADD", "register:40f0:8", ["const:b89f0c:8", "const:4:8"]]
- 00b89f0c ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b89f50 ["INT_ADD", "register:40f0:8", ["const:b89f50:8", "const:4:8"]]
+ 00b89f50 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b89f0c bytes 1d4d0194
+ 00b89f50 bytes 204d0194
- 00b89f58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89f58 ["INT_ADD", "register:40f0:8", ["const:b89f58:8", "const:4:8"]]
- 00b89f58 ["CALLIND", null, ["register:0:8"]]
+ 00b89f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b89f9c ["INT_ADD", "register:40f0:8", ["const:b89f9c:8", "const:4:8"]]
+ 00b89f9c ["CALLIND", null, ["register:0:8"]]
- 00b89f58 bytes 00013fd6
+ 00b89f9c bytes 00013fd6
- 00b89f94 ["INT_ADD", "register:40f0:8", ["const:b89f94:8", "const:4:8"]]
- 00b89f94 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b89fd8 ["INT_ADD", "register:40f0:8", ["const:b89fd8:8", "const:4:8"]]
+ 00b89fd8 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b89f94 bytes fb4c0194
+ 00b89fd8 bytes fe4c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f52919aa09dbbef24f4743a8d4f5d9ba"></a>

### [`00b89ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ff0.md) → [`00b8a034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a034.md) FUN_00b8a034

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b89ff0.md#insn-00b8a004)
- 新版 [`00b8a048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a034.md#insn-00b8a048)

~~~diff
- 00b8a004 ["INT_ADD", "register:40f0:8", ["const:b8a004:8", "const:4:8"]]
- 00b8a004 ["CALL", null, ["callee:00be13c0:8"]]
+ 00b8a048 ["INT_ADD", "register:40f0:8", ["const:b8a048:8", "const:4:8"]]
+ 00b8a048 ["CALL", null, ["callee:00be13c0:8"]]
- 00b8a004 bytes db5c0194
+ 00b8a048 bytes de5c0194
~~~


<a id="compare-9522f3620239fef59b3e9b1b563f59a8"></a>

### [`00b8a0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0b4.md) → [`00b8a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md) FUN_00b8a0f8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md) [`00be1470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0b4.md#insn-00b8a0f4) · [`00b8a154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0b4.md#insn-00b8a154) · [`00b8a1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0b4.md#insn-00b8a1a0)
- 新版 [`00b8a138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a138) · [`00b8a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a198) · [`00b8a1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0f8.md#insn-00b8a1e4)

~~~diff
- 00b8a0f4 ["INT_ADD", "register:40f0:8", ["const:b8a0f4:8", "const:4:8"]]
- 00b8a0f4 ["CALL", null, ["callee:00be14c0:8"]]
+ 00b8a138 ["INT_ADD", "register:40f0:8", ["const:b8a138:8", "const:4:8"]]
+ 00b8a138 ["CALL", null, ["callee:00be14c0:8"]]
- 00b8a0f4 bytes df5c0194
+ 00b8a138 bytes e25c0194
- 00b8a154 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a154 ["INT_ADD", "register:40f0:8", ["const:b8a154:8", "const:4:8"]]
- 00b8a154 ["CALLIND", null, ["register:0:8"]]
+ 00b8a198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a198 ["INT_ADD", "register:40f0:8", ["const:b8a198:8", "const:4:8"]]
+ 00b8a198 ["CALLIND", null, ["register:0:8"]]
- 00b8a154 bytes 00013fd6
+ 00b8a198 bytes 00013fd6
- 00b8a1a0 ["INT_ADD", "register:40f0:8", ["const:b8a1a0:8", "const:4:8"]]
- 00b8a1a0 ["CALL", null, ["callee:00be14a0:8"]]
+ 00b8a1e4 ["INT_ADD", "register:40f0:8", ["const:b8a1e4:8", "const:4:8"]]
+ 00b8a1e4 ["CALL", null, ["callee:00be14a0:8"]]
- 00b8a1a0 bytes ac5c0194
+ 00b8a1e4 bytes af5c0194
~~~


<a id="compare-886668595e6b7345b9e93333a683f96e"></a>

### [`00b8a1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a1dc.md) → [`00b8a220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md) FUN_00b8a220

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b8a09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a09c.md) [`00b8a0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0a8.md) · 呼出先 4件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md) [`00be1460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1460.md) [`00be1470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1470.md) [`00be1480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1480.md)
- 新版 呼出元 2件 [`00b8a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0e0.md) [`00b8a0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0ec.md) · 呼出先 4件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14b0.md) [`00be14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14c0.md) [`00be14d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a1dc.md#insn-00b8a22c) · [`00b8a25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a1dc.md#insn-00b8a25c) · [`00b8a2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a1dc.md#insn-00b8a2a8)
- 新版 [`00b8a270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md#insn-00b8a270) · [`00b8a2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md#insn-00b8a2a0) · [`00b8a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md#insn-00b8a2ec)

~~~diff
- 00b8a22c ["INT_ADD", "register:40f0:8", ["const:b8a22c:8", "const:4:8"]]
- 00b8a22c ["CALL", null, ["callee:00be14d0:8"]]
+ 00b8a270 ["INT_ADD", "register:40f0:8", ["const:b8a270:8", "const:4:8"]]
+ 00b8a270 ["CALL", null, ["callee:00be14d0:8"]]
- 00b8a22c bytes 955c0194
+ 00b8a270 bytes 985c0194
- 00b8a25c ["INT_ADD", "register:40f0:8", ["const:b8a25c:8", "const:4:8"]]
- 00b8a25c ["CALL", null, ["callee:00be14b0:8"]]
+ 00b8a2a0 ["INT_ADD", "register:40f0:8", ["const:b8a2a0:8", "const:4:8"]]
+ 00b8a2a0 ["CALL", null, ["callee:00be14b0:8"]]
- 00b8a25c bytes 815c0194
+ 00b8a2a0 bytes 845c0194
- 00b8a2a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a2a8 ["INT_ADD", "register:40f0:8", ["const:b8a2a8:8", "const:4:8"]]
- 00b8a2a8 ["CALLIND", null, ["register:0:8"]]
+ 00b8a2ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a2ec ["INT_ADD", "register:40f0:8", ["const:b8a2ec:8", "const:4:8"]]
+ 00b8a2ec ["CALLIND", null, ["register:0:8"]]
- 00b8a2a8 bytes 00013fd6
+ 00b8a2ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bea5634e09a959f2d388896e5286b32"></a>

### [`00b8a37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a37c.md) → [`00b8a3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3c0.md) FUN_00b8a3c0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a37c.md#insn-00b8a390)
- 新版 [`00b8a3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3c0.md#insn-00b8a3d4)

~~~diff
- 00b8a390 ["INT_ADD", "register:40f0:8", ["const:b8a390:8", "const:4:8"]]
- 00b8a390 ["CALL", null, ["callee:00be13c0:8"]]
+ 00b8a3d4 ["INT_ADD", "register:40f0:8", ["const:b8a3d4:8", "const:4:8"]]
+ 00b8a3d4 ["CALL", null, ["callee:00be13c0:8"]]
- 00b8a390 bytes f85b0194
+ 00b8a3d4 bytes fb5b0194
~~~


<a id="compare-a9794bc91b8cb45083a12354cf4d890c"></a>

### [`00b8a404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a404.md) → [`00b8a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md) FUN_00b8a448

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a404.md#insn-00b8a43c) · [`00b8a45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a404.md#insn-00b8a45c) · [`00b8a484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a404.md#insn-00b8a484)
- 新版 [`00b8a480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a480) · [`00b8a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a4a0) · [`00b8a4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a448.md#insn-00b8a4c8)

~~~diff
- 00b8a43c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a43c ["INT_ADD", "register:40f0:8", ["const:b8a43c:8", "const:4:8"]]
- 00b8a43c ["CALLIND", null, ["register:0:8"]]
+ 00b8a480 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a480 ["INT_ADD", "register:40f0:8", ["const:b8a480:8", "const:4:8"]]
+ 00b8a480 ["CALLIND", null, ["register:0:8"]]
- 00b8a43c bytes 00013fd6
+ 00b8a480 bytes 00013fd6
- 00b8a45c ["INT_ADD", "register:40f0:8", ["const:b8a45c:8", "const:4:8"]]
- 00b8a45c ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b8a4a0 ["INT_ADD", "register:40f0:8", ["const:b8a4a0:8", "const:4:8"]]
+ 00b8a4a0 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b8a45c bytes c94b0194
+ 00b8a4a0 bytes cc4b0194
- 00b8a484 ["INT_ADD", "register:40f0:8", ["const:b8a484:8", "const:4:8"]]
- 00b8a484 ["CALL", null, ["callee:00bdd360:8"]]
+ 00b8a4c8 ["INT_ADD", "register:40f0:8", ["const:b8a4c8:8", "const:4:8"]]
+ 00b8a4c8 ["CALL", null, ["callee:00bdd360:8"]]
- 00b8a484 bytes a34b0194
+ 00b8a4c8 bytes a64b0194
~~~


<a id="compare-019f151ba5677847ac01e90be2b9f264"></a>

### [`00b8a4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a4a8.md) → [`00b8a4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a4ec.md) FUN_00b8a4ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a4a8.md#insn-00b8a510)
- 新版 [`00b8a554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a4ec.md#insn-00b8a554)

~~~diff
- 00b8a510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a510 ["INT_ADD", "register:40f0:8", ["const:b8a510:8", "const:4:8"]]
- 00b8a510 ["CALLIND", null, ["register:0:8"]]
+ 00b8a554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a554 ["INT_ADD", "register:40f0:8", ["const:b8a554:8", "const:4:8"]]
+ 00b8a554 ["CALLIND", null, ["register:0:8"]]
- 00b8a510 bytes 00013fd6
+ 00b8a554 bytes 00013fd6
~~~


<a id="compare-75c78fe954f7fb871b90c0af196fc4e3"></a>

### [`00b8a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a54c.md) → [`00b8a590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md) FUN_00b8a590

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md) [`00be1490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md) [`00be14e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a54c.md#insn-00b8a58c) · [`00b8a5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a54c.md#insn-00b8a5d8) · [`00b8a614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a54c.md#insn-00b8a614)
- 新版 [`00b8a5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a5d0) · [`00b8a61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a61c) · [`00b8a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a590.md#insn-00b8a658)

~~~diff
- 00b8a58c ["INT_ADD", "register:40f0:8", ["const:b8a58c:8", "const:4:8"]]
- 00b8a58c ["CALL", null, ["callee:00be14e0:8"]]
+ 00b8a5d0 ["INT_ADD", "register:40f0:8", ["const:b8a5d0:8", "const:4:8"]]
+ 00b8a5d0 ["CALL", null, ["callee:00be14e0:8"]]
- 00b8a58c bytes c15b0194
+ 00b8a5d0 bytes c45b0194
- 00b8a5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a5d8 ["INT_ADD", "register:40f0:8", ["const:b8a5d8:8", "const:4:8"]]
- 00b8a5d8 ["CALLIND", null, ["register:0:8"]]
+ 00b8a61c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a61c ["INT_ADD", "register:40f0:8", ["const:b8a61c:8", "const:4:8"]]
+ 00b8a61c ["CALLIND", null, ["register:0:8"]]
- 00b8a5d8 bytes 00013fd6
+ 00b8a61c bytes 00013fd6
- 00b8a614 ["INT_ADD", "register:40f0:8", ["const:b8a614:8", "const:4:8"]]
- 00b8a614 ["CALL", null, ["callee:00bdd3d0:8"]]
+ 00b8a658 ["INT_ADD", "register:40f0:8", ["const:b8a658:8", "const:4:8"]]
+ 00b8a658 ["CALL", null, ["callee:00bdd3d0:8"]]
- 00b8a614 bytes 5b4b0194
+ 00b8a658 bytes 5e4b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-494797bf0a5690782bff332dd50cb9aa"></a>

### [`00b8a6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a6bc.md) → [`00b8a700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a700.md) _ZNSt6__ndk17collateIcED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a6bc.md#insn-00b8a6d0)
- 新版 [`00b8a714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a700.md#insn-00b8a714)

~~~diff
- 00b8a6d0 ["INT_ADD", "register:40f0:8", ["const:b8a6d0:8", "const:4:8"]]
- 00b8a6d0 ["CALL", null, ["callee:00be1500:8"]]
+ 00b8a714 ["INT_ADD", "register:40f0:8", ["const:b8a714:8", "const:4:8"]]
+ 00b8a714 ["CALL", null, ["callee:00be1500:8"]]
- 00b8a6d0 bytes 785b0194
+ 00b8a714 bytes 7b5b0194
~~~


<a id="compare-514099ab3c53825bd761baa8ca8b03c0"></a>

### [`00b8a74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a74c.md) → [`00b8a790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md) _ZNKSt6__ndk17collateIcE12do_transformEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a74c.md#insn-00b8a7b4) · [`00b8a7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a74c.md#insn-00b8a7dc) · [`00b8a804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a74c.md#insn-00b8a804)
- 新版 [`00b8a7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a7f8) · [`00b8a820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a820) · [`00b8a848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a790.md#insn-00b8a848)

~~~diff
- 00b8a7b4 ["INT_ADD", "register:40f0:8", ["const:b8a7b4:8", "const:4:8"]]
- 00b8a7b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b8a7f8 ["INT_ADD", "register:40f0:8", ["const:b8a7f8:8", "const:4:8"]]
+ 00b8a7f8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b8a7b4 bytes 0f420194
+ 00b8a7f8 bytes 12420194
- 00b8a7dc ["INT_ADD", "register:40f0:8", ["const:b8a7dc:8", "const:4:8"]]
- 00b8a7dc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b8a820 ["INT_ADD", "register:40f0:8", ["const:b8a820:8", "const:4:8"]]
+ 00b8a820 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b8a7dc bytes 61420194
+ 00b8a820 bytes 64420194
- 00b8a804 ["INT_ADD", "register:40f0:8", ["const:b8a804:8", "const:4:8"]]
- 00b8a804 ["CALL", null, ["callee:00418c24:8"]]
+ 00b8a848 ["INT_ADD", "register:40f0:8", ["const:b8a848:8", "const:4:8"]]
+ 00b8a848 ["CALL", null, ["callee:00418c24:8"]]
- 00b8a804 bytes 0839e297
+ 00b8a848 bytes f738e297
~~~


<a id="compare-cd0c05f8d9a1886ef970c105d1055773"></a>

### [`00b8a848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a848.md) → [`00b8a88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a88c.md) _ZNSt6__ndk17collateIwED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be14c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a848.md#insn-00b8a85c)
- 新版 [`00b8a8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a88c.md#insn-00b8a8a0)

~~~diff
- 00b8a85c ["INT_ADD", "register:40f0:8", ["const:b8a85c:8", "const:4:8"]]
- 00b8a85c ["CALL", null, ["callee:00be1510:8"]]
+ 00b8a8a0 ["INT_ADD", "register:40f0:8", ["const:b8a8a0:8", "const:4:8"]]
+ 00b8a8a0 ["CALL", null, ["callee:00be1510:8"]]
- 00b8a85c bytes 195b0194
+ 00b8a8a0 bytes 1c5b0194
~~~


<a id="compare-b5f0d031064cf3700ce74b3ad424d3fc"></a>

### [`00b8a8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a8cc.md) → [`00b8a910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md) _ZNKSt6__ndk17collateIwE12do_transformEPKwS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a8cc.md#insn-00b8a940) · [`00b8a974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a8cc.md#insn-00b8a974) · [`00b8a99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a8cc.md#insn-00b8a99c)
- 新版 [`00b8a984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a984) · [`00b8a9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a9b8) · [`00b8a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a9e0)

~~~diff
- 00b8a940 ["INT_ADD", "register:40f0:8", ["const:b8a940:8", "const:4:8"]]
- 00b8a940 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b8a984 ["INT_ADD", "register:40f0:8", ["const:b8a984:8", "const:4:8"]]
+ 00b8a984 ["CALL", null, ["callee:00bdb040:8"]]
- 00b8a940 bytes ac410194
+ 00b8a984 bytes af410194
- 00b8a974 ["INT_ADD", "register:40f0:8", ["const:b8a974:8", "const:4:8"]]
- 00b8a974 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b8a9b8 ["INT_ADD", "register:40f0:8", ["const:b8a9b8:8", "const:4:8"]]
+ 00b8a9b8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b8a974 bytes fb410194
+ 00b8a9b8 bytes fe410194
- 00b8a99c ["INT_ADD", "register:40f0:8", ["const:b8a99c:8", "const:4:8"]]
- 00b8a99c ["CALL", null, ["callee:006ad8a4:8"]]
+ 00b8a9e0 ["INT_ADD", "register:40f0:8", ["const:b8a9e0:8", "const:4:8"]]
+ 00b8a9e0 ["CALL", null, ["callee:006ad8a4:8"]]
- 00b8a99c bytes c28bec97
+ 00b8a9e0 bytes b18bec97
~~~


<a id="compare-c34040ec42537ac5170c540339794f60"></a>

### [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) → [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) FUN_00b8aca8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) [`00b965c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md) [`00b9671c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md) [`00b967d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md) [`00b96928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md) · 呼出先 3件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md)
- 新版 呼出元 7件 [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) [`00b96608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md) [`00b96760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md) [`00b9681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md) [`00b9696c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8acc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md#insn-00b8acc4) · [`00b8acd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md#insn-00b8acd0) · [`00b8ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md#insn-00b8ad74)
- 新版 [`00b8ad08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8ad08) · [`00b8ad14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8ad14) · [`00b8adb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8adb8)

~~~diff
- 00b8acc4 ["INT_ADD", "register:40f0:8", ["const:b8acc4:8", "const:4:8"]]
- 00b8acc4 ["CALL", null, ["callee:00bdd1d0:8"]]
+ 00b8ad08 ["INT_ADD", "register:40f0:8", ["const:b8ad08:8", "const:4:8"]]
+ 00b8ad08 ["CALL", null, ["callee:00bdd1d0:8"]]
- 00b8acc4 bytes 2f490194
+ 00b8ad08 bytes 32490194
- 00b8acd0 ["INT_ADD", "register:40f0:8", ["const:b8acd0:8", "const:4:8"]]
- 00b8acd0 ["CALL", null, ["callee:00be0f80:8"]]
+ 00b8ad14 ["INT_ADD", "register:40f0:8", ["const:b8ad14:8", "const:4:8"]]
+ 00b8ad14 ["CALL", null, ["callee:00be0f80:8"]]
- 00b8acd0 bytes 98580194
+ 00b8ad14 bytes 9b580194
- 00b8ad74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8ad74 ["INT_ADD", "register:40f0:8", ["const:b8ad74:8", "const:4:8"]]
- 00b8ad74 ["CALLIND", null, ["register:0:8"]]
+ 00b8adb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8adb8 ["INT_ADD", "register:40f0:8", ["const:b8adb8:8", "const:4:8"]]
+ 00b8adb8 ["CALLIND", null, ["register:0:8"]]
- 00b8ad74 bytes 00013fd6
+ 00b8adb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e545308ab3ccd4de4cdde5ef89292d25"></a>

### [`00b8b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md) → [`00b8b11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md) FUN_00b8b11c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8b0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d0.md) · 呼出先 6件 [`00bb92b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)
- 新版 呼出元 1件 [`00b8b114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b114.md) · 呼出先 6件 [`00bb92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md#insn-00b8b160) · [`00b8b17c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md#insn-00b8b17c) · [`00b8b200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md#insn-00b8b200)
- 新版 [`00b8b1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b1a4) · [`00b8b1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b1c0) · [`00b8b244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b244)

~~~diff
- 00b8b160 ["INT_ADD", "register:40f0:8", ["const:b8b160:8", "const:4:8"]]
- 00b8b160 ["CALL", null, ["callee:00be1520:8"]]
+ 00b8b1a4 ["INT_ADD", "register:40f0:8", ["const:b8b1a4:8", "const:4:8"]]
+ 00b8b1a4 ["CALL", null, ["callee:00be1520:8"]]
- 00b8b160 bytes dc580194
+ 00b8b1a4 bytes df580194
- 00b8b17c ["INT_ADD", "register:40f0:8", ["const:b8b17c:8", "const:4:8"]]
- 00b8b17c ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b8b1c0 ["INT_ADD", "register:40f0:8", ["const:b8b1c0:8", "const:4:8"]]
+ 00b8b1c0 ["CALL", null, ["callee:00bdefc0:8"]]
- 00b8b17c bytes 7d4f0194
+ 00b8b1c0 bytes 804f0194
- 00b8b200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8b200 ["INT_ADD", "register:40f0:8", ["const:b8b200:8", "const:4:8"]]
- 00b8b200 ["CALLIND", null, ["register:0:8"]]
+ 00b8b244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8b244 ["INT_ADD", "register:40f0:8", ["const:b8b244:8", "const:4:8"]]
+ 00b8b244 ["CALLIND", null, ["register:0:8"]]
- 00b8b200 bytes 00013fd6
+ 00b8b244 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

