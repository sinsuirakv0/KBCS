# v15.7.3 → v15.7.4 · 要調査の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-b64f884be1f919ecf18ec8016ba57a6c"></a>

### [`00ac9aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md) → [`00ac9b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9b30.md) FUN_00ac9b30

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00729118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729118.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00729118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729118.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9b64) · [`00ac9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9b88) · [`00ac9bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9bb4)
- 新版 `00ac9ba8`（命令位置の公開資料なし） · `00ac9bcc`（命令位置の公開資料なし） · `00ac9bf8`（命令位置の公開資料なし）

~~~diff
- 00ac9b64 ["INT_ADD", "register:40f0:8", ["const:ac9b64:8", "const:4:8"]]
- 00ac9b64 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ac9ba8 ["INT_ADD", "register:40f0:8", ["const:ac9ba8:8", "const:4:8"]]
+ 00ac9ba8 ["CALL", null, ["callee:00bdb040:8"]]
- 00ac9b64 bytes 23450494
+ 00ac9ba8 bytes 26450494
- 00ac9b88 ["INT_ADD", "register:40f0:8", ["const:ac9b88:8", "const:4:8"]]
- 00ac9b88 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9bcc ["INT_ADD", "register:40f0:8", ["const:ac9bcc:8", "const:4:8"]]
+ 00ac9bcc ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9b88 bytes 9a450494
+ 00ac9bcc bytes 9d450494
- 00ac9bb4 ["INT_ADD", "register:40f0:8", ["const:ac9bb4:8", "const:4:8"]]
- 00ac9bb4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9bf8 ["INT_ADD", "register:40f0:8", ["const:ac9bf8:8", "const:4:8"]]
+ 00ac9bf8 ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9bb4 bytes 8f450494
+ 00ac9bf8 bytes 92450494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d41623a6497868d44aa274bfc3d8db"></a>

### [`00ac9c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md) → [`00ac9c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9c5c.md) FUN_00ac9c5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00ac9dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9dc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00ac9e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e0c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9ccc) · [`00ac9d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9d14) · [`00ac9d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9d68)
- 新版 `00ac9d10`（命令位置の公開資料なし） · `00ac9d58`（命令位置の公開資料なし） · `00ac9dac`（命令位置の公開資料なし）

~~~diff
- 00ac9ccc ["INT_ADD", "register:40f0:8", ["const:ac9ccc:8", "const:4:8"]]
- 00ac9ccc ["CALL", null, ["callee:00bdb040:8"]]
+ 00ac9d10 ["INT_ADD", "register:40f0:8", ["const:ac9d10:8", "const:4:8"]]
+ 00ac9d10 ["CALL", null, ["callee:00bdb040:8"]]
- 00ac9ccc bytes c9440494
+ 00ac9d10 bytes cc440494
- 00ac9d14 ["INT_ADD", "register:40f0:8", ["const:ac9d14:8", "const:4:8"]]
- 00ac9d14 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9d58 ["INT_ADD", "register:40f0:8", ["const:ac9d58:8", "const:4:8"]]
+ 00ac9d58 ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9d14 bytes 37450494
+ 00ac9d58 bytes 3a450494
- 00ac9d68 ["INT_ADD", "register:40f0:8", ["const:ac9d68:8", "const:4:8"]]
- 00ac9d68 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9dac ["INT_ADD", "register:40f0:8", ["const:ac9dac:8", "const:4:8"]]
+ 00ac9dac ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9d68 bytes 22450494
+ 00ac9dac bytes 25450494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ade99bf36843d3c66aeb22dd21ba099c"></a>

### [`00ac9ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md) → [`00ac9e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e20.md) FUN_00ac9e20

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00ac9f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00ac9fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9fb4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9e84) · [`00ac9ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9ec4) · [`00ac9f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9f08)
- 新版 `00ac9ec8`（命令位置の公開資料なし） · `00ac9f08`（命令位置の公開資料なし） · `00ac9f4c`（命令位置の公開資料なし）

~~~diff
- 00ac9e84 ["INT_ADD", "register:40f0:8", ["const:ac9e84:8", "const:4:8"]]
- 00ac9e84 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ac9ec8 ["INT_ADD", "register:40f0:8", ["const:ac9ec8:8", "const:4:8"]]
+ 00ac9ec8 ["CALL", null, ["callee:00bdb040:8"]]
- 00ac9e84 bytes 5b440494
+ 00ac9ec8 bytes 5e440494
- 00ac9ec4 ["INT_ADD", "register:40f0:8", ["const:ac9ec4:8", "const:4:8"]]
- 00ac9ec4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9f08 ["INT_ADD", "register:40f0:8", ["const:ac9f08:8", "const:4:8"]]
+ 00ac9f08 ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9ec4 bytes cb440494
+ 00ac9f08 bytes ce440494
- 00ac9f08 ["INT_ADD", "register:40f0:8", ["const:ac9f08:8", "const:4:8"]]
- 00ac9f08 ["CALL", null, ["callee:00bdb240:8"]]
+ 00ac9f4c ["INT_ADD", "register:40f0:8", ["const:ac9f4c:8", "const:4:8"]]
+ 00ac9f4c ["CALL", null, ["callee:00bdb240:8"]]
- 00ac9f08 bytes ba440494
+ 00ac9f4c bytes bd440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52598ac1490065c347266c9e5869a933"></a>

### [`00ac9f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md) → [`00ac9fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9fc8.md) FUN_00ac9fc8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca114.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca158.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca028) · [`00aca068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca068) · [`00aca0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca0b4)
- 新版 `00aca06c`（命令位置の公開資料なし） · `00aca0ac`（命令位置の公開資料なし） · `00aca0f8`（命令位置の公開資料なし）

~~~diff
- 00aca028 ["INT_ADD", "register:40f0:8", ["const:aca028:8", "const:4:8"]]
- 00aca028 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca06c ["INT_ADD", "register:40f0:8", ["const:aca06c:8", "const:4:8"]]
+ 00aca06c ["CALL", null, ["callee:00bdb040:8"]]
- 00aca028 bytes f2430494
+ 00aca06c bytes f5430494
- 00aca068 ["INT_ADD", "register:40f0:8", ["const:aca068:8", "const:4:8"]]
- 00aca068 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca0ac ["INT_ADD", "register:40f0:8", ["const:aca0ac:8", "const:4:8"]]
+ 00aca0ac ["CALL", null, ["callee:00bdb240:8"]]
- 00aca068 bytes 62440494
+ 00aca0ac bytes 65440494
- 00aca0b4 ["INT_ADD", "register:40f0:8", ["const:aca0b4:8", "const:4:8"]]
- 00aca0b4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca0f8 ["INT_ADD", "register:40f0:8", ["const:aca0f8:8", "const:4:8"]]
+ 00aca0f8 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca0b4 bytes 4f440494
+ 00aca0f8 bytes 52440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef539b6816b9ff0f49c927667c8451c"></a>

### [`00aca128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md) → [`00aca16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca16c.md) FUN_00aca16c

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca254.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca298.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1a0) · [`00aca1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1c4) · [`00aca1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1f0)
- 新版 `00aca1e4`（命令位置の公開資料なし） · `00aca208`（命令位置の公開資料なし） · `00aca234`（命令位置の公開資料なし）

~~~diff
- 00aca1a0 ["INT_ADD", "register:40f0:8", ["const:aca1a0:8", "const:4:8"]]
- 00aca1a0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca1e4 ["INT_ADD", "register:40f0:8", ["const:aca1e4:8", "const:4:8"]]
+ 00aca1e4 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca1a0 bytes 94430494
+ 00aca1e4 bytes 97430494
- 00aca1c4 ["INT_ADD", "register:40f0:8", ["const:aca1c4:8", "const:4:8"]]
- 00aca1c4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca208 ["INT_ADD", "register:40f0:8", ["const:aca208:8", "const:4:8"]]
+ 00aca208 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca1c4 bytes 0b440494
+ 00aca208 bytes 0e440494
- 00aca1f0 ["INT_ADD", "register:40f0:8", ["const:aca1f0:8", "const:4:8"]]
- 00aca1f0 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca234 ["INT_ADD", "register:40f0:8", ["const:aca234:8", "const:4:8"]]
+ 00aca234 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca1f0 bytes 00440494
+ 00aca234 bytes 03440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-241a7068feed00d264b2287025858412"></a>

### [`00aca268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md) → [`00aca2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca2ac.md) FUN_00aca2ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca3fc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca440.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca310) · [`00aca350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca350) · [`00aca394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca394)
- 新版 `00aca354`（命令位置の公開資料なし） · `00aca394`（命令位置の公開資料なし） · `00aca3d8`（命令位置の公開資料なし）

~~~diff
- 00aca310 ["INT_ADD", "register:40f0:8", ["const:aca310:8", "const:4:8"]]
- 00aca310 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca354 ["INT_ADD", "register:40f0:8", ["const:aca354:8", "const:4:8"]]
+ 00aca354 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca310 bytes 38430494
+ 00aca354 bytes 3b430494
- 00aca350 ["INT_ADD", "register:40f0:8", ["const:aca350:8", "const:4:8"]]
- 00aca350 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca394 ["INT_ADD", "register:40f0:8", ["const:aca394:8", "const:4:8"]]
+ 00aca394 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca350 bytes a8430494
+ 00aca394 bytes ab430494
- 00aca394 ["INT_ADD", "register:40f0:8", ["const:aca394:8", "const:4:8"]]
- 00aca394 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca3d8 ["INT_ADD", "register:40f0:8", ["const:aca3d8:8", "const:4:8"]]
+ 00aca3d8 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca394 bytes 97430494
+ 00aca3d8 bytes 9a430494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70466fde5f349a60306a7417285ce591"></a>

### [`00aca410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md) → [`00aca454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca454.md) FUN_00aca454

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca5e4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca4b4) · [`00aca4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca4f4) · [`00aca540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca540)
- 新版 `00aca4f8`（命令位置の公開資料なし） · `00aca538`（命令位置の公開資料なし） · `00aca584`（命令位置の公開資料なし）

~~~diff
- 00aca4b4 ["INT_ADD", "register:40f0:8", ["const:aca4b4:8", "const:4:8"]]
- 00aca4b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca4f8 ["INT_ADD", "register:40f0:8", ["const:aca4f8:8", "const:4:8"]]
+ 00aca4f8 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca4b4 bytes cf420494
+ 00aca4f8 bytes d2420494
- 00aca4f4 ["INT_ADD", "register:40f0:8", ["const:aca4f4:8", "const:4:8"]]
- 00aca4f4 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca538 ["INT_ADD", "register:40f0:8", ["const:aca538:8", "const:4:8"]]
+ 00aca538 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca4f4 bytes 3f430494
+ 00aca538 bytes 42430494
- 00aca540 ["INT_ADD", "register:40f0:8", ["const:aca540:8", "const:4:8"]]
- 00aca540 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca584 ["INT_ADD", "register:40f0:8", ["const:aca584:8", "const:4:8"]]
+ 00aca584 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca540 bytes 2c430494
+ 00aca584 bytes 2f430494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333da8101c3b032156bc7ee6203a33d4"></a>

### [`00aca5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md) → [`00aca60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca60c.md) FUN_00aca60c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca6f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00aca738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca738.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca640) · [`00aca664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca664) · [`00aca690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca690)
- 新版 `00aca684`（命令位置の公開資料なし） · `00aca6a8`（命令位置の公開資料なし） · `00aca6d4`（命令位置の公開資料なし）

~~~diff
- 00aca640 ["INT_ADD", "register:40f0:8", ["const:aca640:8", "const:4:8"]]
- 00aca640 ["CALL", null, ["callee:00bdb040:8"]]
+ 00aca684 ["INT_ADD", "register:40f0:8", ["const:aca684:8", "const:4:8"]]
+ 00aca684 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca640 bytes 6c420494
+ 00aca684 bytes 6f420494
- 00aca664 ["INT_ADD", "register:40f0:8", ["const:aca664:8", "const:4:8"]]
- 00aca664 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca6a8 ["INT_ADD", "register:40f0:8", ["const:aca6a8:8", "const:4:8"]]
+ 00aca6a8 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca664 bytes e3420494
+ 00aca6a8 bytes e6420494
- 00aca690 ["INT_ADD", "register:40f0:8", ["const:aca690:8", "const:4:8"]]
- 00aca690 ["CALL", null, ["callee:00bdb240:8"]]
+ 00aca6d4 ["INT_ADD", "register:40f0:8", ["const:aca6d4:8", "const:4:8"]]
+ 00aca6d4 ["CALL", null, ["callee:00bdb240:8"]]
- 00aca690 bytes d8420494
+ 00aca6d4 bytes db420494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6abed0fc89884112cd10e3dc0e8b28d1"></a>

### [`00aca940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md) → [`00aca984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00aca984.md) FUN_00aca984

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00acabb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabb4.md) [`00acabc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00acabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acabf8.md) [`00acac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acac0c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00aca9e0) · [`00acaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00acaa70) · [`00acaa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00acaa8c)
- 新版 `00acaa24`（命令位置の公開資料なし） · `00acaab4`（命令位置の公開資料なし） · `00acaad0`（命令位置の公開資料なし）

~~~diff
- 00aca9e0 ["INT_ADD", "register:40f0:8", ["const:aca9e0:8", "const:4:8"]]
- 00aca9e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acaa24 ["INT_ADD", "register:40f0:8", ["const:acaa24:8", "const:4:8"]]
+ 00acaa24 ["CALL", null, ["callee:00bdb040:8"]]
- 00aca9e0 bytes 84410494
+ 00acaa24 bytes 87410494
- 00acaa70 ["INT_ADD", "register:40f0:8", ["const:acaa70:8", "const:4:8"]]
- 00acaa70 ["CALL", null, ["callee:00acac0c:8"]]
+ 00acaab4 ["INT_ADD", "register:40f0:8", ["const:acaab4:8", "const:4:8"]]
+ 00acaab4 ["CALL", null, ["callee:00acac0c:8"]]
- 00acaa70 bytes 56000094
+ 00acaab4 bytes 56000094
- 00acaa8c ["INT_ADD", "register:40f0:8", ["const:acaa8c:8", "const:4:8"]]
- 00acaa8c ["CALL", null, ["callee:00bdb060:8"]]
+ 00acaad0 ["INT_ADD", "register:40f0:8", ["const:acaad0:8", "const:4:8"]]
+ 00acaad0 ["CALL", null, ["callee:00bdb060:8"]]
- 00acaa8c bytes 61410494
+ 00acaad0 bytes 64410494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc6afdaa97a90e681941c42b6975b58"></a>

### [`00acab14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md) → [`00acab58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acab58.md) FUN_00acab58

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab64) · [`00acab74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab74) · [`00acab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab84)
- 新版 `00acaba8`（命令位置の公開資料なし） · `00acabb8`（命令位置の公開資料なし） · `00acabc8`（命令位置の公開資料なし）

~~~diff
- 00acab64 ["INT_ADD", "register:40f0:8", ["const:acab64:8", "const:4:8"]]
- 00acab64 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acaba8 ["INT_ADD", "register:40f0:8", ["const:acaba8:8", "const:4:8"]]
+ 00acaba8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acab64 bytes 2b410494
+ 00acaba8 bytes 2e410494
- 00acab74 ["INT_ADD", "register:40f0:8", ["const:acab74:8", "const:4:8"]]
- 00acab74 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acabb8 ["INT_ADD", "register:40f0:8", ["const:acabb8:8", "const:4:8"]]
+ 00acabb8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acab74 bytes 27410494
+ 00acabb8 bytes 2a410494
- 00acab84 ["INT_ADD", "register:40f0:8", ["const:acab84:8", "const:4:8"]]
- 00acab84 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acabc8 ["INT_ADD", "register:40f0:8", ["const:acabc8:8", "const:4:8"]]
+ 00acabc8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acab84 bytes 23410494
+ 00acabc8 bytes 26410494
~~~


<a id="compare-c7db17a6f61d274ac4c18a01cd3195a5"></a>

### [`00acacd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacd0.md) → [`00acad14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md) FUN_00acad14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`0076a658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076a/0076a658.md) [`007d95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d9/007d95c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`0076a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076a/0076a658.md) [`007d95c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d9/007d95c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacd0.md#insn-00acad74) · [`00acadbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacd0.md#insn-00acadbc) · [`00acadd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acacd0.md#insn-00acadd4)
- 新版 `00acadb8`（命令位置の公開資料なし） · `00acae00`（命令位置の公開資料なし） · `00acae18`（命令位置の公開資料なし）

~~~diff
- 00acad74 ["INT_ADD", "register:40f0:8", ["const:acad74:8", "const:4:8"]]
- 00acad74 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acadb8 ["INT_ADD", "register:40f0:8", ["const:acadb8:8", "const:4:8"]]
+ 00acadb8 ["CALL", null, ["callee:00bdb040:8"]]
- 00acad74 bytes 9f400494
+ 00acadb8 bytes a2400494
- 00acadbc ["INT_ADD", "register:40f0:8", ["const:acadbc:8", "const:4:8"]]
- 00acadbc ["CALL", null, ["callee:0051d884:8"]]
+ 00acae00 ["INT_ADD", "register:40f0:8", ["const:acae00:8", "const:4:8"]]
+ 00acae00 ["CALL", null, ["callee:0051d884:8"]]
- 00acadbc bytes b24ae997
+ 00acae00 bytes a14ae997
- 00acadd4 ["INT_ADD", "register:40f0:8", ["const:acadd4:8", "const:4:8"]]
- 00acadd4 ["CALL", null, ["callee:007d95c0:8"]]
+ 00acae18 ["INT_ADD", "register:40f0:8", ["const:acae18:8", "const:4:8"]]
+ 00acae18 ["CALL", null, ["callee:007d95c0:8"]]
- 00acadd4 bytes fb39f497
+ 00acae18 bytes ea39f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da3f0b786e0c05acb406fd879a13c03"></a>

### [`00acaee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md) → [`00acaf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acaf24.md) FUN_00acaf24

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acaf60) · [`00acaf94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acaf94) · [`00acafa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acafa0)
- 新版 `00acafa4`（命令位置の公開資料なし） · `00acafd8`（命令位置の公開資料なし） · `00acafe4`（命令位置の公開資料なし）

~~~diff
- 00acaf60 ["INT_ADD", "register:40f0:8", ["const:acaf60:8", "const:4:8"]]
- 00acaf60 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acafa4 ["INT_ADD", "register:40f0:8", ["const:acafa4:8", "const:4:8"]]
+ 00acafa4 ["CALL", null, ["callee:00bdb040:8"]]
- 00acaf60 bytes 24400494
+ 00acafa4 bytes 27400494
- 00acaf94 ["INT_ADD", "register:40f0:8", ["const:acaf94:8", "const:4:8"]]
- 00acaf94 ["CALL", null, ["callee:005c3468:8"]]
+ 00acafd8 ["INT_ADD", "register:40f0:8", ["const:acafd8:8", "const:4:8"]]
+ 00acafd8 ["CALL", null, ["callee:005c3468:8"]]
- 00acaf94 bytes 35e1eb97
+ 00acafd8 bytes 24e1eb97
- 00acafa0 ["INT_ADD", "register:40f0:8", ["const:acafa0:8", "const:4:8"]]
- 00acafa0 ["CALL", null, ["callee:005c3468:8"]]
+ 00acafe4 ["INT_ADD", "register:40f0:8", ["const:acafe4:8", "const:4:8"]]
+ 00acafe4 ["CALL", null, ["callee:005c3468:8"]]
- 00acafa0 bytes 32e1eb97
+ 00acafe4 bytes 21e1eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08c23328ea293d8236a6dd27f528c8bf"></a>

### [`00acb04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md) → [`00acb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb090.md) FUN_00acb090

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 6件 [`005f064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062ca28.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 6件 [`005f064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ca28.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb0c4) · [`00acb0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb0e8) · [`00acb138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb138)
- 新版 `00acb108`（命令位置の公開資料なし） · `00acb12c`（命令位置の公開資料なし） · `00acb17c`（命令位置の公開資料なし）

