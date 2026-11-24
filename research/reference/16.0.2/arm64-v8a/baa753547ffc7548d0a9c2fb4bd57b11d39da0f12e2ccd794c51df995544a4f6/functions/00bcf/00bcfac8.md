# 00bcfac8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfa2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-adbd381b7691697c3e6871e6e5066cc0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0abc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0abc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-7165fc8528fdf4f503e02a9e51c6545b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfac8",
  "name": "_ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "947e2d450390a12d91550e547960666d878f8817ee3e22b399e2169572b41011",
  "source_text_sha256": "947e2d450390a12d91550e547960666d878f8817ee3e22b399e2169572b41011",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfac8",
        "00bcfb87"
      ]
    ],
    "bytes_sha256": "6a289d301307cbd781efdeb8ea9682f79983a4d7b3fe354e5f06ff6b369adb95",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5dc70](../00c5d/00c5dc70.md)
- [00c5ddf0](../00c5d/00c5ddf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1342 bytes

~~~c

void _ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               void *param_5)

{
  long lVar1;
  undefined4 uVar2;
  long lVar3;
  undefined8 local_78;
  undefined1 local_70;
  void *local_68;
  undefined1 auStack_60 [20];
  undefined1 local_4c;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  local_4c = 0;
  uVar2 = _ZN8firebase4auth34MapFutureCallbackResultToAuthErrorEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPb
                    ();
  lVar3 = *(long *)((long)param_5 + 0x10);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
  local_70 = local_4c;
  local_78 = param_2;
  local_68 = param_5;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSE_E_EEvRKNS_12FutureHandleEiSD_RKT0_
            (lVar3 + 0x10,auStack_60,uVar2,param_4,&local_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfac8"></a> `00bcfac8` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfacc"></a> `00bcfacc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfad0"></a> `00bcfad0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfad4"></a> `00bcfad4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfad8"></a> `00bcfad8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfadc"></a> `00bcfadc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcfae0"></a> `00bcfae0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcfae4"></a> `00bcfae4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfae8"></a> `00bcfae8` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bcfaec"></a> `00bcfaec` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bcfaf0"></a> `00bcfaf0` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bcfaf4"></a> `00bcfaf4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcfaf8"></a> `00bcfaf8` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfafc"></a> `00bcfafc` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfb00"></a> `00bcfb00` | `bc 38 02 94` | bl 0x00c5ddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb04"></a> `00bcfb04` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb08"></a> `00bcfb08` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bcfb0c"></a> `00bcfb0c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfb10"></a> `00bcfb10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfb14"></a> `00bcfb14` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfb18"></a> `00bcfb18` | `ee 2c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb1c"></a> `00bcfb1c` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfb20"></a> `00bcfb20` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfb24"></a> `00bcfb24` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfb28"></a> `00bcfb28` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb2c"></a> `00bcfb2c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfb30"></a> `00bcfb30` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfb34"></a> `00bcfb34` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfb38"></a> `00bcfb38` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bcfb3c"></a> `00bcfb3c` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bcfb40"></a> `00bcfb40` | `4c 38 02 94` | bl 0x00c5dc70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb44"></a> `00bcfb44` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfb48"></a> `00bcfb48` | `06 2c 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb4c"></a> `00bcfb4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfb50"></a> `00bcfb50` | `04 2c 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb54"></a> `00bcfb54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfb58"></a> `00bcfb58` | `0a 21 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb5c"></a> `00bcfb5c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfb60"></a> `00bcfb60` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfb64"></a> `00bcfb64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcfb68"></a> `00bcfb68` | `e1 00 00 54` | b.ne 0x00bcfb84 | `CONDITIONAL_JUMP`
<a id="insn-00bcfb6c"></a> `00bcfb6c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfb70"></a> `00bcfb70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfb74"></a> `00bcfb74` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfb78"></a> `00bcfb78` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfb7c"></a> `00bcfb7c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfb80"></a> `00bcfb80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfb84"></a> `00bcfb84` | `0b 21 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfac8`](#insn-00bcfac8) 範囲 `[['00bcfac8', '00bcfb6b']]`
  - `CONDITIONAL_JUMP` [`00bcfb68`](#insn-00bcfb68) → [`00bcfb84`](#insn-00bcfb84)
  - `FALL_THROUGH` [`00bcfb68`](#insn-00bcfb68) → [`00bcfb6c`](#insn-00bcfb6c)
- ブロック [`00bcfb6c`](#insn-00bcfb6c) 範囲 `[['00bcfb6c', '00bcfb83']]`
- ブロック [`00bcfb84`](#insn-00bcfb84) 範囲 `[['00bcfb84', '00bcfb87']]`

## 命令位置別の参照

- [`00bcfacc`](#insn-00bcfacc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad0`](#insn-00bcfad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad4`](#insn-00bcfad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad8`](#insn-00bcfad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfaf8`](#insn-00bcfaf8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfafc`](#insn-00bcfafc) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb00`](#insn-00bcfb00) → [`00c5ddf0`](../00c5d/00c5ddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb18`](#insn-00bcfb18) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb1c`](#insn-00bcfb1c) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb20`](#insn-00bcfb20) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb24`](#insn-00bcfb24) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb28`](#insn-00bcfb28) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb40`](#insn-00bcfb40) → [`00c5dc70`](../00c5d/00c5dc70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb48`](#insn-00bcfb48) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb50`](#insn-00bcfb50) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb58`](#insn-00bcfb58) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb60`](#insn-00bcfb60) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb68`](#insn-00bcfb68) → [`00bcfb84`](#insn-00bcfb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb6c`](#insn-00bcfb6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb70`](#insn-00bcfb70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb74`](#insn-00bcfb74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb78`](#insn-00bcfb78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb84`](#insn-00bcfb84) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfacc`](#insn-00bcfacc)

~~~json
{
  "source": "00bcfacc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfad0`](#insn-00bcfad0)

~~~json
{
  "source": "00bcfad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfad4`](#insn-00bcfad4)

~~~json
{
  "source": "00bcfad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfad8`](#insn-00bcfad8)

~~~json
{
  "source": "00bcfad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfaf8`](#insn-00bcfaf8)

~~~json
{
  "source": "00bcfaf8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfafc`](#insn-00bcfafc)

~~~json
{
  "source": "00bcfafc",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb00`](#insn-00bcfb00)

~~~json
{
  "source": "00bcfb00",
  "target": "00c5ddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb18`](#insn-00bcfb18)

~~~json
{
  "source": "00bcfb18",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb1c`](#insn-00bcfb1c)

~~~json
{
  "source": "00bcfb1c",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb20`](#insn-00bcfb20)

~~~json
{
  "source": "00bcfb20",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb24`](#insn-00bcfb24)

~~~json
{
  "source": "00bcfb24",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb28`](#insn-00bcfb28)

~~~json
{
  "source": "00bcfb28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb40`](#insn-00bcfb40)

~~~json
{
  "source": "00bcfb40",
  "target": "00c5dc70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb48`](#insn-00bcfb48)

~~~json
{
  "source": "00bcfb48",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb50`](#insn-00bcfb50)

~~~json
{
  "source": "00bcfb50",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb58`](#insn-00bcfb58)

~~~json
{
  "source": "00bcfb58",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb60`](#insn-00bcfb60)

~~~json
{
  "source": "00bcfb60",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb68`](#insn-00bcfb68)

~~~json
{
  "source": "00bcfb68",
  "target": "00bcfb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb6c`](#insn-00bcfb6c)

~~~json
{
  "source": "00bcfb6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb70`](#insn-00bcfb70)

~~~json
{
  "source": "00bcfb70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb74`](#insn-00bcfb74)

~~~json
{
  "source": "00bcfb74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb78`](#insn-00bcfb78)

~~~json
{
  "source": "00bcfb78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb84`](#insn-00bcfb84)

~~~json
{
  "source": "00bcfb84",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
