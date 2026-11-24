# 00bccb4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccab0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-a775bfa83135a0e75e33fba3769e691c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcdb40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcdb40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-7a2cc5a75ad7398b83947721d4589f36)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccb4c",
  "name": "_ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89c1f15a3bc5327998a91403afd28a235f499703c10957f0b9804dda01181a65",
  "source_text_sha256": "89c1f15a3bc5327998a91403afd28a235f499703c10957f0b9804dda01181a65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccb4c",
        "00bccbb7"
      ]
    ],
    "bytes_sha256": "0d2e7e280b6832c9c4ba16463884287ef24008df91c37f1a65a0b58cc9f5407f",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 681 bytes

~~~c

bool _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
                    /* try { // try from 00bccb60 to 00cccb77 has its CatchHandler @ 00bce978 */
  if (DAT_011268f8 == '\0') {
                    /* try { // try from 00bccb78 to 00cccc2b has its CatchHandler @ 00bcc640 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011268f0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011268f8 = iVar2 == 0;
    bVar1 = (bool)DAT_011268f8;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccb4c"></a> `00bccb4c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccb50"></a> `00bccb50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb54"></a> `00bccb54` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccb58"></a> `00bccb58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bccb5c"></a> `00bccb5c` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb60"></a> `00bccb60` | `a8 e2 63 39` | ldrb w8,[x21, #0x8f8] | `FALL_THROUGH`
<a id="insn-00bccb64"></a> `00bccb64` | `68 00 00 34` | cbz w8,0x00bccb70 | `CONDITIONAL_JUMP`
<a id="insn-00bccb68"></a> `00bccb68` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bccb6c"></a> `00bccb6c` | `0f 00 00 14` | b 0x00bccba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bccb70"></a> `00bccb70` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bccb74"></a> `00bccb74` | `c9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb78"></a> `00bccb78` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bccb7c"></a> `00bccb7c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bccb80"></a> `00bccb80` | `21 79 44 f9` | ldr x1,[x9, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccb84"></a> `00bccb84` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bccb88"></a> `00bccb88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccb8c"></a> `00bccb8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccb90"></a> `00bccb90` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bccb94"></a> `00bccb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccb98"></a> `00bccb98` | `26 39 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bccb9c"></a> `00bccb9c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bccba0"></a> `00bccba0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bccba4"></a> `00bccba4` | `a0 e2 23 39` | strb w0,[x21, #0x8f8] | `FALL_THROUGH`
<a id="insn-00bccba8"></a> `00bccba8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccbac"></a> `00bccbac` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbb0"></a> `00bccbb0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccbb4"></a> `00bccbb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccb4c`](#insn-00bccb4c) 範囲 `[['00bccb4c', '00bccb5f']]`
  - `FALL_THROUGH` [`00bccb5c`](#insn-00bccb5c) → [`00bccb60`](#insn-00bccb60)
- ブロック [`00bccb60`](#insn-00bccb60) 範囲 `[['00bccb60', '00bccb67']]`
  - `CONDITIONAL_JUMP` [`00bccb64`](#insn-00bccb64) → [`00bccb70`](#insn-00bccb70)
  - `FALL_THROUGH` [`00bccb64`](#insn-00bccb64) → [`00bccb68`](#insn-00bccb68)
- ブロック [`00bccb68`](#insn-00bccb68) 範囲 `[['00bccb68', '00bccb6f']]`
  - `UNCONDITIONAL_JUMP` [`00bccb6c`](#insn-00bccb6c) → [`00bccba8`](#insn-00bccba8)
- ブロック [`00bccb70`](#insn-00bccb70) 範囲 `[['00bccb70', '00bccb77']]`
  - `FALL_THROUGH` [`00bccb74`](#insn-00bccb74) → [`00bccb78`](#insn-00bccb78)
- ブロック [`00bccb78`](#insn-00bccb78) 範囲 `[['00bccb78', '00bccba7']]`
  - `FALL_THROUGH` [`00bccba4`](#insn-00bccba4) → [`00bccba8`](#insn-00bccba8)
- ブロック [`00bccba8`](#insn-00bccba8) 範囲 `[['00bccba8', '00bccbb7']]`

## 命令位置別の参照

- [`00bccb4c`](#insn-00bccb4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb50`](#insn-00bccb50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb54`](#insn-00bccb54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb60`](#insn-00bccb60) → `011268f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccb64`](#insn-00bccb64) → [`00bccb70`](#insn-00bccb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb6c`](#insn-00bccb6c) → [`00bccba8`](#insn-00bccba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb80`](#insn-00bccb80) → `011268f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb98`](#insn-00bccb98) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bccba4`](#insn-00bccba4) → `011268f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccba8`](#insn-00bccba8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbac`](#insn-00bccbac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccb4c`](#insn-00bccb4c)

~~~json
{
  "source": "00bccb4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb50`](#insn-00bccb50)

~~~json
{
  "source": "00bccb50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb54`](#insn-00bccb54)

~~~json
{
  "source": "00bccb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb60`](#insn-00bccb60)

~~~json
{
  "source": "00bccb60",
  "target": "011268f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb64`](#insn-00bccb64)

~~~json
{
  "source": "00bccb64",
  "target": "00bccb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb6c`](#insn-00bccb6c)

~~~json
{
  "source": "00bccb6c",
  "target": "00bccba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb80`](#insn-00bccb80)

~~~json
{
  "source": "00bccb80",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb98`](#insn-00bccb98)

~~~json
{
  "source": "00bccb98",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccba4`](#insn-00bccba4)

~~~json
{
  "source": "00bccba4",
  "target": "011268f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccba8`](#insn-00bccba8)

~~~json
{
  "source": "00bccba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbac`](#insn-00bccbac)

~~~json
{
  "source": "00bccbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