~~~diff
- 00acb0c4 ["INT_ADD", "register:40f0:8", ["const:acb0c4:8", "const:4:8"]]
- 00acb0c4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acb108 ["INT_ADD", "register:40f0:8", ["const:acb108:8", "const:4:8"]]
+ 00acb108 ["CALL", null, ["callee:00bdb040:8"]]
- 00acb0c4 bytes cb3f0494
+ 00acb108 bytes ce3f0494
- 00acb0e8 ["INT_ADD", "register:40f0:8", ["const:acb0e8:8", "const:4:8"]]
- 00acb0e8 ["CALL", null, ["callee:0062ca28:8"]]
+ 00acb12c ["INT_ADD", "register:40f0:8", ["const:acb12c:8", "const:4:8"]]
+ 00acb12c ["CALL", null, ["callee:0062ca28:8"]]
- 00acb0e8 bytes 5086ed97
+ 00acb12c bytes 3f86ed97
- 00acb138 ["INT_ADD", "register:40f0:8", ["const:acb138:8", "const:4:8"]]
- 00acb138 ["CALL", null, ["callee:005f064c:8"]]
+ 00acb17c ["INT_ADD", "register:40f0:8", ["const:acb17c:8", "const:4:8"]]
+ 00acb17c ["CALL", null, ["callee:005f064c:8"]]
- 00acb138 bytes 4595ec97
+ 00acb17c bytes 3495ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4943c2f54faab7fbde3eaba7f2a77f"></a>

### [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) → [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) FUN_00acb1b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`005f064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062ca28.md) [`00acb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md)
- 新版 呼出元 1件 [`00ac0004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac0/00ac0004.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005f064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062ca28.md) [`00acb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb218) · [`00acb278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb278) · [`00acb29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb29c)
- 新版 `00acb25c`（命令位置の公開資料なし） · `00acb2bc`（命令位置の公開資料なし） · `00acb2e0`（命令位置の公開資料なし）

~~~diff
- 00acb218 ["INT_ADD", "register:40f0:8", ["const:acb218:8", "const:4:8"]]
- 00acb218 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acb25c ["INT_ADD", "register:40f0:8", ["const:acb25c:8", "const:4:8"]]
+ 00acb25c ["CALL", null, ["callee:00bdb040:8"]]
- 00acb218 bytes 763f0494
+ 00acb25c bytes 793f0494
- 00acb278 ["INT_ADD", "register:40f0:8", ["const:acb278:8", "const:4:8"]]
- 00acb278 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acb2bc ["INT_ADD", "register:40f0:8", ["const:acb2bc:8", "const:4:8"]]
+ 00acb2bc ["CALL", null, ["callee:00bdb040:8"]]
- 00acb278 bytes 5e3f0494
+ 00acb2bc bytes 613f0494
- 00acb29c ["INT_ADD", "register:40f0:8", ["const:acb29c:8", "const:4:8"]]
- 00acb29c ["CALL", null, ["callee:0062ca28:8"]]
+ 00acb2e0 ["INT_ADD", "register:40f0:8", ["const:acb2e0:8", "const:4:8"]]
+ 00acb2e0 ["CALL", null, ["callee:0062ca28:8"]]
- 00acb29c bytes e385ed97
+ 00acb2e0 bytes d285ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496508f6bf865fd1a8b80e782c51edae"></a>

### [`00acb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md) → [`00acb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md) FUN_00acb43c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md#insn-00acb474) · [`00acb4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md#insn-00acb4bc)
- 新版 `00acb4b8`（命令位置の公開資料なし） · `00acb500`（命令位置の公開資料なし）

~~~diff
- 00acb474 ["INT_ADD", "register:40f0:8", ["const:acb474:8", "const:4:8"]]
- 00acb474 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acb4b8 ["INT_ADD", "register:40f0:8", ["const:acb4b8:8", "const:4:8"]]
+ 00acb4b8 ["CALL", null, ["callee:00bdb060:8"]]
- 00acb474 bytes e73e0494
+ 00acb4b8 bytes ea3e0494
- 00acb4bc ["INT_ADD", "register:40f0:8", ["const:acb4bc:8", "const:4:8"]]
- 00acb4bc ["CALL", null, ["callee:00bdb060:8"]]
+ 00acb500 ["INT_ADD", "register:40f0:8", ["const:acb500:8", "const:4:8"]]
+ 00acb500 ["CALL", null, ["callee:00bdb060:8"]]
- 00acb4bc bytes d53e0494
+ 00acb500 bytes d83e0494
~~~


<a id="compare-82c5db005612a3e3fb6bdff63bca5ebe"></a>

### [`00acb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md) → [`00acb558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb558.md) FUN_00acb558

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00acb1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb1b8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md#insn-00acb548) · [`00acb598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md#insn-00acb598)
- 新版 `00acb58c`（命令位置の公開資料なし） · `00acb5dc`（命令位置の公開資料なし）

~~~diff
- 00acb548 ["INT_ADD", "register:40f0:8", ["const:acb548:8", "const:4:8"]]
- 00acb548 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acb58c ["INT_ADD", "register:40f0:8", ["const:acb58c:8", "const:4:8"]]
+ 00acb58c ["CALL", null, ["callee:00bdb060:8"]]
- 00acb548 bytes b23e0494
+ 00acb58c bytes b53e0494
- 00acb598 ["INT_ADD", "register:40f0:8", ["const:acb598:8", "const:4:8"]]
- 00acb598 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acb5dc ["INT_ADD", "register:40f0:8", ["const:acb5dc:8", "const:4:8"]]
+ 00acb5dc ["CALL", null, ["callee:00bdb060:8"]]
- 00acb598 bytes 9e3e0494
+ 00acb5dc bytes a13e0494
~~~


<a id="compare-2d122cdcfaad15f1e6eb8bac785d5148"></a>

### [`00acbcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md) → [`00acbd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) FUN_00acbd14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00418a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a68.md) [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 4件 [`00449bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bcc.md) [`00449be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449be4.md) [`00449bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bf0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00418a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418a68.md) [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) · 呼出先 4件 [`00449bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bcc.md) [`00449be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449be4.md) [`00449bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bf0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acbce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbce0) · [`00acbce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbce8) · [`00acbcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbcf0)
- 新版 `00acbd24`（命令位置の公開資料なし） · `00acbd2c`（命令位置の公開資料なし） · `00acbd34`（命令位置の公開資料なし）

~~~diff
- 00acbce0 ["INT_ADD", "register:40f0:8", ["const:acbce0:8", "const:4:8"]]
- 00acbce0 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbd24 ["INT_ADD", "register:40f0:8", ["const:acbd24:8", "const:4:8"]]
+ 00acbd24 ["CALL", null, ["callee:0081f580:8"]]
- 00acbce0 bytes 284ef597
+ 00acbd24 bytes 174ef597
- 00acbce8 ["INT_ADD", "register:40f0:8", ["const:acbce8:8", "const:4:8"]]
- 00acbce8 ["CALL", null, ["callee:00449be4:8"]]
+ 00acbd2c ["INT_ADD", "register:40f0:8", ["const:acbd2c:8", "const:4:8"]]
+ 00acbd2c ["CALL", null, ["callee:00449be4:8"]]
- 00acbce8 bytes bff7e597
+ 00acbd2c bytes aef7e597
- 00acbcf0 ["INT_ADD", "register:40f0:8", ["const:acbcf0:8", "const:4:8"]]
- 00acbcf0 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbd34 ["INT_ADD", "register:40f0:8", ["const:acbd34:8", "const:4:8"]]
+ 00acbd34 ["CALL", null, ["callee:0081f580:8"]]
- 00acbcf0 bytes 244ef597
+ 00acbd34 bytes 134ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dabb5543493adea6282dc538b809d4ab"></a>

### [`00acbd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd38.md) → [`00acbd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd7c.md) FUN_00acbd7c

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004188e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004188e8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`004188e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acbd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd38.md#insn-00acbd48)
- 新版 `00acbd8c`（命令位置の公開資料なし）

~~~diff
- 00acbd48 ["INT_ADD", "register:40f0:8", ["const:acbd48:8", "const:4:8"]]
- 00acbd48 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbd8c ["INT_ADD", "register:40f0:8", ["const:acbd8c:8", "const:4:8"]]
+ 00acbd8c ["CALL", null, ["callee:0081f580:8"]]
- 00acbd48 bytes 0e4ef597
+ 00acbd8c bytes fd4df597
~~~


<a id="compare-ccdec77a2e1a475f46e5ccbaf4ea92a0"></a>

### [`00acc528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) → [`00acc56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) FUN_00acc56c

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 5件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9f4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`004588f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/004588f4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) · 呼出先 5件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`004588f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acc530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc530) · [`00acc53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc53c) · [`00acc540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc540)
- 新版 `00acc574`（命令位置の公開資料なし） · `00acc580`（命令位置の公開資料なし） · `00acc584`（命令位置の公開資料なし）

~~~diff
- 00acc530 ["INT_ADD", "register:40f0:8", ["const:acc530:8", "const:4:8"]]
- 00acc530 ["CALL", null, ["callee:0081f580:8"]]
+ 00acc574 ["INT_ADD", "register:40f0:8", ["const:acc574:8", "const:4:8"]]
+ 00acc574 ["CALL", null, ["callee:0081f580:8"]]
- 00acc530 bytes 144cf597
+ 00acc574 bytes 034cf597
- 00acc53c ["COPY", "register:0:8", ["register:4040:8"]]
- 00acc53c ["INT_ADD", "register:40f0:8", ["const:acc53c:8", "const:4:8"]]
- 00acc53c ["CALLIND", null, ["register:0:8"]]
+ 00acc580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acc580 ["INT_ADD", "register:40f0:8", ["const:acc580:8", "const:4:8"]]
+ 00acc580 ["CALLIND", null, ["register:0:8"]]
- 00acc53c bytes 00013fd6
+ 00acc580 bytes 00013fd6
- 00acc540 ["INT_ADD", "register:40f0:8", ["const:acc540:8", "const:4:8"]]
- 00acc540 ["CALL", null, ["ram:457e1c:8"]]
+ 00acc584 ["INT_ADD", "register:40f0:8", ["const:acc584:8", "const:4:8"]]
+ 00acc584 ["CALL", null, ["ram:457e1c:8"]]
- 00acc540 bytes 372ee697
+ 00acc584 bytes 262ee697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fbc4c50e35d44385784e24056626e15"></a>

### [`00acd34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md) → [`00acd390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md) FUN_00acd390

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md#insn-00acd368)
- 新版 `00acd3ac`（命令位置の公開資料なし）

~~~diff
- 00acd368 ["INT_ADD", "register:40f0:8", ["const:acd368:8", "const:4:8"]]
- 00acd368 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd3ac ["INT_ADD", "register:40f0:8", ["const:acd3ac:8", "const:4:8"]]
+ 00acd3ac ["CALL", null, ["callee:0081f580:8"]]
- 00acd368 bytes 8648f597
+ 00acd3ac bytes 7548f597
~~~


<a id="compare-faa56819740377c0a4fbeb7e8707232e"></a>

### [`00acd394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md) → [`00acd3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md) FUN_00acd3d8

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md#insn-00acd3b0)
- 新版 `00acd3f4`（命令位置の公開資料なし）

~~~diff
- 00acd3b0 ["INT_ADD", "register:40f0:8", ["const:acd3b0:8", "const:4:8"]]
- 00acd3b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd3f4 ["INT_ADD", "register:40f0:8", ["const:acd3f4:8", "const:4:8"]]
+ 00acd3f4 ["CALL", null, ["callee:0081f580:8"]]
- 00acd3b0 bytes 7448f597
+ 00acd3f4 bytes 6348f597
~~~


<a id="compare-e7883df7b1aadf979ca1fe309cbee8da"></a>

### [`00acd3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md) → [`00acd420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md) FUN_00acd420

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md#insn-00acd3f8)
- 新版 `00acd43c`（命令位置の公開資料なし）

~~~diff
- 00acd3f8 ["INT_ADD", "register:40f0:8", ["const:acd3f8:8", "const:4:8"]]
- 00acd3f8 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd43c ["INT_ADD", "register:40f0:8", ["const:acd43c:8", "const:4:8"]]
+ 00acd43c ["CALL", null, ["callee:0081f580:8"]]
- 00acd3f8 bytes 6248f597
+ 00acd43c bytes 5148f597
~~~


<a id="compare-3c2f7c8cf144fd15d7f6df5976c4e524"></a>

### [`00acd428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md) → [`00acd46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd46c.md) FUN_00acd46c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a54.md) · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`00423bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bb8.md)
- 新版 呼出元 1件 [`00418a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418a54.md) · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) [`00423bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd438) · [`00acd43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd43c) · [`00acd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd448)
- 新版 `00acd47c`（命令位置の公開資料なし） · `00acd480`（命令位置の公開資料なし） · `00acd48c`（命令位置の公開資料なし）

~~~diff
- 00acd438 ["INT_ADD", "register:40f0:8", ["const:acd438:8", "const:4:8"]]
- 00acd438 ["CALL", null, ["callee:00646dc4:8"]]
+ 00acd47c ["INT_ADD", "register:40f0:8", ["const:acd47c:8", "const:4:8"]]
+ 00acd47c ["CALL", null, ["callee:00646dc4:8"]]
- 00acd438 bytes 63e6ed97
+ 00acd47c bytes 52e6ed97
- 00acd43c ["INT_ADD", "register:40f0:8", ["const:acd43c:8", "const:4:8"]]
- 00acd43c ["CALL", null, ["callee:0081f580:8"]]
+ 00acd480 ["INT_ADD", "register:40f0:8", ["const:acd480:8", "const:4:8"]]
+ 00acd480 ["CALL", null, ["callee:0081f580:8"]]
- 00acd43c bytes 5148f597
+ 00acd480 bytes 4048f597
- 00acd448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acd448 ["INT_ADD", "register:40f0:8", ["const:acd448:8", "const:4:8"]]
- 00acd448 ["CALLIND", null, ["register:0:8"]]
+ 00acd48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acd48c ["INT_ADD", "register:40f0:8", ["const:acd48c:8", "const:4:8"]]
+ 00acd48c ["CALLIND", null, ["register:0:8"]]
- 00acd448 bytes 00013fd6
+ 00acd48c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75346c8a88efdc6824d392bc997a3ffa"></a>

### [`00acd4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4f0.md) → [`00acd534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd534.md) FUN_00acd534

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4f0.md#insn-00acd4f8)
- 新版 `00acd53c`（命令位置の公開資料なし）

~~~diff
- 00acd4f8 ["INT_ADD", "register:40f0:8", ["const:acd4f8:8", "const:4:8"]]
- 00acd4f8 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd53c ["INT_ADD", "register:40f0:8", ["const:acd53c:8", "const:4:8"]]
+ 00acd53c ["CALL", null, ["callee:0081f580:8"]]
- 00acd4f8 bytes 2248f597
+ 00acd53c bytes 1148f597
~~~


<a id="compare-850d3721842f4042279f73d30bcf25ba"></a>

### [`00acd574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd574.md) → [`00acd5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5b8.md) FUN_00acd5b8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd574.md#insn-00acd57c)
- 新版 `00acd5c0`（命令位置の公開資料なし）

~~~diff
- 00acd57c ["INT_ADD", "register:40f0:8", ["const:acd57c:8", "const:4:8"]]
- 00acd57c ["CALL", null, ["callee:0081f580:8"]]
+ 00acd5c0 ["INT_ADD", "register:40f0:8", ["const:acd5c0:8", "const:4:8"]]
+ 00acd5c0 ["CALL", null, ["callee:0081f580:8"]]
- 00acd57c bytes 0148f597
+ 00acd5c0 bytes f047f597
~~~


<a id="compare-2ac3ee9faf736e3f5be8057e6a570c50"></a>

### [`00acd5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md) → [`00acd5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5fc.md) FUN_00acd5fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00acc554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00acd7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd7bc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00acc598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc598.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00acd800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd800.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md#insn-00acd648) · [`00acd6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md#insn-00acd6a4) · [`00acd728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md#insn-00acd728)
- 新版 `00acd68c`（命令位置の公開資料なし） · `00acd6e8`（命令位置の公開資料なし） · `00acd76c`（命令位置の公開資料なし）

~~~diff
- 00acd648 ["INT_ADD", "register:40f0:8", ["const:acd648:8", "const:4:8"]]
- 00acd648 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acd68c ["INT_ADD", "register:40f0:8", ["const:acd68c:8", "const:4:8"]]
+ 00acd68c ["CALL", null, ["callee:00bdb040:8"]]
- 00acd648 bytes 6a360494
+ 00acd68c bytes 6d360494
- 00acd6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acd6a4 ["INT_ADD", "register:40f0:8", ["const:acd6a4:8", "const:4:8"]]
- 00acd6a4 ["CALLIND", null, ["register:0:8"]]
+ 00acd6e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acd6e8 ["INT_ADD", "register:40f0:8", ["const:acd6e8:8", "const:4:8"]]
+ 00acd6e8 ["CALLIND", null, ["register:0:8"]]
- 00acd6a4 bytes 00013fd6
+ 00acd6e8 bytes 00013fd6
- 00acd728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acd728 ["INT_ADD", "register:40f0:8", ["const:acd728:8", "const:4:8"]]
- 00acd728 ["CALLIND", null, ["register:0:8"]]
+ 00acd76c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acd76c ["INT_ADD", "register:40f0:8", ["const:acd76c:8", "const:4:8"]]
+ 00acd76c ["CALLIND", null, ["register:0:8"]]
- 00acd728 bytes 00013fd6
+ 00acd76c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d049e66ca09a0ce0585a276f33a44e74"></a>

### [`00acd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd900.md) → [`00acd944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd944.md) FUN_00acd944

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acc554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00acc598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc598.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd900.md#insn-00acd920)
- 新版 `00acd964`（命令位置の公開資料なし）

~~~diff
- 00acd920 ["INT_ADD", "register:40f0:8", ["const:acd920:8", "const:4:8"]]
- 00acd920 ["CALL", null, ["callee:00bdb060:8"]]
+ 00acd964 ["INT_ADD", "register:40f0:8", ["const:acd964:8", "const:4:8"]]
+ 00acd964 ["CALL", null, ["callee:00bdb060:8"]]
- 00acd920 bytes bc350494
+ 00acd964 bytes bf350494
~~~


<a id="compare-de44ee105b47a440fbbea40d150aef29"></a>

### [`00acf428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md) → [`00acf46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf46c.md) FUN_00acf46c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0094847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md) · 呼出先 2件 [`0066f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0094847c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00948/0094847c.md) · 呼出先 2件 [`0066f824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f824.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md#insn-00acf468) · [`00acf490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md#insn-00acf490)
- 新版 `00acf4ac`（命令位置の公開資料なし） · `00acf4d4`（命令位置の公開資料なし）

~~~diff
- 00acf468 ["INT_ADD", "register:40f0:8", ["const:acf468:8", "const:4:8"]]
- 00acf468 ["CALL", null, ["callee:0066f824:8"]]
+ 00acf4ac ["INT_ADD", "register:40f0:8", ["const:acf4ac:8", "const:4:8"]]
+ 00acf4ac ["CALL", null, ["callee:0066f824:8"]]
- 00acf468 bytes ef80ee97
+ 00acf4ac bytes de80ee97
- 00acf490 ["INT_ADD", "register:40f0:8", ["const:acf490:8", "const:4:8"]]
- 00acf490 ["CALL", null, ["callee:00bdb090:8"]]
+ 00acf4d4 ["INT_ADD", "register:40f0:8", ["const:acf4d4:8", "const:4:8"]]
+ 00acf4d4 ["CALL", null, ["callee:00bdb090:8"]]
- 00acf490 bytes ec2e0494
+ 00acf4d4 bytes ef2e0494
~~~


