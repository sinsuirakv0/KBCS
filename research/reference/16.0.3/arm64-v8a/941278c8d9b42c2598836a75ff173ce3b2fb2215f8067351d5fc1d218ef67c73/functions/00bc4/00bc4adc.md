# 00bc4adc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc3ae8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3ae8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0080.md#compare-ab45c07df4077ef5789da20b09f3bced)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc4adc",
  "name": "_ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74d6906b100a44facdfca7509fc3650dad0d416f021dbdc697afda88cd3f8c86",
  "source_text_sha256": "74d6906b100a44facdfca7509fc3650dad0d416f021dbdc697afda88cd3f8c86",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc4adc",
        "00bc4b4b"
      ]
    ],
    "bytes_sha256": "6dcfaee8f33b81ed90f86309f1d9dfc97da160572a7021444d3f2d6135280424",
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

- [00c5c000](../00c5c/00c5c000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 542 bytes

~~~c

void _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv
               (long *param_1)

{
  if (DAT_01127758 != 0) {
    if (DAT_01127760 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127760 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bc4b30 to 00cc4ce3 has its CatchHandler @ 00bc4954 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127758);
    DAT_01127758 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc4adc"></a> `00bc4adc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc4ae0"></a> `00bc4ae0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc4ae4"></a> `00bc4ae4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc4ae8"></a> `00bc4ae8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc4aec"></a> `00bc4aec` | `14 2b 00 f0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc4af0"></a> `00bc4af0` | `81 ae 43 f9` | ldr x1,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc4af4"></a> `00bc4af4` | `41 02 00 b4` | cbz x1,0x00bc4b3c | `CONDITIONAL_JUMP`
<a id="insn-00bc4af8"></a> `00bc4af8` | `15 2b 00 f0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc4afc"></a> `00bc4afc` | `a8 82 5d 39` | ldrb w8,[x21, #0x760] | `FALL_THROUGH`
<a id="insn-00bc4b00"></a> `00bc4b00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc4b04"></a> `00bc4b04` | `c8 00 00 34` | cbz w8,0x00bc4b1c | `CONDITIONAL_JUMP`
<a id="insn-00bc4b08"></a> `00bc4b08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc4b0c"></a> `00bc4b0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc4b10"></a> `00bc4b10` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc4b14"></a> `00bc4b14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc4b18"></a> `00bc4b18` | `bf 82 1d 39` | strb wzr,[x21, #0x760] | `FALL_THROUGH`
<a id="insn-00bc4b1c"></a> `00bc4b1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc4b20"></a> `00bc4b20` | `38 5d 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc4b24"></a> `00bc4b24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc4b28"></a> `00bc4b28` | `81 ae 43 f9` | ldr x1,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc4b2c"></a> `00bc4b2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc4b30"></a> `00bc4b30` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc4b34"></a> `00bc4b34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc4b38"></a> `00bc4b38` | `9f ae 03 f9` | str xzr,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc4b3c"></a> `00bc4b3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc4b40"></a> `00bc4b40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc4b44"></a> `00bc4b44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc4b48"></a> `00bc4b48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc4adc`](#insn-00bc4adc) 範囲 `[['00bc4adc', '00bc4af7']]`
  - `CONDITIONAL_JUMP` [`00bc4af4`](#insn-00bc4af4) → [`00bc4b3c`](#insn-00bc4b3c)
  - `FALL_THROUGH` [`00bc4af4`](#insn-00bc4af4) → [`00bc4af8`](#insn-00bc4af8)
- ブロック [`00bc4af8`](#insn-00bc4af8) 範囲 `[['00bc4af8', '00bc4b07']]`
  - `CONDITIONAL_JUMP` [`00bc4b04`](#insn-00bc4b04) → [`00bc4b1c`](#insn-00bc4b1c)
  - `FALL_THROUGH` [`00bc4b04`](#insn-00bc4b04) → [`00bc4b08`](#insn-00bc4b08)
- ブロック [`00bc4b08`](#insn-00bc4b08) 範囲 `[['00bc4b08', '00bc4b1b']]`
  - `FALL_THROUGH` [`00bc4b18`](#insn-00bc4b18) → [`00bc4b1c`](#insn-00bc4b1c)
- ブロック [`00bc4b1c`](#insn-00bc4b1c) 範囲 `[['00bc4b1c', '00bc4b2f']]`
  - `FALL_THROUGH` [`00bc4b2c`](#insn-00bc4b2c) → [`00bc4b30`](#insn-00bc4b30)
- ブロック [`00bc4b30`](#insn-00bc4b30) 範囲 `[['00bc4b30', '00bc4b3b']]`
  - `FALL_THROUGH` [`00bc4b38`](#insn-00bc4b38) → [`00bc4b3c`](#insn-00bc4b3c)
- ブロック [`00bc4b3c`](#insn-00bc4b3c) 範囲 `[['00bc4b3c', '00bc4b4b']]`

## 命令位置別の参照

- [`00bc4adc`](#insn-00bc4adc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4ae0`](#insn-00bc4ae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4ae4`](#insn-00bc4ae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4af0`](#insn-00bc4af0) → `01127758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc4af4`](#insn-00bc4af4) → [`00bc4b3c`](#insn-00bc4b3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4afc`](#insn-00bc4afc) → `01127760`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc4b04`](#insn-00bc4b04) → [`00bc4b1c`](#insn-00bc4b1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4b18`](#insn-00bc4b18) → `01127760`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc4b20`](#insn-00bc4b20) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc4b28`](#insn-00bc4b28) → `01127758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc4b38`](#insn-00bc4b38) → `01127758`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc4b3c`](#insn-00bc4b3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc4b40`](#insn-00bc4b40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc4adc`](#insn-00bc4adc)

~~~json
{
  "source": "00bc4adc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4ae0`](#insn-00bc4ae0)

~~~json
{
  "source": "00bc4ae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4ae4`](#insn-00bc4ae4)

~~~json
{
  "source": "00bc4ae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4af0`](#insn-00bc4af0)

~~~json
{
  "source": "00bc4af0",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc4af4`](#insn-00bc4af4)

~~~json
{
  "source": "00bc4af4",
  "target": "00bc4b3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4afc`](#insn-00bc4afc)

~~~json
{
  "source": "00bc4afc",
  "target": "01127760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127760",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc4b04`](#insn-00bc4b04)

~~~json
{
  "source": "00bc4b04",
  "target": "00bc4b1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4b18`](#insn-00bc4b18)

~~~json
{
  "source": "00bc4b18",
  "target": "01127760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127760",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc4b20`](#insn-00bc4b20)

~~~json
{
  "source": "00bc4b20",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc4b28`](#insn-00bc4b28)

~~~json
{
  "source": "00bc4b28",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc4b38`](#insn-00bc4b38)

~~~json
{
  "source": "00bc4b38",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc4b3c`](#insn-00bc4b3c)

~~~json
{
  "source": "00bc4b3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc4b40`](#insn-00bc4b40)

~~~json
{
  "source": "00bc4b40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
