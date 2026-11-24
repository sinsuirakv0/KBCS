# 00bcc4bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc420`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-6c5c3418e91e1cfa93d27ed20f4a58a3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcd4b0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcd4b0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-02d4c7d7da64f1451bd3090d050c8d4c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc4bc",
  "name": "_ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5bebeef8462c46fb289b89d70fbf867904a8a73afc243025007c48cd2dc401b4",
  "source_text_sha256": "5bebeef8462c46fb289b89d70fbf867904a8a73afc243025007c48cd2dc401b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc4bc",
        "00bcc527"
      ]
    ],
    "bytes_sha256": "f3da93eda0c27748cfa6ee0b50ad8bf015d08a9524699958316ad009adbe201b",
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

## 疑似コード / UTF-8 479 bytes

~~~c

bool _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126830 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126828,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126830 = iVar2 == 0;
    bVar1 = (bool)DAT_01126830;
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
<a id="insn-00bcc4bc"></a> `00bcc4bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcc4c0"></a> `00bcc4c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc4c4"></a> `00bcc4c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc4c8"></a> `00bcc4c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcc4cc"></a> `00bcc4cc` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc4d0"></a> `00bcc4d0` | `a8 c2 60 39` | ldrb w8,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00bcc4d4"></a> `00bcc4d4` | `68 00 00 34` | cbz w8,0x00bcc4e0 | `CONDITIONAL_JUMP`
<a id="insn-00bcc4d8"></a> `00bcc4d8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bcc4dc"></a> `00bcc4dc` | `0f 00 00 14` | b 0x00bcc518 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc4e0"></a> `00bcc4e0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcc4e4"></a> `00bcc4e4` | `c9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc4e8"></a> `00bcc4e8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bcc4ec"></a> `00bcc4ec` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bcc4f0"></a> `00bcc4f0` | `21 15 44 f9` | ldr x1,[x9, #0x828] | `FALL_THROUGH`
<a id="insn-00bcc4f4"></a> `00bcc4f4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bcc4f8"></a> `00bcc4f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcc4fc"></a> `00bcc4fc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcc500"></a> `00bcc500` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcc504"></a> `00bcc504` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc508"></a> `00bcc508` | `ca 3a 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc50c"></a> `00bcc50c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bcc510"></a> `00bcc510` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bcc514"></a> `00bcc514` | `a0 c2 20 39` | strb w0,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00bcc518"></a> `00bcc518` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc51c"></a> `00bcc51c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc520"></a> `00bcc520` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcc524"></a> `00bcc524` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc4bc`](#insn-00bcc4bc) 範囲 `[['00bcc4bc', '00bcc4d7']]`
  - `CONDITIONAL_JUMP` [`00bcc4d4`](#insn-00bcc4d4) → [`00bcc4e0`](#insn-00bcc4e0)
  - `FALL_THROUGH` [`00bcc4d4`](#insn-00bcc4d4) → [`00bcc4d8`](#insn-00bcc4d8)
- ブロック [`00bcc4d8`](#insn-00bcc4d8) 範囲 `[['00bcc4d8', '00bcc4df']]`
  - `UNCONDITIONAL_JUMP` [`00bcc4dc`](#insn-00bcc4dc) → [`00bcc518`](#insn-00bcc518)
- ブロック [`00bcc4e0`](#insn-00bcc4e0) 範囲 `[['00bcc4e0', '00bcc517']]`
  - `FALL_THROUGH` [`00bcc514`](#insn-00bcc514) → [`00bcc518`](#insn-00bcc518)
- ブロック [`00bcc518`](#insn-00bcc518) 範囲 `[['00bcc518', '00bcc527']]`

## 命令位置別の参照

- [`00bcc4bc`](#insn-00bcc4bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4c0`](#insn-00bcc4c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4c4`](#insn-00bcc4c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4d0`](#insn-00bcc4d0) → `01126830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc4d4`](#insn-00bcc4d4) → [`00bcc4e0`](#insn-00bcc4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4dc`](#insn-00bcc4dc) → [`00bcc518`](#insn-00bcc518) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc4f0`](#insn-00bcc4f0) → `01126828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc508`](#insn-00bcc508) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bcc514`](#insn-00bcc514) → `01126830`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcc518`](#insn-00bcc518) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc51c`](#insn-00bcc51c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc4bc`](#insn-00bcc4bc)

~~~json
{
  "source": "00bcc4bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4c0`](#insn-00bcc4c0)

~~~json
{
  "source": "00bcc4c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4c4`](#insn-00bcc4c4)

~~~json
{
  "source": "00bcc4c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4d0`](#insn-00bcc4d0)

~~~json
{
  "source": "00bcc4d0",
  "target": "01126830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc4d4`](#insn-00bcc4d4)

~~~json
{
  "source": "00bcc4d4",
  "target": "00bcc4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4dc`](#insn-00bcc4dc)

~~~json
{
  "source": "00bcc4dc",
  "target": "00bcc518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc4f0`](#insn-00bcc4f0)

~~~json
{
  "source": "00bcc4f0",
  "target": "01126828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc508`](#insn-00bcc508)

~~~json
{
  "source": "00bcc508",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc514`](#insn-00bcc514)

~~~json
{
  "source": "00bcc514",
  "target": "01126830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc518`](#insn-00bcc518)

~~~json
{
  "source": "00bcc518",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc51c`](#insn-00bcc51c)

~~~json
{
  "source": "00bcc51c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