<a id="compare-bdb0ae57dce34b8263b4ad5832435c2e"></a>

### [`00acf8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md) → [`00acf910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf910.md) FUN_00acf910

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`0063e818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e818.md) [`0063e8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e8b4.md) [`0063ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063ea04.md) [`006e34b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) [`0063e818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e818.md) [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0063ea04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ea04.md) [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md#insn-00acf8d4)
- 新版 `00acf918`（命令位置の公開資料なし）

~~~diff
- 00acf8d4 ["INT_ADD", "register:40f0:8", ["const:acf8d4:8", "const:4:8"]]
- 00acf8d4 ["CALL", null, ["callee:00adc094:8"]]
+ 00acf918 ["INT_ADD", "register:40f0:8", ["const:acf918:8", "const:4:8"]]
+ 00acf918 ["CALL", null, ["callee:00adc094:8"]]
- 00acf8d4 bytes df310094
+ 00acf918 bytes df310094
~~~


<a id="compare-53d6b3cc7b29495438086c82290d85ac"></a>

### [`00acf95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md) → [`00acf9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9a0.md) FUN_00acf9a0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`0063e774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e774.md) [`0063e8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e8b4.md) [`0063e910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e910.md) [`0063edf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063edf8.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) [`0063e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e774.md) [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0063e910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e910.md) [`0063edf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063edf8.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md#insn-00acf964)
- 新版 `00acf9a8`（命令位置の公開資料なし）

~~~diff
- 00acf964 ["INT_ADD", "register:40f0:8", ["const:acf964:8", "const:4:8"]]
- 00acf964 ["CALL", null, ["callee:00adc094:8"]]
+ 00acf9a8 ["INT_ADD", "register:40f0:8", ["const:acf9a8:8", "const:4:8"]]
+ 00acf9a8 ["CALL", null, ["callee:00adc094:8"]]
- 00acf964 bytes bb310094
+ 00acf9a8 bytes bb310094
~~~


<a id="compare-7ea5f5dfa073704bf5aae6dbfcb38a54"></a>

### [`00acfa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md) → [`00acfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfad8.md) FUN_00acfad8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`0058b674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058b674.md) [`005d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d8/005d8f58.md) [`00617dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00617/00617dec.md) [`00624a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00624/00624a0c.md) [`0062da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da7c.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)
- 新版 呼出元 33件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md) [`005d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d8/005d8f58.md) [`00617dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/00617dec.md) [`00624a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624a0c.md) [`0062da7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da7c.md) · 呼出先 1件 [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acfaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md#insn-00acfaa8) · [`00acfac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md#insn-00acfac4)
- 新版 `00acfaec`（命令位置の公開資料なし） · `00acfb08`（命令位置の公開資料なし）

~~~diff
- 00acfaa8 ["INT_ADD", "register:40f0:8", ["const:acfaa8:8", "const:4:8"]]
- 00acfaa8 ["CALL", null, ["callee:00adc094:8"]]
+ 00acfaec ["INT_ADD", "register:40f0:8", ["const:acfaec:8", "const:4:8"]]
+ 00acfaec ["CALL", null, ["callee:00adc094:8"]]
- 00acfaa8 bytes 6a310094
+ 00acfaec bytes 6a310094
- 00acfac4 ["INT_ADD", "register:40f0:8", ["const:acfac4:8", "const:4:8"]]
- 00acfac4 ["CALL", null, ["callee:00adc094:8"]]
+ 00acfb08 ["INT_ADD", "register:40f0:8", ["const:acfb08:8", "const:4:8"]]
+ 00acfb08 ["CALL", null, ["callee:00adc094:8"]]
- 00acfac4 bytes 63310094
+ 00acfb08 bytes 63310094
~~~


<a id="compare-b2eb5918ebbade3be2088abb60972b5d"></a>

### [`00acfe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md) → [`00acfe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md) FUN_00acfe60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acfae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad08f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00acfb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ad0938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0938.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acfe78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfe78) · [`00acfe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfe8c) · [`00acfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfec0)
- 新版 `00acfebc`（命令位置の公開資料なし） · `00acfed0`（命令位置の公開資料なし） · `00acff04`（命令位置の公開資料なし）

~~~diff
- 00acfe78 ["INT_ADD", "register:40f0:8", ["const:acfe78:8", "const:4:8"]]
- 00acfe78 ["CALL", null, ["callee:00418fe0:8"]]
+ 00acfebc ["INT_ADD", "register:40f0:8", ["const:acfebc:8", "const:4:8"]]
+ 00acfebc ["CALL", null, ["callee:00418fe0:8"]]
- 00acfe78 bytes 5a24e597
+ 00acfebc bytes 4924e597
- 00acfe8c ["INT_ADD", "register:40f0:8", ["const:acfe8c:8", "const:4:8"]]
- 00acfe8c ["CALL", null, ["callee:00418fe0:8"]]
+ 00acfed0 ["INT_ADD", "register:40f0:8", ["const:acfed0:8", "const:4:8"]]
+ 00acfed0 ["CALL", null, ["callee:00418fe0:8"]]
- 00acfe8c bytes 5524e597
+ 00acfed0 bytes 4424e597
- 00acfec0 ["INT_ADD", "register:40f0:8", ["const:acfec0:8", "const:4:8"]]
- 00acfec0 ["CALL", null, ["callee:00ad0938:8"]]
+ 00acff04 ["INT_ADD", "register:40f0:8", ["const:acff04:8", "const:4:8"]]
+ 00acff04 ["CALL", null, ["callee:00ad0938:8"]]
- 00acfec0 bytes 8d020094
+ 00acff04 bytes 8d020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34ea7f359568061af6b11440cf1c565c"></a>

### [`00ad06b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md) → [`00ad06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad06fc.md) FUN_00ad06fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acff54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acff54.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00acff98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acff98.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ad1a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1a38.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad0720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md#insn-00ad0720) · [`00ad0748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md#insn-00ad0748) · [`00ad0774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md#insn-00ad0774)
- 新版 `00ad0764`（命令位置の公開資料なし） · `00ad078c`（命令位置の公開資料なし） · `00ad07b8`（命令位置の公開資料なし）

~~~diff
- 00ad0720 ["INT_ADD", "register:40f0:8", ["const:ad0720:8", "const:4:8"]]
- 00ad0720 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad0764 ["INT_ADD", "register:40f0:8", ["const:ad0764:8", "const:4:8"]]
+ 00ad0764 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad0720 bytes 3022e597
+ 00ad0764 bytes 1f22e597
- 00ad0748 ["INT_ADD", "register:40f0:8", ["const:ad0748:8", "const:4:8"]]
- 00ad0748 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad078c ["INT_ADD", "register:40f0:8", ["const:ad078c:8", "const:4:8"]]
+ 00ad078c ["CALL", null, ["callee:00418fe0:8"]]
- 00ad0748 bytes 2622e597
+ 00ad078c bytes 1522e597
- 00ad0774 ["INT_ADD", "register:40f0:8", ["const:ad0774:8", "const:4:8"]]
- 00ad0774 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad07b8 ["INT_ADD", "register:40f0:8", ["const:ad07b8:8", "const:4:8"]]
+ 00ad07b8 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad0774 bytes 1b22e597
+ 00ad07b8 bytes 0a22e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7824ae9e0bf14916080b32ec6baddea"></a>

### [`00ad19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md) → [`00ad1a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1a38.md) FUN_00ad1a38

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad06b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad1c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00ad06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad06fc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ad1c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad1/00ad1c78.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1a5c) · [`00ad1a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1a84) · [`00ad1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1ab0)
- 新版 `00ad1aa0`（命令位置の公開資料なし） · `00ad1ac8`（命令位置の公開資料なし） · `00ad1af4`（命令位置の公開資料なし）

~~~diff
- 00ad1a5c ["INT_ADD", "register:40f0:8", ["const:ad1a5c:8", "const:4:8"]]
- 00ad1a5c ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1aa0 ["INT_ADD", "register:40f0:8", ["const:ad1aa0:8", "const:4:8"]]
+ 00ad1aa0 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad1a5c bytes 611de597
+ 00ad1aa0 bytes 501de597
- 00ad1a84 ["INT_ADD", "register:40f0:8", ["const:ad1a84:8", "const:4:8"]]
- 00ad1a84 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1ac8 ["INT_ADD", "register:40f0:8", ["const:ad1ac8:8", "const:4:8"]]
+ 00ad1ac8 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad1a84 bytes 571de597
+ 00ad1ac8 bytes 461de597
- 00ad1ab0 ["INT_ADD", "register:40f0:8", ["const:ad1ab0:8", "const:4:8"]]
- 00ad1ab0 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1af4 ["INT_ADD", "register:40f0:8", ["const:ad1af4:8", "const:4:8"]]
+ 00ad1af4 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad1ab0 bytes 4c1de597
+ 00ad1af4 bytes 3b1de597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75383aa2d531d89213494bb907df3450"></a>

### [`00ad3660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3660.md) → [`00ad36a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad36a4.md) FUN_00ad36a4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00860de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860de0.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00860de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860de0.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad3684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3660.md#insn-00ad3684) · [`00ad368c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3660.md#insn-00ad368c) · [`00ad3698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3660.md#insn-00ad3698)
- 新版 `00ad36c8`（命令位置の公開資料なし） · `00ad36d0`（命令位置の公開資料なし） · `00ad36dc`（命令位置の公開資料なし）

~~~diff
- 00ad3684 ["INT_ADD", "register:40f0:8", ["const:ad3684:8", "const:4:8"]]
- 00ad3684 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad36c8 ["INT_ADD", "register:40f0:8", ["const:ad36c8:8", "const:4:8"]]
+ 00ad36c8 ["CALL", null, ["callee:00565f94:8"]]
- 00ad3684 bytes 444aea97
+ 00ad36c8 bytes 334aea97
- 00ad368c ["INT_ADD", "register:40f0:8", ["const:ad368c:8", "const:4:8"]]
- 00ad368c ["CALL", null, ["callee:00566284:8"]]
+ 00ad36d0 ["INT_ADD", "register:40f0:8", ["const:ad36d0:8", "const:4:8"]]
+ 00ad36d0 ["CALL", null, ["callee:00566284:8"]]
- 00ad368c bytes fe4aea97
+ 00ad36d0 bytes ed4aea97
- 00ad3698 ["INT_ADD", "register:40f0:8", ["const:ad3698:8", "const:4:8"]]
- 00ad3698 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad36dc ["INT_ADD", "register:40f0:8", ["const:ad36dc:8", "const:4:8"]]
+ 00ad36dc ["CALL", null, ["callee:00bdb040:8"]]
- 00ad3698 bytes 561e0494
+ 00ad36dc bytes 591e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a2dce7f098e768b75a8870436ce204"></a>

### [`00ad4850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4850.md) → [`00ad4894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4894.md) FUN_00ad4894

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad486c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4850.md#insn-00ad486c) · [`00ad48a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4850.md#insn-00ad48a8) · [`00ad48b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4850.md#insn-00ad48b8)
- 新版 `00ad48b0`（命令位置の公開資料なし） · `00ad48ec`（命令位置の公開資料なし） · `00ad48fc`（命令位置の公開資料なし）

~~~diff
- 00ad486c ["INT_ADD", "register:40f0:8", ["const:ad486c:8", "const:4:8"]]
- 00ad486c ["CALL", null, ["callee:0044a5b8:8"]]
+ 00ad48b0 ["INT_ADD", "register:40f0:8", ["const:ad48b0:8", "const:4:8"]]
+ 00ad48b0 ["CALL", null, ["callee:0044a5b8:8"]]
- 00ad486c bytes 53d7e597
+ 00ad48b0 bytes 42d7e597
- 00ad48a8 ["INT_ADD", "register:40f0:8", ["const:ad48a8:8", "const:4:8"]]
- 00ad48a8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad48ec ["INT_ADD", "register:40f0:8", ["const:ad48ec:8", "const:4:8"]]
+ 00ad48ec ["CALL", null, ["callee:00bdb060:8"]]
- 00ad48a8 bytes da190494
+ 00ad48ec bytes dd190494
- 00ad48b8 ["INT_ADD", "register:40f0:8", ["const:ad48b8:8", "const:4:8"]]
- 00ad48b8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ad48fc ["INT_ADD", "register:40f0:8", ["const:ad48fc:8", "const:4:8"]]
+ 00ad48fc ["CALL", null, ["callee:00bdb060:8"]]
- 00ad48b8 bytes d6190494
+ 00ad48fc bytes d9190494
~~~


<a id="compare-b4b453f3a48f98cd2846a6653f328b45"></a>

### [`00ad48e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md) → [`00ad492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad492c.md) FUN_00ad492c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad435c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad435c.md) [`00ad6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6bb0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00ad43a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad43a0.md) [`00ad6bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6bf4.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md#insn-00ad4954) · [`00ad4964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md#insn-00ad4964) · [`00ad4984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad48e8.md#insn-00ad4984)
- 新版 `00ad4998`（命令位置の公開資料なし） · `00ad49a8`（命令位置の公開資料なし） · `00ad49c8`（命令位置の公開資料なし）

~~~diff
- 00ad4954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4954 ["INT_ADD", "register:40f0:8", ["const:ad4954:8", "const:4:8"]]
- 00ad4954 ["CALLIND", null, ["register:0:8"]]
+ 00ad4998 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4998 ["INT_ADD", "register:40f0:8", ["const:ad4998:8", "const:4:8"]]
+ 00ad4998 ["CALLIND", null, ["register:0:8"]]
- 00ad4954 bytes 00013fd6
+ 00ad4998 bytes 00013fd6
- 00ad4964 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4964 ["INT_ADD", "register:40f0:8", ["const:ad4964:8", "const:4:8"]]
- 00ad4964 ["CALLIND", null, ["register:0:8"]]
+ 00ad49a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad49a8 ["INT_ADD", "register:40f0:8", ["const:ad49a8:8", "const:4:8"]]
+ 00ad49a8 ["CALLIND", null, ["register:0:8"]]
- 00ad4964 bytes 00013fd6
+ 00ad49a8 bytes 00013fd6
- 00ad4984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4984 ["INT_ADD", "register:40f0:8", ["const:ad4984:8", "const:4:8"]]
- 00ad4984 ["CALLIND", null, ["register:0:8"]]
+ 00ad49c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad49c8 ["INT_ADD", "register:40f0:8", ["const:ad49c8:8", "const:4:8"]]
+ 00ad49c8 ["CALLIND", null, ["register:0:8"]]
- 00ad4984 bytes 00013fd6
+ 00ad49c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafca14a23f7b1913b9f835ac2626c5c"></a>

### [`00ad4a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md) → [`00ad4a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4a94.md) FUN_00ad4a94

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad4424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md) [`00ad6c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00ad4468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4468.md) [`00ad6cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6cbc.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4abc) · [`00ad4acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4acc) · [`00ad4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4aec)
- 新版 `00ad4b00`（命令位置の公開資料なし） · `00ad4b10`（命令位置の公開資料なし） · `00ad4b30`（命令位置の公開資料なし）

~~~diff
- 00ad4abc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4abc ["INT_ADD", "register:40f0:8", ["const:ad4abc:8", "const:4:8"]]
- 00ad4abc ["CALLIND", null, ["register:0:8"]]
+ 00ad4b00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4b00 ["INT_ADD", "register:40f0:8", ["const:ad4b00:8", "const:4:8"]]
+ 00ad4b00 ["CALLIND", null, ["register:0:8"]]
- 00ad4abc bytes 00013fd6
+ 00ad4b00 bytes 00013fd6
- 00ad4acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4acc ["INT_ADD", "register:40f0:8", ["const:ad4acc:8", "const:4:8"]]
- 00ad4acc ["CALLIND", null, ["register:0:8"]]
+ 00ad4b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4b10 ["INT_ADD", "register:40f0:8", ["const:ad4b10:8", "const:4:8"]]
+ 00ad4b10 ["CALLIND", null, ["register:0:8"]]
- 00ad4acc bytes 00013fd6
+ 00ad4b10 bytes 00013fd6
- 00ad4aec ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4aec ["INT_ADD", "register:40f0:8", ["const:ad4aec:8", "const:4:8"]]
- 00ad4aec ["CALLIND", null, ["register:0:8"]]
+ 00ad4b30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4b30 ["INT_ADD", "register:40f0:8", ["const:ad4b30:8", "const:4:8"]]
+ 00ad4b30 ["CALLIND", null, ["register:0:8"]]
- 00ad4aec bytes 00013fd6
+ 00ad4b30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff70ef6473c77feab2338940a092be7"></a>

### [`00ad4bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md) → [`00ad4bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4bfc.md) FUN_00ad4bfc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad44ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00ad4530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4c58) · [`00ad4c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4c7c) · [`00ad4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4cc0)
- 新版 `00ad4c9c`（命令位置の公開資料なし） · `00ad4cc0`（命令位置の公開資料なし） · `00ad4d04`（命令位置の公開資料なし）

~~~diff
- 00ad4c58 ["INT_ADD", "register:40f0:8", ["const:ad4c58:8", "const:4:8"]]
- 00ad4c58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad4c9c ["INT_ADD", "register:40f0:8", ["const:ad4c9c:8", "const:4:8"]]
+ 00ad4c9c ["CALL", null, ["callee:00bdb040:8"]]
- 00ad4c58 bytes e6180494
+ 00ad4c9c bytes e9180494
- 00ad4c7c ["INT_ADD", "register:40f0:8", ["const:ad4c7c:8", "const:4:8"]]
- 00ad4c7c ["CALL", null, ["callee:00bdb190:8"]]
+ 00ad4cc0 ["INT_ADD", "register:40f0:8", ["const:ad4cc0:8", "const:4:8"]]
+ 00ad4cc0 ["CALL", null, ["callee:00bdb190:8"]]
- 00ad4c7c bytes 31190494
+ 00ad4cc0 bytes 34190494
- 00ad4cc0 ["INT_ADD", "register:40f0:8", ["const:ad4cc0:8", "const:4:8"]]
- 00ad4cc0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad4d04 ["INT_ADD", "register:40f0:8", ["const:ad4d04:8", "const:4:8"]]
+ 00ad4d04 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad4cc0 bytes cc180494
+ 00ad4d04 bytes cf180494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf5a20d97226308e0abe3eab8971626"></a>

### [`00ad4db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md) → [`00ad4df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4df8.md) FUN_00ad4df8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad44ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00ad4530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad4/00ad4530.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md#insn-00ad4e54) · [`00ad4e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md#insn-00ad4e78) · [`00ad4ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md#insn-00ad4ebc)
- 新版 `00ad4e98`（命令位置の公開資料なし） · `00ad4ebc`（命令位置の公開資料なし） · `00ad4f00`（命令位置の公開資料なし）

~~~diff
- 00ad4e54 ["INT_ADD", "register:40f0:8", ["const:ad4e54:8", "const:4:8"]]
- 00ad4e54 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad4e98 ["INT_ADD", "register:40f0:8", ["const:ad4e98:8", "const:4:8"]]
+ 00ad4e98 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad4e54 bytes 67180494
+ 00ad4e98 bytes 6a180494
- 00ad4e78 ["INT_ADD", "register:40f0:8", ["const:ad4e78:8", "const:4:8"]]
- 00ad4e78 ["CALL", null, ["callee:00bdb190:8"]]
+ 00ad4ebc ["INT_ADD", "register:40f0:8", ["const:ad4ebc:8", "const:4:8"]]
+ 00ad4ebc ["CALL", null, ["callee:00bdb190:8"]]
- 00ad4e78 bytes b2180494
+ 00ad4ebc bytes b5180494
- 00ad4ebc ["INT_ADD", "register:40f0:8", ["const:ad4ebc:8", "const:4:8"]]
- 00ad4ebc ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad4f00 ["INT_ADD", "register:40f0:8", ["const:ad4f00:8", "const:4:8"]]
+ 00ad4f00 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad4ebc bytes 4d180494
+ 00ad4f00 bytes 50180494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dbc9ff5455b3eafa76e09c9a1ddac04"></a>

