# 00bfafec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9ff8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9ff8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-65443d507f3fe6579c82ccf12c4253fc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfafec",
  "name": "_ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c2e9bf0b89dcda319b57bb25b48af1ae75d21dbce02597a2b616b85119042ee",
  "source_text_sha256": "7c2e9bf0b89dcda319b57bb25b48af1ae75d21dbce02597a2b616b85119042ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfafec",
        "00bfb037"
      ]
    ],
    "bytes_sha256": "da00c98ff08903b148ac478cec549923c0e5e2adcec9c13b9e76afaa9931b0fb",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c59390](../00c59/00c59390.md)
- [00c59550](../00c59/00c59550.md)
- [00c5f2e0](../00c5f/00c5f2e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 473 bytes

~~~c

void _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr(long *param_1)

{
  long lVar1;
  undefined1 auStack_8 [8];
  
  lVar1 = *param_1;
  if (lVar1 != 0) {
    _ZNSt13exception_ptrC1ERKS_(auStack_8);
    _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr(lVar1,auStack_8)
    ;
    _ZNSt13exception_ptrD1Ev(auStack_8);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfafec"></a> `00bfafec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaff0"></a> `00bfaff0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfaff4"></a> `00bfaff4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaff8"></a> `00bfaff8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaffc"></a> `00bfaffc` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bfb000"></a> `00bfb000` | `93 01 00 b4` | cbz x19,0x00bfb030 | `CONDITIONAL_JUMP`
<a id="insn-00bfb004"></a> `00bfb004` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfb008"></a> `00bfb008` | `52 79 01 94` | bl 0x00c59550 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb00c"></a> `00bfb00c` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfb010"></a> `00bfb010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfb014"></a> `00bfb014` | `b3 90 01 94` | bl 0x00c5f2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb018"></a> `00bfb018` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfb01c"></a> `00bfb01c` | `dd 78 01 94` | bl 0x00c59390 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb020"></a> `00bfb020` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb024"></a> `00bfb024` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfb028"></a> `00bfb028` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb02c"></a> `00bfb02c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb030"></a> `00bfb030` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb034"></a> `00bfb034` | `80 7e e1 97` | bl 0x0045aa34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfafec`](#insn-00bfafec) 範囲 `[['00bfafec', '00bfb003']]`
  - `CONDITIONAL_JUMP` [`00bfb000`](#insn-00bfb000) → [`00bfb030`](#insn-00bfb030)
  - `FALL_THROUGH` [`00bfb000`](#insn-00bfb000) → [`00bfb004`](#insn-00bfb004)
- ブロック [`00bfb004`](#insn-00bfb004) 範囲 `[['00bfb004', '00bfb02f']]`
- ブロック [`00bfb030`](#insn-00bfb030) 範囲 `[['00bfb030', '00bfb037']]`

## 命令位置別の参照

- [`00bfaff0`](#insn-00bfaff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaff4`](#insn-00bfaff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb000`](#insn-00bfb000) → [`00bfb030`](#insn-00bfb030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb008`](#insn-00bfb008) → [`00c59550`](../00c59/00c59550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59550` · 推定シンボル `None` · 推定型 `None`
- [`00bfb014`](#insn-00bfb014) → [`00c5f2e0`](../00c5f/00c5f2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f2e0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb01c`](#insn-00bfb01c) → [`00c59390`](../00c59/00c59390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59390` · 推定シンボル `None` · 推定型 `None`
- [`00bfb020`](#insn-00bfb020) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb024`](#insn-00bfb024) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb034`](#insn-00bfb034) → [`0045aa34`](../0045a/0045aa34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045aa34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaff0`](#insn-00bfaff0)

~~~json
{
  "source": "00bfaff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaff4`](#insn-00bfaff4)

~~~json
{
  "source": "00bfaff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb000`](#insn-00bfb000)

~~~json
{
  "source": "00bfb000",
  "target": "00bfb030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb008`](#insn-00bfb008)

~~~json
{
  "source": "00bfb008",
  "target": "00c59550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb014`](#insn-00bfb014)

~~~json
{
  "source": "00bfb014",
  "target": "00c5f2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb01c`](#insn-00bfb01c)

~~~json
{
  "source": "00bfb01c",
  "target": "00c59390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb020`](#insn-00bfb020)

~~~json
{
  "source": "00bfb020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb024`](#insn-00bfb024)

~~~json
{
  "source": "00bfb024",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb034`](#insn-00bfb034)

~~~json
{
  "source": "00bfb034",
  "target": "0045aa34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
