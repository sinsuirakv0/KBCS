# 00bcfde0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfd44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-2fe500d6beb4df98f3d78c525ea1a8cd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0dd4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0dd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-a2f640f506219e709930f6a3e7f0ee57)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfde0",
  "name": "_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e024528974e920cf84b39fc5b52f586a78f8b2082ad45784f77c20bf5eec594",
  "source_text_sha256": "7e024528974e920cf84b39fc5b52f586a78f8b2082ad45784f77c20bf5eec594",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfde0",
        "00bcfe9f"
      ]
    ],
    "bytes_sha256": "1e5435d1eaf0715158af8a285da5eb37b03ab83e09c7337e9dc165eee4760b2f",
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
- [00c5dc60](../00c5d/00c5dc60.md)
- [00c5ddf0](../00c5d/00c5ddf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1312 bytes

~~~c

void _ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
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
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
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
<a id="insn-00bcfde0"></a> `00bcfde0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfde4"></a> `00bcfde4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfde8"></a> `00bcfde8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfdec"></a> `00bcfdec` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfdf0"></a> `00bcfdf0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfdf4"></a> `00bcfdf4` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcfdf8"></a> `00bcfdf8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcfdfc"></a> `00bcfdfc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfe00"></a> `00bcfe00` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bcfe04"></a> `00bcfe04` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bcfe08"></a> `00bcfe08` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bcfe0c"></a> `00bcfe0c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcfe10"></a> `00bcfe10` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfe14"></a> `00bcfe14` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfe18"></a> `00bcfe18` | `f6 37 02 94` | bl 0x00c5ddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe1c"></a> `00bcfe1c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe20"></a> `00bcfe20` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bcfe24"></a> `00bcfe24` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe28"></a> `00bcfe28` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfe2c"></a> `00bcfe2c` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfe30"></a> `00bcfe30` | `28 2c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe34"></a> `00bcfe34` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfe38"></a> `00bcfe38` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfe3c"></a> `00bcfe3c` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfe40"></a> `00bcfe40` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe44"></a> `00bcfe44` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe48"></a> `00bcfe48` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfe4c"></a> `00bcfe4c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfe50"></a> `00bcfe50` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bcfe54"></a> `00bcfe54` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bcfe58"></a> `00bcfe58` | `82 37 02 94` | bl 0x00c5dc60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe5c"></a> `00bcfe5c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfe60"></a> `00bcfe60` | `40 2b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe64"></a> `00bcfe64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe68"></a> `00bcfe68` | `3e 2b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe6c"></a> `00bcfe6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe70"></a> `00bcfe70` | `44 20 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe74"></a> `00bcfe74` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfe78"></a> `00bcfe78` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfe7c"></a> `00bcfe7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcfe80"></a> `00bcfe80` | `e1 00 00 54` | b.ne 0x00bcfe9c | `CONDITIONAL_JUMP`
<a id="insn-00bcfe84"></a> `00bcfe84` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfe88"></a> `00bcfe88` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfe8c"></a> `00bcfe8c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfe90"></a> `00bcfe90` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfe94"></a> `00bcfe94` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfe98"></a> `00bcfe98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfe9c"></a> `00bcfe9c` | `45 20 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfde0`](#insn-00bcfde0) 範囲 `[['00bcfde0', '00bcfe83']]`
  - `CONDITIONAL_JUMP` [`00bcfe80`](#insn-00bcfe80) → [`00bcfe9c`](#insn-00bcfe9c)
  - `FALL_THROUGH` [`00bcfe80`](#insn-00bcfe80) → [`00bcfe84`](#insn-00bcfe84)
- ブロック [`00bcfe84`](#insn-00bcfe84) 範囲 `[['00bcfe84', '00bcfe9b']]`
- ブロック [`00bcfe9c`](#insn-00bcfe9c) 範囲 `[['00bcfe9c', '00bcfe9f']]`

## 命令位置別の参照

- [`00bcfde4`](#insn-00bcfde4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfde8`](#insn-00bcfde8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdec`](#insn-00bcfdec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdf0`](#insn-00bcfdf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe10`](#insn-00bcfe10) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe14`](#insn-00bcfe14) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe18`](#insn-00bcfe18) → [`00c5ddf0`](../00c5d/00c5ddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddf0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe30`](#insn-00bcfe30) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe34`](#insn-00bcfe34) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe38`](#insn-00bcfe38) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe3c`](#insn-00bcfe3c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe40`](#insn-00bcfe40) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe58`](#insn-00bcfe58) → [`00c5dc60`](../00c5d/00c5dc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe60`](#insn-00bcfe60) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe68`](#insn-00bcfe68) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe70`](#insn-00bcfe70) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe78`](#insn-00bcfe78) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe80`](#insn-00bcfe80) → [`00bcfe9c`](#insn-00bcfe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe84`](#insn-00bcfe84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe88`](#insn-00bcfe88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe8c`](#insn-00bcfe8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe90`](#insn-00bcfe90) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe9c`](#insn-00bcfe9c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfde4`](#insn-00bcfde4)

~~~json
{
  "source": "00bcfde4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfde8`](#insn-00bcfde8)

~~~json
{
  "source": "00bcfde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdec`](#insn-00bcfdec)

~~~json
{
  "source": "00bcfdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdf0`](#insn-00bcfdf0)

~~~json
{
  "source": "00bcfdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe10`](#insn-00bcfe10)

~~~json
{
  "source": "00bcfe10",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe14`](#insn-00bcfe14)

~~~json
{
  "source": "00bcfe14",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe18`](#insn-00bcfe18)

~~~json
{
  "source": "00bcfe18",
  "target": "00c5ddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe30`](#insn-00bcfe30)

~~~json
{
  "source": "00bcfe30",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe34`](#insn-00bcfe34)

~~~json
{
  "source": "00bcfe34",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe38`](#insn-00bcfe38)

~~~json
{
  "source": "00bcfe38",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe3c`](#insn-00bcfe3c)

~~~json
{
  "source": "00bcfe3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe40`](#insn-00bcfe40)

~~~json
{
  "source": "00bcfe40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe58`](#insn-00bcfe58)

~~~json
{
  "source": "00bcfe58",
  "target": "00c5dc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe60`](#insn-00bcfe60)

~~~json
{
  "source": "00bcfe60",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe68`](#insn-00bcfe68)

~~~json
{
  "source": "00bcfe68",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe70`](#insn-00bcfe70)

~~~json
{
  "source": "00bcfe70",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe78`](#insn-00bcfe78)

~~~json
{
  "source": "00bcfe78",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe80`](#insn-00bcfe80)

~~~json
{
  "source": "00bcfe80",
  "target": "00bcfe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe84`](#insn-00bcfe84)

~~~json
{
  "source": "00bcfe84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe88`](#insn-00bcfe88)

~~~json
{
  "source": "00bcfe88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe8c`](#insn-00bcfe8c)

~~~json
{
  "source": "00bcfe8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe90`](#insn-00bcfe90)

~~~json
{
  "source": "00bcfe90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe9c`](#insn-00bcfe9c)

~~~json
{
  "source": "00bcfe9c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