### [`00ad5818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5818.md) → [`00ad585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad585c.md) FUN_00ad585c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00646d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646d78.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00646d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646d78.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad583c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5818.md#insn-00ad583c) · [`00ad5850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5818.md#insn-00ad5850) · [`00ad5854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5818.md#insn-00ad5854)
- 新版 `00ad5880`（命令位置の公開資料なし） · `00ad5894`（命令位置の公開資料なし） · `00ad5898`（命令位置の公開資料なし）

~~~diff
- 00ad583c ["INT_ADD", "register:40f0:8", ["const:ad583c:8", "const:4:8"]]
- 00ad583c ["CALL", null, ["callee:00565f94:8"]]
+ 00ad5880 ["INT_ADD", "register:40f0:8", ["const:ad5880:8", "const:4:8"]]
+ 00ad5880 ["CALL", null, ["callee:00565f94:8"]]
- 00ad583c bytes d641ea97
+ 00ad5880 bytes c541ea97
- 00ad5850 ["INT_ADD", "register:40f0:8", ["const:ad5850:8", "const:4:8"]]
- 00ad5850 ["CALL", null, ["callee:005669f8:8"]]
+ 00ad5894 ["INT_ADD", "register:40f0:8", ["const:ad5894:8", "const:4:8"]]
+ 00ad5894 ["CALL", null, ["callee:005669f8:8"]]
- 00ad5850 bytes 6a44ea97
+ 00ad5894 bytes 5944ea97
- 00ad5854 ["INT_ADD", "register:40f0:8", ["const:ad5854:8", "const:4:8"]]
- 00ad5854 ["CALL", null, ["callee:00566284:8"]]
+ 00ad5898 ["INT_ADD", "register:40f0:8", ["const:ad5898:8", "const:4:8"]]
+ 00ad5898 ["CALL", null, ["callee:00566284:8"]]
- 00ad5854 bytes 8c42ea97
+ 00ad5898 bytes 7b42ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e69688e3765c8cbf59f3ff8f68d2acd6"></a>

### [`00ad59a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad59a4.md) → [`00ad59e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad59e8.md) FUN_00ad59e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`00646df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646df0.md) [`00739948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00739/00739948.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 3件 [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`00646df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646df0.md) [`00739948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00739/00739948.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad59c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad59a4.md#insn-00ad59c8) · [`00ad59d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad59a4.md#insn-00ad59d0) · [`00ad59dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad59a4.md#insn-00ad59dc)
- 新版 `00ad5a0c`（命令位置の公開資料なし） · `00ad5a14`（命令位置の公開資料なし） · `00ad5a20`（命令位置の公開資料なし）

~~~diff
- 00ad59c8 ["INT_ADD", "register:40f0:8", ["const:ad59c8:8", "const:4:8"]]
- 00ad59c8 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad5a0c ["INT_ADD", "register:40f0:8", ["const:ad5a0c:8", "const:4:8"]]
+ 00ad5a0c ["CALL", null, ["callee:00565f94:8"]]
- 00ad59c8 bytes 7341ea97
+ 00ad5a0c bytes 6241ea97
- 00ad59d0 ["INT_ADD", "register:40f0:8", ["const:ad59d0:8", "const:4:8"]]
- 00ad59d0 ["CALL", null, ["callee:00566284:8"]]
+ 00ad5a14 ["INT_ADD", "register:40f0:8", ["const:ad5a14:8", "const:4:8"]]
+ 00ad5a14 ["CALL", null, ["callee:00566284:8"]]
- 00ad59d0 bytes 2d42ea97
+ 00ad5a14 bytes 1c42ea97
- 00ad59dc ["INT_ADD", "register:40f0:8", ["const:ad59dc:8", "const:4:8"]]
- 00ad59dc ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad5a20 ["INT_ADD", "register:40f0:8", ["const:ad5a20:8", "const:4:8"]]
+ 00ad5a20 ["CALL", null, ["callee:00bdb040:8"]]
- 00ad59dc bytes 85150494
+ 00ad5a20 bytes 88150494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc17a38092f4f02f583d04f957097bf5"></a>

### [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) → [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) FUN_00ad6078

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad5ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec0.md) [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) · 呼出先 2件 [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00ad5f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f04.md) [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) · 呼出先 2件 [`00ad6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6078.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad6050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad6050) · [`00ad605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad605c) · [`00ad6090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad6090)
- 新版 `00ad6094`（命令位置の公開資料なし） · `00ad60a0`（命令位置の公開資料なし） · `00ad60d4`（命令位置の公開資料なし）

~~~diff
- 00ad6050 ["INT_ADD", "register:40f0:8", ["const:ad6050:8", "const:4:8"]]
- 00ad6050 ["CALL", null, ["local:b0:8"]]
+ 00ad6094 ["INT_ADD", "register:40f0:8", ["const:ad6094:8", "const:4:8"]]
+ 00ad6094 ["CALL", null, ["local:b0:8"]]
- 00ad6050 bytes f9ffff97
+ 00ad6094 bytes f9ffff97
- 00ad605c ["INT_ADD", "register:40f0:8", ["const:ad605c:8", "const:4:8"]]
- 00ad605c ["CALL", null, ["local:b0:8"]]
+ 00ad60a0 ["INT_ADD", "register:40f0:8", ["const:ad60a0:8", "const:4:8"]]
+ 00ad60a0 ["CALL", null, ["local:b0:8"]]
- 00ad605c bytes f6ffff97
+ 00ad60a0 bytes f6ffff97
- 00ad6090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad6090 ["INT_ADD", "register:40f0:8", ["const:ad6090:8", "const:4:8"]]
- 00ad6090 ["CALLIND", null, ["register:0:8"]]
+ 00ad60d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad60d4 ["INT_ADD", "register:40f0:8", ["const:ad60d4:8", "const:4:8"]]
+ 00ad60d4 ["CALLIND", null, ["register:0:8"]]
- 00ad6090 bytes 00013fd6
+ 00ad60d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d5a7a0f624310754429ec862887726"></a>

### [`00ad60b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md) → [`00ad60f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad60f8.md) FUN_00ad60f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad5ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00ad5f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad5f0c.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad6138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md#insn-00ad6138) · [`00ad6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md#insn-00ad6164)
- 新版 `00ad617c`（命令位置の公開資料なし） · `00ad61a8`（命令位置の公開資料なし）

~~~diff
- 00ad6138 ["INT_ADD", "register:40f0:8", ["const:ad6138:8", "const:4:8"]]
- 00ad6138 ["CALL", null, ["callee:00bdb200:8"]]
+ 00ad617c ["INT_ADD", "register:40f0:8", ["const:ad617c:8", "const:4:8"]]
+ 00ad617c ["CALL", null, ["callee:00bdb200:8"]]
- 00ad6138 bytes 1e140494
+ 00ad617c bytes 21140494
- 00ad6164 ["INT_ADD", "register:40f0:8", ["const:ad6164:8", "const:4:8"]]
- 00ad6164 ["CALL", null, ["callee:00bdb200:8"]]
+ 00ad61a8 ["INT_ADD", "register:40f0:8", ["const:ad61a8:8", "const:4:8"]]
+ 00ad61a8 ["CALL", null, ["callee:00bdb200:8"]]
- 00ad6164 bytes 13140494
+ 00ad61a8 bytes 16140494
~~~


<a id="compare-b0213af9a2b9fd64e7858894e26cfe47"></a>

### [`00ad61e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md) → [`00ad6228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad6228.md) FUN_00ad6228

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad6204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad6204) · [`00ad620c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad620c) · [`00ad6218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad6218)
- 新版 `00ad6248`（命令位置の公開資料なし） · `00ad6250`（命令位置の公開資料なし） · `00ad625c`（命令位置の公開資料なし）

~~~diff
- 00ad6204 ["INT_ADD", "register:40f0:8", ["const:ad6204:8", "const:4:8"]]
- 00ad6204 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad6248 ["INT_ADD", "register:40f0:8", ["const:ad6248:8", "const:4:8"]]
+ 00ad6248 ["CALL", null, ["callee:00565f94:8"]]
- 00ad6204 bytes 643fea97
+ 00ad6248 bytes 533fea97
- 00ad620c ["INT_ADD", "register:40f0:8", ["const:ad620c:8", "const:4:8"]]
- 00ad620c ["CALL", null, ["callee:00566284:8"]]
+ 00ad6250 ["INT_ADD", "register:40f0:8", ["const:ad6250:8", "const:4:8"]]
+ 00ad6250 ["CALL", null, ["callee:00566284:8"]]
- 00ad620c bytes 1e40ea97
+ 00ad6250 bytes 0d40ea97
- 00ad6218 ["INT_ADD", "register:40f0:8", ["const:ad6218:8", "const:4:8"]]
- 00ad6218 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ad625c ["INT_ADD", "register:40f0:8", ["const:ad625c:8", "const:4:8"]]
+ 00ad625c ["CALL", null, ["callee:00bdb040:8"]]
- 00ad6218 bytes 76130494
+ 00ad625c bytes 79130494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afba6780d1e3331cd0bcbdc950ba1b32"></a>

### [`00ad74b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md) → [`00ad74f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad74f8.md) FUN_00ad74f8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00ad9088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9088.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad74f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad74f0) · [`00ad7520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad7520) · [`00ad7550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad7550)
- 新版 `00ad7534`（命令位置の公開資料なし） · `00ad7564`（命令位置の公開資料なし） · `00ad7594`（命令位置の公開資料なし）

~~~diff
- 00ad74f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad74f0 ["INT_ADD", "register:40f0:8", ["const:ad74f0:8", "const:4:8"]]
- 00ad74f0 ["CALLIND", null, ["register:0:8"]]
+ 00ad7534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad7534 ["INT_ADD", "register:40f0:8", ["const:ad7534:8", "const:4:8"]]
+ 00ad7534 ["CALLIND", null, ["register:0:8"]]
- 00ad74f0 bytes 00013fd6
+ 00ad7534 bytes 00013fd6
- 00ad7520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7520 ["INT_ADD", "register:40f0:8", ["const:ad7520:8", "const:4:8"]]
- 00ad7520 ["CALLIND", null, ["register:0:8"]]
+ 00ad7564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad7564 ["INT_ADD", "register:40f0:8", ["const:ad7564:8", "const:4:8"]]
+ 00ad7564 ["CALLIND", null, ["register:0:8"]]
- 00ad7520 bytes 00013fd6
+ 00ad7564 bytes 00013fd6
- 00ad7550 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7550 ["INT_ADD", "register:40f0:8", ["const:ad7550:8", "const:4:8"]]
- 00ad7550 ["CALLIND", null, ["register:0:8"]]
+ 00ad7594 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad7594 ["INT_ADD", "register:40f0:8", ["const:ad7594:8", "const:4:8"]]
+ 00ad7594 ["CALLIND", null, ["register:0:8"]]
- 00ad7550 bytes 00013fd6
+ 00ad7594 bytes 00013fd6
~~~


<a id="compare-449346ce6adf808408cf9f4273df670b"></a>

### [`00ad7aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7aa4.md) → [`00ad7ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7ae8.md) FUN_00ad7ae8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00854800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854800.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00854800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00854/00854800.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad7ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7aa4.md#insn-00ad7ac8) · [`00ad7ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7aa4.md#insn-00ad7ad0) · [`00ad7b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7aa4.md#insn-00ad7b1c)
- 新版 `00ad7b0c`（命令位置の公開資料なし） · `00ad7b14`（命令位置の公開資料なし） · `00ad7b60`（命令位置の公開資料なし）

~~~diff
- 00ad7ac8 ["INT_ADD", "register:40f0:8", ["const:ad7ac8:8", "const:4:8"]]
- 00ad7ac8 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad7b0c ["INT_ADD", "register:40f0:8", ["const:ad7b0c:8", "const:4:8"]]
+ 00ad7b0c ["CALL", null, ["callee:00565f94:8"]]
- 00ad7ac8 bytes 3339ea97
+ 00ad7b0c bytes 2239ea97
- 00ad7ad0 ["INT_ADD", "register:40f0:8", ["const:ad7ad0:8", "const:4:8"]]
- 00ad7ad0 ["CALL", null, ["callee:00566284:8"]]
+ 00ad7b14 ["INT_ADD", "register:40f0:8", ["const:ad7b14:8", "const:4:8"]]
+ 00ad7b14 ["CALL", null, ["callee:00566284:8"]]
- 00ad7ad0 bytes ed39ea97
+ 00ad7b14 bytes dc39ea97
- 00ad7b1c ["INT_ADD", "register:40f0:8", ["const:ad7b1c:8", "const:4:8"]]
- 00ad7b1c ["CALL", null, ["callee:00566448:8"]]
+ 00ad7b60 ["INT_ADD", "register:40f0:8", ["const:ad7b60:8", "const:4:8"]]
+ 00ad7b60 ["CALL", null, ["callee:00566448:8"]]
- 00ad7b1c bytes 4b3aea97
+ 00ad7b60 bytes 3a3aea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-430b0de4db2858314b5d12b6f1c8ac3c"></a>

### [`00ad8458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md) → [`00ad849c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad849c.md) FUN_00ad849c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad7f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00ad7fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad7/00ad7fc8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad84a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad84a0) · [`00ad84e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad84e0) · [`00ad8518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad8518)
- 新版 `00ad84e4`（命令位置の公開資料なし） · `00ad8524`（命令位置の公開資料なし） · `00ad855c`（命令位置の公開資料なし）

~~~diff
- 00ad84a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad84a0 ["INT_ADD", "register:40f0:8", ["const:ad84a0:8", "const:4:8"]]
- 00ad84a0 ["CALLIND", null, ["register:0:8"]]
+ 00ad84e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad84e4 ["INT_ADD", "register:40f0:8", ["const:ad84e4:8", "const:4:8"]]
+ 00ad84e4 ["CALLIND", null, ["register:0:8"]]
- 00ad84a0 bytes 00013fd6
+ 00ad84e4 bytes 00013fd6
- 00ad84e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad84e0 ["INT_ADD", "register:40f0:8", ["const:ad84e0:8", "const:4:8"]]
- 00ad84e0 ["CALLIND", null, ["register:0:8"]]
+ 00ad8524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad8524 ["INT_ADD", "register:40f0:8", ["const:ad8524:8", "const:4:8"]]
+ 00ad8524 ["CALLIND", null, ["register:0:8"]]
- 00ad84e0 bytes 00013fd6
+ 00ad8524 bytes 00013fd6
- 00ad8518 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad8518 ["INT_ADD", "register:40f0:8", ["const:ad8518:8", "const:4:8"]]
- 00ad8518 ["CALLIND", null, ["register:0:8"]]
+ 00ad855c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad855c ["INT_ADD", "register:40f0:8", ["const:ad855c:8", "const:4:8"]]
+ 00ad855c ["CALLIND", null, ["register:0:8"]]
- 00ad8518 bytes 00013fd6
+ 00ad855c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fabf8db7e2104956696a9dd480c635c0"></a>

