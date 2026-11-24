# 00bcdef4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccf00`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccf00.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-3939f0f7548c09659f43fb83b580cde7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdef4",
  "name": "_ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2fe16cec49703704218ea88259e7b889732b9debb5413c787a32e022dff4eb07",
  "source_text_sha256": "2fe16cec49703704218ea88259e7b889732b9debb5413c787a32e022dff4eb07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdef4",
        "00bcdf63"
      ]
    ],
    "bytes_sha256": "18b5b7e3d650883a23c50e2850a9d359d75dbd9fa455efcc4383b6917a7ae3f0",
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

## 疑似コード / UTF-8 590 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bcdef4 to 00ccdf0b has its CatchHandler @ 00bcf958 */
                    /* try { // try from 00bcdf0c to 00ccdfbf has its CatchHandler @ 00bcd634 */
  if (DAT_011278d8 != 0) {
    if (DAT_011278e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278d8);
    DAT_011278d8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdef4"></a> `00bcdef4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcdef8"></a> `00bcdef8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdefc"></a> `00bcdefc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdf00"></a> `00bcdf00` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdf04"></a> `00bcdf04` | `d4 2a 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdf08"></a> `00bcdf08` | `81 6e 44 f9` | ldr x1,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bcdf0c"></a> `00bcdf0c` | `41 02 00 b4` | cbz x1,0x00bcdf54 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf10"></a> `00bcdf10` | `d5 2a 00 d0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdf14"></a> `00bcdf14` | `a8 82 63 39` | ldrb w8,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bcdf18"></a> `00bcdf18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdf1c"></a> `00bcdf1c` | `c8 00 00 34` | cbz w8,0x00bcdf34 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf20"></a> `00bcdf20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf24"></a> `00bcdf24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdf28"></a> `00bcdf28` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bcdf2c"></a> `00bcdf2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdf30"></a> `00bcdf30` | `bf 82 23 39` | strb wzr,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bcdf34"></a> `00bcdf34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdf38"></a> `00bcdf38` | `32 38 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf3c"></a> `00bcdf3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf40"></a> `00bcdf40` | `81 6e 44 f9` | ldr x1,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bcdf44"></a> `00bcdf44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdf48"></a> `00bcdf48` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bcdf4c"></a> `00bcdf4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdf50"></a> `00bcdf50` | `9f 6e 04 f9` | str xzr,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bcdf54"></a> `00bcdf54` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdf58"></a> `00bcdf58` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf5c"></a> `00bcdf5c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcdf60"></a> `00bcdf60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdef4`](#insn-00bcdef4) 範囲 `[['00bcdef4', '00bcdf0b']]`
  - `FALL_THROUGH` [`00bcdf08`](#insn-00bcdf08) → [`00bcdf0c`](#insn-00bcdf0c)
- ブロック [`00bcdf0c`](#insn-00bcdf0c) 範囲 `[['00bcdf0c', '00bcdf0f']]`
  - `CONDITIONAL_JUMP` [`00bcdf0c`](#insn-00bcdf0c) → [`00bcdf54`](#insn-00bcdf54)
  - `FALL_THROUGH` [`00bcdf0c`](#insn-00bcdf0c) → [`00bcdf10`](#insn-00bcdf10)
- ブロック [`00bcdf10`](#insn-00bcdf10) 範囲 `[['00bcdf10', '00bcdf1f']]`
  - `CONDITIONAL_JUMP` [`00bcdf1c`](#insn-00bcdf1c) → [`00bcdf34`](#insn-00bcdf34)
  - `FALL_THROUGH` [`00bcdf1c`](#insn-00bcdf1c) → [`00bcdf20`](#insn-00bcdf20)
- ブロック [`00bcdf20`](#insn-00bcdf20) 範囲 `[['00bcdf20', '00bcdf33']]`
  - `FALL_THROUGH` [`00bcdf30`](#insn-00bcdf30) → [`00bcdf34`](#insn-00bcdf34)
- ブロック [`00bcdf34`](#insn-00bcdf34) 範囲 `[['00bcdf34', '00bcdf53']]`
  - `FALL_THROUGH` [`00bcdf50`](#insn-00bcdf50) → [`00bcdf54`](#insn-00bcdf54)
- ブロック [`00bcdf54`](#insn-00bcdf54) 範囲 `[['00bcdf54', '00bcdf63']]`

## 命令位置別の参照

- [`00bcdef4`](#insn-00bcdef4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdef8`](#insn-00bcdef8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdefc`](#insn-00bcdefc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf08`](#insn-00bcdf08) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdf0c`](#insn-00bcdf0c) → [`00bcdf54`](#insn-00bcdf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf14`](#insn-00bcdf14) → `011278e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcdf1c`](#insn-00bcdf1c) → [`00bcdf34`](#insn-00bcdf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf30`](#insn-00bcdf30) → `011278e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcdf38`](#insn-00bcdf38) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf40`](#insn-00bcdf40) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdf50`](#insn-00bcdf50) → `011278d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdf54`](#insn-00bcdf54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf58`](#insn-00bcdf58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdef4`](#insn-00bcdef4)

~~~json
{
  "source": "00bcdef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdef8`](#insn-00bcdef8)

~~~json
{
  "source": "00bcdef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdefc`](#insn-00bcdefc)

~~~json
{
  "source": "00bcdefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf08`](#insn-00bcdf08)

~~~json
{
  "source": "00bcdf08",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf0c`](#insn-00bcdf0c)

~~~json
{
  "source": "00bcdf0c",
  "target": "00bcdf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf14`](#insn-00bcdf14)

~~~json
{
  "source": "00bcdf14",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf1c`](#insn-00bcdf1c)

~~~json
{
  "source": "00bcdf1c",
  "target": "00bcdf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf30`](#insn-00bcdf30)

~~~json
{
  "source": "00bcdf30",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf38`](#insn-00bcdf38)

~~~json
{
  "source": "00bcdf38",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf40`](#insn-00bcdf40)

~~~json
{
  "source": "00bcdf40",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf50`](#insn-00bcdf50)

~~~json
{
  "source": "00bcdf50",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf54`](#insn-00bcdf54)

~~~json
{
  "source": "00bcdf54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf58`](#insn-00bcdf58)

~~~json
{
  "source": "00bcdf58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
