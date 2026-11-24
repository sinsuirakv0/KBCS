# 00bcfa2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcf604`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-8c84ae322cde55e659b94c40fa24bce3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcfac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-adbd381b7691697c3e6871e6e5066cc0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfa2c",
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
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfa2c",
        "00bcfaeb"
      ]
    ],
    "bytes_sha256": "9e0a7a960c8d4bb1aafd504757ff93bbd3fa4cda413691fc8adae28a56e21bb4",
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

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5dba0](../00c5d/00c5dba0.md)
- [00c5dd20](../00c5d/00c5dd20.md)

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
<a id="insn-00bcfa2c"></a> `00bcfa2c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfa30"></a> `00bcfa30` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfa34"></a> `00bcfa34` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfa38"></a> `00bcfa38` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfa3c"></a> `00bcfa3c` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfa40"></a> `00bcfa40` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcfa44"></a> `00bcfa44` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcfa48"></a> `00bcfa48` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfa4c"></a> `00bcfa4c` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bcfa50"></a> `00bcfa50` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bcfa54"></a> `00bcfa54` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bcfa58"></a> `00bcfa58` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcfa5c"></a> `00bcfa5c` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfa60"></a> `00bcfa60` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfa64"></a> `00bcfa64` | `af 38 02 94` | bl 0x00c5dd20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfa68"></a> `00bcfa68` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfa6c"></a> `00bcfa6c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bcfa70"></a> `00bcfa70` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfa74"></a> `00bcfa74` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfa78"></a> `00bcfa78` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfa7c"></a> `00bcfa7c` | `e1 2c 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfa80"></a> `00bcfa80` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfa84"></a> `00bcfa84` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfa88"></a> `00bcfa88` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfa8c"></a> `00bcfa8c` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfa90"></a> `00bcfa90` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfa94"></a> `00bcfa94` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfa98"></a> `00bcfa98` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfa9c"></a> `00bcfa9c` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bcfaa0"></a> `00bcfaa0` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bcfaa4"></a> `00bcfaa4` | `3f 38 02 94` | bl 0x00c5dba0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfaa8"></a> `00bcfaa8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfaac"></a> `00bcfaac` | `f9 2b 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfab0"></a> `00bcfab0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfab4"></a> `00bcfab4` | `f7 2b 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfab8"></a> `00bcfab8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfabc"></a> `00bcfabc` | `fd 20 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfac0"></a> `00bcfac0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfac4"></a> `00bcfac4` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfac8"></a> `00bcfac8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcfacc"></a> `00bcfacc` | `e1 00 00 54` | b.ne 0x00bcfae8 | `CONDITIONAL_JUMP`
<a id="insn-00bcfad0"></a> `00bcfad0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfad4"></a> `00bcfad4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfad8"></a> `00bcfad8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfadc"></a> `00bcfadc` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfae0"></a> `00bcfae0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfae4"></a> `00bcfae4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfae8"></a> `00bcfae8` | `fe 20 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfa2c`](#insn-00bcfa2c) 範囲 `[['00bcfa2c', '00bcfacf']]`
  - `CONDITIONAL_JUMP` [`00bcfacc`](#insn-00bcfacc) → [`00bcfae8`](#insn-00bcfae8)
  - `FALL_THROUGH` [`00bcfacc`](#insn-00bcfacc) → [`00bcfad0`](#insn-00bcfad0)
- ブロック [`00bcfad0`](#insn-00bcfad0) 範囲 `[['00bcfad0', '00bcfae7']]`
- ブロック [`00bcfae8`](#insn-00bcfae8) 範囲 `[['00bcfae8', '00bcfaeb']]`

## 命令位置別の参照

- [`00bcfa30`](#insn-00bcfa30) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa34`](#insn-00bcfa34) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa38`](#insn-00bcfa38) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa3c`](#insn-00bcfa3c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa5c`](#insn-00bcfa5c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa60`](#insn-00bcfa60) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa64`](#insn-00bcfa64) → [`00c5dd20`](../00c5d/00c5dd20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd20` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa7c`](#insn-00bcfa7c) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa80`](#insn-00bcfa80) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa84`](#insn-00bcfa84) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa88`](#insn-00bcfa88) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfa8c`](#insn-00bcfa8c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfaa4`](#insn-00bcfaa4) → [`00c5dba0`](../00c5d/00c5dba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dba0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfaac`](#insn-00bcfaac) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcfab4`](#insn-00bcfab4) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcfabc`](#insn-00bcfabc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfac4`](#insn-00bcfac4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfacc`](#insn-00bcfacc) → [`00bcfae8`](#insn-00bcfae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad0`](#insn-00bcfad0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad4`](#insn-00bcfad4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfad8`](#insn-00bcfad8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfadc`](#insn-00bcfadc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfae8`](#insn-00bcfae8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfa30`](#insn-00bcfa30)

~~~json
{
  "source": "00bcfa30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa34`](#insn-00bcfa34)

~~~json
{
  "source": "00bcfa34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa38`](#insn-00bcfa38)

~~~json
{
  "source": "00bcfa38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa3c`](#insn-00bcfa3c)

~~~json
{
  "source": "00bcfa3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa5c`](#insn-00bcfa5c)

~~~json
{
  "source": "00bcfa5c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa60`](#insn-00bcfa60)

~~~json
{
  "source": "00bcfa60",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa64`](#insn-00bcfa64)

~~~json
{
  "source": "00bcfa64",
  "target": "00c5dd20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfa7c`](#insn-00bcfa7c)

~~~json
{
  "source": "00bcfa7c",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfa80`](#insn-00bcfa80)

~~~json
{
  "source": "00bcfa80",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa84`](#insn-00bcfa84)

~~~json
{
  "source": "00bcfa84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa88`](#insn-00bcfa88)

~~~json
{
  "source": "00bcfa88",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfa8c`](#insn-00bcfa8c)

~~~json
{
  "source": "00bcfa8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfaa4`](#insn-00bcfaa4)

~~~json
{
  "source": "00bcfaa4",
  "target": "00c5dba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfaac`](#insn-00bcfaac)

~~~json
{
  "source": "00bcfaac",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfab4`](#insn-00bcfab4)

~~~json
{
  "source": "00bcfab4",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfabc`](#insn-00bcfabc)

~~~json
{
  "source": "00bcfabc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfac4`](#insn-00bcfac4)

~~~json
{
  "source": "00bcfac4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfacc`](#insn-00bcfacc)

~~~json
{
  "source": "00bcfacc",
  "target": "00bcfae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfad0`](#insn-00bcfad0)

~~~json
{
  "source": "00bcfad0",
  "target": "Stack[-0x10]",
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
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfadc`](#insn-00bcfadc)

~~~json
{
  "source": "00bcfadc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfae8`](#insn-00bcfae8)

~~~json
{
  "source": "00bcfae8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