### [`00ad99ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad99ac.md) → [`00ad99f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad99f0.md) FUN_00ad99f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0085f460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008602c0.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)
- 新版 呼出元 3件 [`0085f460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f460.md) [`00860170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860170.md) [`008602c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008602c0.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad99d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad99ac.md#insn-00ad99d0) · [`00ad99d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad99ac.md#insn-00ad99d8) · [`00ad9a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad99ac.md#insn-00ad9a34)
- 新版 `00ad9a14`（命令位置の公開資料なし） · `00ad9a1c`（命令位置の公開資料なし） · `00ad9a78`（命令位置の公開資料なし）

~~~diff
- 00ad99d0 ["INT_ADD", "register:40f0:8", ["const:ad99d0:8", "const:4:8"]]
- 00ad99d0 ["CALL", null, ["callee:00565f94:8"]]
+ 00ad9a14 ["INT_ADD", "register:40f0:8", ["const:ad9a14:8", "const:4:8"]]
+ 00ad9a14 ["CALL", null, ["callee:00565f94:8"]]
- 00ad99d0 bytes 7131ea97
+ 00ad9a14 bytes 6031ea97
- 00ad99d8 ["INT_ADD", "register:40f0:8", ["const:ad99d8:8", "const:4:8"]]
- 00ad99d8 ["CALL", null, ["callee:00566284:8"]]
+ 00ad9a1c ["INT_ADD", "register:40f0:8", ["const:ad9a1c:8", "const:4:8"]]
+ 00ad9a1c ["CALL", null, ["callee:00566284:8"]]
- 00ad99d8 bytes 2b32ea97
+ 00ad9a1c bytes 1a32ea97
- 00ad9a34 ["INT_ADD", "register:40f0:8", ["const:ad9a34:8", "const:4:8"]]
- 00ad9a34 ["CALL", null, ["callee:00566448:8"]]
+ 00ad9a78 ["INT_ADD", "register:40f0:8", ["const:ad9a78:8", "const:4:8"]]
+ 00ad9a78 ["CALL", null, ["callee:00566448:8"]]
- 00ad9a34 bytes 8532ea97
+ 00ad9a78 bytes 7432ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b44558c8af01be365c5f9ece316ca0d"></a>

### [`00ad9eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9eb8.md) → [`00ad9efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9efc.md) FUN_00ad9efc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad9b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00ad9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad9f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9eb8.md#insn-00ad9f00) · [`00ad9f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9eb8.md#insn-00ad9f40) · [`00ad9f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9eb8.md#insn-00ad9f78)
- 新版 `00ad9f44`（命令位置の公開資料なし） · `00ad9f84`（命令位置の公開資料なし） · `00ad9fbc`（命令位置の公開資料なし）

~~~diff
- 00ad9f00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad9f00 ["INT_ADD", "register:40f0:8", ["const:ad9f00:8", "const:4:8"]]
- 00ad9f00 ["CALLIND", null, ["register:0:8"]]
+ 00ad9f44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad9f44 ["INT_ADD", "register:40f0:8", ["const:ad9f44:8", "const:4:8"]]
+ 00ad9f44 ["CALLIND", null, ["register:0:8"]]
- 00ad9f00 bytes 00013fd6
+ 00ad9f44 bytes 00013fd6
- 00ad9f40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad9f40 ["INT_ADD", "register:40f0:8", ["const:ad9f40:8", "const:4:8"]]
- 00ad9f40 ["CALLIND", null, ["register:0:8"]]
+ 00ad9f84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad9f84 ["INT_ADD", "register:40f0:8", ["const:ad9f84:8", "const:4:8"]]
+ 00ad9f84 ["CALLIND", null, ["register:0:8"]]
- 00ad9f40 bytes 00013fd6
+ 00ad9f84 bytes 00013fd6
- 00ad9f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad9f78 ["INT_ADD", "register:40f0:8", ["const:ad9f78:8", "const:4:8"]]
- 00ad9f78 ["CALLIND", null, ["register:0:8"]]
+ 00ad9fbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad9fbc ["INT_ADD", "register:40f0:8", ["const:ad9fbc:8", "const:4:8"]]
+ 00ad9fbc ["CALLIND", null, ["register:0:8"]]
- 00ad9f78 bytes 00013fd6
+ 00ad9fbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cc2601b60e8dfe19dbd96dd848669f9"></a>

### [`00adb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md) → [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) FUN_00adb11c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad90c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90c4.md) [`00adb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md) · 呼出先 2件 [`00adb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00ad9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9108.md) [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) · 呼出先 2件 [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md#insn-00adb0f4) · [`00adb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md#insn-00adb100) · [`00adb134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb0d8.md#insn-00adb134)
- 新版 `00adb138`（命令位置の公開資料なし） · `00adb144`（命令位置の公開資料なし） · `00adb178`（命令位置の公開資料なし）

~~~diff
- 00adb0f4 ["INT_ADD", "register:40f0:8", ["const:adb0f4:8", "const:4:8"]]
- 00adb0f4 ["CALL", null, ["local:b0:8"]]
+ 00adb138 ["INT_ADD", "register:40f0:8", ["const:adb138:8", "const:4:8"]]
+ 00adb138 ["CALL", null, ["local:b0:8"]]
- 00adb0f4 bytes f9ffff97
+ 00adb138 bytes f9ffff97
- 00adb100 ["INT_ADD", "register:40f0:8", ["const:adb100:8", "const:4:8"]]
- 00adb100 ["CALL", null, ["local:b0:8"]]
+ 00adb144 ["INT_ADD", "register:40f0:8", ["const:adb144:8", "const:4:8"]]
+ 00adb144 ["CALL", null, ["local:b0:8"]]
- 00adb100 bytes f6ffff97
+ 00adb144 bytes f6ffff97
- 00adb134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb134 ["INT_ADD", "register:40f0:8", ["const:adb134:8", "const:4:8"]]
- 00adb134 ["CALLIND", null, ["register:0:8"]]
+ 00adb178 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb178 ["INT_ADD", "register:40f0:8", ["const:adb178:8", "const:4:8"]]
+ 00adb178 ["CALLIND", null, ["register:0:8"]]
- 00adb134 bytes 00013fd6
+ 00adb178 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f79f46f87b8ef90839b648fd4e029e8"></a>

### [`00adb1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md) → [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) FUN_00adb1fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad90cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad90cc.md) [`00adb1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md) · 呼出先 2件 [`00adb1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`00ad9110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9110.md) [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) · 呼出先 2件 [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md#insn-00adb1d4) · [`00adb1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md#insn-00adb1e0) · [`00adb218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md#insn-00adb218)
- 新版 `00adb218`（命令位置の公開資料なし） · `00adb224`（命令位置の公開資料なし） · `00adb25c`（命令位置の公開資料なし）

~~~diff
- 00adb1d4 ["INT_ADD", "register:40f0:8", ["const:adb1d4:8", "const:4:8"]]
- 00adb1d4 ["CALL", null, ["local:b0:8"]]
+ 00adb218 ["INT_ADD", "register:40f0:8", ["const:adb218:8", "const:4:8"]]
+ 00adb218 ["CALL", null, ["local:b0:8"]]
- 00adb1d4 bytes f9ffff97
+ 00adb218 bytes f9ffff97
- 00adb1e0 ["INT_ADD", "register:40f0:8", ["const:adb1e0:8", "const:4:8"]]
- 00adb1e0 ["CALL", null, ["local:b0:8"]]
+ 00adb224 ["INT_ADD", "register:40f0:8", ["const:adb224:8", "const:4:8"]]
+ 00adb224 ["CALL", null, ["local:b0:8"]]
- 00adb1e0 bytes f6ffff97
+ 00adb224 bytes f6ffff97
- 00adb218 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb218 ["INT_ADD", "register:40f0:8", ["const:adb218:8", "const:4:8"]]
- 00adb218 ["CALLIND", null, ["register:0:8"]]
+ 00adb25c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb25c ["INT_ADD", "register:40f0:8", ["const:adb25c:8", "const:4:8"]]
+ 00adb25c ["CALLIND", null, ["register:0:8"]]
- 00adb218 bytes 00013fd6
+ 00adb25c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eeaf3d90e40f81f8f573aeb7337b48c"></a>

### [`00adb268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md) → [`00adb2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md) FUN_00adb2ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad9b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9b20.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00adb3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb3ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00ad9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00adb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md#insn-00adb29c) · [`00adb2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md#insn-00adb2bc) · [`00adb2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md#insn-00adb2f8)
- 新版 `00adb2e0`（命令位置の公開資料なし） · `00adb300`（命令位置の公開資料なし） · `00adb33c`（命令位置の公開資料なし）

~~~diff
- 00adb29c ["INT_ADD", "register:40f0:8", ["const:adb29c:8", "const:4:8"]]
- 00adb29c ["CALL", null, ["callee:00adb3f0:8"]]
+ 00adb2e0 ["INT_ADD", "register:40f0:8", ["const:adb2e0:8", "const:4:8"]]
+ 00adb2e0 ["CALL", null, ["callee:00adb3f0:8"]]
- 00adb29c bytes 44000094
+ 00adb2e0 bytes 44000094
- 00adb2bc ["INT_ADD", "register:40f0:8", ["const:adb2bc:8", "const:4:8"]]
- 00adb2bc ["CALL", null, ["callee:00bdb040:8"]]
+ 00adb300 ["INT_ADD", "register:40f0:8", ["const:adb300:8", "const:4:8"]]
+ 00adb300 ["CALL", null, ["callee:00bdb040:8"]]
- 00adb2bc bytes 4dff0394
+ 00adb300 bytes 50ff0394
- 00adb2f8 ["INT_ADD", "register:40f0:8", ["const:adb2f8:8", "const:4:8"]]
- 00adb2f8 ["CALL", null, ["callee:00418fe0:8"]]
+ 00adb33c ["INT_ADD", "register:40f0:8", ["const:adb33c:8", "const:4:8"]]
+ 00adb33c ["CALL", null, ["callee:00418fe0:8"]]
- 00adb2f8 bytes 3af7e497
+ 00adb33c bytes 29f7e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54f83913834aa592fce6e9b3e6afe12e"></a>

### [`00adb3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb3ac.md) → [`00adb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md) FUN_00adb3f0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00adb268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00adb2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb3ac.md#insn-00adb430) · [`00adb45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb3ac.md#insn-00adb45c)
- 新版 `00adb474`（命令位置の公開資料なし） · `00adb4a0`（命令位置の公開資料なし）

~~~diff
- 00adb430 ["INT_ADD", "register:40f0:8", ["const:adb430:8", "const:4:8"]]
- 00adb430 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adb474 ["INT_ADD", "register:40f0:8", ["const:adb474:8", "const:4:8"]]
+ 00adb474 ["CALL", null, ["callee:00bdb200:8"]]
- 00adb430 bytes 60ff0394
+ 00adb474 bytes 63ff0394
- 00adb45c ["INT_ADD", "register:40f0:8", ["const:adb45c:8", "const:4:8"]]
- 00adb45c ["CALL", null, ["callee:00bdb200:8"]]
+ 00adb4a0 ["INT_ADD", "register:40f0:8", ["const:adb4a0:8", "const:4:8"]]
+ 00adb4a0 ["CALL", null, ["callee:00bdb200:8"]]
- 00adb45c bytes 55ff0394
+ 00adb4a0 bytes 58ff0394
~~~


<a id="compare-fc771773dd4055e2fa472dfe2bb8ad58"></a>

### [`00adb4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb4b0.md) → [`00adb4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb4f4.md) FUN_00adb4f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb4b0.md#insn-00adb508) · [`00adb53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb4b0.md#insn-00adb53c) · [`00adb568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb4b0.md#insn-00adb568)
- 新版 `00adb54c`（命令位置の公開資料なし） · `00adb580`（命令位置の公開資料なし） · `00adb5ac`（命令位置の公開資料なし）

~~~diff
- 00adb508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb508 ["INT_ADD", "register:40f0:8", ["const:adb508:8", "const:4:8"]]
- 00adb508 ["CALLIND", null, ["register:0:8"]]
+ 00adb54c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb54c ["INT_ADD", "register:40f0:8", ["const:adb54c:8", "const:4:8"]]
+ 00adb54c ["CALLIND", null, ["register:0:8"]]
- 00adb508 bytes 00013fd6
+ 00adb54c bytes 00013fd6
- 00adb53c ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb53c ["INT_ADD", "register:40f0:8", ["const:adb53c:8", "const:4:8"]]
- 00adb53c ["CALLIND", null, ["register:0:8"]]
+ 00adb580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb580 ["INT_ADD", "register:40f0:8", ["const:adb580:8", "const:4:8"]]
+ 00adb580 ["CALLIND", null, ["register:0:8"]]
- 00adb53c bytes 00013fd6
+ 00adb580 bytes 00013fd6
- 00adb568 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb568 ["INT_ADD", "register:40f0:8", ["const:adb568:8", "const:4:8"]]
- 00adb568 ["CALLIND", null, ["register:0:8"]]
+ 00adb5ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb5ac ["INT_ADD", "register:40f0:8", ["const:adb5ac:8", "const:4:8"]]
+ 00adb5ac ["CALLIND", null, ["register:0:8"]]
- 00adb568 bytes 00013fd6
+ 00adb5ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98d248616613fe03d64eccc4eb2588a3"></a>

### [`00adb58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md) → [`00adb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md) FUN_00adb5d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ada110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada110.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00adb6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00ada154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00adb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md#insn-00adb5c0) · [`00adb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md#insn-00adb5e0) · [`00adb61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md#insn-00adb61c)
- 新版 `00adb604`（命令位置の公開資料なし） · `00adb624`（命令位置の公開資料なし） · `00adb660`（命令位置の公開資料なし）

~~~diff
- 00adb5c0 ["INT_ADD", "register:40f0:8", ["const:adb5c0:8", "const:4:8"]]
- 00adb5c0 ["CALL", null, ["callee:00adb708:8"]]
+ 00adb604 ["INT_ADD", "register:40f0:8", ["const:adb604:8", "const:4:8"]]
+ 00adb604 ["CALL", null, ["callee:00adb708:8"]]
- 00adb5c0 bytes 41000094
+ 00adb604 bytes 41000094
- 00adb5e0 ["INT_ADD", "register:40f0:8", ["const:adb5e0:8", "const:4:8"]]
- 00adb5e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00adb624 ["INT_ADD", "register:40f0:8", ["const:adb624:8", "const:4:8"]]
+ 00adb624 ["CALL", null, ["callee:00bdb040:8"]]
- 00adb5e0 bytes 84fe0394
+ 00adb624 bytes 87fe0394
- 00adb61c ["INT_ADD", "register:40f0:8", ["const:adb61c:8", "const:4:8"]]
- 00adb61c ["CALL", null, ["callee:00418fe0:8"]]
+ 00adb660 ["INT_ADD", "register:40f0:8", ["const:adb660:8", "const:4:8"]]
+ 00adb660 ["CALL", null, ["callee:00418fe0:8"]]
- 00adb61c bytes 71f6e497
+ 00adb660 bytes 60f6e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-018023a3a35caafe74d92edf87c5589a"></a>

### [`00adb6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md) → [`00adb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md) FUN_00adb708

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00adb58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb58c.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00adb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md#insn-00adb748) · [`00adb774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb6c4.md#insn-00adb774)
- 新版 `00adb78c`（命令位置の公開資料なし） · `00adb7b8`（命令位置の公開資料なし）

~~~diff
- 00adb748 ["INT_ADD", "register:40f0:8", ["const:adb748:8", "const:4:8"]]
- 00adb748 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adb78c ["INT_ADD", "register:40f0:8", ["const:adb78c:8", "const:4:8"]]
+ 00adb78c ["CALL", null, ["callee:00bdb200:8"]]
- 00adb748 bytes 9afe0394
+ 00adb78c bytes 9dfe0394
- 00adb774 ["INT_ADD", "register:40f0:8", ["const:adb774:8", "const:4:8"]]
- 00adb774 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adb7b8 ["INT_ADD", "register:40f0:8", ["const:adb7b8:8", "const:4:8"]]
+ 00adb7b8 ["CALL", null, ["callee:00bdb200:8"]]
- 00adb774 bytes 8ffe0394
+ 00adb7b8 bytes 92fe0394
~~~


<a id="compare-b988f031bc0370313d8fa260133abd4e"></a>

### [`00adb7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md) → [`00adb80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb80c.md) FUN_00adb80c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb824) · [`00adb850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb850) · [`00adb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb860)
- 新版 `00adb868`（命令位置の公開資料なし） · `00adb894`（命令位置の公開資料なし） · `00adb8a4`（命令位置の公開資料なし）

~~~diff
- 00adb824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb824 ["INT_ADD", "register:40f0:8", ["const:adb824:8", "const:4:8"]]
- 00adb824 ["CALLIND", null, ["register:0:8"]]
+ 00adb868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb868 ["INT_ADD", "register:40f0:8", ["const:adb868:8", "const:4:8"]]
+ 00adb868 ["CALLIND", null, ["register:0:8"]]
- 00adb824 bytes 00013fd6
+ 00adb868 bytes 00013fd6
- 00adb850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb850 ["INT_ADD", "register:40f0:8", ["const:adb850:8", "const:4:8"]]
- 00adb850 ["CALLIND", null, ["register:0:8"]]
+ 00adb894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb894 ["INT_ADD", "register:40f0:8", ["const:adb894:8", "const:4:8"]]
+ 00adb894 ["CALLIND", null, ["register:0:8"]]
- 00adb850 bytes 00013fd6
+ 00adb894 bytes 00013fd6
- 00adb860 ["INT_ADD", "register:40f0:8", ["const:adb860:8", "const:4:8"]]
- 00adb860 ["CALL", null, ["callee:00bdb060:8"]]
+ 00adb8a4 ["INT_ADD", "register:40f0:8", ["const:adb8a4:8", "const:4:8"]]
+ 00adb8a4 ["CALL", null, ["callee:00bdb060:8"]]
- 00adb860 bytes ecfd0394
+ 00adb8a4 bytes effd0394
~~~


<a id="compare-c631472fedcdac9e0fa990982f9a238c"></a>

### [`00adb874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb874.md) → [`00adb8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb8b8.md) FUN_00adb8b8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ada5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada5ac.md) [`00ada774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb874.md#insn-00adb8e0) · [`00adb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb874.md#insn-00adb8f0) · [`00adb910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb874.md#insn-00adb910)
- 新版 `00adb924`（命令位置の公開資料なし） · `00adb934`（命令位置の公開資料なし） · `00adb954`（命令位置の公開資料なし）

~~~diff
- 00adb8e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb8e0 ["INT_ADD", "register:40f0:8", ["const:adb8e0:8", "const:4:8"]]
- 00adb8e0 ["CALLIND", null, ["register:0:8"]]
+ 00adb924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb924 ["INT_ADD", "register:40f0:8", ["const:adb924:8", "const:4:8"]]
+ 00adb924 ["CALLIND", null, ["register:0:8"]]
- 00adb8e0 bytes 00013fd6
+ 00adb924 bytes 00013fd6
- 00adb8f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb8f0 ["INT_ADD", "register:40f0:8", ["const:adb8f0:8", "const:4:8"]]
- 00adb8f0 ["CALLIND", null, ["register:0:8"]]
+ 00adb934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb934 ["INT_ADD", "register:40f0:8", ["const:adb934:8", "const:4:8"]]
+ 00adb934 ["CALLIND", null, ["register:0:8"]]
- 00adb8f0 bytes 00013fd6
+ 00adb934 bytes 00013fd6
- 00adb910 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb910 ["INT_ADD", "register:40f0:8", ["const:adb910:8", "const:4:8"]]
- 00adb910 ["CALLIND", null, ["register:0:8"]]
+ 00adb954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb954 ["INT_ADD", "register:40f0:8", ["const:adb954:8", "const:4:8"]]
+ 00adb954 ["CALLIND", null, ["register:0:8"]]
- 00adb910 bytes 00013fd6
+ 00adb954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67a1c427627250c0d92a6e8175f9478"></a>

### [`00adb9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md) → [`00adba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) FUN_00adba20

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00adacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md) [`00adad88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md) [`00adae94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 3件 [`00adad0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md) [`00adadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md) [`00adaed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaed8.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adba48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md#insn-00adba48) · [`00adbaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb9dc.md#insn-00adbaa4)
- 新版 `00adba8c`（命令位置の公開資料なし） · `00adbae8`（命令位置の公開資料なし）

~~~diff
- 00adba48 ["INT_ADD", "register:40f0:8", ["const:adba48:8", "const:4:8"]]
- 00adba48 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adba8c ["INT_ADD", "register:40f0:8", ["const:adba8c:8", "const:4:8"]]
+ 00adba8c ["CALL", null, ["callee:00bdb200:8"]]
- 00adba48 bytes dafd0394
+ 00adba8c bytes ddfd0394
- 00adbaa4 ["INT_ADD", "register:40f0:8", ["const:adbaa4:8", "const:4:8"]]
- 00adbaa4 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adbae8 ["INT_ADD", "register:40f0:8", ["const:adbae8:8", "const:4:8"]]
+ 00adbae8 ["CALL", null, ["callee:00bdb200:8"]]
- 00adbaa4 bytes c3fd0394
+ 00adbae8 bytes c6fd0394
~~~


<a id="compare-dc032cada1fa32174e7da13ebbfad492"></a>

### [`00adbae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md) → [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) FUN_00adbb24

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00adaf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md) [`00adb014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00adaf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md) [`00adb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adbb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md#insn-00adbb4c) · [`00adbba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md#insn-00adbba8)
- 新版 `00adbb90`（命令位置の公開資料なし） · `00adbbec`（命令位置の公開資料なし）

~~~diff
- 00adbb4c ["INT_ADD", "register:40f0:8", ["const:adbb4c:8", "const:4:8"]]
- 00adbb4c ["CALL", null, ["callee:00bdb200:8"]]
+ 00adbb90 ["INT_ADD", "register:40f0:8", ["const:adbb90:8", "const:4:8"]]
+ 00adbb90 ["CALL", null, ["callee:00bdb200:8"]]
- 00adbb4c bytes 99fd0394
+ 00adbb90 bytes 9cfd0394
- 00adbba8 ["INT_ADD", "register:40f0:8", ["const:adbba8:8", "const:4:8"]]
- 00adbba8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00adbbec ["INT_ADD", "register:40f0:8", ["const:adbbec:8", "const:4:8"]]
+ 00adbbec ["CALL", null, ["callee:00bdb200:8"]]
- 00adbba8 bytes 82fd0394
+ 00adbbec bytes 85fd0394
~~~


<a id="compare-2b980a83138a8a414fbcd03c1b23100d"></a>

### [`00adc024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc024.md) → [`00adc068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc068.md) FUN_00adc068

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`00814828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00814/00814828.md) · 呼出先 1件 [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md)
- 新版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) [`00814828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00814/00814828.md) · 呼出先 1件 [`005c3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c3/005c3468.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adc038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc024.md#insn-00adc038)
- 新版 `00adc07c`（命令位置の公開資料なし）

~~~diff
- 00adc038 ["INT_ADD", "register:40f0:8", ["const:adc038:8", "const:4:8"]]
- 00adc038 ["CALL", null, ["callee:005c3468:8"]]
+ 00adc07c ["INT_ADD", "register:40f0:8", ["const:adc07c:8", "const:4:8"]]
+ 00adc07c ["CALL", null, ["callee:005c3468:8"]]
- 00adc038 bytes 0c9deb97
+ 00adc07c bytes fb9ceb97
~~~


<a id="compare-a38da5d13a45f1d1bf357983e2d63ff3"></a>

### [`00adc4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md) → [`00adc50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc50c.md) FUN_00adc50c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`0073e4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e89c.md) · 呼出先 5件 [`00426e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) [`00adc624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 10件 [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0073dc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073dc48.md) [`0073e258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e258.md) [`0073e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e89c.md) · 呼出先 5件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00adc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adc50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md#insn-00adc50c) · [`00adc528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md#insn-00adc528) · [`00adc564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md#insn-00adc564)
- 新版 `00adc550`（命令位置の公開資料なし） · `00adc56c`（命令位置の公開資料なし） · `00adc5a8`（命令位置の公開資料なし）

~~~diff
- 00adc50c ["INT_ADD", "register:40f0:8", ["const:adc50c:8", "const:4:8"]]
- 00adc50c ["CALL", null, ["callee:00bdb040:8"]]
+ 00adc550 ["INT_ADD", "register:40f0:8", ["const:adc550:8", "const:4:8"]]
+ 00adc550 ["CALL", null, ["callee:00bdb040:8"]]
- 00adc50c bytes b9fa0394
+ 00adc550 bytes bcfa0394
- 00adc528 ["INT_ADD", "register:40f0:8", ["const:adc528:8", "const:4:8"]]
- 00adc528 ["CALL", null, ["callee:00bdb240:8"]]
+ 00adc56c ["INT_ADD", "register:40f0:8", ["const:adc56c:8", "const:4:8"]]
+ 00adc56c ["CALL", null, ["callee:00bdb240:8"]]
- 00adc528 bytes 32fb0394
+ 00adc56c bytes 35fb0394
- 00adc564 ["INT_ADD", "register:40f0:8", ["const:adc564:8", "const:4:8"]]
- 00adc564 ["CALL", null, ["callee:00bdb040:8"]]
+ 00adc5a8 ["INT_ADD", "register:40f0:8", ["const:adc5a8:8", "const:4:8"]]
+ 00adc5a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00adc564 bytes a3fa0394
+ 00adc5a8 bytes a6fa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d532b8c0511e13a8a617090ccce561f1"></a>

### [`00adc880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc880.md) → [`00adc8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md) FUN_00adc8c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00845f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845f8c.md) · 呼出先 7件 [`00426e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) [`00adc624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc624.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00845f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f8c.md) · 呼出先 7件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00adc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adc8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc880.md#insn-00adc8f0) · [`00adc94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc880.md#insn-00adc94c) · [`00adc968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc880.md#insn-00adc968)
- 新版 `00adc934`（命令位置の公開資料なし） · `00adc990`（命令位置の公開資料なし） · `00adc9ac`（命令位置の公開資料なし）

~~~diff
- 00adc8f0 ["INT_ADD", "register:40f0:8", ["const:adc8f0:8", "const:4:8"]]
- 00adc8f0 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00adc934 ["INT_ADD", "register:40f0:8", ["const:adc934:8", "const:4:8"]]
+ 00adc934 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00adc8f0 bytes ecf90394
+ 00adc934 bytes eff90394
- 00adc94c ["INT_ADD", "register:40f0:8", ["const:adc94c:8", "const:4:8"]]
- 00adc94c ["CALL", null, ["callee:00bdb040:8"]]
+ 00adc990 ["INT_ADD", "register:40f0:8", ["const:adc990:8", "const:4:8"]]
+ 00adc990 ["CALL", null, ["callee:00bdb040:8"]]
- 00adc94c bytes a9f90394
+ 00adc990 bytes acf90394
- 00adc968 ["INT_ADD", "register:40f0:8", ["const:adc968:8", "const:4:8"]]
- 00adc968 ["CALL", null, ["callee:00bdb240:8"]]
+ 00adc9ac ["INT_ADD", "register:40f0:8", ["const:adc9ac:8", "const:4:8"]]
+ 00adc9ac ["CALL", null, ["callee:00bdb240:8"]]
- 00adc968 bytes 22fa0394
+ 00adc9ac bytes 25fa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cadd9d85cad6c81d3751fc68ba060d6"></a>

### [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md) → [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md) FUN_00adcadc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00453c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00453/00453c78.md) [`0046aa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046aa44.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 20件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`0046aa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046aa44.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adcb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md#insn-00adcb00) · [`00adcb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md#insn-00adcb20) · [`00adcc7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md#insn-00adcc7c)
- 新版 `00adcb44`（命令位置の公開資料なし） · `00adcb64`（命令位置の公開資料なし） · `00adccc0`（命令位置の公開資料なし）

~~~diff
- 00adcb00 ["INT_ADD", "register:40f0:8", ["const:adcb00:8", "const:4:8"]]
- 00adcb00 ["CALL", null, ["callee:00bdb040:8"]]
+ 00adcb44 ["INT_ADD", "register:40f0:8", ["const:adcb44:8", "const:4:8"]]
+ 00adcb44 ["CALL", null, ["callee:00bdb040:8"]]
- 00adcb00 bytes 3cf90394
+ 00adcb44 bytes 3ff90394
- 00adcb20 ["INT_ADD", "register:40f0:8", ["const:adcb20:8", "const:4:8"]]
- 00adcb20 ["CALL", null, ["callee:00bdb240:8"]]
+ 00adcb64 ["INT_ADD", "register:40f0:8", ["const:adcb64:8", "const:4:8"]]
+ 00adcb64 ["CALL", null, ["callee:00bdb240:8"]]
- 00adcb20 bytes b4f90394
+ 00adcb64 bytes b7f90394
- 00adcc7c ["INT_ADD", "register:40f0:8", ["const:adcc7c:8", "const:4:8"]]
- 00adcc7c ["CALL", null, ["callee:00418c24:8"]]
+ 00adccc0 ["INT_ADD", "register:40f0:8", ["const:adccc0:8", "const:4:8"]]
+ 00adccc0 ["CALL", null, ["callee:00418c24:8"]]
- 00adcc7c bytes eaefe497
+ 00adccc0 bytes d9efe497
~~~


<a id="compare-c4147b039d77d7811c2176dbf07af803"></a>

### [`00add674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add674.md) → [`00add6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md) FUN_00add6b8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ade6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade6f8.md) · 呼出先 1件 [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00ade73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md) · 呼出先 1件 [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00add690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add674.md#insn-00add690) · [`00add6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add674.md#insn-00add6a0) · [`00add6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00add/00add674.md#insn-00add6b8)
- 新版 `00add6d4`（命令位置の公開資料なし） · `00add6e4`（命令位置の公開資料なし） · `00add6fc`（命令位置の公開資料なし）

~~~diff
- 00add690 ["INT_ADD", "register:40f0:8", ["const:add690:8", "const:4:8"]]
- 00add690 ["CALL", null, ["callee:00464a64:8"]]
+ 00add6d4 ["INT_ADD", "register:40f0:8", ["const:add6d4:8", "const:4:8"]]
+ 00add6d4 ["CALL", null, ["callee:00464a64:8"]]
- 00add690 bytes f51ce697
+ 00add6d4 bytes e41ce697
- 00add6a0 ["INT_ADD", "register:40f0:8", ["const:add6a0:8", "const:4:8"]]
- 00add6a0 ["CALL", null, ["callee:00464a64:8"]]
+ 00add6e4 ["INT_ADD", "register:40f0:8", ["const:add6e4:8", "const:4:8"]]
+ 00add6e4 ["CALL", null, ["callee:00464a64:8"]]
- 00add6a0 bytes f11ce697
+ 00add6e4 bytes e01ce697
- 00add6b8 ["INT_ADD", "register:40f0:8", ["const:add6b8:8", "const:4:8"]]
- 00add6b8 ["CALL", null, ["callee:00464a64:8"]]
+ 00add6fc ["INT_ADD", "register:40f0:8", ["const:add6fc:8", "const:4:8"]]
+ 00add6fc ["CALL", null, ["callee:00464a64:8"]]
- 00add6b8 bytes eb1ce697
+ 00add6fc bytes da1ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a573e7d94c1b492b5d21ae46721867"></a>

### [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md) → [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md) FUN_00ade610

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 39件 [`005a79d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a79d8.md) [`005e144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e144c.md) [`0065040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/0065040c.md) [`00653214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/00653214.md) [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 39件 [`005a79d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a79d8.md) [`005e144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e144c.md) [`0065040c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/0065040c.md) [`00653214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/00653214.md) [`006a8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a8e60.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ade5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md#insn-00ade5e4) · [`00ade628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md#insn-00ade628) · [`00ade63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md#insn-00ade63c)
- 新版 `00ade628`（命令位置の公開資料なし） · `00ade66c`（命令位置の公開資料なし） · `00ade680`（命令位置の公開資料なし）

~~~diff
- 00ade5e4 ["INT_ADD", "register:40f0:8", ["const:ade5e4:8", "const:4:8"]]
- 00ade5e4 ["CALL", null, ["callee:0081f580:8"]]
+ 00ade628 ["INT_ADD", "register:40f0:8", ["const:ade628:8", "const:4:8"]]
+ 00ade628 ["CALL", null, ["callee:0081f580:8"]]
- 00ade5e4 bytes e703f597
+ 00ade628 bytes d603f597
- 00ade628 ["INT_ADD", "register:40f0:8", ["const:ade628:8", "const:4:8"]]
- 00ade628 ["CALL", null, ["callee:0081f580:8"]]
+ 00ade66c ["INT_ADD", "register:40f0:8", ["const:ade66c:8", "const:4:8"]]
+ 00ade66c ["CALL", null, ["callee:0081f580:8"]]
- 00ade628 bytes d603f597
+ 00ade66c bytes c503f597
- 00ade63c ["INT_ADD", "register:40f0:8", ["const:ade63c:8", "const:4:8"]]
- 00ade63c ["CALL", null, ["callee:0081f580:8"]]
+ 00ade680 ["INT_ADD", "register:40f0:8", ["const:ade680:8", "const:4:8"]]
+ 00ade680 ["CALL", null, ["callee:0081f580:8"]]
- 00ade63c bytes d103f597
+ 00ade680 bytes c003f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-989bbaf25533e97da9c6268ac857819b"></a>

### [`00adf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md) → [`00adf6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md) FUN_00adf6e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00ade2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade2f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adf720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md#insn-00adf720) · [`00adf780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md#insn-00adf780) · [`00adf7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf6a0.md#insn-00adf7b4)
- 新版 `00adf764`（命令位置の公開資料なし） · `00adf7c4`（命令位置の公開資料なし） · `00adf7f8`（命令位置の公開資料なし）

~~~diff
- 00adf720 ["INT_ADD", "register:40f0:8", ["const:adf720:8", "const:4:8"]]
- 00adf720 ["CALL", null, ["callee:00ade338:8"]]
+ 00adf764 ["INT_ADD", "register:40f0:8", ["const:adf764:8", "const:4:8"]]
+ 00adf764 ["CALL", null, ["callee:00ade338:8"]]
- 00adf720 bytes f5faff97
+ 00adf764 bytes f5faff97
- 00adf780 ["INT_ADD", "register:40f0:8", ["const:adf780:8", "const:4:8"]]
- 00adf780 ["CALL", null, ["callee:00bdb040:8"]]
+ 00adf7c4 ["INT_ADD", "register:40f0:8", ["const:adf7c4:8", "const:4:8"]]
+ 00adf7c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00adf780 bytes 1cee0394
+ 00adf7c4 bytes 1fee0394
- 00adf7b4 ["INT_ADD", "register:40f0:8", ["const:adf7b4:8", "const:4:8"]]
- 00adf7b4 ["CALL", null, ["callee:00419064:8"]]
+ 00adf7f8 ["INT_ADD", "register:40f0:8", ["const:adf7f8:8", "const:4:8"]]
+ 00adf7f8 ["CALL", null, ["callee:00419064:8"]]
- 00adf7b4 bytes 2ce6e497
+ 00adf7f8 bytes 1be6e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e80e99f295a5fa0605e48ee9513ed9"></a>

### [`00adf8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf8e0.md) → [`00adf924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf924.md) FUN_00adf924

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006aef04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aef04.md) [`00730204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00730/00730204.md) [`0094f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f64c.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 1件 [`00ade5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ade/00ade5cc.md)
- 新版 呼出元 6件 [`006aef04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aef04.md) [`00730204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00730/00730204.md) [`0094f64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f64c.md) [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 1件 [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adf900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf8e0.md#insn-00adf900) · [`00adf964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf8e0.md#insn-00adf964)
- 新版 `00adf944`（命令位置の公開資料なし） · `00adf9a8`（命令位置の公開資料なし）

~~~diff
- 00adf900 ["INT_ADD", "register:40f0:8", ["const:adf900:8", "const:4:8"]]
- 00adf900 ["CALL", null, ["callee:00ade610:8"]]
+ 00adf944 ["INT_ADD", "register:40f0:8", ["const:adf944:8", "const:4:8"]]
+ 00adf944 ["CALL", null, ["callee:00ade610:8"]]
- 00adf900 bytes 33fbff97
+ 00adf944 bytes 33fbff97
- 00adf964 ["INT_ADD", "register:40f0:8", ["const:adf964:8", "const:4:8"]]
- 00adf964 ["CALL", null, ["callee:00ade610:8"]]
+ 00adf9a8 ["INT_ADD", "register:40f0:8", ["const:adf9a8:8", "const:4:8"]]
+ 00adf9a8 ["CALL", null, ["callee:00ade610:8"]]
- 00adf964 bytes 1afbff97
+ 00adf9a8 bytes 1afbff97
~~~


<a id="compare-93250923e018157d30ec7c57e91d5f6e"></a>

### [`00adf9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9fc.md) → [`00adfa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa40.md) FUN_00adfa40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adfa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9fc.md#insn-00adfa28) · [`00adfa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9fc.md#insn-00adfa2c) · [`00adfa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adf9fc.md#insn-00adfa4c)
- 新版 `00adfa6c`（命令位置の公開資料なし） · `00adfa70`（命令位置の公開資料なし） · `00adfa90`（命令位置の公開資料なし）

~~~diff
- 00adfa28 ["INT_ADD", "register:40f0:8", ["const:adfa28:8", "const:4:8"]]
- 00adfa28 ["CALL", null, ["callee:00885f80:8"]]
+ 00adfa6c ["INT_ADD", "register:40f0:8", ["const:adfa6c:8", "const:4:8"]]
+ 00adfa6c ["CALL", null, ["callee:00885f80:8"]]
- 00adfa28 bytes 5699f697
+ 00adfa6c bytes 4599f697
- 00adfa2c ["INT_ADD", "register:40f0:8", ["const:adfa2c:8", "const:4:8"]]
- 00adfa2c ["CALL", null, ["ram:457e1c:8"]]
+ 00adfa70 ["INT_ADD", "register:40f0:8", ["const:adfa70:8", "const:4:8"]]
+ 00adfa70 ["CALL", null, ["ram:457e1c:8"]]
- 00adfa2c bytes fce0e597
+ 00adfa70 bytes ebe0e597
- 00adfa4c ["INT_ADD", "register:40f0:8", ["const:adfa4c:8", "const:4:8"]]
- 00adfa4c ["CALL", null, ["callee:0081f580:8"]]
+ 00adfa90 ["INT_ADD", "register:40f0:8", ["const:adfa90:8", "const:4:8"]]
+ 00adfa90 ["CALL", null, ["callee:0081f580:8"]]
- 00adfa4c bytes cdfef497
+ 00adfa90 bytes bcfef497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a1f13fb3ba88041efb3bd5f2c25f9b"></a>

### [`00ae002c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md) → [`00ae0070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md) FUN_00ae0070

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md) · 呼出先 2件 [`00bddac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddac0.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) · 呼出先 2件 [`00bddb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb10.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae003c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md#insn-00ae003c) · [`00ae004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md#insn-00ae004c)
- 新版 `00ae0080`（命令位置の公開資料なし） · `00ae0090`（命令位置の公開資料なし）

~~~diff
- 00ae003c ["INT_ADD", "register:40f0:8", ["const:ae003c:8", "const:4:8"]]
- 00ae003c ["CALL", null, ["callee:00bdde00:8"]]
+ 00ae0080 ["INT_ADD", "register:40f0:8", ["const:ae0080:8", "const:4:8"]]
+ 00ae0080 ["CALL", null, ["callee:00bdde00:8"]]
- 00ae003c bytes 5df70394
+ 00ae0080 bytes 60f70394
- 00ae004c ["INT_ADD", "register:40f0:8", ["const:ae004c:8", "const:4:8"]]
- 00ae004c ["CALL", null, ["callee:00bddb10:8"]]
+ 00ae0090 ["INT_ADD", "register:40f0:8", ["const:ae0090:8", "const:4:8"]]
+ 00ae0090 ["CALL", null, ["callee:00bddb10:8"]]
- 00ae004c bytes 9df60394
+ 00ae0090 bytes a0f60394
~~~


<a id="compare-32bc1c168f89c30502302e1bafc19784"></a>

### [`00ae0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0060.md) → [`00ae00a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00a4.md) FUN_00ae00a4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md) · 呼出先 2件 [`00bddaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) · 呼出先 2件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0060.md#insn-00ae0070)
- 新版 `00ae00b4`（命令位置の公開資料なし）

~~~diff
- 00ae0070 ["INT_ADD", "register:40f0:8", ["const:ae0070:8", "const:4:8"]]
- 00ae0070 ["CALL", null, ["callee:00bdde00:8"]]
+ 00ae00b4 ["INT_ADD", "register:40f0:8", ["const:ae00b4:8", "const:4:8"]]
+ 00ae00b4 ["CALL", null, ["callee:00bdde00:8"]]
- 00ae0070 bytes 50f70394
+ 00ae00b4 bytes 53f70394
~~~


<a id="compare-c7fb608680020854d914a440adca5c38"></a>

### [`00ae02ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae02ac.md) → [`00ae02f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae02f0.md) _ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdde90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde90.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00bddee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddee0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae02e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae02ac.md#insn-00ae02e0) · [`00ae0304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae02ac.md#insn-00ae0304) · [`00ae0318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae02ac.md#insn-00ae0318)
- 新版 `00ae0324`（命令位置の公開資料なし） · `00ae0348`（命令位置の公開資料なし） · `00ae035c`（命令位置の公開資料なし）

~~~diff
- 00ae02e0 ["INT_ADD", "register:40f0:8", ["const:ae02e0:8", "const:4:8"]]
- 00ae02e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ae0324 ["INT_ADD", "register:40f0:8", ["const:ae0324:8", "const:4:8"]]
+ 00ae0324 ["CALL", null, ["callee:00bdb040:8"]]
- 00ae02e0 bytes 44eb0394
+ 00ae0324 bytes 47eb0394
- 00ae0304 ["INT_ADD", "register:40f0:8", ["const:ae0304:8", "const:4:8"]]
- 00ae0304 ["CALL", null, ["callee:00bdde10:8"]]
+ 00ae0348 ["INT_ADD", "register:40f0:8", ["const:ae0348:8", "const:4:8"]]
+ 00ae0348 ["CALL", null, ["callee:00bdde10:8"]]
- 00ae0304 bytes aff60394
+ 00ae0348 bytes b2f60394
- 00ae0318 ["INT_ADD", "register:40f0:8", ["const:ae0318:8", "const:4:8"]]
- 00ae0318 ["CALL", null, ["callee:00bddd80:8"]]
+ 00ae035c ["INT_ADD", "register:40f0:8", ["const:ae035c:8", "const:4:8"]]
+ 00ae035c ["CALL", null, ["callee:00bddd80:8"]]
- 00ae0318 bytes 86f60394
+ 00ae035c bytes 89f60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7280cad9940fddada44f0a2db28e4c68"></a>

### [`00ae037c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae037c.md) → [`00ae03c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae03c0.md) _ZNSt6__ndk113__vector_baseIN8firebase10FutureBaseENS_9allocatorIS2_EEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdde70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde70.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)
- 新版 呼出元 1件 [`00bddec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddec0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae03ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae037c.md#insn-00ae03ac) · [`00ae03c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae037c.md#insn-00ae03c4) · [`00ae03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae037c.md#insn-00ae03d8)
- 新版 `00ae03f0`（命令位置の公開資料なし） · `00ae0408`（命令位置の公開資料なし） · `00ae041c`（命令位置の公開資料なし）

~~~diff
- 00ae03ac ["INT_ADD", "register:40f0:8", ["const:ae03ac:8", "const:4:8"]]
- 00ae03ac ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae03f0 ["INT_ADD", "register:40f0:8", ["const:ae03f0:8", "const:4:8"]]
+ 00ae03f0 ["CALL", null, ["callee:00bddc20:8"]]
- 00ae03ac bytes 09f60394
+ 00ae03f0 bytes 0cf60394
- 00ae03c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae03c4 ["INT_ADD", "register:40f0:8", ["const:ae03c4:8", "const:4:8"]]
- 00ae03c4 ["CALLIND", null, ["register:0:8"]]
+ 00ae0408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0408 ["INT_ADD", "register:40f0:8", ["const:ae0408:8", "const:4:8"]]
+ 00ae0408 ["CALLIND", null, ["register:0:8"]]
- 00ae03c4 bytes 00013fd6
+ 00ae0408 bytes 00013fd6
- 00ae03d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae03d8 ["INT_ADD", "register:40f0:8", ["const:ae03d8:8", "const:4:8"]]
- 00ae03d8 ["CALLIND", null, ["register:0:8"]]
+ 00ae041c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae041c ["INT_ADD", "register:40f0:8", ["const:ae041c:8", "const:4:8"]]
+ 00ae041c ["CALLIND", null, ["register:0:8"]]
- 00ae03d8 bytes 00013fd6
+ 00ae041c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2777aa0a2ef5689e1b8afe6b122f4e1d"></a>

### [`00ae04fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md) → [`00ae0540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0540.md) _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdde80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00bdded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdded0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdded0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md#insn-00ae0518) · [`00ae0524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md#insn-00ae0524)
- 新版 `00ae055c`（命令位置の公開資料なし） · `00ae0568`（命令位置の公開資料なし）

~~~diff
- 00ae0518 ["INT_ADD", "register:40f0:8", ["const:ae0518:8", "const:4:8"]]
- 00ae0518 ["CALL", null, ["callee:00bdded0:8"]]
+ 00ae055c ["INT_ADD", "register:40f0:8", ["const:ae055c:8", "const:4:8"]]
+ 00ae055c ["CALL", null, ["callee:00bdded0:8"]]
- 00ae0518 bytes 5af60394
+ 00ae055c bytes 5df60394
- 00ae0524 ["INT_ADD", "register:40f0:8", ["const:ae0524:8", "const:4:8"]]
- 00ae0524 ["CALL", null, ["callee:00bdded0:8"]]
+ 00ae0568 ["INT_ADD", "register:40f0:8", ["const:ae0568:8", "const:4:8"]]
+ 00ae0568 ["CALL", null, ["callee:00bdded0:8"]]
- 00ae0524 bytes 57f60394
+ 00ae0568 bytes 5af60394
~~~


<a id="compare-53db7ad1a65d1cf4af77ef267211584d"></a>

### [`00ae1264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1264.md) → [`00ae12a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae12a8.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae12d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1264.md#insn-00ae12d8) · [`00ae12fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1264.md#insn-00ae12fc)
- 新版 `00ae131c`（命令位置の公開資料なし） · `00ae1340`（命令位置の公開資料なし）

~~~diff
- 00ae12d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae12d8 ["INT_ADD", "register:40f0:8", ["const:ae12d8:8", "const:4:8"]]
- 00ae12d8 ["CALLIND", null, ["register:0:8"]]
+ 00ae131c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae131c ["INT_ADD", "register:40f0:8", ["const:ae131c:8", "const:4:8"]]
+ 00ae131c ["CALLIND", null, ["register:0:8"]]
- 00ae12d8 bytes 00013fd6
+ 00ae131c bytes 00013fd6
- 00ae12fc ["INT_ADD", "register:40f0:8", ["const:ae12fc:8", "const:4:8"]]
- 00ae12fc ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae1340 ["INT_ADD", "register:40f0:8", ["const:ae1340:8", "const:4:8"]]
+ 00ae1340 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae12fc bytes 51e70394
+ 00ae1340 bytes 54e70394
~~~


<a id="compare-cfd953e66f17df371e59e405a207d522"></a>

### [`00ae1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1890.md) → [`00ae18d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae18d4.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcS6_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae18b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1890.md#insn-00ae18b8) · [`00ae18d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1890.md#insn-00ae18d0) · [`00ae18dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1890.md#insn-00ae18dc)
- 新版 `00ae18fc`（命令位置の公開資料なし） · `00ae1914`（命令位置の公開資料なし） · `00ae1920`（命令位置の公開資料なし）

~~~diff
- 00ae18b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae18b8 ["INT_ADD", "register:40f0:8", ["const:ae18b8:8", "const:4:8"]]
- 00ae18b8 ["CALLIND", null, ["register:0:8"]]
+ 00ae18fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae18fc ["INT_ADD", "register:40f0:8", ["const:ae18fc:8", "const:4:8"]]
+ 00ae18fc ["CALLIND", null, ["register:0:8"]]
- 00ae18b8 bytes 00013fd6
+ 00ae18fc bytes 00013fd6
- 00ae18d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae18d0 ["INT_ADD", "register:40f0:8", ["const:ae18d0:8", "const:4:8"]]
- 00ae18d0 ["CALLIND", null, ["register:0:8"]]
+ 00ae1914 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1914 ["INT_ADD", "register:40f0:8", ["const:ae1914:8", "const:4:8"]]
+ 00ae1914 ["CALLIND", null, ["register:0:8"]]
- 00ae18d0 bytes 00013fd6
+ 00ae1914 bytes 00013fd6
- 00ae18dc ["INT_ADD", "register:40f0:8", ["const:ae18dc:8", "const:4:8"]]
- 00ae18dc ["CALL", null, ["callee:00bde110:8"]]
+ 00ae1920 ["INT_ADD", "register:40f0:8", ["const:ae1920:8", "const:4:8"]]
+ 00ae1920 ["CALL", null, ["callee:00bde110:8"]]
- 00ae18dc bytes f9f10394
+ 00ae1920 bytes fcf10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f77747c59566364048e85f06dcdc0f9c"></a>

### [`00ae1934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1934.md) → [`00ae1978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1978.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcd

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1934.md#insn-00ae1960) · [`00ae196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1934.md#insn-00ae196c) · [`00ae1984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1934.md#insn-00ae1984)
- 新版 `00ae19a4`（命令位置の公開資料なし） · `00ae19b0`（命令位置の公開資料なし） · `00ae19c8`（命令位置の公開資料なし）

~~~diff
- 00ae1960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1960 ["INT_ADD", "register:40f0:8", ["const:ae1960:8", "const:4:8"]]
- 00ae1960 ["CALLIND", null, ["register:0:8"]]
+ 00ae19a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae19a4 ["INT_ADD", "register:40f0:8", ["const:ae19a4:8", "const:4:8"]]
+ 00ae19a4 ["CALLIND", null, ["register:0:8"]]
- 00ae1960 bytes 00013fd6
+ 00ae19a4 bytes 00013fd6
- 00ae196c ["INT_ADD", "register:40f0:8", ["const:ae196c:8", "const:4:8"]]
- 00ae196c ["CALL", null, ["callee:00bde110:8"]]
+ 00ae19b0 ["INT_ADD", "register:40f0:8", ["const:ae19b0:8", "const:4:8"]]
+ 00ae19b0 ["CALL", null, ["callee:00bde110:8"]]
- 00ae196c bytes d5f10394
+ 00ae19b0 bytes d8f10394
- 00ae1984 ["INT_ADD", "register:40f0:8", ["const:ae1984:8", "const:4:8"]]
- 00ae1984 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae19c8 ["INT_ADD", "register:40f0:8", ["const:ae19c8:8", "const:4:8"]]
+ 00ae19c8 ["CALL", null, ["callee:00551e14:8"]]
- 00ae1984 bytes 24c1e997
+ 00ae19c8 bytes 13c1e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eec47f7930a599d33966425b5936f40"></a>

### [`00ae19b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae19b4.md) → [`00ae19f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae19f8.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae19dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae19b4.md#insn-00ae19dc) · [`00ae19e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae19b4.md#insn-00ae19e8) · [`00ae1a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae19b4.md#insn-00ae1a00)
- 新版 `00ae1a20`（命令位置の公開資料なし） · `00ae1a2c`（命令位置の公開資料なし） · `00ae1a44`（命令位置の公開資料なし）

~~~diff
- 00ae19dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae19dc ["INT_ADD", "register:40f0:8", ["const:ae19dc:8", "const:4:8"]]
- 00ae19dc ["CALLIND", null, ["register:0:8"]]
+ 00ae1a20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1a20 ["INT_ADD", "register:40f0:8", ["const:ae1a20:8", "const:4:8"]]
+ 00ae1a20 ["CALLIND", null, ["register:0:8"]]
- 00ae19dc bytes 00013fd6
+ 00ae1a20 bytes 00013fd6
- 00ae19e8 ["INT_ADD", "register:40f0:8", ["const:ae19e8:8", "const:4:8"]]
- 00ae19e8 ["CALL", null, ["callee:00bde110:8"]]
+ 00ae1a2c ["INT_ADD", "register:40f0:8", ["const:ae1a2c:8", "const:4:8"]]
+ 00ae1a2c ["CALL", null, ["callee:00bde110:8"]]
- 00ae19e8 bytes b6f10394
+ 00ae1a2c bytes b9f10394
- 00ae1a00 ["INT_ADD", "register:40f0:8", ["const:ae1a00:8", "const:4:8"]]
- 00ae1a00 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae1a44 ["INT_ADD", "register:40f0:8", ["const:ae1a44:8", "const:4:8"]]
+ 00ae1a44 ["CALL", null, ["callee:00551e14:8"]]
- 00ae1a00 bytes 05c1e997
+ 00ae1a44 bytes f4c0e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-252927546710fabf010a4712ef2bdda5"></a>

### [`00ae1a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1a2c.md) → [`00ae1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1a70.md) _ZN8firebase9analytics20AddArrayListToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1a2c.md#insn-00ae1a54) · [`00ae1a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1a2c.md#insn-00ae1a60) · [`00ae1a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1a2c.md#insn-00ae1a78)
- 新版 `00ae1a98`（命令位置の公開資料なし） · `00ae1aa4`（命令位置の公開資料なし） · `00ae1abc`（命令位置の公開資料なし）

~~~diff
- 00ae1a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1a54 ["INT_ADD", "register:40f0:8", ["const:ae1a54:8", "const:4:8"]]
- 00ae1a54 ["CALLIND", null, ["register:0:8"]]
+ 00ae1a98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1a98 ["INT_ADD", "register:40f0:8", ["const:ae1a98:8", "const:4:8"]]
+ 00ae1a98 ["CALLIND", null, ["register:0:8"]]
- 00ae1a54 bytes 00013fd6
+ 00ae1a98 bytes 00013fd6
- 00ae1a60 ["INT_ADD", "register:40f0:8", ["const:ae1a60:8", "const:4:8"]]
- 00ae1a60 ["CALL", null, ["callee:00bde110:8"]]
+ 00ae1aa4 ["INT_ADD", "register:40f0:8", ["const:ae1aa4:8", "const:4:8"]]
+ 00ae1aa4 ["CALL", null, ["callee:00bde110:8"]]
- 00ae1a60 bytes 98f10394
+ 00ae1aa4 bytes 9bf10394
- 00ae1a78 ["INT_ADD", "register:40f0:8", ["const:ae1a78:8", "const:4:8"]]
- 00ae1a78 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae1abc ["INT_ADD", "register:40f0:8", ["const:ae1abc:8", "const:4:8"]]
+ 00ae1abc ["CALL", null, ["callee:00551e14:8"]]
- 00ae1a78 bytes e7c0e997
+ 00ae1abc bytes d6c0e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86be1b5d7d8be95fe15b7228776c63d0"></a>

### [`00ae1aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1aa4.md) → [`00ae1ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1ae8.md) _ZN8firebase9analytics17AddBundleToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1aa4.md#insn-00ae1acc) · [`00ae1ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1aa4.md#insn-00ae1ad8) · [`00ae1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1aa4.md#insn-00ae1af0)
- 新版 `00ae1b10`（命令位置の公開資料なし） · `00ae1b1c`（命令位置の公開資料なし） · `00ae1b34`（命令位置の公開資料なし）

~~~diff
- 00ae1acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1acc ["INT_ADD", "register:40f0:8", ["const:ae1acc:8", "const:4:8"]]
- 00ae1acc ["CALLIND", null, ["register:0:8"]]
+ 00ae1b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1b10 ["INT_ADD", "register:40f0:8", ["const:ae1b10:8", "const:4:8"]]
+ 00ae1b10 ["CALLIND", null, ["register:0:8"]]
- 00ae1acc bytes 00013fd6
+ 00ae1b10 bytes 00013fd6
- 00ae1ad8 ["INT_ADD", "register:40f0:8", ["const:ae1ad8:8", "const:4:8"]]
- 00ae1ad8 ["CALL", null, ["callee:00bde110:8"]]
+ 00ae1b1c ["INT_ADD", "register:40f0:8", ["const:ae1b1c:8", "const:4:8"]]
+ 00ae1b1c ["CALL", null, ["callee:00bde110:8"]]
- 00ae1ad8 bytes 7af10394
+ 00ae1b1c bytes 7df10394
- 00ae1af0 ["INT_ADD", "register:40f0:8", ["const:ae1af0:8", "const:4:8"]]
- 00ae1af0 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae1b34 ["INT_ADD", "register:40f0:8", ["const:ae1b34:8", "const:4:8"]]
+ 00ae1b34 ["CALL", null, ["callee:00551e14:8"]]
- 00ae1af0 bytes c9c0e997
+ 00ae1b34 bytes b8c0e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c095a119c5e6d769ed8fc32cfb11a5b"></a>

### [`00ae2ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2ef0.md) → [`00ae2f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2f34.md) _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHand

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddef0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00bddf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf40.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae2f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2ef0.md#insn-00ae2f10) · [`00ae2f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2ef0.md#insn-00ae2f24) · [`00ae2f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2ef0.md#insn-00ae2f38)
- 新版 `00ae2f54`（命令位置の公開資料なし） · `00ae2f68`（命令位置の公開資料なし） · `00ae2f7c`（命令位置の公開資料なし）

~~~diff
- 00ae2f10 ["INT_ADD", "register:40f0:8", ["const:ae2f10:8", "const:4:8"]]
- 00ae2f10 ["CALL", null, ["callee:00bdde10:8"]]
+ 00ae2f54 ["INT_ADD", "register:40f0:8", ["const:ae2f54:8", "const:4:8"]]
+ 00ae2f54 ["CALL", null, ["callee:00bdde10:8"]]
- 00ae2f10 bytes aceb0394
+ 00ae2f54 bytes afeb0394
- 00ae2f24 ["INT_ADD", "register:40f0:8", ["const:ae2f24:8", "const:4:8"]]
- 00ae2f24 ["CALL", null, ["callee:00bddf80:8"]]
+ 00ae2f68 ["INT_ADD", "register:40f0:8", ["const:ae2f68:8", "const:4:8"]]
+ 00ae2f68 ["CALL", null, ["callee:00bddf80:8"]]
- 00ae2f24 bytes 03ec0394
+ 00ae2f68 bytes 06ec0394
- 00ae2f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae2f38 ["INT_ADD", "register:40f0:8", ["const:ae2f38:8", "const:4:8"]]
- 00ae2f38 ["CALLIND", null, ["register:0:8"]]
+ 00ae2f7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae2f7c ["INT_ADD", "register:40f0:8", ["const:ae2f7c:8", "const:4:8"]]
+ 00ae2f7c ["CALLIND", null, ["register:0:8"]]
- 00ae2f38 bytes 00013fd6
+ 00ae2f7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-762151b2a17ca60cd84f527ffe081482"></a>

### [`00ae31b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae31b8.md) → [`00ae31fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae31fc.md) _ZN8firebase6FutureIlEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00bddf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf50.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae31d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae31b8.md#insn-00ae31d8) · [`00ae31ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae31b8.md#insn-00ae31ec) · [`00ae3200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae31b8.md#insn-00ae3200)
- 新版 `00ae321c`（命令位置の公開資料なし） · `00ae3230`（命令位置の公開資料なし） · `00ae3244`（命令位置の公開資料なし）

~~~diff
- 00ae31d8 ["INT_ADD", "register:40f0:8", ["const:ae31d8:8", "const:4:8"]]
- 00ae31d8 ["CALL", null, ["callee:00bdde10:8"]]
+ 00ae321c ["INT_ADD", "register:40f0:8", ["const:ae321c:8", "const:4:8"]]
+ 00ae321c ["CALL", null, ["callee:00bdde10:8"]]
- 00ae31d8 bytes faea0394
+ 00ae321c bytes fdea0394
- 00ae31ec ["INT_ADD", "register:40f0:8", ["const:ae31ec:8", "const:4:8"]]
- 00ae31ec ["CALL", null, ["callee:00bddf80:8"]]
+ 00ae3230 ["INT_ADD", "register:40f0:8", ["const:ae3230:8", "const:4:8"]]
+ 00ae3230 ["CALL", null, ["callee:00bddf80:8"]]
- 00ae31ec bytes 51eb0394
+ 00ae3230 bytes 54eb0394
- 00ae3200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae3200 ["INT_ADD", "register:40f0:8", ["const:ae3200:8", "const:4:8"]]
- 00ae3200 ["CALLIND", null, ["register:0:8"]]
+ 00ae3244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae3244 ["INT_ADD", "register:40f0:8", ["const:ae3244:8", "const:4:8"]]
+ 00ae3244 ["CALLIND", null, ["register:0:8"]]
- 00ae3200 bytes 00013fd6
+ 00ae3244 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca43ff8777b7e86484c1eba6f2422457"></a>

### [`00ae3694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md) → [`00ae36d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae36d8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)
- 新版 呼出元 1件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md#insn-00ae3708) · [`00ae373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md#insn-00ae373c)
- 新版 `00ae374c`（命令位置の公開資料なし） · `00ae3780`（命令位置の公開資料なし）

~~~diff
- 00ae3708 ["INT_ADD", "register:40f0:8", ["const:ae3708:8", "const:4:8"]]
- 00ae3708 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00ae374c ["INT_ADD", "register:40f0:8", ["const:ae374c:8", "const:4:8"]]
+ 00ae374c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00ae3708 bytes 66de0394
+ 00ae374c bytes 69de0394
- 00ae373c ["INT_ADD", "register:40f0:8", ["const:ae373c:8", "const:4:8"]]
- 00ae373c ["CALL", null, ["callee:00bde220:8"]]
+ 00ae3780 ["INT_ADD", "register:40f0:8", ["const:ae3780:8", "const:4:8"]]
+ 00ae3780 ["CALL", null, ["callee:00bde220:8"]]
- 00ae373c bytes a5ea0394
+ 00ae3780 bytes a8ea0394
~~~


<a id="compare-8b87208ac3f732512e5aa6be4d0c2f2b"></a>

### [`00ae375c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md) → [`00ae37a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae37a0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde210.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae37fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md#insn-00ae37fc) · [`00ae3814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md#insn-00ae3814) · [`00ae3828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md#insn-00ae3828)
- 新版 `00ae3840`（命令位置の公開資料なし） · `00ae3858`（命令位置の公開資料なし） · `00ae386c`（命令位置の公開資料なし）

~~~diff
- 00ae37fc ["INT_ADD", "register:40f0:8", ["const:ae37fc:8", "const:4:8"]]
- 00ae37fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00ae3840 ["INT_ADD", "register:40f0:8", ["const:ae3840:8", "const:4:8"]]
+ 00ae3840 ["CALL", null, ["callee:00bdb040:8"]]
- 00ae37fc bytes fddd0394
+ 00ae3840 bytes 00de0394
- 00ae3814 ["INT_ADD", "register:40f0:8", ["const:ae3814:8", "const:4:8"]]
- 00ae3814 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ae3858 ["INT_ADD", "register:40f0:8", ["const:ae3858:8", "const:4:8"]]
+ 00ae3858 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ae3814 bytes 53de0394
+ 00ae3858 bytes 56de0394
- 00ae3828 ["INT_ADD", "register:40f0:8", ["const:ae3828:8", "const:4:8"]]
- 00ae3828 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ae386c ["INT_ADD", "register:40f0:8", ["const:ae386c:8", "const:4:8"]]
+ 00ae386c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ae3828 bytes 4ede0394
+ 00ae386c bytes 51de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f47ba1e931cf73045903e496b71b5838"></a>

### [`00ae3894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md) → [`00ae38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae38d8.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)
- 新版 呼出元 1件 [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae38bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md#insn-00ae38bc) · [`00ae38d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md#insn-00ae38d4) · [`00ae38e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md#insn-00ae38e8)
- 新版 `00ae3900`（命令位置の公開資料なし） · `00ae3918`（命令位置の公開資料なし） · `00ae392c`（命令位置の公開資料なし）

~~~diff
- 00ae38bc ["INT_ADD", "register:40f0:8", ["const:ae38bc:8", "const:4:8"]]
- 00ae38bc ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae3900 ["INT_ADD", "register:40f0:8", ["const:ae3900:8", "const:4:8"]]
+ 00ae3900 ["CALL", null, ["callee:00bddc20:8"]]
- 00ae38bc bytes c5e80394
+ 00ae3900 bytes c8e80394
- 00ae38d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae38d4 ["INT_ADD", "register:40f0:8", ["const:ae38d4:8", "const:4:8"]]
- 00ae38d4 ["CALLIND", null, ["register:0:8"]]
+ 00ae3918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae3918 ["INT_ADD", "register:40f0:8", ["const:ae3918:8", "const:4:8"]]
+ 00ae3918 ["CALLIND", null, ["register:0:8"]]
- 00ae38d4 bytes 00013fd6
+ 00ae3918 bytes 00013fd6
- 00ae38e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae38e8 ["INT_ADD", "register:40f0:8", ["const:ae38e8:8", "const:4:8"]]
- 00ae38e8 ["CALLIND", null, ["register:0:8"]]
+ 00ae392c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae392c ["INT_ADD", "register:40f0:8", ["const:ae392c:8", "const:4:8"]]
+ 00ae392c ["CALLIND", null, ["register:0:8"]]
- 00ae38e8 bytes 00013fd6
+ 00ae392c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149f4a0738fe9929e73c615c107fed0d"></a>

### [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) → [`00ae3e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00ae2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md) [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`00ae2c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md) [`00b4de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4de48.md) [`00b6eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md#insn-00ae3de8)
- 新版 `00ae3e2c`（命令位置の公開資料なし）

~~~diff
- 00ae3de8 ["INT_ADD", "register:40f0:8", ["const:ae3de8:8", "const:4:8"]]
- 00ae3de8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00ae3e2c ["INT_ADD", "register:40f0:8", ["const:ae3e2c:8", "const:4:8"]]
+ 00ae3e2c ["CALL", null, ["callee:00bdb060:8"]]
- 00ae3de8 bytes 8adc0394
+ 00ae3e2c bytes 8ddc0394
~~~


<a id="compare-5344ebae8703d17fc6ae2d0f7d0449a3"></a>

### [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) → [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) FUN_00ae3f74

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00ae3f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md) [`00ae445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae445c.md) [`00ae4488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md) · 呼出先 2件 [`00ae44d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 3件 [`00ae3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md) [`00ae44a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44a0.md) [`00ae44cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md) · 呼出先 2件 [`00ae4514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md#insn-00ae3f44) · [`00ae3f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md#insn-00ae3f5c)
- 新版 `00ae3f88`（命令位置の公開資料なし） · `00ae3fa0`（命令位置の公開資料なし）

~~~diff
- 00ae3f44 ["INT_ADD", "register:40f0:8", ["const:ae3f44:8", "const:4:8"]]
- 00ae3f44 ["CALL", null, ["callee:00ae4514:8"]]
+ 00ae3f88 ["INT_ADD", "register:40f0:8", ["const:ae3f88:8", "const:4:8"]]
+ 00ae3f88 ["CALL", null, ["callee:00ae4514:8"]]
- 00ae3f44 bytes 63010094
+ 00ae3f88 bytes 63010094
- 00ae3f5c ["INT_ADD", "register:40f0:8", ["const:ae3f5c:8", "const:4:8"]]
- 00ae3f5c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00ae3fa0 ["INT_ADD", "register:40f0:8", ["const:ae3fa0:8", "const:4:8"]]
+ 00ae3fa0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00ae3f5c bytes c5e80394
+ 00ae3fa0 bytes c8e80394
~~~


<a id="compare-2ecbbf655e8a9f38951ef5e9f8237f54"></a>

### [`00ae4094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4094.md) → [`00ae40d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae40d8.md) _ZN8firebase8LogDebugEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae4110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4094.md#insn-00ae4110) · [`00ae4134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4094.md#insn-00ae4134)
- 新版 `00ae4154`（命令位置の公開資料なし） · `00ae4178`（命令位置の公開資料なし）

~~~diff
- 00ae4110 ["INT_ADD", "register:40f0:8", ["const:ae4110:8", "const:4:8"]]
- 00ae4110 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae4154 ["INT_ADD", "register:40f0:8", ["const:ae4154:8", "const:4:8"]]
+ 00ae4154 ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae4110 bytes 50e80394
+ 00ae4154 bytes 53e80394
- 00ae4134 ["INT_ADD", "register:40f0:8", ["const:ae4134:8", "const:4:8"]]
- 00ae4134 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae4178 ["INT_ADD", "register:40f0:8", ["const:ae4178:8", "const:4:8"]]
+ 00ae4178 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae4134 bytes c3db0394
+ 00ae4178 bytes c6db0394
~~~


<a id="compare-dcc4aaafcde702d93e62a36f45b9dbcc"></a>

### [`00ae4138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4138.md) → [`00ae417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae417c.md) _ZN8firebase7LogInfoEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde110.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bde160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde160.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae41b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4138.md#insn-00ae41b4) · [`00ae41d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4138.md#insn-00ae41d8)
- 新版 `00ae41f8`（命令位置の公開資料なし） · `00ae421c`（命令位置の公開資料なし）

~~~diff
- 00ae41b4 ["INT_ADD", "register:40f0:8", ["const:ae41b4:8", "const:4:8"]]
- 00ae41b4 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae41f8 ["INT_ADD", "register:40f0:8", ["const:ae41f8:8", "const:4:8"]]
+ 00ae41f8 ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae41b4 bytes 27e80394
+ 00ae41f8 bytes 2ae80394
- 00ae41d8 ["INT_ADD", "register:40f0:8", ["const:ae41d8:8", "const:4:8"]]
- 00ae41d8 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae421c ["INT_ADD", "register:40f0:8", ["const:ae421c:8", "const:4:8"]]
+ 00ae421c ["CALL", null, ["callee:00bdb090:8"]]
- 00ae41d8 bytes 9adb0394
+ 00ae421c bytes 9ddb0394
~~~


<a id="compare-06a9d60011b119ff3d7328e71a443dc8"></a>

### [`00ae41dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae41dc.md) → [`00ae4220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4220.md) _ZN8firebase10LogWarningEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae4258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae41dc.md#insn-00ae4258) · [`00ae427c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae41dc.md#insn-00ae427c)
- 新版 `00ae429c`（命令位置の公開資料なし） · `00ae42c0`（命令位置の公開資料なし）

~~~diff
- 00ae4258 ["INT_ADD", "register:40f0:8", ["const:ae4258:8", "const:4:8"]]
- 00ae4258 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae429c ["INT_ADD", "register:40f0:8", ["const:ae429c:8", "const:4:8"]]
+ 00ae429c ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae4258 bytes fee70394
+ 00ae429c bytes 01e80394
- 00ae427c ["INT_ADD", "register:40f0:8", ["const:ae427c:8", "const:4:8"]]
- 00ae427c ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae42c0 ["INT_ADD", "register:40f0:8", ["const:ae42c0:8", "const:4:8"]]
+ 00ae42c0 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae427c bytes 71db0394
+ 00ae42c0 bytes 74db0394
~~~


<a id="compare-275657848d0ec9550c6b0e52977405b5"></a>

### [`00ae4280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4280.md) → [`00ae42c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae42c4.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae42fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4280.md#insn-00ae42fc) · [`00ae4320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4280.md#insn-00ae4320)
- 新版 `00ae4340`（命令位置の公開資料なし） · `00ae4364`（命令位置の公開資料なし）

~~~diff
- 00ae42fc ["INT_ADD", "register:40f0:8", ["const:ae42fc:8", "const:4:8"]]
- 00ae42fc ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae4340 ["INT_ADD", "register:40f0:8", ["const:ae4340:8", "const:4:8"]]
+ 00ae4340 ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae42fc bytes d5e70394
+ 00ae4340 bytes d8e70394
- 00ae4320 ["INT_ADD", "register:40f0:8", ["const:ae4320:8", "const:4:8"]]
- 00ae4320 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae4364 ["INT_ADD", "register:40f0:8", ["const:ae4364:8", "const:4:8"]]
+ 00ae4364 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae4320 bytes 48db0394
+ 00ae4364 bytes 4bdb0394
~~~


<a id="compare-d76c6064e7ab07d66777a49e99c50081"></a>

### [`00ae4324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4324.md) → [`00ae4368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4368.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae43a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4324.md#insn-00ae43a0) · [`00ae43c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4324.md#insn-00ae43c4)
- 新版 `00ae43e4`（命令位置の公開資料なし） · `00ae4408`（命令位置の公開資料なし）

~~~diff
- 00ae43a0 ["INT_ADD", "register:40f0:8", ["const:ae43a0:8", "const:4:8"]]
- 00ae43a0 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae43e4 ["INT_ADD", "register:40f0:8", ["const:ae43e4:8", "const:4:8"]]
+ 00ae43e4 ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae43a0 bytes ace70394
+ 00ae43e4 bytes afe70394
- 00ae43c4 ["INT_ADD", "register:40f0:8", ["const:ae43c4:8", "const:4:8"]]
- 00ae43c4 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae4408 ["INT_ADD", "register:40f0:8", ["const:ae4408:8", "const:4:8"]]
+ 00ae4408 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae43c4 bytes 1fdb0394
+ 00ae4408 bytes 22db0394
~~~


<a id="compare-09eccf6ee4df177e700d013cdf4c6c9b"></a>

### [`00ae43c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae43c8.md) → [`00ae440c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae440c.md) _ZN8firebase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)
- 新版 呼出元 1件 [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae4434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae43c8.md#insn-00ae4434) · [`00ae4458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae43c8.md#insn-00ae4458)
- 新版 `00ae4478`（命令位置の公開資料なし） · `00ae449c`（命令位置の公開資料なし）

~~~diff
- 00ae4434 ["INT_ADD", "register:40f0:8", ["const:ae4434:8", "const:4:8"]]
- 00ae4434 ["CALL", null, ["callee:00bde2a0:8"]]
+ 00ae4478 ["INT_ADD", "register:40f0:8", ["const:ae4478:8", "const:4:8"]]
+ 00ae4478 ["CALL", null, ["callee:00bde2a0:8"]]
- 00ae4434 bytes 87e70394
+ 00ae4478 bytes 8ae70394
- 00ae4458 ["INT_ADD", "register:40f0:8", ["const:ae4458:8", "const:4:8"]]
- 00ae4458 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae449c ["INT_ADD", "register:40f0:8", ["const:ae449c:8", "const:4:8"]]
+ 00ae449c ["CALL", null, ["callee:00bdb090:8"]]
- 00ae4458 bytes fada0394
+ 00ae449c bytes fdda0394
~~~


<a id="compare-061d447edf425feacb5c0fec8037dc43"></a>

### [`00ae45b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae45b0.md) → [`00ae45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae45f4.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae45d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae45b0.md#insn-00ae45d8) · [`00ae45fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae45b0.md#insn-00ae45fc)
- 新版 `00ae461c`（命令位置の公開資料なし） · `00ae4640`（命令位置の公開資料なし）

~~~diff
- 00ae45d8 ["INT_ADD", "register:40f0:8", ["const:ae45d8:8", "const:4:8"]]
- 00ae45d8 ["CALL", null, ["callee:00bde370:8"]]
+ 00ae461c ["INT_ADD", "register:40f0:8", ["const:ae461c:8", "const:4:8"]]
+ 00ae461c ["CALL", null, ["callee:00bde370:8"]]
- 00ae45d8 bytes 52e70394
+ 00ae461c bytes 55e70394
- 00ae45fc ["INT_ADD", "register:40f0:8", ["const:ae45fc:8", "const:4:8"]]
- 00ae45fc ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae4640 ["INT_ADD", "register:40f0:8", ["const:ae4640:8", "const:4:8"]]
+ 00ae4640 ["CALL", null, ["callee:00bdb090:8"]]
- 00ae45fc bytes 91da0394
+ 00ae4640 bytes 94da0394
~~~


<a id="compare-6ee3c908009f4fc8bd872165a186a694"></a>

### [`00ae49e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae49e8.md) → [`00ae4a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a2c.md) _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae4a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae49e8.md#insn-00ae4a00) · [`00ae4a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae49e8.md#insn-00ae4a18) · [`00ae4a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae49e8.md#insn-00ae4a28)
- 新版 `00ae4a44`（命令位置の公開資料なし） · `00ae4a5c`（命令位置の公開資料なし） · `00ae4a6c`（命令位置の公開資料なし）

~~~diff
- 00ae4a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4a00 ["INT_ADD", "register:40f0:8", ["const:ae4a00:8", "const:4:8"]]
- 00ae4a00 ["CALLIND", null, ["register:0:8"]]
+ 00ae4a44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4a44 ["INT_ADD", "register:40f0:8", ["const:ae4a44:8", "const:4:8"]]
+ 00ae4a44 ["CALLIND", null, ["register:0:8"]]
- 00ae4a00 bytes 00013fd6
+ 00ae4a44 bytes 00013fd6
- 00ae4a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4a18 ["INT_ADD", "register:40f0:8", ["const:ae4a18:8", "const:4:8"]]
- 00ae4a18 ["CALLIND", null, ["register:0:8"]]
+ 00ae4a5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4a5c ["INT_ADD", "register:40f0:8", ["const:ae4a5c:8", "const:4:8"]]
+ 00ae4a5c ["CALLIND", null, ["register:0:8"]]
- 00ae4a18 bytes 00013fd6
+ 00ae4a5c bytes 00013fd6
- 00ae4a28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4a28 ["INT_ADD", "register:40f0:8", ["const:ae4a28:8", "const:4:8"]]
- 00ae4a28 ["CALLIND", null, ["register:0:8"]]
+ 00ae4a6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4a6c ["INT_ADD", "register:40f0:8", ["const:ae4a6c:8", "const:4:8"]]
+ 00ae4a6c ["CALLIND", null, ["register:0:8"]]
- 00ae4a28 bytes 00013fd6
+ 00ae4a6c bytes 00013fd6
~~~


<a id="compare-90628430a8bd9a396a6fcbf41d1a0c47"></a>

### [`00af1514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1514.md) → [`00af1558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af1558.md) _ZN7_JNIEnv20CallStaticVoidMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bde3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3c0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af1588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1514.md#insn-00af1588) · [`00af15ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1514.md#insn-00af15ac)
- 新版 `00af15cc`（命令位置の公開資料なし） · `00af15f0`（命令位置の公開資料なし）

~~~diff
- 00af1588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1588 ["INT_ADD", "register:40f0:8", ["const:af1588:8", "const:4:8"]]
- 00af1588 ["CALLIND", null, ["register:0:8"]]
+ 00af15cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af15cc ["INT_ADD", "register:40f0:8", ["const:af15cc:8", "const:4:8"]]
+ 00af15cc ["CALLIND", null, ["register:0:8"]]
- 00af1588 bytes 00013fd6
+ 00af15cc bytes 00013fd6
- 00af15ac ["INT_ADD", "register:40f0:8", ["const:af15ac:8", "const:4:8"]]
- 00af15ac ["CALL", null, ["callee:00bdb090:8"]]
+ 00af15f0 ["INT_ADD", "register:40f0:8", ["const:af15f0:8", "const:4:8"]]
+ 00af15f0 ["CALL", null, ["callee:00bdb090:8"]]
- 00af15ac bytes a5a60394
+ 00af15f0 bytes a8a60394
~~~


<a id="compare-c4bccde40b1c7e7d88d01e9ae15f3539"></a>

### [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) → [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) FUN_00af15f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00ae4b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md) [`00ae4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md)
- 新版 呼出元 2件 [`00ae4b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md) [`00ae4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md#insn-00af1620) · [`00af1644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md#insn-00af1644)
- 新版 `00af1664`（命令位置の公開資料なし） · `00af1688`（命令位置の公開資料なし）

~~~diff
- 00af1620 ["INT_ADD", "register:40f0:8", ["const:af1620:8", "const:4:8"]]
- 00af1620 ["CALL", null, ["callee:00bde2d0:8"]]
+ 00af1664 ["INT_ADD", "register:40f0:8", ["const:af1664:8", "const:4:8"]]
+ 00af1664 ["CALL", null, ["callee:00bde2d0:8"]]
- 00af1620 bytes 18b30394
+ 00af1664 bytes 1bb30394
- 00af1644 ["INT_ADD", "register:40f0:8", ["const:af1644:8", "const:4:8"]]
- 00af1644 ["CALL", null, ["callee:00bdb090:8"]]
+ 00af1688 ["INT_ADD", "register:40f0:8", ["const:af1688:8", "const:4:8"]]
+ 00af1688 ["CALL", null, ["callee:00bdb090:8"]]
- 00af1644 bytes 7fa60394
+ 00af1688 bytes 82a60394
~~~


<a id="compare-b370fbeee77e1346f7892f45998fa022"></a>

### [`00af315c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af315c.md) → [`00af31a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af31a0.md) _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md) · 呼出先 1件 [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md)
- 新版 呼出元 1件 [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md) · 呼出先 1件 [`00bde0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af315c.md#insn-00af3170)
- 新版 `00af31b4`（命令位置の公開資料なし）

~~~diff
- 00af3170 ["INT_ADD", "register:40f0:8", ["const:af3170:8", "const:4:8"]]
- 00af3170 ["CALL", null, ["callee:00bde0a0:8"]]
+ 00af31b4 ["INT_ADD", "register:40f0:8", ["const:af31b4:8", "const:4:8"]]
+ 00af31b4 ["CALL", null, ["callee:00bde0a0:8"]]
- 00af3170 bytes b8ab0394
+ 00af31b4 bytes bbab0394
~~~


<a id="compare-86f71d8082e5ff25ed90b446c9bf568e"></a>

### [`00af3450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md) → [`00af3494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af3/00af3494.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bddd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd50.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af34ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af34ac) · [`00af3524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af3524) · [`00af355c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af355c)
- 新版 `00af34f0`（命令位置の公開資料なし） · `00af3568`（命令位置の公開資料なし） · `00af35a0`（命令位置の公開資料なし）

~~~diff
- 00af34ac ["INT_ADD", "register:40f0:8", ["const:af34ac:8", "const:4:8"]]
- 00af34ac ["CALL", null, ["callee:00bdb040:8"]]
+ 00af34f0 ["INT_ADD", "register:40f0:8", ["const:af34f0:8", "const:4:8"]]
+ 00af34f0 ["CALL", null, ["callee:00bdb040:8"]]
- 00af34ac bytes d19e0394
+ 00af34f0 bytes d49e0394
- 00af3524 ["INT_ADD", "register:40f0:8", ["const:af3524:8", "const:4:8"]]
- 00af3524 ["CALL", null, ["callee:00bdb060:8"]]
+ 00af3568 ["INT_ADD", "register:40f0:8", ["const:af3568:8", "const:4:8"]]
+ 00af3568 ["CALL", null, ["callee:00bdb060:8"]]
- 00af3524 bytes bb9e0394
+ 00af3568 bytes be9e0394
- 00af355c ["INT_ADD", "register:40f0:8", ["const:af355c:8", "const:4:8"]]
- 00af355c ["CALL", null, ["callee:00bde2c0:8"]]
+ 00af35a0 ["INT_ADD", "register:40f0:8", ["const:af35a0:8", "const:4:8"]]
+ 00af35a0 ["CALL", null, ["callee:00bde2c0:8"]]
- 00af355c bytes 45ab0394
+ 00af35a0 bytes 48ab0394
~~~


