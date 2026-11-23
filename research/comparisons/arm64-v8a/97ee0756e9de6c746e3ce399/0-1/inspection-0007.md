# v15.7.2 → v15.7.3 · 要調査の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-97b3cd5cf521d363a94309b6635e0d33"></a>

### [`00bbf0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf0e8.md) → [`00bbf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md) FUN_00bbf1b0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 2件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbf184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf0e8.md#insn-00bbf184) · [`00bbf200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf0e8.md#insn-00bbf200) · [`00bbf220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf0e8.md#insn-00bbf220)
- 新版 [`00bbf24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf24c) · [`00bbf2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf2c8) · [`00bbf2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md#insn-00bbf2e8)

~~~diff
- 00bbf184 ["INT_ADD", "register:40f0:8", ["const:bbf184:8", "const:4:8"]]
- 00bbf184 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00bbf24c ["INT_ADD", "register:40f0:8", ["const:bbf24c:8", "const:4:8"]]
+ 00bbf24c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00bbf184 bytes 9b6f0094
+ 00bbf24c bytes 956f0094
- 00bbf200 ["INT_ADD", "register:40f0:8", ["const:bbf200:8", "const:4:8"]]
- 00bbf200 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bbf2c8 ["INT_ADD", "register:40f0:8", ["const:bbf2c8:8", "const:4:8"]]
+ 00bbf2c8 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bbf200 bytes 44710094
+ 00bbf2c8 bytes 3e710094
- 00bbf220 ["INT_ADD", "register:40f0:8", ["const:bbf220:8", "const:4:8"]]
- 00bbf220 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00bbf2e8 ["INT_ADD", "register:40f0:8", ["const:bbf2e8:8", "const:4:8"]]
+ 00bbf2e8 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00bbf220 bytes 746f0094
+ 00bbf2e8 bytes 6e6f0094
~~~


<a id="compare-bced895da71b3b1dc634f2a3b8218d21"></a>

### [`00bbfcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md) → [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) FUN_00bbfdb4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbfd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md#insn-00bbfd34) · [`00bbfd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md#insn-00bbfd48) · [`00bbfd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md#insn-00bbfd50)
- 新版 [`00bbfdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfdfc) · [`00bbfe10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfe10) · [`00bbfe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md#insn-00bbfe18)

~~~diff
- 00bbfd34 ["INT_ADD", "register:40f0:8", ["const:bbfd34:8", "const:4:8"]]
- 00bbfd34 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bbfdfc ["INT_ADD", "register:40f0:8", ["const:bbfdfc:8", "const:4:8"]]
+ 00bbfdfc ["CALL", null, ["callee:00bdd200:8"]]
- 00bbfd34 bytes 07750094
+ 00bbfdfc bytes 01750094
- 00bbfd48 ["INT_ADD", "register:40f0:8", ["const:bbfd48:8", "const:4:8"]]
- 00bbfd48 ["CALL", null, ["callee:00bde270:8"]]
+ 00bbfe10 ["INT_ADD", "register:40f0:8", ["const:bbfe10:8", "const:4:8"]]
+ 00bbfe10 ["CALL", null, ["callee:00bde270:8"]]
- 00bbfd48 bytes 1e790094
+ 00bbfe10 bytes 18790094
- 00bbfd50 ["INT_ADD", "register:40f0:8", ["const:bbfd50:8", "const:4:8"]]
- 00bbfd50 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bbfe18 ["INT_ADD", "register:40f0:8", ["const:bbfe18:8", "const:4:8"]]
+ 00bbfe18 ["CALL", null, ["callee:00bdd180:8"]]
- 00bbfd50 bytes e0740094
+ 00bbfe18 bytes da740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5421dc89327a432d95fbf4f0d1d45ab"></a>

### [`00bc00b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc00b4.md) → [`00bc017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md) FUN_00bc017c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 2件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc0128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc00b4.md#insn-00bc0128) · [`00bc0150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc00b4.md#insn-00bc0150) · [`00bc01e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc00b4.md#insn-00bc01e4)
- 新版 [`00bc01f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc01f0) · [`00bc0218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc0218) · [`00bc02ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md#insn-00bc02ac)

~~~diff
- 00bc0128 ["INT_ADD", "register:40f0:8", ["const:bc0128:8", "const:4:8"]]
- 00bc0128 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bc01f0 ["INT_ADD", "register:40f0:8", ["const:bc01f0:8", "const:4:8"]]
+ 00bc01f0 ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bc0128 bytes 7a6d0094
+ 00bc01f0 bytes 746d0094
- 00bc0150 ["INT_ADD", "register:40f0:8", ["const:bc0150:8", "const:4:8"]]
- 00bc0150 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00bc0218 ["INT_ADD", "register:40f0:8", ["const:bc0218:8", "const:4:8"]]
+ 00bc0218 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00bc0150 bytes a86b0094
+ 00bc0218 bytes a26b0094
- 00bc01e4 ["INT_ADD", "register:40f0:8", ["const:bc01e4:8", "const:4:8"]]
- 00bc01e4 ["CALL", null, ["callee:00bdb7c0:8"]]
+ 00bc02ac ["INT_ADD", "register:40f0:8", ["const:bc02ac:8", "const:4:8"]]
+ 00bc02ac ["CALL", null, ["callee:00bdb7c0:8"]]
- 00bc01e4 bytes 4b6d0094
+ 00bc02ac bytes 456d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26e9db9e361aac1db831ef3559ee144"></a>

### [`00bc0db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0db4.md) → [`00bc0e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md) FUN_00bc0e7c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc0e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0db4.md#insn-00bc0e04) · [`00bc0e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0db4.md#insn-00bc0e20) · [`00bc0e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0db4.md#insn-00bc0e44)
- 新版 [`00bc0ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0ecc) · [`00bc0ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0ee8) · [`00bc0f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0e7c.md#insn-00bc0f0c)

~~~diff
- 00bc0e04 ["INT_ADD", "register:40f0:8", ["const:bc0e04:8", "const:4:8"]]
- 00bc0e04 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc0ecc ["INT_ADD", "register:40f0:8", ["const:bc0ecc:8", "const:4:8"]]
+ 00bc0ecc ["CALL", null, ["callee:00bdd200:8"]]
- 00bc0e04 bytes d3700094
+ 00bc0ecc bytes cd700094
- 00bc0e20 ["INT_ADD", "register:40f0:8", ["const:bc0e20:8", "const:4:8"]]
- 00bc0e20 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc0ee8 ["INT_ADD", "register:40f0:8", ["const:bc0ee8:8", "const:4:8"]]
+ 00bc0ee8 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc0e20 bytes a4680094
+ 00bc0ee8 bytes 9e680094
- 00bc0e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc0e44 ["INT_ADD", "register:40f0:8", ["const:bc0e44:8", "const:4:8"]]
- 00bc0e44 ["CALLIND", null, ["register:0:8"]]
+ 00bc0f0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc0f0c ["INT_ADD", "register:40f0:8", ["const:bc0f0c:8", "const:4:8"]]
+ 00bc0f0c ["CALLIND", null, ["register:0:8"]]
- 00bc0e44 bytes 00013fd6
+ 00bc0f0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72693887cb4dec45cb8d9012fbdd4d5a"></a>

### [`00bc1300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1300.md) → [`00bc13c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md) FUN_00bc13c8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc1350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1300.md#insn-00bc1350) · [`00bc136c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1300.md#insn-00bc136c) · [`00bc1390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1300.md#insn-00bc1390)
- 新版 [`00bc1418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1418) · [`00bc1434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1434) · [`00bc1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc13c8.md#insn-00bc1458)

~~~diff
- 00bc1350 ["INT_ADD", "register:40f0:8", ["const:bc1350:8", "const:4:8"]]
- 00bc1350 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc1418 ["INT_ADD", "register:40f0:8", ["const:bc1418:8", "const:4:8"]]
+ 00bc1418 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc1350 bytes 806f0094
+ 00bc1418 bytes 7a6f0094
- 00bc136c ["INT_ADD", "register:40f0:8", ["const:bc136c:8", "const:4:8"]]
- 00bc136c ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc1434 ["INT_ADD", "register:40f0:8", ["const:bc1434:8", "const:4:8"]]
+ 00bc1434 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc136c bytes 51670094
+ 00bc1434 bytes 4b670094
- 00bc1390 ["INT_ADD", "register:40f0:8", ["const:bc1390:8", "const:4:8"]]
- 00bc1390 ["CALL", null, ["callee:00bde270:8"]]
+ 00bc1458 ["INT_ADD", "register:40f0:8", ["const:bc1458:8", "const:4:8"]]
+ 00bc1458 ["CALL", null, ["callee:00bde270:8"]]
- 00bc1390 bytes 8c730094
+ 00bc1458 bytes 86730094
~~~


<a id="compare-63aeda4195003195dd22e20a596ecde1"></a>

### [`00bc13ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc13ac.md) → [`00bc1474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md) FUN_00bc1474

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc13e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc13ac.md#insn-00bc13e0) · [`00bc1404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc13ac.md#insn-00bc1404) · [`00bc1450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc13ac.md#insn-00bc1450)
- 新版 [`00bc14a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc14a8) · [`00bc14cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc14cc) · [`00bc1518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1474.md#insn-00bc1518)

~~~diff
- 00bc13e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc13e0 ["INT_ADD", "register:40f0:8", ["const:bc13e0:8", "const:4:8"]]
- 00bc13e0 ["CALLIND", null, ["register:0:8"]]
+ 00bc14a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc14a8 ["INT_ADD", "register:40f0:8", ["const:bc14a8:8", "const:4:8"]]
+ 00bc14a8 ["CALLIND", null, ["register:0:8"]]
- 00bc13e0 bytes 00013fd6
+ 00bc14a8 bytes 00013fd6
- 00bc1404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1404 ["INT_ADD", "register:40f0:8", ["const:bc1404:8", "const:4:8"]]
- 00bc1404 ["CALLIND", null, ["register:0:8"]]
+ 00bc14cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc14cc ["INT_ADD", "register:40f0:8", ["const:bc14cc:8", "const:4:8"]]
+ 00bc14cc ["CALLIND", null, ["register:0:8"]]
- 00bc1404 bytes 00013fd6
+ 00bc14cc bytes 00013fd6
- 00bc1450 ["INT_ADD", "register:40f0:8", ["const:bc1450:8", "const:4:8"]]
- 00bc1450 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc1518 ["INT_ADD", "register:40f0:8", ["const:bc1518:8", "const:4:8"]]
+ 00bc1518 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc1450 bytes 406f0094
+ 00bc1518 bytes 3a6f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e6db59a8ddf89d0b4abda4077543ae2"></a>

### [`00bc29f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md) → [`00bc2abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md) FUN_00bc2abc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bc1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) · 呼出先 4件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md#insn-00bc2a3c) · [`00bc2a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md#insn-00bc2a50) · [`00bc2a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md#insn-00bc2a58)
- 新版 [`00bc2b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b04) · [`00bc2b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b18) · [`00bc2b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md#insn-00bc2b20)

~~~diff
- 00bc2a3c ["INT_ADD", "register:40f0:8", ["const:bc2a3c:8", "const:4:8"]]
- 00bc2a3c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc2b04 ["INT_ADD", "register:40f0:8", ["const:bc2b04:8", "const:4:8"]]
+ 00bc2b04 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc2a3c bytes c5690094
+ 00bc2b04 bytes bf690094
- 00bc2a50 ["INT_ADD", "register:40f0:8", ["const:bc2a50:8", "const:4:8"]]
- 00bc2a50 ["CALL", null, ["callee:00bde270:8"]]
+ 00bc2b18 ["INT_ADD", "register:40f0:8", ["const:bc2b18:8", "const:4:8"]]
+ 00bc2b18 ["CALL", null, ["callee:00bde270:8"]]
- 00bc2a50 bytes dc6d0094
+ 00bc2b18 bytes d66d0094
- 00bc2a58 ["INT_ADD", "register:40f0:8", ["const:bc2a58:8", "const:4:8"]]
- 00bc2a58 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc2b20 ["INT_ADD", "register:40f0:8", ["const:bc2b20:8", "const:4:8"]]
+ 00bc2b20 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc2a58 bytes 9e690094
+ 00bc2b20 bytes 98690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817fafaa5023f67079122f200fc7ae17"></a>

### [`00bc2b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2b78.md) → [`00bc2c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2c40.md) FUN_00bc2c40

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2b78.md#insn-00bc2bc4)
- 新版 [`00bc2c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2c40.md#insn-00bc2c8c)

~~~diff
- 00bc2bc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2bc4 ["INT_ADD", "register:40f0:8", ["const:bc2bc4:8", "const:4:8"]]
- 00bc2bc4 ["CALLIND", null, ["register:0:8"]]
+ 00bc2c8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2c8c ["INT_ADD", "register:40f0:8", ["const:bc2c8c:8", "const:4:8"]]
+ 00bc2c8c ["CALLIND", null, ["register:0:8"]]
- 00bc2bc4 bytes 20013fd6
+ 00bc2c8c bytes 20013fd6
~~~


<a id="compare-538b7f8697dffdfbb9f9e92a59278953"></a>

### [`00bc2bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2bfc.md) → [`00bc2cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2cc4.md) FUN_00bc2cc4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2bfc.md#insn-00bc2c48)
- 新版 [`00bc2d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2cc4.md#insn-00bc2d10)

~~~diff
- 00bc2c48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2c48 ["INT_ADD", "register:40f0:8", ["const:bc2c48:8", "const:4:8"]]
- 00bc2c48 ["CALLIND", null, ["register:0:8"]]
+ 00bc2d10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2d10 ["INT_ADD", "register:40f0:8", ["const:bc2d10:8", "const:4:8"]]
+ 00bc2d10 ["CALLIND", null, ["register:0:8"]]
- 00bc2c48 bytes 20013fd6
+ 00bc2d10 bytes 20013fd6
~~~


<a id="compare-13619e192f49a4d4b6ce15668066c67d"></a>

### [`00bc2c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2c80.md) → [`00bc2d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2d48.md) FUN_00bc2d48

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2c80.md#insn-00bc2ccc)
- 新版 [`00bc2d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2d48.md#insn-00bc2d94)

~~~diff
- 00bc2ccc ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2ccc ["INT_ADD", "register:40f0:8", ["const:bc2ccc:8", "const:4:8"]]
- 00bc2ccc ["CALLIND", null, ["register:0:8"]]
+ 00bc2d94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2d94 ["INT_ADD", "register:40f0:8", ["const:bc2d94:8", "const:4:8"]]
+ 00bc2d94 ["CALLIND", null, ["register:0:8"]]
- 00bc2ccc bytes 20013fd6
+ 00bc2d94 bytes 20013fd6
~~~


<a id="compare-fd24f446d4161325a1d04ce0b936df73"></a>

### [`00bc2d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2d04.md) → [`00bc2dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2dcc.md) FUN_00bc2dcc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2d04.md#insn-00bc2d38)
- 新版 [`00bc2e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2dcc.md#insn-00bc2e00)

~~~diff
- 00bc2d38 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2d38 ["INT_ADD", "register:40f0:8", ["const:bc2d38:8", "const:4:8"]]
- 00bc2d38 ["CALLIND", null, ["register:0:8"]]
+ 00bc2e00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bc2e00 ["INT_ADD", "register:40f0:8", ["const:bc2e00:8", "const:4:8"]]
+ 00bc2e00 ["CALLIND", null, ["register:0:8"]]
- 00bc2d38 bytes 20013fd6
+ 00bc2e00 bytes 20013fd6
~~~


<a id="compare-e94ac651f47dad6dc7839843818c65cc"></a>

### [`00bc2d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2d58.md) → [`00bc2e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e20.md) FUN_00bc2e20

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2d58.md#insn-00bc2d88)
- 新版 [`00bc2e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e20.md#insn-00bc2e50)

~~~diff
- 00bc2d88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2d88 ["INT_ADD", "register:40f0:8", ["const:bc2d88:8", "const:4:8"]]
- 00bc2d88 ["CALLIND", null, ["register:0:8"]]
+ 00bc2e50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2e50 ["INT_ADD", "register:40f0:8", ["const:bc2e50:8", "const:4:8"]]
+ 00bc2e50 ["CALLIND", null, ["register:0:8"]]
- 00bc2d88 bytes 00013fd6
+ 00bc2e50 bytes 00013fd6
~~~


<a id="compare-68ff94fce16f91b8092104cb7422cfa9"></a>

### [`00bc2da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2da8.md) → [`00bc2e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e70.md) FUN_00bc2e70

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2da8.md#insn-00bc2dd8)
- 新版 [`00bc2ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2e70.md#insn-00bc2ea0)

~~~diff
- 00bc2dd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2dd8 ["INT_ADD", "register:40f0:8", ["const:bc2dd8:8", "const:4:8"]]
- 00bc2dd8 ["CALLIND", null, ["register:0:8"]]
+ 00bc2ea0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2ea0 ["INT_ADD", "register:40f0:8", ["const:bc2ea0:8", "const:4:8"]]
+ 00bc2ea0 ["CALLIND", null, ["register:0:8"]]
- 00bc2dd8 bytes 00013fd6
+ 00bc2ea0 bytes 00013fd6
~~~


<a id="compare-7c6577eb05f2dc717773ec88f00eb424"></a>

### [`00bc6e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6e30.md) → [`00bc6ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md) FUN_00bc6ef8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc6ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6e30.md#insn-00bc6ea4) · [`00bc6ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6e30.md#insn-00bc6ec8) · [`00bc6f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6e30.md#insn-00bc6f04)
- 新版 [`00bc6f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6f6c) · [`00bc6f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6f90) · [`00bc6fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6ef8.md#insn-00bc6fcc)

~~~diff
- 00bc6ea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc6ea4 ["INT_ADD", "register:40f0:8", ["const:bc6ea4:8", "const:4:8"]]
- 00bc6ea4 ["CALLIND", null, ["register:0:8"]]
+ 00bc6f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc6f6c ["INT_ADD", "register:40f0:8", ["const:bc6f6c:8", "const:4:8"]]
+ 00bc6f6c ["CALLIND", null, ["register:0:8"]]
- 00bc6ea4 bytes 00013fd6
+ 00bc6f6c bytes 00013fd6
- 00bc6ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc6ec8 ["INT_ADD", "register:40f0:8", ["const:bc6ec8:8", "const:4:8"]]
- 00bc6ec8 ["CALLIND", null, ["register:0:8"]]
+ 00bc6f90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc6f90 ["INT_ADD", "register:40f0:8", ["const:bc6f90:8", "const:4:8"]]
+ 00bc6f90 ["CALLIND", null, ["register:0:8"]]
- 00bc6ec8 bytes 00013fd6
+ 00bc6f90 bytes 00013fd6
- 00bc6f04 ["INT_ADD", "register:40f0:8", ["const:bc6f04:8", "const:4:8"]]
- 00bc6f04 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc6fcc ["INT_ADD", "register:40f0:8", ["const:bc6fcc:8", "const:4:8"]]
+ 00bc6fcc ["CALL", null, ["callee:00bdd200:8"]]
- 00bc6f04 bytes 93580094
+ 00bc6fcc bytes 8d580094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a011d8fea5433d0a5bfcaa106c3773ff"></a>

### [`00bc7404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7404.md) → [`00bc74cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md) FUN_00bc74cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7404.md#insn-00bc7454) · [`00bc7470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7404.md#insn-00bc7470) · [`00bc74ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7404.md#insn-00bc74ac)
- 新版 [`00bc751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc751c) · [`00bc7538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc7538) · [`00bc7574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc74cc.md#insn-00bc7574)

~~~diff
- 00bc7454 ["INT_ADD", "register:40f0:8", ["const:bc7454:8", "const:4:8"]]
- 00bc7454 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc751c ["INT_ADD", "register:40f0:8", ["const:bc751c:8", "const:4:8"]]
+ 00bc751c ["CALL", null, ["callee:00bdd200:8"]]
- 00bc7454 bytes 3f570094
+ 00bc751c bytes 39570094
- 00bc7470 ["INT_ADD", "register:40f0:8", ["const:bc7470:8", "const:4:8"]]
- 00bc7470 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc7538 ["INT_ADD", "register:40f0:8", ["const:bc7538:8", "const:4:8"]]
+ 00bc7538 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc7470 bytes 104f0094
+ 00bc7538 bytes 0a4f0094
- 00bc74ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc74ac ["INT_ADD", "register:40f0:8", ["const:bc74ac:8", "const:4:8"]]
- 00bc74ac ["CALLIND", null, ["register:0:8"]]
+ 00bc7574 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7574 ["INT_ADD", "register:40f0:8", ["const:bc7574:8", "const:4:8"]]
+ 00bc7574 ["CALLIND", null, ["register:0:8"]]
- 00bc74ac bytes 00013fd6
+ 00bc7574 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27b1ea2575532238db04321a0be1fa2"></a>

### [`00bc75ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc75ec.md) → [`00bc76b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md) FUN_00bc76b4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc75ec.md#insn-00bc7638) · [`00bc765c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc75ec.md#insn-00bc765c) · [`00bc76a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc75ec.md#insn-00bc76a0)
- 新版 [`00bc7700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7700) · [`00bc7724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7724) · [`00bc7768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc76b4.md#insn-00bc7768)

~~~diff
- 00bc7638 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7638 ["INT_ADD", "register:40f0:8", ["const:bc7638:8", "const:4:8"]]
- 00bc7638 ["CALLIND", null, ["register:0:8"]]
+ 00bc7700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7700 ["INT_ADD", "register:40f0:8", ["const:bc7700:8", "const:4:8"]]
+ 00bc7700 ["CALLIND", null, ["register:0:8"]]
- 00bc7638 bytes 00013fd6
+ 00bc7700 bytes 00013fd6
- 00bc765c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc765c ["INT_ADD", "register:40f0:8", ["const:bc765c:8", "const:4:8"]]
- 00bc765c ["CALLIND", null, ["register:0:8"]]
+ 00bc7724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7724 ["INT_ADD", "register:40f0:8", ["const:bc7724:8", "const:4:8"]]
+ 00bc7724 ["CALLIND", null, ["register:0:8"]]
- 00bc765c bytes 00013fd6
+ 00bc7724 bytes 00013fd6
- 00bc76a0 ["INT_ADD", "register:40f0:8", ["const:bc76a0:8", "const:4:8"]]
- 00bc76a0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc7768 ["INT_ADD", "register:40f0:8", ["const:bc7768:8", "const:4:8"]]
+ 00bc7768 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc76a0 bytes ac560094
+ 00bc7768 bytes a6560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3fe97cc964eb66a47a83b1e80f27f99"></a>

### [`00bc77d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc77d4.md) → [`00bc789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md) FUN_00bc789c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc781c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc77d4.md#insn-00bc781c) · [`00bc7840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc77d4.md#insn-00bc7840) · [`00bc787c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc77d4.md#insn-00bc787c)
- 新版 [`00bc78e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc78e4) · [`00bc7908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc7908) · [`00bc7944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc789c.md#insn-00bc7944)

~~~diff
- 00bc781c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc781c ["INT_ADD", "register:40f0:8", ["const:bc781c:8", "const:4:8"]]
- 00bc781c ["CALLIND", null, ["register:0:8"]]
+ 00bc78e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc78e4 ["INT_ADD", "register:40f0:8", ["const:bc78e4:8", "const:4:8"]]
+ 00bc78e4 ["CALLIND", null, ["register:0:8"]]
- 00bc781c bytes 00013fd6
+ 00bc78e4 bytes 00013fd6
- 00bc7840 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7840 ["INT_ADD", "register:40f0:8", ["const:bc7840:8", "const:4:8"]]
- 00bc7840 ["CALLIND", null, ["register:0:8"]]
+ 00bc7908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7908 ["INT_ADD", "register:40f0:8", ["const:bc7908:8", "const:4:8"]]
+ 00bc7908 ["CALLIND", null, ["register:0:8"]]
- 00bc7840 bytes 00013fd6
+ 00bc7908 bytes 00013fd6
- 00bc787c ["INT_ADD", "register:40f0:8", ["const:bc787c:8", "const:4:8"]]
- 00bc787c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc7944 ["INT_ADD", "register:40f0:8", ["const:bc7944:8", "const:4:8"]]
+ 00bc7944 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc787c bytes 35560094
+ 00bc7944 bytes 2f560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8bb54e1398f7fb5da5cdb987bb33662"></a>

### [`00bc7b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7b34.md) → [`00bc7bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md) FUN_00bc7bfc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7b34.md#insn-00bc7b80) · [`00bc7ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7b34.md#insn-00bc7ba4) · [`00bc7be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7b34.md#insn-00bc7be8)
- 新版 [`00bc7c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7c48) · [`00bc7c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7c6c) · [`00bc7cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7bfc.md#insn-00bc7cb0)

~~~diff
- 00bc7b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7b80 ["INT_ADD", "register:40f0:8", ["const:bc7b80:8", "const:4:8"]]
- 00bc7b80 ["CALLIND", null, ["register:0:8"]]
+ 00bc7c48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7c48 ["INT_ADD", "register:40f0:8", ["const:bc7c48:8", "const:4:8"]]
+ 00bc7c48 ["CALLIND", null, ["register:0:8"]]
- 00bc7b80 bytes 00013fd6
+ 00bc7c48 bytes 00013fd6
- 00bc7ba4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc7ba4 ["INT_ADD", "register:40f0:8", ["const:bc7ba4:8", "const:4:8"]]
- 00bc7ba4 ["CALLIND", null, ["register:0:8"]]
+ 00bc7c6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc7c6c ["INT_ADD", "register:40f0:8", ["const:bc7c6c:8", "const:4:8"]]
+ 00bc7c6c ["CALLIND", null, ["register:0:8"]]
- 00bc7ba4 bytes 00013fd6
+ 00bc7c6c bytes 00013fd6
- 00bc7be8 ["INT_ADD", "register:40f0:8", ["const:bc7be8:8", "const:4:8"]]
- 00bc7be8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc7cb0 ["INT_ADD", "register:40f0:8", ["const:bc7cb0:8", "const:4:8"]]
+ 00bc7cb0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc7be8 bytes 5a550094
+ 00bc7cb0 bytes 54550094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c8100927e9f7b1c4622a135ce9a61f"></a>

### [`00bc7e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7e68.md) → [`00bc7f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md) FUN_00bc7f30

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc7eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7e68.md#insn-00bc7eb8) · [`00bc7f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7e68.md#insn-00bc7f04) · [`00bc7f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7e68.md#insn-00bc7f64)
- 新版 [`00bc7f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc7f80) · [`00bc7fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc7fcc) · [`00bc802c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md#insn-00bc802c)

~~~diff
- 00bc7eb8 ["INT_ADD", "register:40f0:8", ["const:bc7eb8:8", "const:4:8"]]
- 00bc7eb8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc7f80 ["INT_ADD", "register:40f0:8", ["const:bc7f80:8", "const:4:8"]]
+ 00bc7f80 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc7eb8 bytes a6540094
+ 00bc7f80 bytes a0540094
- 00bc7f04 ["INT_ADD", "register:40f0:8", ["const:bc7f04:8", "const:4:8"]]
- 00bc7f04 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc7fcc ["INT_ADD", "register:40f0:8", ["const:bc7fcc:8", "const:4:8"]]
+ 00bc7fcc ["CALL", null, ["callee:00bdd200:8"]]
- 00bc7f04 bytes 93540094
+ 00bc7fcc bytes 8d540094
- 00bc7f64 ["INT_ADD", "register:40f0:8", ["const:bc7f64:8", "const:4:8"]]
- 00bc7f64 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc802c ["INT_ADD", "register:40f0:8", ["const:bc802c:8", "const:4:8"]]
+ 00bc802c ["CALL", null, ["callee:00bdd200:8"]]
- 00bc7f64 bytes 7b540094
+ 00bc802c bytes 75540094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aeb62c1c4660e3415e865ebb6d7f4ab"></a>

### [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) → [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) FUN_00bc8290

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`00bc7e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7e68.md) [`00bc85d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc85d0.md) [`00bc86fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc86fc.md) [`00bcbaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md) [`00bcbf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md) · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 15件 [`00bc7f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc7f30.md) [`00bc8698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md) [`00bc87c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md) [`00bcbbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md) [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md#insn-00bc8258) · [`00bc82a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md#insn-00bc82a8) · [`00bc82cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md#insn-00bc82cc)
- 新版 [`00bc8320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8320) · [`00bc8370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8370) · [`00bc8394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md#insn-00bc8394)

~~~diff
- 00bc8258 ["INT_ADD", "register:40f0:8", ["const:bc8258:8", "const:4:8"]]
- 00bc8258 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8320 ["INT_ADD", "register:40f0:8", ["const:bc8320:8", "const:4:8"]]
+ 00bc8320 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8258 bytes be530094
+ 00bc8320 bytes b8530094
- 00bc82a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc82a8 ["INT_ADD", "register:40f0:8", ["const:bc82a8:8", "const:4:8"]]
- 00bc82a8 ["CALLIND", null, ["register:0:8"]]
+ 00bc8370 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8370 ["INT_ADD", "register:40f0:8", ["const:bc8370:8", "const:4:8"]]
+ 00bc8370 ["CALLIND", null, ["register:0:8"]]
- 00bc82a8 bytes 00013fd6
+ 00bc8370 bytes 00013fd6
- 00bc82cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc82cc ["INT_ADD", "register:40f0:8", ["const:bc82cc:8", "const:4:8"]]
- 00bc82cc ["CALLIND", null, ["register:0:8"]]
+ 00bc8394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8394 ["INT_ADD", "register:40f0:8", ["const:bc8394:8", "const:4:8"]]
+ 00bc8394 ["CALLIND", null, ["register:0:8"]]
- 00bc82cc bytes 00013fd6
+ 00bc8394 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fafeace09b7adcb74067aaa40b5738a"></a>

### [`00bc83f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc83f8.md) → [`00bc84c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md) FUN_00bc84c0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc83f8.md#insn-00bc8444) · [`00bc8490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc83f8.md#insn-00bc8490) · [`00bc84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc83f8.md#insn-00bc84f4)
- 新版 [`00bc850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc850c) · [`00bc8558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc8558) · [`00bc85bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc84c0.md#insn-00bc85bc)

~~~diff
- 00bc8444 ["INT_ADD", "register:40f0:8", ["const:bc8444:8", "const:4:8"]]
- 00bc8444 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc850c ["INT_ADD", "register:40f0:8", ["const:bc850c:8", "const:4:8"]]
+ 00bc850c ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8444 bytes 43530094
+ 00bc850c bytes 3d530094
- 00bc8490 ["INT_ADD", "register:40f0:8", ["const:bc8490:8", "const:4:8"]]
- 00bc8490 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8558 ["INT_ADD", "register:40f0:8", ["const:bc8558:8", "const:4:8"]]
+ 00bc8558 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8490 bytes 30530094
+ 00bc8558 bytes 2a530094
- 00bc84f4 ["INT_ADD", "register:40f0:8", ["const:bc84f4:8", "const:4:8"]]
- 00bc84f4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc85bc ["INT_ADD", "register:40f0:8", ["const:bc85bc:8", "const:4:8"]]
+ 00bc85bc ["CALL", null, ["callee:00bdd200:8"]]
- 00bc84f4 bytes 17530094
+ 00bc85bc bytes 11530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-571cf05d583217722648c1b1a285864b"></a>

### [`00bc85d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc85d0.md) → [`00bc8698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md) FUN_00bc8698

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc85fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc85d0.md#insn-00bc85fc) · [`00bc8620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc85d0.md#insn-00bc8620) · [`00bc8658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc85d0.md#insn-00bc8658)
- 新版 [`00bc86c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc86c4) · [`00bc86e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc86e8) · [`00bc8720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8698.md#insn-00bc8720)

~~~diff
- 00bc85fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc85fc ["INT_ADD", "register:40f0:8", ["const:bc85fc:8", "const:4:8"]]
- 00bc85fc ["CALLIND", null, ["register:0:8"]]
+ 00bc86c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc86c4 ["INT_ADD", "register:40f0:8", ["const:bc86c4:8", "const:4:8"]]
+ 00bc86c4 ["CALLIND", null, ["register:0:8"]]
- 00bc85fc bytes 00013fd6
+ 00bc86c4 bytes 00013fd6
- 00bc8620 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8620 ["INT_ADD", "register:40f0:8", ["const:bc8620:8", "const:4:8"]]
- 00bc8620 ["CALLIND", null, ["register:0:8"]]
+ 00bc86e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc86e8 ["INT_ADD", "register:40f0:8", ["const:bc86e8:8", "const:4:8"]]
+ 00bc86e8 ["CALLIND", null, ["register:0:8"]]
- 00bc8620 bytes 00013fd6
+ 00bc86e8 bytes 00013fd6
- 00bc8658 ["INT_ADD", "register:40f0:8", ["const:bc8658:8", "const:4:8"]]
- 00bc8658 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8720 ["INT_ADD", "register:40f0:8", ["const:bc8720:8", "const:4:8"]]
+ 00bc8720 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8658 bytes be520094
+ 00bc8720 bytes b8520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5139d4817c847d302002f66e1a973629"></a>

### [`00bc86fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc86fc.md) → [`00bc87c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md) FUN_00bc87c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc874c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc86fc.md#insn-00bc874c) · [`00bc8780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc86fc.md#insn-00bc8780) · [`00bc87a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc86fc.md#insn-00bc87a4)
- 新版 [`00bc8814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc8814) · [`00bc8848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc8848) · [`00bc886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc87c4.md#insn-00bc886c)

~~~diff
- 00bc874c ["INT_ADD", "register:40f0:8", ["const:bc874c:8", "const:4:8"]]
- 00bc874c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8814 ["INT_ADD", "register:40f0:8", ["const:bc8814:8", "const:4:8"]]
+ 00bc8814 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc874c bytes 81520094
+ 00bc8814 bytes 7b520094
- 00bc8780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8780 ["INT_ADD", "register:40f0:8", ["const:bc8780:8", "const:4:8"]]
- 00bc8780 ["CALLIND", null, ["register:0:8"]]
+ 00bc8848 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8848 ["INT_ADD", "register:40f0:8", ["const:bc8848:8", "const:4:8"]]
+ 00bc8848 ["CALLIND", null, ["register:0:8"]]
- 00bc8780 bytes 00013fd6
+ 00bc8848 bytes 00013fd6
- 00bc87a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc87a4 ["INT_ADD", "register:40f0:8", ["const:bc87a4:8", "const:4:8"]]
- 00bc87a4 ["CALLIND", null, ["register:0:8"]]
+ 00bc886c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc886c ["INT_ADD", "register:40f0:8", ["const:bc886c:8", "const:4:8"]]
+ 00bc886c ["CALLIND", null, ["register:0:8"]]
- 00bc87a4 bytes 00013fd6
+ 00bc886c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfc53edfd7f348f7a99f1523746c9096"></a>

### [`00bc88dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc88dc.md) → [`00bc89a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md) FUN_00bc89a4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc88dc.md#insn-00bc8924) · [`00bc8948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc88dc.md#insn-00bc8948) · [`00bc8984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc88dc.md#insn-00bc8984)
- 新版 [`00bc89ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc89ec) · [`00bc8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc8a10) · [`00bc8a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc89a4.md#insn-00bc8a4c)

~~~diff
- 00bc8924 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8924 ["INT_ADD", "register:40f0:8", ["const:bc8924:8", "const:4:8"]]
- 00bc8924 ["CALLIND", null, ["register:0:8"]]
+ 00bc89ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc89ec ["INT_ADD", "register:40f0:8", ["const:bc89ec:8", "const:4:8"]]
+ 00bc89ec ["CALLIND", null, ["register:0:8"]]
- 00bc8924 bytes 00013fd6
+ 00bc89ec bytes 00013fd6
- 00bc8948 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8948 ["INT_ADD", "register:40f0:8", ["const:bc8948:8", "const:4:8"]]
- 00bc8948 ["CALLIND", null, ["register:0:8"]]
+ 00bc8a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc8a10 ["INT_ADD", "register:40f0:8", ["const:bc8a10:8", "const:4:8"]]
+ 00bc8a10 ["CALLIND", null, ["register:0:8"]]
- 00bc8948 bytes 00013fd6
+ 00bc8a10 bytes 00013fd6
- 00bc8984 ["INT_ADD", "register:40f0:8", ["const:bc8984:8", "const:4:8"]]
- 00bc8984 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8a4c ["INT_ADD", "register:40f0:8", ["const:bc8a4c:8", "const:4:8"]]
+ 00bc8a4c ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8984 bytes f3510094
+ 00bc8a4c bytes ed510094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b89d8444d3ab3ee0793eb1d9678116c"></a>

### [`00bc8d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc8d88.md) → [`00bc8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md) FUN_00bc8e50

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc8ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc8d88.md#insn-00bc8ddc) · [`00bc8df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc8d88.md#insn-00bc8df8) · [`00bc8e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc8d88.md#insn-00bc8e38)
- 新版 [`00bc8ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8ea4) · [`00bc8ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8ec0) · [`00bc8f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8e50.md#insn-00bc8f00)

~~~diff
- 00bc8ddc ["INT_ADD", "register:40f0:8", ["const:bc8ddc:8", "const:4:8"]]
- 00bc8ddc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8ea4 ["INT_ADD", "register:40f0:8", ["const:bc8ea4:8", "const:4:8"]]
+ 00bc8ea4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8ddc bytes dd500094
+ 00bc8ea4 bytes d7500094
- 00bc8df8 ["INT_ADD", "register:40f0:8", ["const:bc8df8:8", "const:4:8"]]
- 00bc8df8 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc8ec0 ["INT_ADD", "register:40f0:8", ["const:bc8ec0:8", "const:4:8"]]
+ 00bc8ec0 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc8df8 bytes ae480094
+ 00bc8ec0 bytes a8480094
- 00bc8e38 ["INT_ADD", "register:40f0:8", ["const:bc8e38:8", "const:4:8"]]
- 00bc8e38 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc8f00 ["INT_ADD", "register:40f0:8", ["const:bc8f00:8", "const:4:8"]]
+ 00bc8f00 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc8e38 bytes c6500094
+ 00bc8f00 bytes c0500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ab39ae18fc488dfd83541f7d4c07d3"></a>

### [`00bc90cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc90cc.md) → [`00bc9194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md) FUN_00bc9194

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc90cc.md#insn-00bc9120) · [`00bc913c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc90cc.md#insn-00bc913c) · [`00bc9180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc90cc.md#insn-00bc9180)
- 新版 [`00bc91e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc91e8) · [`00bc9204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc9204) · [`00bc9248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9194.md#insn-00bc9248)

~~~diff
- 00bc9120 ["INT_ADD", "register:40f0:8", ["const:bc9120:8", "const:4:8"]]
- 00bc9120 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc91e8 ["INT_ADD", "register:40f0:8", ["const:bc91e8:8", "const:4:8"]]
+ 00bc91e8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc9120 bytes 0c500094
+ 00bc91e8 bytes 06500094
- 00bc913c ["INT_ADD", "register:40f0:8", ["const:bc913c:8", "const:4:8"]]
- 00bc913c ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc9204 ["INT_ADD", "register:40f0:8", ["const:bc9204:8", "const:4:8"]]
+ 00bc9204 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc913c bytes dd470094
+ 00bc9204 bytes d7470094
- 00bc9180 ["INT_ADD", "register:40f0:8", ["const:bc9180:8", "const:4:8"]]
- 00bc9180 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc9248 ["INT_ADD", "register:40f0:8", ["const:bc9248:8", "const:4:8"]]
+ 00bc9248 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc9180 bytes f44f0094
+ 00bc9248 bytes ee4f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7123f81b438aa1252a2a03102912a1cb"></a>

### [`00bc9e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9e70.md) → [`00bc9f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md) FUN_00bc9f38

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9e70.md#insn-00bc9ed0) · [`00bc9f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9e70.md#insn-00bc9f28) · [`00bc9f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9e70.md#insn-00bc9f44)
- 新版 [`00bc9f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bc9f98) · [`00bc9ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bc9ff0) · [`00bca00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9f38.md#insn-00bca00c)

~~~diff
- 00bc9ed0 ["INT_ADD", "register:40f0:8", ["const:bc9ed0:8", "const:4:8"]]
- 00bc9ed0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc9f98 ["INT_ADD", "register:40f0:8", ["const:bc9f98:8", "const:4:8"]]
+ 00bc9f98 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc9ed0 bytes a04c0094
+ 00bc9f98 bytes 9a4c0094
- 00bc9f28 ["INT_ADD", "register:40f0:8", ["const:bc9f28:8", "const:4:8"]]
- 00bc9f28 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc9ff0 ["INT_ADD", "register:40f0:8", ["const:bc9ff0:8", "const:4:8"]]
+ 00bc9ff0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc9f28 bytes 8a4c0094
+ 00bc9ff0 bytes 844c0094
- 00bc9f44 ["INT_ADD", "register:40f0:8", ["const:bc9f44:8", "const:4:8"]]
- 00bc9f44 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bca00c ["INT_ADD", "register:40f0:8", ["const:bca00c:8", "const:4:8"]]
+ 00bca00c ["CALL", null, ["callee:00bdb160:8"]]
- 00bc9f44 bytes 5b440094
+ 00bca00c bytes 55440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-610dcfa74e06e1d9aca52db8f770472d"></a>

### [`00bca7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca7a4.md) → [`00bca86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md) FUN_00bca86c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca7a4.md#insn-00bca7e8) · [`00bca824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca7a4.md#insn-00bca824) · [`00bca848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca7a4.md#insn-00bca848)
- 新版 [`00bca8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca8b0) · [`00bca8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca8ec) · [`00bca910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca86c.md#insn-00bca910)

~~~diff
- 00bca7e8 ["INT_ADD", "register:40f0:8", ["const:bca7e8:8", "const:4:8"]]
- 00bca7e8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bca8b0 ["INT_ADD", "register:40f0:8", ["const:bca8b0:8", "const:4:8"]]
+ 00bca8b0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bca7e8 bytes 5a4a0094
+ 00bca8b0 bytes 544a0094
- 00bca824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca824 ["INT_ADD", "register:40f0:8", ["const:bca824:8", "const:4:8"]]
- 00bca824 ["CALLIND", null, ["register:0:8"]]
+ 00bca8ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca8ec ["INT_ADD", "register:40f0:8", ["const:bca8ec:8", "const:4:8"]]
+ 00bca8ec ["CALLIND", null, ["register:0:8"]]
- 00bca824 bytes 00013fd6
+ 00bca8ec bytes 00013fd6
- 00bca848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca848 ["INT_ADD", "register:40f0:8", ["const:bca848:8", "const:4:8"]]
- 00bca848 ["CALLIND", null, ["register:0:8"]]
+ 00bca910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bca910 ["INT_ADD", "register:40f0:8", ["const:bca910:8", "const:4:8"]]
+ 00bca910 ["CALLIND", null, ["register:0:8"]]
- 00bca848 bytes 00013fd6
+ 00bca910 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4cca48a748e6813aed4d677aa870563"></a>

### [`00bcb380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb380.md) → [`00bcb448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md) FUN_00bcb448

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb380.md#insn-00bcb3c8) · [`00bcb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb380.md#insn-00bcb430) · [`00bcb44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb380.md#insn-00bcb44c)
- 新版 [`00bcb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb490) · [`00bcb4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb4f8) · [`00bcb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb448.md#insn-00bcb514)

~~~diff
- 00bcb3c8 ["INT_ADD", "register:40f0:8", ["const:bcb3c8:8", "const:4:8"]]
- 00bcb3c8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb490 ["INT_ADD", "register:40f0:8", ["const:bcb490:8", "const:4:8"]]
+ 00bcb490 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb3c8 bytes 62470094
+ 00bcb490 bytes 5c470094
- 00bcb430 ["INT_ADD", "register:40f0:8", ["const:bcb430:8", "const:4:8"]]
- 00bcb430 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb4f8 ["INT_ADD", "register:40f0:8", ["const:bcb4f8:8", "const:4:8"]]
+ 00bcb4f8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb430 bytes 48470094
+ 00bcb4f8 bytes 42470094
- 00bcb44c ["INT_ADD", "register:40f0:8", ["const:bcb44c:8", "const:4:8"]]
- 00bcb44c ["CALL", null, ["callee:00bdb160:8"]]
+ 00bcb514 ["INT_ADD", "register:40f0:8", ["const:bcb514:8", "const:4:8"]]
+ 00bcb514 ["CALL", null, ["callee:00bdb160:8"]]
- 00bcb44c bytes 193f0094
+ 00bcb514 bytes 133f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-247746bc6d8cf49215110a797350c653"></a>

### [`00bcb570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb570.md) → [`00bcb638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md) FUN_00bcb638

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb570.md#insn-00bcb5dc) · [`00bcb634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb570.md#insn-00bcb634) · [`00bcb694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb570.md#insn-00bcb694)
- 新版 [`00bcb6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb6a4) · [`00bcb6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb6fc) · [`00bcb75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb638.md#insn-00bcb75c)

~~~diff
- 00bcb5dc ["INT_ADD", "register:40f0:8", ["const:bcb5dc:8", "const:4:8"]]
- 00bcb5dc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb6a4 ["INT_ADD", "register:40f0:8", ["const:bcb6a4:8", "const:4:8"]]
+ 00bcb6a4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb5dc bytes dd460094
+ 00bcb6a4 bytes d7460094
- 00bcb634 ["INT_ADD", "register:40f0:8", ["const:bcb634:8", "const:4:8"]]
- 00bcb634 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb6fc ["INT_ADD", "register:40f0:8", ["const:bcb6fc:8", "const:4:8"]]
+ 00bcb6fc ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb634 bytes c7460094
+ 00bcb6fc bytes c1460094
- 00bcb694 ["INT_ADD", "register:40f0:8", ["const:bcb694:8", "const:4:8"]]
- 00bcb694 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb75c ["INT_ADD", "register:40f0:8", ["const:bcb75c:8", "const:4:8"]]
+ 00bcb75c ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb694 bytes af460094
+ 00bcb75c bytes a9460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7976199f9974643ffc2bb632e092a6a"></a>

### [`00bcb82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb82c.md) → [`00bcb8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb8f4.md) FUN_00bcb8f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb82c.md#insn-00bcb850)
- 新版 [`00bcb918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb8f4.md#insn-00bcb918)

~~~diff
- 00bcb850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb850 ["INT_ADD", "register:40f0:8", ["const:bcb850:8", "const:4:8"]]
- 00bcb850 ["CALLIND", null, ["register:0:8"]]
+ 00bcb918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb918 ["INT_ADD", "register:40f0:8", ["const:bcb918:8", "const:4:8"]]
+ 00bcb918 ["CALLIND", null, ["register:0:8"]]
- 00bcb850 bytes 00013fd6
+ 00bcb918 bytes 00013fd6
~~~


<a id="compare-e97dd98681504ffe81710aa4be429469"></a>

### [`00bcb89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb89c.md) → [`00bcb964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md) FUN_00bcb964

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb89c.md#insn-00bcb8c0) · [`00bcb8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb89c.md#insn-00bcb8e4) · [`00bcb910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb89c.md#insn-00bcb910)
- 新版 [`00bcb988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb988) · [`00bcb9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb9ac) · [`00bcb9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb964.md#insn-00bcb9d8)

~~~diff
- 00bcb8c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb8c0 ["INT_ADD", "register:40f0:8", ["const:bcb8c0:8", "const:4:8"]]
- 00bcb8c0 ["CALLIND", null, ["register:0:8"]]
+ 00bcb988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb988 ["INT_ADD", "register:40f0:8", ["const:bcb988:8", "const:4:8"]]
+ 00bcb988 ["CALLIND", null, ["register:0:8"]]
- 00bcb8c0 bytes 00013fd6
+ 00bcb988 bytes 00013fd6
- 00bcb8e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb8e4 ["INT_ADD", "register:40f0:8", ["const:bcb8e4:8", "const:4:8"]]
- 00bcb8e4 ["CALLIND", null, ["register:0:8"]]
+ 00bcb9ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcb9ac ["INT_ADD", "register:40f0:8", ["const:bcb9ac:8", "const:4:8"]]
+ 00bcb9ac ["CALLIND", null, ["register:0:8"]]
- 00bcb8e4 bytes 00013fd6
+ 00bcb9ac bytes 00013fd6
- 00bcb910 ["INT_ADD", "register:40f0:8", ["const:bcb910:8", "const:4:8"]]
- 00bcb910 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb9d8 ["INT_ADD", "register:40f0:8", ["const:bcb9d8:8", "const:4:8"]]
+ 00bcb9d8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb910 bytes 10460094
+ 00bcb9d8 bytes 0a460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067bbafccb27f7e9e5b621aead91d0ec"></a>

### [`00bcb9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md) → [`00bcba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md) FUN_00bcba80

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md#insn-00bcb9dc) · [`00bcba00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md#insn-00bcba00) · [`00bcba3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb9b8.md#insn-00bcba3c)
- 新版 [`00bcbaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbaa4) · [`00bcbac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbac8) · [`00bcbb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md#insn-00bcbb04)

~~~diff
- 00bcb9dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb9dc ["INT_ADD", "register:40f0:8", ["const:bcb9dc:8", "const:4:8"]]
- 00bcb9dc ["CALLIND", null, ["register:0:8"]]
+ 00bcbaa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbaa4 ["INT_ADD", "register:40f0:8", ["const:bcbaa4:8", "const:4:8"]]
+ 00bcbaa4 ["CALLIND", null, ["register:0:8"]]
- 00bcb9dc bytes 00013fd6
+ 00bcbaa4 bytes 00013fd6
- 00bcba00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcba00 ["INT_ADD", "register:40f0:8", ["const:bcba00:8", "const:4:8"]]
- 00bcba00 ["CALLIND", null, ["register:0:8"]]
+ 00bcbac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbac8 ["INT_ADD", "register:40f0:8", ["const:bcbac8:8", "const:4:8"]]
+ 00bcbac8 ["CALLIND", null, ["register:0:8"]]
- 00bcba00 bytes 00013fd6
+ 00bcbac8 bytes 00013fd6
- 00bcba3c ["INT_ADD", "register:40f0:8", ["const:bcba3c:8", "const:4:8"]]
- 00bcba3c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbb04 ["INT_ADD", "register:40f0:8", ["const:bcbb04:8", "const:4:8"]]
+ 00bcbb04 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcba3c bytes c5450094
+ 00bcbb04 bytes bf450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84da9486fd89853d811696a4997aedca"></a>

### [`00bcba74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcba74.md) → [`00bcbb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md) FUN_00bcbb3c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcba74.md#insn-00bcbaa0) · [`00bcbac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcba74.md#insn-00bcbac4)
- 新版 [`00bcbb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md#insn-00bcbb68) · [`00bcbb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbb3c.md#insn-00bcbb8c)

~~~diff
- 00bcbaa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbaa0 ["INT_ADD", "register:40f0:8", ["const:bcbaa0:8", "const:4:8"]]
- 00bcbaa0 ["CALLIND", null, ["register:0:8"]]
+ 00bcbb68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbb68 ["INT_ADD", "register:40f0:8", ["const:bcbb68:8", "const:4:8"]]
+ 00bcbb68 ["CALLIND", null, ["register:0:8"]]
- 00bcbaa0 bytes 00013fd6
+ 00bcbb68 bytes 00013fd6
- 00bcbac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbac4 ["INT_ADD", "register:40f0:8", ["const:bcbac4:8", "const:4:8"]]
- 00bcbac4 ["CALLIND", null, ["register:0:8"]]
+ 00bcbb8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbb8c ["INT_ADD", "register:40f0:8", ["const:bcbb8c:8", "const:4:8"]]
+ 00bcbb8c ["CALLIND", null, ["register:0:8"]]
- 00bcbac4 bytes 00013fd6
+ 00bcbb8c bytes 00013fd6
~~~


<a id="compare-5dbe212a0d1be6c5c8454a1dd1b9389e"></a>

### [`00bcbc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbc10.md) → [`00bcbcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md) FUN_00bcbcd8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbc3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbc10.md#insn-00bcbc3c) · [`00bcbc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbc10.md#insn-00bcbc60) · [`00bcbc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbc10.md#insn-00bcbc94)
- 新版 [`00bcbd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd04) · [`00bcbd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd28) · [`00bcbd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbcd8.md#insn-00bcbd5c)

~~~diff
- 00bcbc3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbc3c ["INT_ADD", "register:40f0:8", ["const:bcbc3c:8", "const:4:8"]]
- 00bcbc3c ["CALLIND", null, ["register:0:8"]]
+ 00bcbd04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbd04 ["INT_ADD", "register:40f0:8", ["const:bcbd04:8", "const:4:8"]]
+ 00bcbd04 ["CALLIND", null, ["register:0:8"]]
- 00bcbc3c bytes 00013fd6
+ 00bcbd04 bytes 00013fd6
- 00bcbc60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbc60 ["INT_ADD", "register:40f0:8", ["const:bcbc60:8", "const:4:8"]]
- 00bcbc60 ["CALLIND", null, ["register:0:8"]]
+ 00bcbd28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbd28 ["INT_ADD", "register:40f0:8", ["const:bcbd28:8", "const:4:8"]]
+ 00bcbd28 ["CALLIND", null, ["register:0:8"]]
- 00bcbc60 bytes 00013fd6
+ 00bcbd28 bytes 00013fd6
- 00bcbc94 ["INT_ADD", "register:40f0:8", ["const:bcbc94:8", "const:4:8"]]
- 00bcbc94 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbd5c ["INT_ADD", "register:40f0:8", ["const:bcbd5c:8", "const:4:8"]]
+ 00bcbd5c ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbc94 bytes 2f450094
+ 00bcbd5c bytes 29450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11dc1a3378a2bf18f14f02a4438f5a24"></a>

### [`00bcbd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbd38.md) → [`00bcbe00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md) FUN_00bcbe00

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbd58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbd38.md#insn-00bcbd58) · [`00bcbd84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbd38.md#insn-00bcbd84) · [`00bcbdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbd38.md#insn-00bcbdc4)
- 新版 [`00bcbe20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe20) · [`00bcbe4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe4c) · [`00bcbe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbe00.md#insn-00bcbe8c)

~~~diff
- 00bcbd58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbd58 ["INT_ADD", "register:40f0:8", ["const:bcbd58:8", "const:4:8"]]
- 00bcbd58 ["CALLIND", null, ["register:0:8"]]
+ 00bcbe20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcbe20 ["INT_ADD", "register:40f0:8", ["const:bcbe20:8", "const:4:8"]]
+ 00bcbe20 ["CALLIND", null, ["register:0:8"]]
- 00bcbd58 bytes 00013fd6
+ 00bcbe20 bytes 00013fd6
- 00bcbd84 ["INT_ADD", "register:40f0:8", ["const:bcbd84:8", "const:4:8"]]
- 00bcbd84 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbe4c ["INT_ADD", "register:40f0:8", ["const:bcbe4c:8", "const:4:8"]]
+ 00bcbe4c ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbd84 bytes f3440094
+ 00bcbe4c bytes ed440094
- 00bcbdc4 ["INT_ADD", "register:40f0:8", ["const:bcbdc4:8", "const:4:8"]]
- 00bcbdc4 ["CALL", null, ["callee:00bde270:8"]]
+ 00bcbe8c ["INT_ADD", "register:40f0:8", ["const:bcbe8c:8", "const:4:8"]]
+ 00bcbe8c ["CALL", null, ["callee:00bde270:8"]]
- 00bcbdc4 bytes ff480094
+ 00bcbe8c bytes f9480094
~~~


<a id="compare-164c16137ff0dd5046c110831f7dda4d"></a>

### [`00bcbde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md) → [`00bcbeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md) FUN_00bcbeac

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bcbf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md#insn-00bcbe2c) · [`00bcbe9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md#insn-00bcbe9c) · [`00bcbeb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md#insn-00bcbeb8)
- 新版 [`00bcbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbef4) · [`00bcbf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbf64) · [`00bcbf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md#insn-00bcbf80)

~~~diff
- 00bcbe2c ["INT_ADD", "register:40f0:8", ["const:bcbe2c:8", "const:4:8"]]
- 00bcbe2c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbef4 ["INT_ADD", "register:40f0:8", ["const:bcbef4:8", "const:4:8"]]
+ 00bcbef4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbe2c bytes c9440094
+ 00bcbef4 bytes c3440094
- 00bcbe9c ["INT_ADD", "register:40f0:8", ["const:bcbe9c:8", "const:4:8"]]
- 00bcbe9c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbf64 ["INT_ADD", "register:40f0:8", ["const:bcbf64:8", "const:4:8"]]
+ 00bcbf64 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbe9c bytes ad440094
+ 00bcbf64 bytes a7440094
- 00bcbeb8 ["INT_ADD", "register:40f0:8", ["const:bcbeb8:8", "const:4:8"]]
- 00bcbeb8 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bcbf80 ["INT_ADD", "register:40f0:8", ["const:bcbf80:8", "const:4:8"]]
+ 00bcbf80 ["CALL", null, ["callee:00bdb160:8"]]
- 00bcbeb8 bytes 7e3c0094
+ 00bcbf80 bytes 783c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6345af053fb8171501d549a68832c0b0"></a>

### [`00bcbf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md) → [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) FUN_00bcc00c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bcbde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md) [`00bcc2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc2a4.md) · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 2件 [`00bcbeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md) [`00bcc36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md) · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md#insn-00bcbf98) · [`00bcbfc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md#insn-00bcbfc4) · [`00bcbff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md#insn-00bcbff0)
- 新版 [`00bcc060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md#insn-00bcc060) · [`00bcc08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md#insn-00bcc08c) · [`00bcc0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md#insn-00bcc0b8)

~~~diff
- 00bcbf98 ["INT_ADD", "register:40f0:8", ["const:bcbf98:8", "const:4:8"]]
- 00bcbf98 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc060 ["INT_ADD", "register:40f0:8", ["const:bcc060:8", "const:4:8"]]
+ 00bcc060 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbf98 bytes 6e440094
+ 00bcc060 bytes 68440094
- 00bcbfc4 ["INT_ADD", "register:40f0:8", ["const:bcbfc4:8", "const:4:8"]]
- 00bcbfc4 ["CALL", null, ["callee:00bc8290:8"]]
+ 00bcc08c ["INT_ADD", "register:40f0:8", ["const:bcc08c:8", "const:4:8"]]
+ 00bcc08c ["CALL", null, ["callee:00bc8290:8"]]
- 00bcbfc4 bytes 81f0ff97
+ 00bcc08c bytes 81f0ff97
- 00bcbff0 ["INT_ADD", "register:40f0:8", ["const:bcbff0:8", "const:4:8"]]
- 00bcbff0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc0b8 ["INT_ADD", "register:40f0:8", ["const:bcc0b8:8", "const:4:8"]]
+ 00bcc0b8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbff0 bytes 58440094
+ 00bcc0b8 bytes 52440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14ce57dff874827dcbd7823a924c0ae4"></a>

### [`00bcc2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc2a4.md) → [`00bcc36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md) FUN_00bcc36c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bcbf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbf44.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bcc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc00c.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc2a4.md#insn-00bcc2e8) · [`00bcc324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc2a4.md#insn-00bcc324) · [`00bcc354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc2a4.md#insn-00bcc354)
- 新版 [`00bcc3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc3b0) · [`00bcc3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc3ec) · [`00bcc41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc36c.md#insn-00bcc41c)

~~~diff
- 00bcc2e8 ["INT_ADD", "register:40f0:8", ["const:bcc2e8:8", "const:4:8"]]
- 00bcc2e8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc3b0 ["INT_ADD", "register:40f0:8", ["const:bcc3b0:8", "const:4:8"]]
+ 00bcc3b0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc2e8 bytes 9a430094
+ 00bcc3b0 bytes 94430094
- 00bcc324 ["INT_ADD", "register:40f0:8", ["const:bcc324:8", "const:4:8"]]
- 00bcc324 ["CALL", null, ["callee:00bcc00c:8"]]
+ 00bcc3ec ["INT_ADD", "register:40f0:8", ["const:bcc3ec:8", "const:4:8"]]
+ 00bcc3ec ["CALL", null, ["callee:00bcc00c:8"]]
- 00bcc324 bytes 08ffff97
+ 00bcc3ec bytes 08ffff97
- 00bcc354 ["INT_ADD", "register:40f0:8", ["const:bcc354:8", "const:4:8"]]
- 00bcc354 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc41c ["INT_ADD", "register:40f0:8", ["const:bcc41c:8", "const:4:8"]]
+ 00bcc41c ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc354 bytes 7f430094
+ 00bcc41c bytes 79430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a211db9719d00df082592e693b71af"></a>

### [`00bcc3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc3a8.md) → [`00bcc470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md) FUN_00bcc470

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc3a8.md#insn-00bcc3f8) · [`00bcc42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc3a8.md#insn-00bcc42c) · [`00bcc450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc3a8.md#insn-00bcc450)
- 新版 [`00bcc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc4c0) · [`00bcc4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc4f4) · [`00bcc518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc470.md#insn-00bcc518)

~~~diff
- 00bcc3f8 ["INT_ADD", "register:40f0:8", ["const:bcc3f8:8", "const:4:8"]]
- 00bcc3f8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc4c0 ["INT_ADD", "register:40f0:8", ["const:bcc4c0:8", "const:4:8"]]
+ 00bcc4c0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc3f8 bytes 56430094
+ 00bcc4c0 bytes 50430094
- 00bcc42c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc42c ["INT_ADD", "register:40f0:8", ["const:bcc42c:8", "const:4:8"]]
- 00bcc42c ["CALLIND", null, ["register:0:8"]]
+ 00bcc4f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc4f4 ["INT_ADD", "register:40f0:8", ["const:bcc4f4:8", "const:4:8"]]
+ 00bcc4f4 ["CALLIND", null, ["register:0:8"]]
- 00bcc42c bytes 00013fd6
+ 00bcc4f4 bytes 00013fd6
- 00bcc450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc450 ["INT_ADD", "register:40f0:8", ["const:bcc450:8", "const:4:8"]]
- 00bcc450 ["CALLIND", null, ["register:0:8"]]
+ 00bcc518 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc518 ["INT_ADD", "register:40f0:8", ["const:bcc518:8", "const:4:8"]]
+ 00bcc518 ["CALLIND", null, ["register:0:8"]]
- 00bcc450 bytes 00013fd6
+ 00bcc518 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-825d393cb7a1c76acd73d2e6fdef1592"></a>

### [`00bcc680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc680.md) → [`00bcc748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md) FUN_00bcc748

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcc6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc680.md#insn-00bcc6c8) · [`00bcc724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc680.md#insn-00bcc724) · [`00bcc740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc680.md#insn-00bcc740)
- 新版 [`00bcc790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc790) · [`00bcc7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc7ec) · [`00bcc808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc748.md#insn-00bcc808)

~~~diff
- 00bcc6c8 ["INT_ADD", "register:40f0:8", ["const:bcc6c8:8", "const:4:8"]]
- 00bcc6c8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc790 ["INT_ADD", "register:40f0:8", ["const:bcc790:8", "const:4:8"]]
+ 00bcc790 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc6c8 bytes a2420094
+ 00bcc790 bytes 9c420094
- 00bcc724 ["INT_ADD", "register:40f0:8", ["const:bcc724:8", "const:4:8"]]
- 00bcc724 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc7ec ["INT_ADD", "register:40f0:8", ["const:bcc7ec:8", "const:4:8"]]
+ 00bcc7ec ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc724 bytes 8b420094
+ 00bcc7ec bytes 85420094
- 00bcc740 ["INT_ADD", "register:40f0:8", ["const:bcc740:8", "const:4:8"]]
- 00bcc740 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bcc808 ["INT_ADD", "register:40f0:8", ["const:bcc808:8", "const:4:8"]]
+ 00bcc808 ["CALL", null, ["callee:00bdb160:8"]]
- 00bcc740 bytes 5c3a0094
+ 00bcc808 bytes 563a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ebed47433609f751b19241e79f87592"></a>

### [`00bccef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md) → [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) FUN_00bccfc0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bcc774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc774.md) [`00bce438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce438.md) · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 2件 [`00bcc83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md) [`00bce500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md) · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bccf3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md#insn-00bccf3c) · [`00bccf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md#insn-00bccf60) · [`00bccfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md#insn-00bccfbc)
- 新版 [`00bcd004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd004) · [`00bcd028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd028) · [`00bcd084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md#insn-00bcd084)

~~~diff
- 00bccf3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bccf3c ["INT_ADD", "register:40f0:8", ["const:bccf3c:8", "const:4:8"]]
- 00bccf3c ["CALLIND", null, ["register:0:8"]]
+ 00bcd004 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd004 ["INT_ADD", "register:40f0:8", ["const:bcd004:8", "const:4:8"]]
+ 00bcd004 ["CALLIND", null, ["register:0:8"]]
- 00bccf3c bytes 00013fd6
+ 00bcd004 bytes 00013fd6
- 00bccf60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bccf60 ["INT_ADD", "register:40f0:8", ["const:bccf60:8", "const:4:8"]]
- 00bccf60 ["CALLIND", null, ["register:0:8"]]
+ 00bcd028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd028 ["INT_ADD", "register:40f0:8", ["const:bcd028:8", "const:4:8"]]
+ 00bcd028 ["CALLIND", null, ["register:0:8"]]
- 00bccf60 bytes 00013fd6
+ 00bcd028 bytes 00013fd6
- 00bccfbc ["INT_ADD", "register:40f0:8", ["const:bccfbc:8", "const:4:8"]]
- 00bccfbc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd084 ["INT_ADD", "register:40f0:8", ["const:bcd084:8", "const:4:8"]]
+ 00bcd084 ["CALL", null, ["callee:00bdd200:8"]]
- 00bccfbc bytes 65400094
+ 00bcd084 bytes 5f400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01c94303e4b48f8b768a9f6c6ff12117"></a>

### [`00bcd0b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd0b8.md) → [`00bcd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md) FUN_00bcd180

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd0b8.md#insn-00bcd104) · [`00bcd138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd0b8.md#insn-00bcd138) · [`00bcd15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd0b8.md#insn-00bcd15c)
- 新版 [`00bcd1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd1cc) · [`00bcd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd200) · [`00bcd224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd180.md#insn-00bcd224)

~~~diff
- 00bcd104 ["INT_ADD", "register:40f0:8", ["const:bcd104:8", "const:4:8"]]
- 00bcd104 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd1cc ["INT_ADD", "register:40f0:8", ["const:bcd1cc:8", "const:4:8"]]
+ 00bcd1cc ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd104 bytes 13400094
+ 00bcd1cc bytes 0d400094
- 00bcd138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd138 ["INT_ADD", "register:40f0:8", ["const:bcd138:8", "const:4:8"]]
- 00bcd138 ["CALLIND", null, ["register:0:8"]]
+ 00bcd200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd200 ["INT_ADD", "register:40f0:8", ["const:bcd200:8", "const:4:8"]]
+ 00bcd200 ["CALLIND", null, ["register:0:8"]]
- 00bcd138 bytes 00013fd6
+ 00bcd200 bytes 00013fd6
- 00bcd15c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd15c ["INT_ADD", "register:40f0:8", ["const:bcd15c:8", "const:4:8"]]
- 00bcd15c ["CALLIND", null, ["register:0:8"]]
+ 00bcd224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd224 ["INT_ADD", "register:40f0:8", ["const:bcd224:8", "const:4:8"]]
+ 00bcd224 ["CALLIND", null, ["register:0:8"]]
- 00bcd15c bytes 00013fd6
+ 00bcd224 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d814f48a4c83374fd40e5614b78f65f"></a>

### [`00bcd304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd304.md) → [`00bcd3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md) FUN_00bcd3cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd304.md#insn-00bcd34c) · [`00bcd384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd304.md#insn-00bcd384) · [`00bcd3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd304.md#insn-00bcd3a8)
- 新版 [`00bcd414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd414) · [`00bcd44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd44c) · [`00bcd470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd3cc.md#insn-00bcd470)

~~~diff
- 00bcd34c ["INT_ADD", "register:40f0:8", ["const:bcd34c:8", "const:4:8"]]
- 00bcd34c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd414 ["INT_ADD", "register:40f0:8", ["const:bcd414:8", "const:4:8"]]
+ 00bcd414 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd34c bytes 813f0094
+ 00bcd414 bytes 7b3f0094
- 00bcd384 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd384 ["INT_ADD", "register:40f0:8", ["const:bcd384:8", "const:4:8"]]
- 00bcd384 ["CALLIND", null, ["register:0:8"]]
+ 00bcd44c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd44c ["INT_ADD", "register:40f0:8", ["const:bcd44c:8", "const:4:8"]]
+ 00bcd44c ["CALLIND", null, ["register:0:8"]]
- 00bcd384 bytes 00013fd6
+ 00bcd44c bytes 00013fd6
- 00bcd3a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd3a8 ["INT_ADD", "register:40f0:8", ["const:bcd3a8:8", "const:4:8"]]
- 00bcd3a8 ["CALLIND", null, ["register:0:8"]]
+ 00bcd470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd470 ["INT_ADD", "register:40f0:8", ["const:bcd470:8", "const:4:8"]]
+ 00bcd470 ["CALLIND", null, ["register:0:8"]]
- 00bcd3a8 bytes 00013fd6
+ 00bcd470 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1ebf7c7b87f16466685f3d0c496ab0"></a>

### [`00bcd570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd570.md) → [`00bcd638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md) FUN_00bcd638

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd5a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd570.md#insn-00bcd5a4) · [`00bcd5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd570.md#insn-00bcd5c8) · [`00bcd5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd570.md#insn-00bcd5f4)
- 新版 [`00bcd66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd66c) · [`00bcd690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd690) · [`00bcd6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd638.md#insn-00bcd6bc)

~~~diff
- 00bcd5a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd5a4 ["INT_ADD", "register:40f0:8", ["const:bcd5a4:8", "const:4:8"]]
- 00bcd5a4 ["CALLIND", null, ["register:0:8"]]
+ 00bcd66c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd66c ["INT_ADD", "register:40f0:8", ["const:bcd66c:8", "const:4:8"]]
+ 00bcd66c ["CALLIND", null, ["register:0:8"]]
- 00bcd5a4 bytes 00013fd6
+ 00bcd66c bytes 00013fd6
- 00bcd5c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd5c8 ["INT_ADD", "register:40f0:8", ["const:bcd5c8:8", "const:4:8"]]
- 00bcd5c8 ["CALLIND", null, ["register:0:8"]]
+ 00bcd690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd690 ["INT_ADD", "register:40f0:8", ["const:bcd690:8", "const:4:8"]]
+ 00bcd690 ["CALLIND", null, ["register:0:8"]]
- 00bcd5c8 bytes 00013fd6
+ 00bcd690 bytes 00013fd6
- 00bcd5f4 ["INT_ADD", "register:40f0:8", ["const:bcd5f4:8", "const:4:8"]]
- 00bcd5f4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd6bc ["INT_ADD", "register:40f0:8", ["const:bcd6bc:8", "const:4:8"]]
+ 00bcd6bc ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd5f4 bytes d73e0094
+ 00bcd6bc bytes d13e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc9118e3d214311c3b62bef9e2df0d9"></a>

### [`00bcd68c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd68c.md) → [`00bcd754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md) FUN_00bcd754

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcd6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd68c.md#insn-00bcd6dc) · [`00bcd710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd68c.md#insn-00bcd710) · [`00bcd734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd68c.md#insn-00bcd734)
- 新版 [`00bcd7a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7a4) · [`00bcd7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7d8) · [`00bcd7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd754.md#insn-00bcd7fc)

~~~diff
- 00bcd6dc ["INT_ADD", "register:40f0:8", ["const:bcd6dc:8", "const:4:8"]]
- 00bcd6dc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd7a4 ["INT_ADD", "register:40f0:8", ["const:bcd7a4:8", "const:4:8"]]
+ 00bcd7a4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd6dc bytes 9d3e0094
+ 00bcd7a4 bytes 973e0094
- 00bcd710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd710 ["INT_ADD", "register:40f0:8", ["const:bcd710:8", "const:4:8"]]
- 00bcd710 ["CALLIND", null, ["register:0:8"]]
+ 00bcd7d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd7d8 ["INT_ADD", "register:40f0:8", ["const:bcd7d8:8", "const:4:8"]]
+ 00bcd7d8 ["CALLIND", null, ["register:0:8"]]
- 00bcd710 bytes 00013fd6
+ 00bcd7d8 bytes 00013fd6
- 00bcd734 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd734 ["INT_ADD", "register:40f0:8", ["const:bcd734:8", "const:4:8"]]
- 00bcd734 ["CALLIND", null, ["register:0:8"]]
+ 00bcd7fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd7fc ["INT_ADD", "register:40f0:8", ["const:bcd7fc:8", "const:4:8"]]
+ 00bcd7fc ["CALLIND", null, ["register:0:8"]]
- 00bcd734 bytes 00013fd6
+ 00bcd7fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c3143be155cc5bb08982ea3c6900be1"></a>

### [`00bcdcac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdcac.md) → [`00bcdd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md) FUN_00bcdd74

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcdcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdcac.md#insn-00bcdcf0) · [`00bcdd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdcac.md#insn-00bcdd40) · [`00bcdd64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdcac.md#insn-00bcdd64)
- 新版 [`00bcddb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcddb8) · [`00bcde08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcde08) · [`00bcde2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md#insn-00bcde2c)

~~~diff
- 00bcdcf0 ["INT_ADD", "register:40f0:8", ["const:bcdcf0:8", "const:4:8"]]
- 00bcdcf0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcddb8 ["INT_ADD", "register:40f0:8", ["const:bcddb8:8", "const:4:8"]]
+ 00bcddb8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcdcf0 bytes 183d0094
+ 00bcddb8 bytes 123d0094
- 00bcdd40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcdd40 ["INT_ADD", "register:40f0:8", ["const:bcdd40:8", "const:4:8"]]
- 00bcdd40 ["CALLIND", null, ["register:0:8"]]
+ 00bcde08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcde08 ["INT_ADD", "register:40f0:8", ["const:bcde08:8", "const:4:8"]]
+ 00bcde08 ["CALLIND", null, ["register:0:8"]]
- 00bcdd40 bytes 00013fd6
+ 00bcde08 bytes 00013fd6
- 00bcdd64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcdd64 ["INT_ADD", "register:40f0:8", ["const:bcdd64:8", "const:4:8"]]
- 00bcdd64 ["CALLIND", null, ["register:0:8"]]
+ 00bcde2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcde2c ["INT_ADD", "register:40f0:8", ["const:bcde2c:8", "const:4:8"]]
+ 00bcde2c ["CALLIND", null, ["register:0:8"]]
- 00bcdd64 bytes 00013fd6
+ 00bcde2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48128768252a0ea1a713c93e4380ac2e"></a>

### [`00bcddd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcddd0.md) → [`00bcde98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md) FUN_00bcde98

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcde18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcddd0.md#insn-00bcde18) · [`00bcde7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcddd0.md#insn-00bcde7c) · [`00bcded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcddd0.md#insn-00bcded0)
- 新版 [`00bcdee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdee0) · [`00bcdf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdf44) · [`00bcdf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md#insn-00bcdf98)

~~~diff
- 00bcde18 ["INT_ADD", "register:40f0:8", ["const:bcde18:8", "const:4:8"]]
- 00bcde18 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcdee0 ["INT_ADD", "register:40f0:8", ["const:bcdee0:8", "const:4:8"]]
+ 00bcdee0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcde18 bytes ce3c0094
+ 00bcdee0 bytes c83c0094
- 00bcde7c ["INT_ADD", "register:40f0:8", ["const:bcde7c:8", "const:4:8"]]
- 00bcde7c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcdf44 ["INT_ADD", "register:40f0:8", ["const:bcdf44:8", "const:4:8"]]
+ 00bcdf44 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcde7c bytes b53c0094
+ 00bcdf44 bytes af3c0094
- 00bcded0 ["INT_ADD", "register:40f0:8", ["const:bcded0:8", "const:4:8"]]
- 00bcded0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcdf98 ["INT_ADD", "register:40f0:8", ["const:bcdf98:8", "const:4:8"]]
+ 00bcdf98 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcded0 bytes a03c0094
+ 00bcdf98 bytes 9a3c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea6dbc05f3204744a1c9dc70bc76d61a"></a>

### [`00bce5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce5cc.md) → [`00bce694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md) FUN_00bce694

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce5cc.md#insn-00bce610) · [`00bce65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce5cc.md#insn-00bce65c) · [`00bce6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce5cc.md#insn-00bce6a0)
- 新版 [`00bce6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce6d8) · [`00bce724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce724) · [`00bce768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md#insn-00bce768)

~~~diff
- 00bce610 ["INT_ADD", "register:40f0:8", ["const:bce610:8", "const:4:8"]]
- 00bce610 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bce6d8 ["INT_ADD", "register:40f0:8", ["const:bce6d8:8", "const:4:8"]]
+ 00bce6d8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bce610 bytes d03a0094
+ 00bce6d8 bytes ca3a0094
- 00bce65c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce65c ["INT_ADD", "register:40f0:8", ["const:bce65c:8", "const:4:8"]]
- 00bce65c ["CALLIND", null, ["register:0:8"]]
+ 00bce724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce724 ["INT_ADD", "register:40f0:8", ["const:bce724:8", "const:4:8"]]
+ 00bce724 ["CALLIND", null, ["register:0:8"]]
- 00bce65c bytes 00013fd6
+ 00bce724 bytes 00013fd6
- 00bce6a0 ["INT_ADD", "register:40f0:8", ["const:bce6a0:8", "const:4:8"]]
- 00bce6a0 ["CALL", null, ["callee:00bde270:8"]]
+ 00bce768 ["INT_ADD", "register:40f0:8", ["const:bce768:8", "const:4:8"]]
+ 00bce768 ["CALL", null, ["callee:00bde270:8"]]
- 00bce6a0 bytes c83e0094
+ 00bce768 bytes c23e0094
~~~


<a id="compare-c4c2f3fcff001c0e4e67628fc50e4086"></a>

### [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) → [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) FUN_00bce774

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) [`00bce830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md) · 呼出先 8件 [`00bc1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md) [`00bc1f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md) [`00bc20b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 2件 [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) · 呼出先 8件 [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bce6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md#insn-00bce6e8) · [`00bce71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md#insn-00bce71c) · [`00bce72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md#insn-00bce72c)
- 新版 [`00bce7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7b0) · [`00bce7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7e4) · [`00bce7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md#insn-00bce7f4)

~~~diff
- 00bce6e8 ["INT_ADD", "register:40f0:8", ["const:bce6e8:8", "const:4:8"]]
- 00bce6e8 ["CALL", null, ["callee:00bc1c88:8"]]
+ 00bce7b0 ["INT_ADD", "register:40f0:8", ["const:bce7b0:8", "const:4:8"]]
+ 00bce7b0 ["CALL", null, ["callee:00bc1c88:8"]]
- 00bce6e8 bytes 36cdff97
+ 00bce7b0 bytes 36cdff97
- 00bce71c ["INT_ADD", "register:40f0:8", ["const:bce71c:8", "const:4:8"]]
- 00bce71c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bce7e4 ["INT_ADD", "register:40f0:8", ["const:bce7e4:8", "const:4:8"]]
+ 00bce7e4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bce71c bytes 8d3a0094
+ 00bce7e4 bytes 873a0094
- 00bce72c ["INT_ADD", "register:40f0:8", ["const:bce72c:8", "const:4:8"]]
- 00bce72c ["CALL", null, ["callee:00bde270:8"]]
+ 00bce7f4 ["INT_ADD", "register:40f0:8", ["const:bce7f4:8", "const:4:8"]]
+ 00bce7f4 ["CALL", null, ["callee:00bde270:8"]]
- 00bce72c bytes a53e0094
+ 00bce7f4 bytes 9f3e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be8cbd3f220ee67074a89b1bb2566ac"></a>

### [`00bceac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceac0.md) → [`00bceb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md) FUN_00bceb88

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bceaec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceac0.md#insn-00bceaec) · [`00bceb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceac0.md#insn-00bceb10) · [`00bceb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceac0.md#insn-00bceb3c)
- 新版 [`00bcebb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcebb4) · [`00bcebd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcebd8) · [`00bcec04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md#insn-00bcec04)

~~~diff
- 00bceaec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bceaec ["INT_ADD", "register:40f0:8", ["const:bceaec:8", "const:4:8"]]
- 00bceaec ["CALLIND", null, ["register:0:8"]]
+ 00bcebb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcebb4 ["INT_ADD", "register:40f0:8", ["const:bcebb4:8", "const:4:8"]]
+ 00bcebb4 ["CALLIND", null, ["register:0:8"]]
- 00bceaec bytes 00013fd6
+ 00bcebb4 bytes 00013fd6
- 00bceb10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bceb10 ["INT_ADD", "register:40f0:8", ["const:bceb10:8", "const:4:8"]]
- 00bceb10 ["CALLIND", null, ["register:0:8"]]
+ 00bcebd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcebd8 ["INT_ADD", "register:40f0:8", ["const:bcebd8:8", "const:4:8"]]
+ 00bcebd8 ["CALLIND", null, ["register:0:8"]]
- 00bceb10 bytes 00013fd6
+ 00bcebd8 bytes 00013fd6
- 00bceb3c ["INT_ADD", "register:40f0:8", ["const:bceb3c:8", "const:4:8"]]
- 00bceb3c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcec04 ["INT_ADD", "register:40f0:8", ["const:bcec04:8", "const:4:8"]]
+ 00bcec04 ["CALL", null, ["callee:00bdd200:8"]]
- 00bceb3c bytes 85390094
+ 00bcec04 bytes 7f390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96baddaa35870da3c50d90c30e7ca0da"></a>

### [`00bcef60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcef60.md) → [`00bcf028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md) FUN_00bcf028

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcefa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcef60.md#insn-00bcefa8) · [`00bceff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcef60.md#insn-00bceff0)
- 新版 [`00bcf070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md#insn-00bcf070) · [`00bcf0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf028.md#insn-00bcf0b8)

~~~diff
- 00bcefa8 ["INT_ADD", "register:40f0:8", ["const:bcefa8:8", "const:4:8"]]
- 00bcefa8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf070 ["INT_ADD", "register:40f0:8", ["const:bcf070:8", "const:4:8"]]
+ 00bcf070 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcefa8 bytes 6a380094
+ 00bcf070 bytes 64380094
- 00bceff0 ["INT_ADD", "register:40f0:8", ["const:bceff0:8", "const:4:8"]]
- 00bceff0 ["CALL", null, ["callee:00bde270:8"]]
+ 00bcf0b8 ["INT_ADD", "register:40f0:8", ["const:bcf0b8:8", "const:4:8"]]
+ 00bcf0b8 ["CALL", null, ["callee:00bde270:8"]]
- 00bceff0 bytes 743c0094
+ 00bcf0b8 bytes 6e3c0094
~~~


<a id="compare-13ecdec2edb0760ef3b91c4fbe5e31dd"></a>

### [`00bcf1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf1c8.md) → [`00bcf290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md) FUN_00bcf290

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf20c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf1c8.md#insn-00bcf20c) · [`00bcf248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf1c8.md#insn-00bcf248) · [`00bcf28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf1c8.md#insn-00bcf28c)
- 新版 [`00bcf2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf2d4) · [`00bcf310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf310) · [`00bcf354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf290.md#insn-00bcf354)

~~~diff
- 00bcf20c ["INT_ADD", "register:40f0:8", ["const:bcf20c:8", "const:4:8"]]
- 00bcf20c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf2d4 ["INT_ADD", "register:40f0:8", ["const:bcf2d4:8", "const:4:8"]]
+ 00bcf2d4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf20c bytes d1370094
+ 00bcf2d4 bytes cb370094
- 00bcf248 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf248 ["INT_ADD", "register:40f0:8", ["const:bcf248:8", "const:4:8"]]
- 00bcf248 ["CALLIND", null, ["register:0:8"]]
+ 00bcf310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf310 ["INT_ADD", "register:40f0:8", ["const:bcf310:8", "const:4:8"]]
+ 00bcf310 ["CALLIND", null, ["register:0:8"]]
- 00bcf248 bytes 00013fd6
+ 00bcf310 bytes 00013fd6
- 00bcf28c ["INT_ADD", "register:40f0:8", ["const:bcf28c:8", "const:4:8"]]
- 00bcf28c ["CALL", null, ["callee:00bde270:8"]]
+ 00bcf354 ["INT_ADD", "register:40f0:8", ["const:bcf354:8", "const:4:8"]]
+ 00bcf354 ["CALL", null, ["callee:00bde270:8"]]
- 00bcf28c bytes cd3b0094
+ 00bcf354 bytes c73b0094
~~~


<a id="compare-b2fb87b0d0b056739740f0db6b52eefc"></a>

### [`00bcf8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf8c4.md) → [`00bcf98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf98c.md) FUN_00bcf98c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcf2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf2ac.md) · 呼出先 1件 [`00bc11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc11e0.md)
- 新版 呼出元 1件 [`00bcf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf374.md) · 呼出先 1件 [`00bc12a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc12a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf8c4.md#insn-00bcf8e0)
- 新版 [`00bcf9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf98c.md#insn-00bcf9a8)

~~~diff
- 00bcf8e0 ["INT_ADD", "register:40f0:8", ["const:bcf8e0:8", "const:4:8"]]
- 00bcf8e0 ["CALL", null, ["callee:00bc12a8:8"]]
+ 00bcf9a8 ["INT_ADD", "register:40f0:8", ["const:bcf9a8:8", "const:4:8"]]
+ 00bcf9a8 ["CALL", null, ["callee:00bc12a8:8"]]
- 00bcf8e0 bytes 40c6ff97
+ 00bcf9a8 bytes 40c6ff97
~~~


<a id="compare-8653bf011e6a772c40d8bea91bdd01b2"></a>

### [`00bcf92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf92c.md) → [`00bcf9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md) FUN_00bcf9f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf92c.md#insn-00bcf954) · [`00bcf980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf92c.md#insn-00bcf980) · [`00bcf9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf92c.md#insn-00bcf9e8)
- 新版 [`00bcfa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfa1c) · [`00bcfa48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfa48) · [`00bcfab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf9f4.md#insn-00bcfab0)

~~~diff
- 00bcf954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf954 ["INT_ADD", "register:40f0:8", ["const:bcf954:8", "const:4:8"]]
- 00bcf954 ["CALLIND", null, ["register:0:8"]]
+ 00bcfa1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfa1c ["INT_ADD", "register:40f0:8", ["const:bcfa1c:8", "const:4:8"]]
+ 00bcfa1c ["CALLIND", null, ["register:0:8"]]
- 00bcf954 bytes 00013fd6
+ 00bcfa1c bytes 00013fd6
- 00bcf980 ["INT_ADD", "register:40f0:8", ["const:bcf980:8", "const:4:8"]]
- 00bcf980 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfa48 ["INT_ADD", "register:40f0:8", ["const:bcfa48:8", "const:4:8"]]
+ 00bcfa48 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf980 bytes f4350094
+ 00bcfa48 bytes ee350094
- 00bcf9e8 ["INT_ADD", "register:40f0:8", ["const:bcf9e8:8", "const:4:8"]]
- 00bcf9e8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfab0 ["INT_ADD", "register:40f0:8", ["const:bcfab0:8", "const:4:8"]]
+ 00bcfab0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf9e8 bytes da350094
+ 00bcfab0 bytes d4350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ab12b192c6d6ee9d23efa82abc12985"></a>

### [`00bcfa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa9c.md) → [`00bcfb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md) FUN_00bcfb64

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa9c.md#insn-00bcfae8) · [`00bcfb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa9c.md#insn-00bcfb10) · [`00bcfb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfa9c.md#insn-00bcfb48)
- 新版 [`00bcfbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfbb0) · [`00bcfbd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfbd8) · [`00bcfc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md#insn-00bcfc10)

~~~diff
- 00bcfae8 ["INT_ADD", "register:40f0:8", ["const:bcfae8:8", "const:4:8"]]
- 00bcfae8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfbb0 ["INT_ADD", "register:40f0:8", ["const:bcfbb0:8", "const:4:8"]]
+ 00bcfbb0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcfae8 bytes 9a350094
+ 00bcfbb0 bytes 94350094
- 00bcfb10 ["INT_ADD", "register:40f0:8", ["const:bcfb10:8", "const:4:8"]]
- 00bcfb10 ["CALL", null, ["callee:00bc8290:8"]]
+ 00bcfbd8 ["INT_ADD", "register:40f0:8", ["const:bcfbd8:8", "const:4:8"]]
+ 00bcfbd8 ["CALL", null, ["callee:00bc8290:8"]]
- 00bcfb10 bytes aee1ff97
+ 00bcfbd8 bytes aee1ff97
- 00bcfb48 ["INT_ADD", "register:40f0:8", ["const:bcfb48:8", "const:4:8"]]
- 00bcfb48 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfc10 ["INT_ADD", "register:40f0:8", ["const:bcfc10:8", "const:4:8"]]
+ 00bcfc10 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcfb48 bytes 82350094
+ 00bcfc10 bytes 7c350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-702abc73df01807f42d7ba1be651930c"></a>

### [`00bcfc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfc48.md) → [`00bcfd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md) FUN_00bcfd10

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfc48.md#insn-00bcfc98) · [`00bcfccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfc48.md#insn-00bcfccc) · [`00bcfd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfc48.md#insn-00bcfd04)
- 新版 [`00bcfd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfd60) · [`00bcfd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfd94) · [`00bcfdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfd10.md#insn-00bcfdcc)

~~~diff
- 00bcfc98 ["INT_ADD", "register:40f0:8", ["const:bcfc98:8", "const:4:8"]]
- 00bcfc98 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfd60 ["INT_ADD", "register:40f0:8", ["const:bcfd60:8", "const:4:8"]]
+ 00bcfd60 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcfc98 bytes 2e350094
+ 00bcfd60 bytes 28350094
- 00bcfccc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfccc ["INT_ADD", "register:40f0:8", ["const:bcfccc:8", "const:4:8"]]
- 00bcfccc ["CALLIND", null, ["register:0:8"]]
+ 00bcfd94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfd94 ["INT_ADD", "register:40f0:8", ["const:bcfd94:8", "const:4:8"]]
+ 00bcfd94 ["CALLIND", null, ["register:0:8"]]
- 00bcfccc bytes 00013fd6
+ 00bcfd94 bytes 00013fd6
- 00bcfd04 ["INT_ADD", "register:40f0:8", ["const:bcfd04:8", "const:4:8"]]
- 00bcfd04 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfdcc ["INT_ADD", "register:40f0:8", ["const:bcfdcc:8", "const:4:8"]]
+ 00bcfdcc ["CALL", null, ["callee:00bdd200:8"]]
- 00bcfd04 bytes 13350094
+ 00bcfdcc bytes 0d350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a2eeb42f7c3f2d99a55110b41f3a74"></a>

### [`00bcfd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfd54.md) → [`00bcfe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md) FUN_00bcfe1c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcfd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfd54.md#insn-00bcfd80) · [`00bcfda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfd54.md#insn-00bcfda4) · [`00bcfdd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfd54.md#insn-00bcfdd0)
- 新版 [`00bcfe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe48) · [`00bcfe6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe6c) · [`00bcfe98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfe1c.md#insn-00bcfe98)

~~~diff
- 00bcfd80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfd80 ["INT_ADD", "register:40f0:8", ["const:bcfd80:8", "const:4:8"]]
- 00bcfd80 ["CALLIND", null, ["register:0:8"]]
+ 00bcfe48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfe48 ["INT_ADD", "register:40f0:8", ["const:bcfe48:8", "const:4:8"]]
+ 00bcfe48 ["CALLIND", null, ["register:0:8"]]
- 00bcfd80 bytes 00013fd6
+ 00bcfe48 bytes 00013fd6
- 00bcfda4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfda4 ["INT_ADD", "register:40f0:8", ["const:bcfda4:8", "const:4:8"]]
- 00bcfda4 ["CALLIND", null, ["register:0:8"]]
+ 00bcfe6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfe6c ["INT_ADD", "register:40f0:8", ["const:bcfe6c:8", "const:4:8"]]
+ 00bcfe6c ["CALLIND", null, ["register:0:8"]]
- 00bcfda4 bytes 00013fd6
+ 00bcfe6c bytes 00013fd6
- 00bcfdd0 ["INT_ADD", "register:40f0:8", ["const:bcfdd0:8", "const:4:8"]]
- 00bcfdd0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcfe98 ["INT_ADD", "register:40f0:8", ["const:bcfe98:8", "const:4:8"]]
+ 00bcfe98 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcfdd0 bytes e0340094
+ 00bcfe98 bytes da340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf167b0436f5f061b6880ced1b10892"></a>

### [`00bcffa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcffa4.md) → [`00bd006c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md) FUN_00bd006c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcffd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcffa4.md#insn-00bcffd0) · [`00bcfff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcffa4.md#insn-00bcfff4) · [`00bd0020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcffa4.md#insn-00bd0020)
- 新版 [`00bd0098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd0098) · [`00bd00bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd00bc) · [`00bd00e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md#insn-00bd00e8)

~~~diff
- 00bcffd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcffd0 ["INT_ADD", "register:40f0:8", ["const:bcffd0:8", "const:4:8"]]
- 00bcffd0 ["CALLIND", null, ["register:0:8"]]
+ 00bd0098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0098 ["INT_ADD", "register:40f0:8", ["const:bd0098:8", "const:4:8"]]
+ 00bd0098 ["CALLIND", null, ["register:0:8"]]
- 00bcffd0 bytes 00013fd6
+ 00bd0098 bytes 00013fd6
- 00bcfff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfff4 ["INT_ADD", "register:40f0:8", ["const:bcfff4:8", "const:4:8"]]
- 00bcfff4 ["CALLIND", null, ["register:0:8"]]
+ 00bd00bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd00bc ["INT_ADD", "register:40f0:8", ["const:bd00bc:8", "const:4:8"]]
+ 00bd00bc ["CALLIND", null, ["register:0:8"]]
- 00bcfff4 bytes 00013fd6
+ 00bd00bc bytes 00013fd6
- 00bd0020 ["INT_ADD", "register:40f0:8", ["const:bd0020:8", "const:4:8"]]
- 00bd0020 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd00e8 ["INT_ADD", "register:40f0:8", ["const:bd00e8:8", "const:4:8"]]
+ 00bd00e8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0020 bytes 4c340094
+ 00bd00e8 bytes 46340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60d21e1b9c8cbe5a90f1a5f79e3b0011"></a>

### [`00bd02c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd02c8.md) → [`00bd0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md) FUN_00bd0390

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd02f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd02c8.md#insn-00bd02f4) · [`00bd0318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd02c8.md#insn-00bd0318) · [`00bd0344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd02c8.md#insn-00bd0344)
- 新版 [`00bd03bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd03bc) · [`00bd03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd03e0) · [`00bd040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0390.md#insn-00bd040c)

~~~diff
- 00bd02f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd02f4 ["INT_ADD", "register:40f0:8", ["const:bd02f4:8", "const:4:8"]]
- 00bd02f4 ["CALLIND", null, ["register:0:8"]]
+ 00bd03bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd03bc ["INT_ADD", "register:40f0:8", ["const:bd03bc:8", "const:4:8"]]
+ 00bd03bc ["CALLIND", null, ["register:0:8"]]
- 00bd02f4 bytes 00013fd6
+ 00bd03bc bytes 00013fd6
- 00bd0318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0318 ["INT_ADD", "register:40f0:8", ["const:bd0318:8", "const:4:8"]]
- 00bd0318 ["CALLIND", null, ["register:0:8"]]
+ 00bd03e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd03e0 ["INT_ADD", "register:40f0:8", ["const:bd03e0:8", "const:4:8"]]
+ 00bd03e0 ["CALLIND", null, ["register:0:8"]]
- 00bd0318 bytes 00013fd6
+ 00bd03e0 bytes 00013fd6
- 00bd0344 ["INT_ADD", "register:40f0:8", ["const:bd0344:8", "const:4:8"]]
- 00bd0344 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd040c ["INT_ADD", "register:40f0:8", ["const:bd040c:8", "const:4:8"]]
+ 00bd040c ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0344 bytes 83330094
+ 00bd040c bytes 7d330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d29b2ce6bb446ec9b71cffaa39d9dd95"></a>

### [`00bd0604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0604.md) → [`00bd06cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md) FUN_00bd06cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0604.md#insn-00bd0650) · [`00bd067c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0604.md#insn-00bd067c) · [`00bd06a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0604.md#insn-00bd06a8)
- 新版 [`00bd0718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0718) · [`00bd0744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0744) · [`00bd0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd06cc.md#insn-00bd0770)

~~~diff
- 00bd0650 ["INT_ADD", "register:40f0:8", ["const:bd0650:8", "const:4:8"]]
- 00bd0650 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0718 ["INT_ADD", "register:40f0:8", ["const:bd0718:8", "const:4:8"]]
+ 00bd0718 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0650 bytes c0320094
+ 00bd0718 bytes ba320094
- 00bd067c ["INT_ADD", "register:40f0:8", ["const:bd067c:8", "const:4:8"]]
- 00bd067c ["CALL", null, ["callee:00bc8290:8"]]
+ 00bd0744 ["INT_ADD", "register:40f0:8", ["const:bd0744:8", "const:4:8"]]
+ 00bd0744 ["CALL", null, ["callee:00bc8290:8"]]
- 00bd067c bytes d3deff97
+ 00bd0744 bytes d3deff97
- 00bd06a8 ["INT_ADD", "register:40f0:8", ["const:bd06a8:8", "const:4:8"]]
- 00bd06a8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0770 ["INT_ADD", "register:40f0:8", ["const:bd0770:8", "const:4:8"]]
+ 00bd0770 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd06a8 bytes aa320094
+ 00bd0770 bytes a4320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dd2d4fc25aba59e1f18919be8da10d2"></a>

### [`00bd06fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd06fc.md) → [`00bd07c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md) FUN_00bd07c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd06fc.md#insn-00bd0728) · [`00bd074c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd06fc.md#insn-00bd074c) · [`00bd0764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd06fc.md#insn-00bd0764)
- 新版 [`00bd07f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd07f0) · [`00bd0814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd0814) · [`00bd082c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd07c4.md#insn-00bd082c)

~~~diff
- 00bd0728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0728 ["INT_ADD", "register:40f0:8", ["const:bd0728:8", "const:4:8"]]
- 00bd0728 ["CALLIND", null, ["register:0:8"]]
+ 00bd07f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd07f0 ["INT_ADD", "register:40f0:8", ["const:bd07f0:8", "const:4:8"]]
+ 00bd07f0 ["CALLIND", null, ["register:0:8"]]
- 00bd0728 bytes 00013fd6
+ 00bd07f0 bytes 00013fd6
- 00bd074c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd074c ["INT_ADD", "register:40f0:8", ["const:bd074c:8", "const:4:8"]]
- 00bd074c ["CALLIND", null, ["register:0:8"]]
+ 00bd0814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0814 ["INT_ADD", "register:40f0:8", ["const:bd0814:8", "const:4:8"]]
+ 00bd0814 ["CALLIND", null, ["register:0:8"]]
- 00bd074c bytes 00013fd6
+ 00bd0814 bytes 00013fd6
- 00bd0764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0764 ["INT_ADD", "register:40f0:8", ["const:bd0764:8", "const:4:8"]]
- 00bd0764 ["CALLIND", null, ["register:0:8"]]
+ 00bd082c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd082c ["INT_ADD", "register:40f0:8", ["const:bd082c:8", "const:4:8"]]
+ 00bd082c ["CALLIND", null, ["register:0:8"]]
- 00bd0764 bytes 00013fd6
+ 00bd082c bytes 00013fd6
~~~


<a id="compare-09508482a3658314ab5e998476122adf"></a>

### [`00bd0948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0948.md) → [`00bd0a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md) FUN_00bd0a10

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd098c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0948.md#insn-00bd098c) · [`00bd09d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0948.md#insn-00bd09d8) · [`00bd0a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0948.md#insn-00bd0a1c)
- 新版 [`00bd0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0a54) · [`00bd0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0aa0) · [`00bd0ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0a10.md#insn-00bd0ae4)

~~~diff
- 00bd098c ["INT_ADD", "register:40f0:8", ["const:bd098c:8", "const:4:8"]]
- 00bd098c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0a54 ["INT_ADD", "register:40f0:8", ["const:bd0a54:8", "const:4:8"]]
+ 00bd0a54 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd098c bytes f1310094
+ 00bd0a54 bytes eb310094
- 00bd09d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd09d8 ["INT_ADD", "register:40f0:8", ["const:bd09d8:8", "const:4:8"]]
- 00bd09d8 ["CALLIND", null, ["register:0:8"]]
+ 00bd0aa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0aa0 ["INT_ADD", "register:40f0:8", ["const:bd0aa0:8", "const:4:8"]]
+ 00bd0aa0 ["CALLIND", null, ["register:0:8"]]
- 00bd09d8 bytes 00013fd6
+ 00bd0aa0 bytes 00013fd6
- 00bd0a1c ["INT_ADD", "register:40f0:8", ["const:bd0a1c:8", "const:4:8"]]
- 00bd0a1c ["CALL", null, ["callee:00bde270:8"]]
+ 00bd0ae4 ["INT_ADD", "register:40f0:8", ["const:bd0ae4:8", "const:4:8"]]
+ 00bd0ae4 ["CALL", null, ["callee:00bde270:8"]]
- 00bd0a1c bytes e9350094
+ 00bd0ae4 bytes e3350094
~~~


<a id="compare-04e54bb863ed6e37b1aee1e757c98fa6"></a>

### [`00bd0a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a40.md) → [`00bd0b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md) FUN_00bd0b08

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a40.md#insn-00bd0a6c) · [`00bd0a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a40.md#insn-00bd0a90) · [`00bd0acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0a40.md#insn-00bd0acc)
- 新版 [`00bd0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b34) · [`00bd0b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b58) · [`00bd0b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0b08.md#insn-00bd0b94)

~~~diff
- 00bd0a6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0a6c ["INT_ADD", "register:40f0:8", ["const:bd0a6c:8", "const:4:8"]]
- 00bd0a6c ["CALLIND", null, ["register:0:8"]]
+ 00bd0b34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b34 ["INT_ADD", "register:40f0:8", ["const:bd0b34:8", "const:4:8"]]
+ 00bd0b34 ["CALLIND", null, ["register:0:8"]]
- 00bd0a6c bytes 00013fd6
+ 00bd0b34 bytes 00013fd6
- 00bd0a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0a90 ["INT_ADD", "register:40f0:8", ["const:bd0a90:8", "const:4:8"]]
- 00bd0a90 ["CALLIND", null, ["register:0:8"]]
+ 00bd0b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b58 ["INT_ADD", "register:40f0:8", ["const:bd0b58:8", "const:4:8"]]
+ 00bd0b58 ["CALLIND", null, ["register:0:8"]]
- 00bd0a90 bytes 00013fd6
+ 00bd0b58 bytes 00013fd6
- 00bd0acc ["INT_ADD", "register:40f0:8", ["const:bd0acc:8", "const:4:8"]]
- 00bd0acc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0b94 ["INT_ADD", "register:40f0:8", ["const:bd0b94:8", "const:4:8"]]
+ 00bd0b94 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0acc bytes a1310094
+ 00bd0b94 bytes 9b310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68a6617e2e9f59d4b9c7ee83becc079b"></a>

### [`00bd0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0f50.md) → [`00bd1018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md) FUN_00bd1018

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0f50.md#insn-00bd0f7c) · [`00bd0fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0f50.md#insn-00bd0fa0) · [`00bd0fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0f50.md#insn-00bd0fcc)
- 新版 [`00bd1044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1044) · [`00bd1068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1068) · [`00bd1094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1018.md#insn-00bd1094)

~~~diff
- 00bd0f7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0f7c ["INT_ADD", "register:40f0:8", ["const:bd0f7c:8", "const:4:8"]]
- 00bd0f7c ["CALLIND", null, ["register:0:8"]]
+ 00bd1044 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1044 ["INT_ADD", "register:40f0:8", ["const:bd1044:8", "const:4:8"]]
+ 00bd1044 ["CALLIND", null, ["register:0:8"]]
- 00bd0f7c bytes 00013fd6
+ 00bd1044 bytes 00013fd6
- 00bd0fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0fa0 ["INT_ADD", "register:40f0:8", ["const:bd0fa0:8", "const:4:8"]]
- 00bd0fa0 ["CALLIND", null, ["register:0:8"]]
+ 00bd1068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1068 ["INT_ADD", "register:40f0:8", ["const:bd1068:8", "const:4:8"]]
+ 00bd1068 ["CALLIND", null, ["register:0:8"]]
- 00bd0fa0 bytes 00013fd6
+ 00bd1068 bytes 00013fd6
- 00bd0fcc ["INT_ADD", "register:40f0:8", ["const:bd0fcc:8", "const:4:8"]]
- 00bd0fcc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd1094 ["INT_ADD", "register:40f0:8", ["const:bd1094:8", "const:4:8"]]
+ 00bd1094 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0fcc bytes 61300094
+ 00bd1094 bytes 5b300094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4cae9105ac0434a40e2e12203123157"></a>

### [`00bd25c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd25c0.md) → [`00bd2688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md) FUN_00bd2688

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd25c0.md#insn-00bd2604) · [`00bd2668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd25c0.md#insn-00bd2668) · [`00bd26ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd25c0.md#insn-00bd26ac)
- 新版 [`00bd26cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd26cc) · [`00bd2730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd2730) · [`00bd2774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2688.md#insn-00bd2774)

~~~diff
- 00bd2604 ["INT_ADD", "register:40f0:8", ["const:bd2604:8", "const:4:8"]]
- 00bd2604 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd26cc ["INT_ADD", "register:40f0:8", ["const:bd26cc:8", "const:4:8"]]
+ 00bd26cc ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2604 bytes d32a0094
+ 00bd26cc bytes cd2a0094
- 00bd2668 ["INT_ADD", "register:40f0:8", ["const:bd2668:8", "const:4:8"]]
- 00bd2668 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2730 ["INT_ADD", "register:40f0:8", ["const:bd2730:8", "const:4:8"]]
+ 00bd2730 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2668 bytes ba2a0094
+ 00bd2730 bytes b42a0094
- 00bd26ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd26ac ["INT_ADD", "register:40f0:8", ["const:bd26ac:8", "const:4:8"]]
- 00bd26ac ["CALLIND", null, ["register:0:8"]]
+ 00bd2774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2774 ["INT_ADD", "register:40f0:8", ["const:bd2774:8", "const:4:8"]]
+ 00bd2774 ["CALLIND", null, ["register:0:8"]]
- 00bd26ac bytes 00013fd6
+ 00bd2774 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d68587719260f600d3f5fe3460480fb"></a>

### [`00bd2838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2838.md) → [`00bd2900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md) FUN_00bd2900

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd287c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2838.md#insn-00bd287c) · [`00bd28e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2838.md#insn-00bd28e4) · [`00bd290c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2838.md#insn-00bd290c)
- 新版 [`00bd2944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd2944) · [`00bd29ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd29ac) · [`00bd29d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2900.md#insn-00bd29d4)

~~~diff
- 00bd287c ["INT_ADD", "register:40f0:8", ["const:bd287c:8", "const:4:8"]]
- 00bd287c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2944 ["INT_ADD", "register:40f0:8", ["const:bd2944:8", "const:4:8"]]
+ 00bd2944 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd287c bytes 352a0094
+ 00bd2944 bytes 2f2a0094
- 00bd28e4 ["INT_ADD", "register:40f0:8", ["const:bd28e4:8", "const:4:8"]]
- 00bd28e4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd29ac ["INT_ADD", "register:40f0:8", ["const:bd29ac:8", "const:4:8"]]
+ 00bd29ac ["CALL", null, ["callee:00bdd200:8"]]
- 00bd28e4 bytes 1b2a0094
+ 00bd29ac bytes 152a0094
- 00bd290c ["INT_ADD", "register:40f0:8", ["const:bd290c:8", "const:4:8"]]
- 00bd290c ["CALL", null, ["callee:00bc8290:8"]]
+ 00bd29d4 ["INT_ADD", "register:40f0:8", ["const:bd29d4:8", "const:4:8"]]
+ 00bd29d4 ["CALL", null, ["callee:00bc8290:8"]]
- 00bd290c bytes 2fd6ff97
+ 00bd29d4 bytes 2fd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a321faa125bef3a52a59a3e5fff404ee"></a>

### [`00bd29a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd29a0.md) → [`00bd2a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md) FUN_00bd2a68

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd29c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd29a0.md#insn-00bd29c0) · [`00bd29ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd29a0.md#insn-00bd29ec) · [`00bd2a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd29a0.md#insn-00bd2a20)
- 新版 [`00bd2a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2a88) · [`00bd2ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2ab4) · [`00bd2ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md#insn-00bd2ae8)

~~~diff
- 00bd29c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd29c0 ["INT_ADD", "register:40f0:8", ["const:bd29c0:8", "const:4:8"]]
- 00bd29c0 ["CALLIND", null, ["register:0:8"]]
+ 00bd2a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2a88 ["INT_ADD", "register:40f0:8", ["const:bd2a88:8", "const:4:8"]]
+ 00bd2a88 ["CALLIND", null, ["register:0:8"]]
- 00bd29c0 bytes 00013fd6
+ 00bd2a88 bytes 00013fd6
- 00bd29ec ["INT_ADD", "register:40f0:8", ["const:bd29ec:8", "const:4:8"]]
- 00bd29ec ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2ab4 ["INT_ADD", "register:40f0:8", ["const:bd2ab4:8", "const:4:8"]]
+ 00bd2ab4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd29ec bytes d9290094
+ 00bd2ab4 bytes d3290094
- 00bd2a20 ["INT_ADD", "register:40f0:8", ["const:bd2a20:8", "const:4:8"]]
- 00bd2a20 ["CALL", null, ["callee:00bde270:8"]]
+ 00bd2ae8 ["INT_ADD", "register:40f0:8", ["const:bd2ae8:8", "const:4:8"]]
+ 00bd2ae8 ["CALL", null, ["callee:00bde270:8"]]
- 00bd2a20 bytes e82d0094
+ 00bd2ae8 bytes e22d0094
~~~


<a id="compare-e2f2f787bd626e3a8c6c828187d7ac00"></a>

### [`00bd2dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2dc0.md) → [`00bd2e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md) FUN_00bd2e88

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2dc0.md#insn-00bd2dec) · [`00bd2e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2dc0.md#insn-00bd2e10) · [`00bd2e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2dc0.md#insn-00bd2e3c)
- 新版 [`00bd2eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2eb4) · [`00bd2ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2ed8) · [`00bd2f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md#insn-00bd2f04)

~~~diff
- 00bd2dec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2dec ["INT_ADD", "register:40f0:8", ["const:bd2dec:8", "const:4:8"]]
- 00bd2dec ["CALLIND", null, ["register:0:8"]]
+ 00bd2eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2eb4 ["INT_ADD", "register:40f0:8", ["const:bd2eb4:8", "const:4:8"]]
+ 00bd2eb4 ["CALLIND", null, ["register:0:8"]]
- 00bd2dec bytes 00013fd6
+ 00bd2eb4 bytes 00013fd6
- 00bd2e10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2e10 ["INT_ADD", "register:40f0:8", ["const:bd2e10:8", "const:4:8"]]
- 00bd2e10 ["CALLIND", null, ["register:0:8"]]
+ 00bd2ed8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2ed8 ["INT_ADD", "register:40f0:8", ["const:bd2ed8:8", "const:4:8"]]
+ 00bd2ed8 ["CALLIND", null, ["register:0:8"]]
- 00bd2e10 bytes 00013fd6
+ 00bd2ed8 bytes 00013fd6
- 00bd2e3c ["INT_ADD", "register:40f0:8", ["const:bd2e3c:8", "const:4:8"]]
- 00bd2e3c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2f04 ["INT_ADD", "register:40f0:8", ["const:bd2f04:8", "const:4:8"]]
+ 00bd2f04 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2e3c bytes c5280094
+ 00bd2f04 bytes bf280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bdbb218fe28d24bd190fd8c7e717a71"></a>

### [`00bd2f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2f34.md) → [`00bd2ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md) FUN_00bd2ffc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2f34.md#insn-00bd2f60) · [`00bd2f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2f34.md#insn-00bd2f84) · [`00bd2fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2f34.md#insn-00bd2fb0)
- 新版 [`00bd3028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd3028) · [`00bd304c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd304c) · [`00bd3078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2ffc.md#insn-00bd3078)

~~~diff
- 00bd2f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2f60 ["INT_ADD", "register:40f0:8", ["const:bd2f60:8", "const:4:8"]]
- 00bd2f60 ["CALLIND", null, ["register:0:8"]]
+ 00bd3028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3028 ["INT_ADD", "register:40f0:8", ["const:bd3028:8", "const:4:8"]]
+ 00bd3028 ["CALLIND", null, ["register:0:8"]]
- 00bd2f60 bytes 00013fd6
+ 00bd3028 bytes 00013fd6
- 00bd2f84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2f84 ["INT_ADD", "register:40f0:8", ["const:bd2f84:8", "const:4:8"]]
- 00bd2f84 ["CALLIND", null, ["register:0:8"]]
+ 00bd304c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd304c ["INT_ADD", "register:40f0:8", ["const:bd304c:8", "const:4:8"]]
+ 00bd304c ["CALLIND", null, ["register:0:8"]]
- 00bd2f84 bytes 00013fd6
+ 00bd304c bytes 00013fd6
- 00bd2fb0 ["INT_ADD", "register:40f0:8", ["const:bd2fb0:8", "const:4:8"]]
- 00bd2fb0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3078 ["INT_ADD", "register:40f0:8", ["const:bd3078:8", "const:4:8"]]
+ 00bd3078 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2fb0 bytes 68280094
+ 00bd3078 bytes 62280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc3142dd0b1e18f3134370ad2eda4d5"></a>

### [`00bd32cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32cc.md) → [`00bd3394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md) FUN_00bd3394

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32cc.md#insn-00bd3320) · [`00bd333c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32cc.md#insn-00bd333c) · [`00bd3374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd32cc.md#insn-00bd3374)
- 新版 [`00bd33e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd33e8) · [`00bd3404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd3404) · [`00bd343c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3394.md#insn-00bd343c)

~~~diff
- 00bd3320 ["INT_ADD", "register:40f0:8", ["const:bd3320:8", "const:4:8"]]
- 00bd3320 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd33e8 ["INT_ADD", "register:40f0:8", ["const:bd33e8:8", "const:4:8"]]
+ 00bd33e8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3320 bytes 8c270094
+ 00bd33e8 bytes 86270094
- 00bd333c ["INT_ADD", "register:40f0:8", ["const:bd333c:8", "const:4:8"]]
- 00bd333c ["CALL", null, ["callee:00bdb160:8"]]
+ 00bd3404 ["INT_ADD", "register:40f0:8", ["const:bd3404:8", "const:4:8"]]
+ 00bd3404 ["CALL", null, ["callee:00bdb160:8"]]
- 00bd333c bytes 5d1f0094
+ 00bd3404 bytes 571f0094
- 00bd3374 ["INT_ADD", "register:40f0:8", ["const:bd3374:8", "const:4:8"]]
- 00bd3374 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd343c ["INT_ADD", "register:40f0:8", ["const:bd343c:8", "const:4:8"]]
+ 00bd343c ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3374 bytes 77270094
+ 00bd343c bytes 71270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de4dddbc7a57e10ddc137d1d54b49972"></a>

### [`00bd3440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3440.md) → [`00bd3508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md) FUN_00bd3508

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3440.md#insn-00bd3484) · [`00bd34d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3440.md#insn-00bd34d0) · [`00bd3514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3440.md#insn-00bd3514)
- 新版 [`00bd354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd354c) · [`00bd3598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd3598) · [`00bd35dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3508.md#insn-00bd35dc)

~~~diff
- 00bd3484 ["INT_ADD", "register:40f0:8", ["const:bd3484:8", "const:4:8"]]
- 00bd3484 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd354c ["INT_ADD", "register:40f0:8", ["const:bd354c:8", "const:4:8"]]
+ 00bd354c ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3484 bytes 33270094
+ 00bd354c bytes 2d270094
- 00bd34d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd34d0 ["INT_ADD", "register:40f0:8", ["const:bd34d0:8", "const:4:8"]]
- 00bd34d0 ["CALLIND", null, ["register:0:8"]]
+ 00bd3598 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3598 ["INT_ADD", "register:40f0:8", ["const:bd3598:8", "const:4:8"]]
+ 00bd3598 ["CALLIND", null, ["register:0:8"]]
- 00bd34d0 bytes 00013fd6
+ 00bd3598 bytes 00013fd6
- 00bd3514 ["INT_ADD", "register:40f0:8", ["const:bd3514:8", "const:4:8"]]
- 00bd3514 ["CALL", null, ["callee:00bde270:8"]]
+ 00bd35dc ["INT_ADD", "register:40f0:8", ["const:bd35dc:8", "const:4:8"]]
+ 00bd35dc ["CALL", null, ["callee:00bde270:8"]]
- 00bd3514 bytes 2b2b0094
+ 00bd35dc bytes 252b0094
~~~


<a id="compare-4c8824c7d96ca2291fb40b33166916d4"></a>

### [`00bd3808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3808.md) → [`00bd38d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md) FUN_00bd38d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3808.md#insn-00bd3830) · [`00bd3868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3808.md#insn-00bd3868) · [`00bd3884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3808.md#insn-00bd3884)
- 新版 [`00bd38f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd38f8) · [`00bd3930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd3930) · [`00bd394c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd38d0.md#insn-00bd394c)

~~~diff
- 00bd3830 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3830 ["INT_ADD", "register:40f0:8", ["const:bd3830:8", "const:4:8"]]
- 00bd3830 ["CALLIND", null, ["register:0:8"]]
+ 00bd38f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd38f8 ["INT_ADD", "register:40f0:8", ["const:bd38f8:8", "const:4:8"]]
+ 00bd38f8 ["CALLIND", null, ["register:0:8"]]
- 00bd3830 bytes 00013fd6
+ 00bd38f8 bytes 00013fd6
- 00bd3868 ["INT_ADD", "register:40f0:8", ["const:bd3868:8", "const:4:8"]]
- 00bd3868 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3930 ["INT_ADD", "register:40f0:8", ["const:bd3930:8", "const:4:8"]]
+ 00bd3930 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3868 bytes 3a260094
+ 00bd3930 bytes 34260094
- 00bd3884 ["INT_ADD", "register:40f0:8", ["const:bd3884:8", "const:4:8"]]
- 00bd3884 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bd394c ["INT_ADD", "register:40f0:8", ["const:bd394c:8", "const:4:8"]]
+ 00bd394c ["CALL", null, ["callee:00bdb160:8"]]
- 00bd3884 bytes 0b1e0094
+ 00bd394c bytes 051e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e29bd588ba4a312aac33ae8a60b04d3"></a>

### [`00bd3b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3b24.md) → [`00bd3bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md) FUN_00bd3bec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd3b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3b24.md#insn-00bd3b50) · [`00bd3b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3b24.md#insn-00bd3b74) · [`00bd3ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3b24.md#insn-00bd3ba0)
- 新版 [`00bd3c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c18) · [`00bd3c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c3c) · [`00bd3c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3bec.md#insn-00bd3c68)

~~~diff
- 00bd3b50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3b50 ["INT_ADD", "register:40f0:8", ["const:bd3b50:8", "const:4:8"]]
- 00bd3b50 ["CALLIND", null, ["register:0:8"]]
+ 00bd3c18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3c18 ["INT_ADD", "register:40f0:8", ["const:bd3c18:8", "const:4:8"]]
+ 00bd3c18 ["CALLIND", null, ["register:0:8"]]
- 00bd3b50 bytes 00013fd6
+ 00bd3c18 bytes 00013fd6
- 00bd3b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3b74 ["INT_ADD", "register:40f0:8", ["const:bd3b74:8", "const:4:8"]]
- 00bd3b74 ["CALLIND", null, ["register:0:8"]]
+ 00bd3c3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3c3c ["INT_ADD", "register:40f0:8", ["const:bd3c3c:8", "const:4:8"]]
+ 00bd3c3c ["CALLIND", null, ["register:0:8"]]
- 00bd3b74 bytes 00013fd6
+ 00bd3c3c bytes 00013fd6
- 00bd3ba0 ["INT_ADD", "register:40f0:8", ["const:bd3ba0:8", "const:4:8"]]
- 00bd3ba0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3c68 ["INT_ADD", "register:40f0:8", ["const:bd3c68:8", "const:4:8"]]
+ 00bd3c68 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3ba0 bytes 6c250094
+ 00bd3c68 bytes 66250094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-030fd132e7e20c28054085afcdaad77d"></a>

### [`00bd3fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fe0.md) → [`00bd40a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md) FUN_00bd40a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fe0.md#insn-00bd4004) · [`00bd402c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fe0.md#insn-00bd402c) · [`00bd405c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3fe0.md#insn-00bd405c)
- 新版 [`00bd40cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd40cc) · [`00bd40f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd40f4) · [`00bd4124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd40a8.md#insn-00bd4124)

~~~diff
- 00bd4004 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4004 ["INT_ADD", "register:40f0:8", ["const:bd4004:8", "const:4:8"]]
- 00bd4004 ["CALLIND", null, ["register:0:8"]]
+ 00bd40cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd40cc ["INT_ADD", "register:40f0:8", ["const:bd40cc:8", "const:4:8"]]
+ 00bd40cc ["CALLIND", null, ["register:0:8"]]
- 00bd4004 bytes 00013fd6
+ 00bd40cc bytes 00013fd6
- 00bd402c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd402c ["INT_ADD", "register:40f0:8", ["const:bd402c:8", "const:4:8"]]
- 00bd402c ["CALLIND", null, ["register:0:8"]]
+ 00bd40f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd40f4 ["INT_ADD", "register:40f0:8", ["const:bd40f4:8", "const:4:8"]]
+ 00bd40f4 ["CALLIND", null, ["register:0:8"]]
- 00bd402c bytes 00013fd6
+ 00bd40f4 bytes 00013fd6
- 00bd405c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd405c ["INT_ADD", "register:40f0:8", ["const:bd405c:8", "const:4:8"]]
- 00bd405c ["CALLIND", null, ["register:0:8"]]
+ 00bd4124 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4124 ["INT_ADD", "register:40f0:8", ["const:bd4124:8", "const:4:8"]]
+ 00bd4124 ["CALLIND", null, ["register:0:8"]]
- 00bd405c bytes 00013fd6
+ 00bd4124 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72fb815c0811893b4464d9e984f37942"></a>

### [`00bd41a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd41a0.md) → [`00bd4268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md) FUN_00bd4268

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd41dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd41a0.md#insn-00bd41dc) · [`00bd420c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd41a0.md#insn-00bd420c) · [`00bd423c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd41a0.md#insn-00bd423c)
- 新版 [`00bd42a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd42a4) · [`00bd42d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd42d4) · [`00bd4304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4268.md#insn-00bd4304)

~~~diff
- 00bd41dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd41dc ["INT_ADD", "register:40f0:8", ["const:bd41dc:8", "const:4:8"]]
- 00bd41dc ["CALLIND", null, ["register:0:8"]]
+ 00bd42a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd42a4 ["INT_ADD", "register:40f0:8", ["const:bd42a4:8", "const:4:8"]]
+ 00bd42a4 ["CALLIND", null, ["register:0:8"]]
- 00bd41dc bytes 00013fd6
+ 00bd42a4 bytes 00013fd6
- 00bd420c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd420c ["INT_ADD", "register:40f0:8", ["const:bd420c:8", "const:4:8"]]
- 00bd420c ["CALLIND", null, ["register:0:8"]]
+ 00bd42d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd42d4 ["INT_ADD", "register:40f0:8", ["const:bd42d4:8", "const:4:8"]]
+ 00bd42d4 ["CALLIND", null, ["register:0:8"]]
- 00bd420c bytes 00013fd6
+ 00bd42d4 bytes 00013fd6
- 00bd423c ["INT_ADD", "register:40f0:8", ["const:bd423c:8", "const:4:8"]]
- 00bd423c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd4304 ["INT_ADD", "register:40f0:8", ["const:bd4304:8", "const:4:8"]]
+ 00bd4304 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd423c bytes c5230094
+ 00bd4304 bytes bf230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c37e4295ec500797845d9d6d7d461102"></a>

### [`00bd428c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd428c.md) → [`00bd4354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md) FUN_00bd4354

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd42e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd428c.md#insn-00bd42e0) · [`00bd42fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd428c.md#insn-00bd42fc) · [`00bd4334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd428c.md#insn-00bd4334)
- 新版 [`00bd43a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43a8) · [`00bd43c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43c4) · [`00bd43fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4354.md#insn-00bd43fc)

~~~diff
- 00bd42e0 ["INT_ADD", "register:40f0:8", ["const:bd42e0:8", "const:4:8"]]
- 00bd42e0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd43a8 ["INT_ADD", "register:40f0:8", ["const:bd43a8:8", "const:4:8"]]
+ 00bd43a8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd42e0 bytes 9c230094
+ 00bd43a8 bytes 96230094
- 00bd42fc ["INT_ADD", "register:40f0:8", ["const:bd42fc:8", "const:4:8"]]
- 00bd42fc ["CALL", null, ["callee:00bdb160:8"]]
+ 00bd43c4 ["INT_ADD", "register:40f0:8", ["const:bd43c4:8", "const:4:8"]]
+ 00bd43c4 ["CALL", null, ["callee:00bdb160:8"]]
- 00bd42fc bytes 6d1b0094
+ 00bd43c4 bytes 671b0094
- 00bd4334 ["INT_ADD", "register:40f0:8", ["const:bd4334:8", "const:4:8"]]
- 00bd4334 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd43fc ["INT_ADD", "register:40f0:8", ["const:bd43fc:8", "const:4:8"]]
+ 00bd43fc ["CALL", null, ["callee:00bdd200:8"]]
- 00bd4334 bytes 87230094
+ 00bd43fc bytes 81230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525aa215f0d174fa7278dbbce4e9dabf"></a>

### [`00bd43f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43f4.md) → [`00bd44bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md) FUN_00bd44bc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43f4.md#insn-00bd4480) · [`00bd44a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43f4.md#insn-00bd44a8) · [`00bd44d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd43f4.md#insn-00bd44d8)
- 新版 [`00bd4548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd4548) · [`00bd4570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd4570) · [`00bd45a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd44bc.md#insn-00bd45a0)

~~~diff
- 00bd4480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4480 ["INT_ADD", "register:40f0:8", ["const:bd4480:8", "const:4:8"]]
- 00bd4480 ["CALLIND", null, ["register:0:8"]]
+ 00bd4548 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4548 ["INT_ADD", "register:40f0:8", ["const:bd4548:8", "const:4:8"]]
+ 00bd4548 ["CALLIND", null, ["register:0:8"]]
- 00bd4480 bytes 00013fd6
+ 00bd4548 bytes 00013fd6
- 00bd44a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd44a8 ["INT_ADD", "register:40f0:8", ["const:bd44a8:8", "const:4:8"]]
- 00bd44a8 ["CALLIND", null, ["register:0:8"]]
+ 00bd4570 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4570 ["INT_ADD", "register:40f0:8", ["const:bd4570:8", "const:4:8"]]
+ 00bd4570 ["CALLIND", null, ["register:0:8"]]
- 00bd44a8 bytes 00013fd6
+ 00bd4570 bytes 00013fd6
- 00bd44d8 ["INT_ADD", "register:40f0:8", ["const:bd44d8:8", "const:4:8"]]
- 00bd44d8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd45a0 ["INT_ADD", "register:40f0:8", ["const:bd45a0:8", "const:4:8"]]
+ 00bd45a0 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd44d8 bytes 1e230094
+ 00bd45a0 bytes 18230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8bbc6ce93981fd1eb9af518751d0dc4"></a>

### [`00bd4734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4734.md) → [`00bd47fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md) FUN_00bd47fc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd47d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4734.md#insn-00bd47d0) · [`00bd4800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4734.md#insn-00bd4800) · [`00bd4830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4734.md#insn-00bd4830)
- 新版 [`00bd4898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd4898) · [`00bd48c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd48c8) · [`00bd48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd47fc.md#insn-00bd48f8)

~~~diff
- 00bd47d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd47d0 ["INT_ADD", "register:40f0:8", ["const:bd47d0:8", "const:4:8"]]
- 00bd47d0 ["CALLIND", null, ["register:0:8"]]
+ 00bd4898 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4898 ["INT_ADD", "register:40f0:8", ["const:bd4898:8", "const:4:8"]]
+ 00bd4898 ["CALLIND", null, ["register:0:8"]]
- 00bd47d0 bytes 00013fd6
+ 00bd4898 bytes 00013fd6
- 00bd4800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4800 ["INT_ADD", "register:40f0:8", ["const:bd4800:8", "const:4:8"]]
- 00bd4800 ["CALLIND", null, ["register:0:8"]]
+ 00bd48c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd48c8 ["INT_ADD", "register:40f0:8", ["const:bd48c8:8", "const:4:8"]]
+ 00bd48c8 ["CALLIND", null, ["register:0:8"]]
- 00bd4800 bytes 00013fd6
+ 00bd48c8 bytes 00013fd6
- 00bd4830 ["INT_ADD", "register:40f0:8", ["const:bd4830:8", "const:4:8"]]
- 00bd4830 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd48f8 ["INT_ADD", "register:40f0:8", ["const:bd48f8:8", "const:4:8"]]
+ 00bd48f8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd4830 bytes 48220094
+ 00bd48f8 bytes 42220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-038d639245cd771280d23082773bfed2"></a>

### [`00bd4ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ad0.md) → [`00bd4b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md) FUN_00bd4b98

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd4bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ad0.md#insn-00bd4afc) · [`00bd4b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ad0.md#insn-00bd4b2c) · [`00bd4b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ad0.md#insn-00bd4b5c)
- 新版 [`00bd4bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4bc4) · [`00bd4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4bf4) · [`00bd4c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md#insn-00bd4c24)

~~~diff
- 00bd4afc ["INT_ADD", "register:40f0:8", ["const:bd4afc:8", "const:4:8"]]
- 00bd4afc ["CALL", null, ["callee:00bd4cc0:8"]]
+ 00bd4bc4 ["INT_ADD", "register:40f0:8", ["const:bd4bc4:8", "const:4:8"]]
+ 00bd4bc4 ["CALL", null, ["callee:00bd4cc0:8"]]
- 00bd4afc bytes 3f000094
+ 00bd4bc4 bytes 3f000094
- 00bd4b2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4b2c ["INT_ADD", "register:40f0:8", ["const:bd4b2c:8", "const:4:8"]]
- 00bd4b2c ["CALLIND", null, ["register:0:8"]]
+ 00bd4bf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4bf4 ["INT_ADD", "register:40f0:8", ["const:bd4bf4:8", "const:4:8"]]
+ 00bd4bf4 ["CALLIND", null, ["register:0:8"]]
- 00bd4b2c bytes 00013fd6
+ 00bd4bf4 bytes 00013fd6
- 00bd4b5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4b5c ["INT_ADD", "register:40f0:8", ["const:bd4b5c:8", "const:4:8"]]
- 00bd4b5c ["CALLIND", null, ["register:0:8"]]
+ 00bd4c24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4c24 ["INT_ADD", "register:40f0:8", ["const:bd4c24:8", "const:4:8"]]
+ 00bd4c24 ["CALLIND", null, ["register:0:8"]]
- 00bd4b5c bytes 00013fd6
+ 00bd4c24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5f308b1f32e2d236f97ca2e9220c810"></a>

### [`00bd4da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4da4.md) → [`00bd4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e6c.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd900.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdd9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9b0.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4da4.md#insn-00bd4db0)
- 新版 [`00bd4e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e6c.md#insn-00bd4e78)

~~~diff
- 00bd4db0 ["INT_ADD", "register:40f0:8", ["const:bd4db0:8", "const:4:8"]]
- 00bd4db0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00bd4e78 ["INT_ADD", "register:40f0:8", ["const:bd4e78:8", "const:4:8"]]
+ 00bd4e78 ["CALL", null, ["callee:00bdaff0:8"]]
- 00bd4db0 bytes 64180094
+ 00bd4e78 bytes 5e180094
~~~


<a id="compare-9dfaa1e727c65ee33a72ad6c6e0fc4e3"></a>

### [`00bd4dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4dd4.md) → [`00bd4e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e9c.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdeea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4dd4.md#insn-00bd4de0)
- 新版 [`00bd4ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4e9c.md#insn-00bd4ea8)

~~~diff
- 00bd4de0 ["INT_ADD", "register:40f0:8", ["const:bd4de0:8", "const:4:8"]]
- 00bd4de0 ["CALL", null, ["callee:00bdef50:8"]]
+ 00bd4ea8 ["INT_ADD", "register:40f0:8", ["const:bd4ea8:8", "const:4:8"]]
+ 00bd4ea8 ["CALL", null, ["callee:00bdef50:8"]]
- 00bd4de0 bytes 30280094
+ 00bd4ea8 bytes 2a280094
~~~


<a id="compare-34c91ebcab3f5ef70ccb87e605c4a4eb"></a>

### [`00bd4e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e34.md) → [`00bd4efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4efc.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e34.md#insn-00bd4e40)
- 新版 [`00bd4f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4efc.md#insn-00bd4f08)

~~~diff
- 00bd4e40 ["INT_ADD", "register:40f0:8", ["const:bd4e40:8", "const:4:8"]]
- 00bd4e40 ["CALL", null, ["callee:00be1eb0:8"]]
+ 00bd4f08 ["INT_ADD", "register:40f0:8", ["const:bd4f08:8", "const:4:8"]]
+ 00bd4f08 ["CALL", null, ["callee:00be1eb0:8"]]
- 00bd4e40 bytes f0330094
+ 00bd4f08 bytes ea330094
~~~


<a id="compare-60aaa6f44aaa529ee14ded4e8709d375"></a>

### [`00bd4e64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e64.md) → [`00bd4f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f2c.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e64.md#insn-00bd4e70)
- 新版 [`00bd4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f2c.md#insn-00bd4f38)

~~~diff
- 00bd4e70 ["INT_ADD", "register:40f0:8", ["const:bd4e70:8", "const:4:8"]]
- 00bd4e70 ["CALL", null, ["callee:00be1ed0:8"]]
+ 00bd4f38 ["INT_ADD", "register:40f0:8", ["const:bd4f38:8", "const:4:8"]]
+ 00bd4f38 ["CALL", null, ["callee:00be1ed0:8"]]
- 00bd4e70 bytes ec330094
+ 00bd4f38 bytes e6330094
~~~


<a id="compare-f0b0e8a7ccfb2d1042b2a2a46a423c35"></a>

### [`00bd4efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md) → [`00bd4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md) __cxa_allocate_exception

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) · 呼出先 3件 [`00bd56c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) · 呼出先 3件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md#insn-00bd4f14) · [`00bd4f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md#insn-00bd4f2c) · [`00bd4f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md#insn-00bd4f44)
- 新版 [`00bd4fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd4fdc) · [`00bd4ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd4ff4) · [`00bd500c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md#insn-00bd500c)

~~~diff
- 00bd4f14 ["INT_ADD", "register:40f0:8", ["const:bd4f14:8", "const:4:8"]]
- 00bd4f14 ["CALL", null, ["callee:00bd5790:8"]]
+ 00bd4fdc ["INT_ADD", "register:40f0:8", ["const:bd4fdc:8", "const:4:8"]]
+ 00bd4fdc ["CALL", null, ["callee:00bd5790:8"]]
- 00bd4f14 bytes ed010094
+ 00bd4fdc bytes ed010094
- 00bd4f2c ["INT_ADD", "register:40f0:8", ["const:bd4f2c:8", "const:4:8"]]
- 00bd4f2c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bd4ff4 ["INT_ADD", "register:40f0:8", ["const:bd4ff4:8", "const:4:8"]]
+ 00bd4ff4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bd4f2c bytes 85180094
+ 00bd4ff4 bytes 7f180094
- 00bd4f44 ["INT_ADD", "register:40f0:8", ["const:bd4f44:8", "const:4:8"]]
- 00bd4f44 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd500c ["INT_ADD", "register:40f0:8", ["const:bd500c:8", "const:4:8"]]
+ 00bd500c ["CALL", null, ["callee:00bdb180:8"]]
- 00bd4f44 bytes 63180094
+ 00bd500c bytes 5d180094
~~~


<a id="compare-a152c09c401b92dee46a2e865c0819f3"></a>

### [`00bd4f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4f4c.md) → [`00bd5014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md) __cxa_begin_catch

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0c0.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00be1cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1cd0.md)
- 新版 呼出元 1件 [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4f4c.md#insn-00bd4f60) · [`00bd4fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4f4c.md#insn-00bd4fe0)
- 新版 [`00bd5028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md#insn-00bd5028) · [`00bd50a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5014.md#insn-00bd50a8)

~~~diff
- 00bd4f60 ["INT_ADD", "register:40f0:8", ["const:bd4f60:8", "const:4:8"]]
- 00bd4f60 ["CALL", null, ["callee:00be1d80:8"]]
+ 00bd5028 ["INT_ADD", "register:40f0:8", ["const:bd5028:8", "const:4:8"]]
+ 00bd5028 ["CALL", null, ["callee:00be1d80:8"]]
- 00bd4f60 bytes 5c330094
+ 00bd5028 bytes 56330094
- 00bd4fe0 ["INT_ADD", "register:40f0:8", ["const:bd4fe0:8", "const:4:8"]]
- 00bd4fe0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd50a8 ["INT_ADD", "register:40f0:8", ["const:bd50a8:8", "const:4:8"]]
+ 00bd50a8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd4fe0 bytes 3c180094
+ 00bd50a8 bytes 36180094
~~~


<a id="compare-bcb1211cf35537cfa17321fb71797d69"></a>

### [`00bd4fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4fe8.md) → [`00bd50b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md) __cxa_free_exception

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdafd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafd0.md) · 呼出先 1件 [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md)
- 新版 呼出元 1件 [`00bdb080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb080.md) · 呼出先 1件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4fe8.md#insn-00bd4ff8)
- 新版 [`00bd50c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md#insn-00bd50c0)

~~~diff
- 00bd4ff8 ["INT_ADD", "register:40f0:8", ["const:bd4ff8:8", "const:4:8"]]
- 00bd4ff8 ["CALL", null, ["callee:00bd5964:8"]]
+ 00bd50c0 ["INT_ADD", "register:40f0:8", ["const:bd50c0:8", "const:4:8"]]
+ 00bd50c0 ["CALL", null, ["callee:00bd5964:8"]]
- 00bd4ff8 bytes 29020094
+ 00bd50c0 bytes 29020094
~~~


<a id="compare-fa19cda38d793c407c8b7872d8281612"></a>

### [`00bd507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md) → [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) FUN_00bd5144

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bd500c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd500c.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bd50d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50d4.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd50a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md#insn-00bd50a0) · [`00bd50b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md#insn-00bd50b8) · [`00bd50c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md#insn-00bd50c0)
- 新版 [`00bd5168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5168) · [`00bd5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5180) · [`00bd5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md#insn-00bd5188)

~~~diff
- 00bd50a0 ["INT_ADD", "register:40f0:8", ["const:bd50a0:8", "const:4:8"]]
- 00bd50a0 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd5168 ["INT_ADD", "register:40f0:8", ["const:bd5168:8", "const:4:8"]]
+ 00bd5168 ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd50a0 bytes 3c070094
+ 00bd5168 bytes 3a070094
- 00bd50b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd50b8 ["INT_ADD", "register:40f0:8", ["const:bd50b8:8", "const:4:8"]]
- 00bd50b8 ["CALLIND", null, ["register:0:8"]]
+ 00bd5180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5180 ["INT_ADD", "register:40f0:8", ["const:bd5180:8", "const:4:8"]]
+ 00bd5180 ["CALLIND", null, ["register:0:8"]]
- 00bd50b8 bytes 00013fd6
+ 00bd5180 bytes 00013fd6
- 00bd50c0 ["INT_ADD", "register:40f0:8", ["const:bd50c0:8", "const:4:8"]]
- 00bd50c0 ["CALL", null, ["callee:00bd5964:8"]]
+ 00bd5188 ["INT_ADD", "register:40f0:8", ["const:bd5188:8", "const:4:8"]]
+ 00bd5188 ["CALL", null, ["callee:00bd5964:8"]]
- 00bd50c0 bytes f7010094
+ 00bd5188 bytes f7010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a0d7642c9fe34e573af5816fdfa0d9"></a>

### [`00bd50e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd50e4.md) → [`00bd51ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd56c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd50f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd50e4.md#insn-00bd50f4) · [`00bd511c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd50e4.md#insn-00bd511c)
- 新版 [`00bd51bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md#insn-00bd51bc) · [`00bd51e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51ac.md#insn-00bd51e4)

~~~diff
- 00bd50f4 ["INT_ADD", "register:40f0:8", ["const:bd50f4:8", "const:4:8"]]
- 00bd50f4 ["CALL", null, ["callee:00bd5790:8"]]
+ 00bd51bc ["INT_ADD", "register:40f0:8", ["const:bd51bc:8", "const:4:8"]]
+ 00bd51bc ["CALL", null, ["callee:00bd5790:8"]]
- 00bd50f4 bytes 75010094
+ 00bd51bc bytes 75010094
- 00bd511c ["INT_ADD", "register:40f0:8", ["const:bd511c:8", "const:4:8"]]
- 00bd511c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd51e4 ["INT_ADD", "register:40f0:8", ["const:bd51e4:8", "const:4:8"]]
+ 00bd51e4 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd511c bytes ed170094
+ 00bd51e4 bytes e7170094
~~~


<a id="compare-3fc78e513da77d2443f9946b77140a2a"></a>

### [`00bd5128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md) → [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) __cxa_throw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) · 呼出先 4件 [`00bd5184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5184.md) [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bdb3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3e0.md) [`00be1cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1cd0.md)
- 新版 呼出元 1件 [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) · 呼出先 4件 [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bdb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb490.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md#insn-00bd5148) · [`00bd5164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md#insn-00bd5164) · [`00bd5178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md#insn-00bd5178)
- 新版 [`00bd5210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd5210) · [`00bd522c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd522c) · [`00bd5240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md#insn-00bd5240)

~~~diff
- 00bd5148 ["INT_ADD", "register:40f0:8", ["const:bd5148:8", "const:4:8"]]
- 00bd5148 ["CALL", null, ["callee:00be1d80:8"]]
+ 00bd5210 ["INT_ADD", "register:40f0:8", ["const:bd5210:8", "const:4:8"]]
+ 00bd5210 ["CALL", null, ["callee:00be1d80:8"]]
- 00bd5148 bytes e2320094
+ 00bd5210 bytes dc320094
- 00bd5164 ["INT_ADD", "register:40f0:8", ["const:bd5164:8", "const:4:8"]]
- 00bd5164 ["CALL", null, ["callee:00bdb490:8"]]
+ 00bd522c ["INT_ADD", "register:40f0:8", ["const:bd522c:8", "const:4:8"]]
+ 00bd522c ["CALL", null, ["callee:00bdb490:8"]]
- 00bd5164 bytes 9f180094
+ 00bd522c bytes 99180094
- 00bd5178 ["INT_ADD", "register:40f0:8", ["const:bd5178:8", "const:4:8"]]
- 00bd5178 ["CALL", null, ["callee:00bd6e80:8"]]
+ 00bd5240 ["INT_ADD", "register:40f0:8", ["const:bd5240:8", "const:4:8"]]
+ 00bd5240 ["CALL", null, ["callee:00bd6e80:8"]]
- 00bd5178 bytes 12070094
+ 00bd5240 bytes 10070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08200d51eb959f7f36a6bb3f51989154"></a>

### [`00bd5184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5184.md) → [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) FUN_00bd524c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md) · 呼出先 2件 [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bdb0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) · 呼出先 2件 [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bdb170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd519c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5184.md#insn-00bd519c) · [`00bd51a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5184.md#insn-00bd51a4)
- 新版 [`00bd5264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md#insn-00bd5264) · [`00bd526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md#insn-00bd526c)

~~~diff
- 00bd519c ["INT_ADD", "register:40f0:8", ["const:bd519c:8", "const:4:8"]]
- 00bd519c ["CALL", null, ["callee:00bdb170:8"]]
+ 00bd5264 ["INT_ADD", "register:40f0:8", ["const:bd5264:8", "const:4:8"]]
+ 00bd5264 ["CALL", null, ["callee:00bdb170:8"]]
- 00bd519c bytes c9170094
+ 00bd5264 bytes c3170094
- 00bd51a4 ["INT_ADD", "register:40f0:8", ["const:bd51a4:8", "const:4:8"]]
- 00bd51a4 ["CALL", null, ["callee:00bbaa2c:8"]]
+ 00bd526c ["INT_ADD", "register:40f0:8", ["const:bd526c:8", "const:4:8"]]
+ 00bd526c ["CALL", null, ["callee:00bbaa2c:8"]]
- 00bd51a4 bytes f095ff97
+ 00bd526c bytes f095ff97
~~~


<a id="compare-cbd7a07ba304a09f014344b70735869a"></a>

### [`00bd51b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd51b4.md) → [`00bd527c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md) __cxa_end_catch

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb380.md) · 呼出先 4件 [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bd71cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd71cc.md) [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 1件 [`00bdb430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb430.md) · 呼出先 4件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bd728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd728c.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd51c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd51b4.md#insn-00bd51c4) · [`00bd5224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd51b4.md#insn-00bd5224) · [`00bd5234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd51b4.md#insn-00bd5234)
- 新版 [`00bd528c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd528c) · [`00bd52ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd52ec) · [`00bd52fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md#insn-00bd52fc)

~~~diff
- 00bd51c4 ["INT_ADD", "register:40f0:8", ["const:bd51c4:8", "const:4:8"]]
- 00bd51c4 ["CALL", null, ["callee:00be1d90:8"]]
+ 00bd528c ["INT_ADD", "register:40f0:8", ["const:bd528c:8", "const:4:8"]]
+ 00bd528c ["CALL", null, ["callee:00be1d90:8"]]
- 00bd51c4 bytes c7320094
+ 00bd528c bytes c1320094
- 00bd5224 ["INT_ADD", "register:40f0:8", ["const:bd5224:8", "const:4:8"]]
- 00bd5224 ["CALL", null, ["callee:00bd5964:8"]]
+ 00bd52ec ["INT_ADD", "register:40f0:8", ["const:bd52ec:8", "const:4:8"]]
+ 00bd52ec ["CALL", null, ["callee:00bd5964:8"]]
- 00bd5224 bytes 9e010094
+ 00bd52ec bytes 9e010094
- 00bd5234 ["INT_ADD", "register:40f0:8", ["const:bd5234:8", "const:4:8"]]
- 00bd5234 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd52fc ["INT_ADD", "register:40f0:8", ["const:bd52fc:8", "const:4:8"]]
+ 00bd52fc ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd5234 bytes d7060094
+ 00bd52fc bytes d5060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1554d57c31eede6a96767449b6fe3963"></a>

### [`00bd52a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52a0.md) → [`00bd5368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e10.md) · 呼出先 2件 [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00be0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ec0.md) · 呼出先 2件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd52c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52a0.md#insn-00bd52c0) · [`00bd52d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52a0.md#insn-00bd52d8) · [`00bd52e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52a0.md#insn-00bd52e0)
- 新版 [`00bd5388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd5388) · [`00bd53a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd53a0) · [`00bd53a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md#insn-00bd53a8)

~~~diff
- 00bd52c0 ["INT_ADD", "register:40f0:8", ["const:bd52c0:8", "const:4:8"]]
- 00bd52c0 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd5388 ["INT_ADD", "register:40f0:8", ["const:bd5388:8", "const:4:8"]]
+ 00bd5388 ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd52c0 bytes b4060094
+ 00bd5388 bytes b2060094
- 00bd52d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd52d8 ["INT_ADD", "register:40f0:8", ["const:bd52d8:8", "const:4:8"]]
- 00bd52d8 ["CALLIND", null, ["register:0:8"]]
+ 00bd53a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd53a0 ["INT_ADD", "register:40f0:8", ["const:bd53a0:8", "const:4:8"]]
+ 00bd53a0 ["CALLIND", null, ["register:0:8"]]
- 00bd52d8 bytes 00013fd6
+ 00bd53a0 bytes 00013fd6
- 00bd52e0 ["INT_ADD", "register:40f0:8", ["const:bd52e0:8", "const:4:8"]]
- 00bd52e0 ["CALL", null, ["callee:00bd5964:8"]]
+ 00bd53a8 ["INT_ADD", "register:40f0:8", ["const:bd53a8:8", "const:4:8"]]
+ 00bd53a8 ["CALL", null, ["callee:00bd5964:8"]]
- 00bd52e0 bytes 6f010094
+ 00bd53a8 bytes 6f010094
~~~


<a id="compare-0f804943742df3f2dac0a7d1290db157"></a>

### [`00bd52fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52fc.md) → [`00bd53c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd53c4.md) __cxa_current_exception_type

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52fc.md#insn-00bd5308)
- 新版 [`00bd53d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd53c4.md#insn-00bd53d0)

~~~diff
- 00bd5308 ["INT_ADD", "register:40f0:8", ["const:bd5308:8", "const:4:8"]]
- 00bd5308 ["CALL", null, ["callee:00be1d90:8"]]
+ 00bd53d0 ["INT_ADD", "register:40f0:8", ["const:bd53d0:8", "const:4:8"]]
+ 00bd53d0 ["CALL", null, ["callee:00be1d90:8"]]
- 00bd5308 bytes 76320094
+ 00bd53d0 bytes 70320094
~~~


<a id="compare-70f8be02a91a5c71e616c08c03406122"></a>

### [`00bd534c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md) → [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) __cxa_rethrow

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5b0.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00be1cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1cd0.md)
- 新版 呼出元 1件 [`00bdb660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb660.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00be1d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md#insn-00bd5360) · [`00bd536c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md#insn-00bd536c) · [`00bd53b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md#insn-00bd53b8)
- 新版 [`00bd5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5428) · [`00bd5434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5434) · [`00bd5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md#insn-00bd5480)

~~~diff
- 00bd5360 ["INT_ADD", "register:40f0:8", ["const:bd5360:8", "const:4:8"]]
- 00bd5360 ["CALL", null, ["callee:00be1d80:8"]]
+ 00bd5428 ["INT_ADD", "register:40f0:8", ["const:bd5428:8", "const:4:8"]]
+ 00bd5428 ["CALL", null, ["callee:00be1d80:8"]]
- 00bd5360 bytes 5c320094
+ 00bd5428 bytes 56320094
- 00bd536c ["INT_ADD", "register:40f0:8", ["const:bd536c:8", "const:4:8"]]
- 00bd536c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd5434 ["INT_ADD", "register:40f0:8", ["const:bd5434:8", "const:4:8"]]
+ 00bd5434 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd536c bytes 59170094
+ 00bd5434 bytes 53170094
- 00bd53b8 ["INT_ADD", "register:40f0:8", ["const:bd53b8:8", "const:4:8"]]
- 00bd53b8 ["CALL", null, ["callee:00bd6e80:8"]]
+ 00bd5480 ["INT_ADD", "register:40f0:8", ["const:bd5480:8", "const:4:8"]]
+ 00bd5480 ["CALL", null, ["callee:00bd6e80:8"]]
- 00bd53b8 bytes 82060094
+ 00bd5480 bytes 80060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af2e9aa8bfd5cd6911deb9942a88428"></a>

### [`00bd5430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5430.md) → [`00bd54f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd54f8.md) __cxa_increment_exception_refcount

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e20.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00be0ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ed0.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd544c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5430.md#insn-00bd544c)
- 新版 [`00bd5514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd54f8.md#insn-00bd5514)

~~~diff
- 00bd544c ["INT_ADD", "register:40f0:8", ["const:bd544c:8", "const:4:8"]]
- 00bd544c ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd5514 ["INT_ADD", "register:40f0:8", ["const:bd5514:8", "const:4:8"]]
+ 00bd5514 ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd544c bytes 51060094
+ 00bd5514 bytes 4f060094
~~~


<a id="compare-930c35b8c1733bd5ad183c6b03a6655d"></a>

### [`00bd545c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd545c.md) → [`00bd5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md) __cxa_current_primary_exception

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e40.md) · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd546c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd545c.md#insn-00bd546c) · [`00bd54b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd545c.md#insn-00bd54b8)
- 新版 [`00bd5534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md#insn-00bd5534) · [`00bd5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5524.md#insn-00bd5580)

~~~diff
- 00bd546c ["INT_ADD", "register:40f0:8", ["const:bd546c:8", "const:4:8"]]
- 00bd546c ["CALL", null, ["callee:00be1d90:8"]]
+ 00bd5534 ["INT_ADD", "register:40f0:8", ["const:bd5534:8", "const:4:8"]]
+ 00bd5534 ["CALL", null, ["callee:00be1d90:8"]]
- 00bd546c bytes 1d320094
+ 00bd5534 bytes 17320094
- 00bd54b8 ["INT_ADD", "register:40f0:8", ["const:bd54b8:8", "const:4:8"]]
- 00bd54b8 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd5580 ["INT_ADD", "register:40f0:8", ["const:bd5580:8", "const:4:8"]]
+ 00bd5580 ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd54b8 bytes 36060094
+ 00bd5580 bytes 34060094
~~~


<a id="compare-1e70498d03538a04397ea7e1181b3a25"></a>

### [`00bd55fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd55fc.md) → [`00bd56c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md) FUN_00bd56c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bd54dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd54dc.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd55fc.md#insn-00bd5628) · [`00bd5640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd55fc.md#insn-00bd5640) · [`00bd5648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd55fc.md#insn-00bd5648)
- 新版 [`00bd56f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd56f0) · [`00bd5708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd5708) · [`00bd5710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md#insn-00bd5710)

~~~diff
- 00bd5628 ["INT_ADD", "register:40f0:8", ["const:bd5628:8", "const:4:8"]]
- 00bd5628 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00bd56f0 ["INT_ADD", "register:40f0:8", ["const:bd56f0:8", "const:4:8"]]
+ 00bd56f0 ["CALL", null, ["callee:00bd6e50:8"]]
- 00bd5628 bytes da050094
+ 00bd56f0 bytes d8050094
- 00bd5640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5640 ["INT_ADD", "register:40f0:8", ["const:bd5640:8", "const:4:8"]]
- 00bd5640 ["CALLIND", null, ["register:0:8"]]
+ 00bd5708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5708 ["INT_ADD", "register:40f0:8", ["const:bd5708:8", "const:4:8"]]
+ 00bd5708 ["CALLIND", null, ["register:0:8"]]
- 00bd5640 bytes 00013fd6
+ 00bd5708 bytes 00013fd6
- 00bd5648 ["INT_ADD", "register:40f0:8", ["const:bd5648:8", "const:4:8"]]
- 00bd5648 ["CALL", null, ["callee:00bd5964:8"]]
+ 00bd5710 ["INT_ADD", "register:40f0:8", ["const:bd5710:8", "const:4:8"]]
+ 00bd5710 ["CALL", null, ["callee:00bd5964:8"]]
- 00bd5648 bytes 95000094
+ 00bd5710 bytes 95000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fa00beba3b88bbec2362cee91d95f36"></a>

### [`00bd5670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5670.md) → [`00bd5738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5738.md) __cxa_uncaught_exception

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd567c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5670.md#insn-00bd567c)
- 新版 [`00bd5744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5738.md#insn-00bd5744)

~~~diff
- 00bd567c ["INT_ADD", "register:40f0:8", ["const:bd567c:8", "const:4:8"]]
- 00bd567c ["CALL", null, ["callee:00be1d90:8"]]
+ 00bd5744 ["INT_ADD", "register:40f0:8", ["const:bd5744:8", "const:4:8"]]
+ 00bd5744 ["CALL", null, ["callee:00be1d90:8"]]
- 00bd567c bytes 99310094
+ 00bd5744 bytes 93310094
~~~


<a id="compare-3a196367b58a38e6fc86e9572f13fd4e"></a>

### [`00bd56a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56a0.md) → [`00bd5768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5768.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e00.md) · 呼出先 1件 [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 1件 [`00be0eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0eb0.md) · 呼出先 1件 [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd56ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56a0.md#insn-00bd56ac)
- 新版 [`00bd5774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5768.md#insn-00bd5774)

~~~diff
- 00bd56ac ["INT_ADD", "register:40f0:8", ["const:bd56ac:8", "const:4:8"]]
- 00bd56ac ["CALL", null, ["callee:00be1d90:8"]]
+ 00bd5774 ["INT_ADD", "register:40f0:8", ["const:bd5774:8", "const:4:8"]]
+ 00bd5774 ["CALL", null, ["callee:00be1d90:8"]]
- 00bd56ac bytes 8d310094
+ 00bd5774 bytes 87310094
~~~


