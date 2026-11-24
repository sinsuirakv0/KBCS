# 00ae0dec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0da8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0da8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-6fdc47a70d203fc7d3dddd10ed00c665)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b407c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b407c4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-21c0128a4fc6205747049f17309b3e27)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0dec",
  "name": "_ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc2d0f4df231ec5d8910e9d70f452c08fc255a5f9dc1e3b5b52befe5486fd4d9",
  "source_text_sha256": "bc2d0f4df231ec5d8910e9d70f452c08fc255a5f9dc1e3b5b52befe5486fd4d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0dec",
        "00ae0e5b"
      ]
    ],
    "bytes_sha256": "57bd11da546100c68585a99163f6e118b1348df6cf4c3def8b0191064f2871fd",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 404 bytes

~~~c

void _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a0118 != 0) {
    if (DAT_010a0120 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0120 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0118);
    DAT_010a0118 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0dec"></a> `00ae0dec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae0df0"></a> `00ae0df0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0df4"></a> `00ae0df4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae0df8"></a> `00ae0df8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae0dfc"></a> `00ae0dfc` | `14 2e 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0e00"></a> `00ae0e00` | `81 8e 40 f9` | ldr x1,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0e04"></a> `00ae0e04` | `41 02 00 b4` | cbz x1,0x00ae0e4c | `CONDITIONAL_JUMP`
<a id="insn-00ae0e08"></a> `00ae0e08` | `15 2e 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0e0c"></a> `00ae0e0c` | `a8 82 44 39` | ldrb w8,[x21, #0x120] | `FALL_THROUGH`
<a id="insn-00ae0e10"></a> `00ae0e10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae0e14"></a> `00ae0e14` | `c8 00 00 34` | cbz w8,0x00ae0e2c | `CONDITIONAL_JUMP`
<a id="insn-00ae0e18"></a> `00ae0e18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae0e1c"></a> `00ae0e1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae0e20"></a> `00ae0e20` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00ae0e24"></a> `00ae0e24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae0e28"></a> `00ae0e28` | `bf 82 04 39` | strb wzr,[x21, #0x120] | `FALL_THROUGH`
<a id="insn-00ae0e2c"></a> `00ae0e2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae0e30"></a> `00ae0e30` | `ac f4 03 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0e34"></a> `00ae0e34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae0e38"></a> `00ae0e38` | `81 8e 40 f9` | ldr x1,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0e3c"></a> `00ae0e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae0e40"></a> `00ae0e40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae0e44"></a> `00ae0e44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae0e48"></a> `00ae0e48` | `9f 8e 00 f9` | str xzr,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-00ae0e4c"></a> `00ae0e4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae0e50"></a> `00ae0e50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0e54"></a> `00ae0e54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae0e58"></a> `00ae0e58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0dec`](#insn-00ae0dec) 範囲 `[['00ae0dec', '00ae0e07']]`
  - `CONDITIONAL_JUMP` [`00ae0e04`](#insn-00ae0e04) → [`00ae0e4c`](#insn-00ae0e4c)
  - `FALL_THROUGH` [`00ae0e04`](#insn-00ae0e04) → [`00ae0e08`](#insn-00ae0e08)
- ブロック [`00ae0e08`](#insn-00ae0e08) 範囲 `[['00ae0e08', '00ae0e17']]`
  - `CONDITIONAL_JUMP` [`00ae0e14`](#insn-00ae0e14) → [`00ae0e2c`](#insn-00ae0e2c)
  - `FALL_THROUGH` [`00ae0e14`](#insn-00ae0e14) → [`00ae0e18`](#insn-00ae0e18)
- ブロック [`00ae0e18`](#insn-00ae0e18) 範囲 `[['00ae0e18', '00ae0e2b']]`
  - `FALL_THROUGH` [`00ae0e28`](#insn-00ae0e28) → [`00ae0e2c`](#insn-00ae0e2c)
- ブロック [`00ae0e2c`](#insn-00ae0e2c) 範囲 `[['00ae0e2c', '00ae0e4b']]`
  - `FALL_THROUGH` [`00ae0e48`](#insn-00ae0e48) → [`00ae0e4c`](#insn-00ae0e4c)
- ブロック [`00ae0e4c`](#insn-00ae0e4c) 範囲 `[['00ae0e4c', '00ae0e5b']]`

## 命令位置別の参照

- [`00ae0dec`](#insn-00ae0dec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0df0`](#insn-00ae0df0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0df4`](#insn-00ae0df4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e00`](#insn-00ae0e00) → `010a0118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e04`](#insn-00ae0e04) → [`00ae0e4c`](#insn-00ae0e4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e0c`](#insn-00ae0e0c) → `010a0120`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae0e14`](#insn-00ae0e14) → [`00ae0e2c`](#insn-00ae0e2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e28`](#insn-00ae0e28) → `010a0120`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae0e30`](#insn-00ae0e30) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e38`](#insn-00ae0e38) → `010a0118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e48`](#insn-00ae0e48) → `010a0118`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e4c`](#insn-00ae0e4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e50`](#insn-00ae0e50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0dec`](#insn-00ae0dec)

~~~json
{
  "source": "00ae0dec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0df0`](#insn-00ae0df0)

~~~json
{
  "source": "00ae0df0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0df4`](#insn-00ae0df4)

~~~json
{
  "source": "00ae0df4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e00`](#insn-00ae0e00)

~~~json
{
  "source": "00ae0e00",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e04`](#insn-00ae0e04)

~~~json
{
  "source": "00ae0e04",
  "target": "00ae0e4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e0c`](#insn-00ae0e0c)

~~~json
{
  "source": "00ae0e0c",
  "target": "010a0120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0120",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e14`](#insn-00ae0e14)

~~~json
{
  "source": "00ae0e14",
  "target": "00ae0e2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e28`](#insn-00ae0e28)

~~~json
{
  "source": "00ae0e28",
  "target": "010a0120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0120",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e30`](#insn-00ae0e30)

~~~json
{
  "source": "00ae0e30",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0e38`](#insn-00ae0e38)

~~~json
{
  "source": "00ae0e38",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e48`](#insn-00ae0e48)

~~~json
{
  "source": "00ae0e48",
  "target": "010a0118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e4c`](#insn-00ae0e4c)

~~~json
{
  "source": "00ae0e4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e50`](#insn-00ae0e50)

~~~json
{
  "source": "00ae0e50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
