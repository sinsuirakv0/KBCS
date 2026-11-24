# 00bdcb7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc754`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-60f6eb35501d1decb2b9824c8df3841c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcc18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-a2018647fee0c740b82146093e16420f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcb7c",
  "name": "_ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2efb92e33579282c34bc66ba1cd1eaae7e9ea8d34db6d0702dfd1548ffc1bd5e",
  "source_text_sha256": "2efb92e33579282c34bc66ba1cd1eaae7e9ea8d34db6d0702dfd1548ffc1bd5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcb7c",
        "00bdcc43"
      ]
    ],
    "bytes_sha256": "880806912c607188c2f233eab7eb50f57450396ecba140c6c094bf3ab75eacf4",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
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
- [00c5dd20](../00c5d/00c5dd20.md)
- [00c5ddc0](../00c5d/00c5ddc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1419 bytes

~~~c

void _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               void *param_5)

{
  int iVar1;
  long lVar2;
  int iVar3;
  long lVar4;
  undefined8 local_78;
  undefined1 local_70;
  void *local_68;
  undefined1 auStack_60 [20];
  undefined1 local_4c;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  local_4c = 0;
  iVar3 = _ZN8firebase4auth34MapFutureCallbackResultToAuthErrorEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPb
                    ();
  lVar4 = *(long *)((long)param_5 + 0x10);
  iVar1 = 0x3b;
  if (iVar3 != 7) {
    iVar1 = iVar3;
  }
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
  local_70 = local_4c;
  local_78 = param_2;
  local_68 = param_5;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
            (lVar4 + 0x10,auStack_60,iVar1,param_4,&local_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
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
<a id="insn-00bdcb7c"></a> `00bdcb7c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdcb80"></a> `00bdcb80` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcb84"></a> `00bdcb84` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdcb88"></a> `00bdcb88` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdcb8c"></a> `00bdcb8c` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdcb90"></a> `00bdcb90` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdcb94"></a> `00bdcb94` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdcb98"></a> `00bdcb98` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdcb9c"></a> `00bdcb9c` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bdcba0"></a> `00bdcba0` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bdcba4"></a> `00bdcba4` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bdcba8"></a> `00bdcba8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdcbac"></a> `00bdcbac` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdcbb0"></a> `00bdcbb0` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bdcbb4"></a> `00bdcbb4` | `5b 04 02 94` | bl 0x00c5dd20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcbb8"></a> `00bdcbb8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcbbc"></a> `00bdcbbc` | `1f 1c 00 71` | cmp w0,#0x7 | `FALL_THROUGH`
<a id="insn-00bdcbc0"></a> `00bdcbc0` | `69 07 80 52` | mov w9,#0x3b | `FALL_THROUGH`
<a id="insn-00bdcbc4"></a> `00bdcbc4` | `36 01 80 1a` | csel w22,w9,w0,eq | `FALL_THROUGH`
<a id="insn-00bdcbc8"></a> `00bdcbc8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcbcc"></a> `00bdcbcc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdcbd0"></a> `00bdcbd0` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcbd4"></a> `00bdcbd4` | `8b f8 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcbd8"></a> `00bdcbd8` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bdcbdc"></a> `00bdcbdc` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcbe0"></a> `00bdcbe0` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdcbe4"></a> `00bdcbe4` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcbe8"></a> `00bdcbe8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcbec"></a> `00bdcbec` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcbf0"></a> `00bdcbf0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdcbf4"></a> `00bdcbf4` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bdcbf8"></a> `00bdcbf8` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bdcbfc"></a> `00bdcbfc` | `71 04 02 94` | bl 0x00c5ddc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc00"></a> `00bdcc00` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcc04"></a> `00bdcc04` | `a3 f7 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc08"></a> `00bdcc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcc0c"></a> `00bdcc0c` | `a1 f7 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc10"></a> `00bdcc10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcc14"></a> `00bdcc14` | `a7 ec 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc18"></a> `00bdcc18` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdcc1c"></a> `00bdcc1c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdcc20"></a> `00bdcc20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdcc24"></a> `00bdcc24` | `e1 00 00 54` | b.ne 0x00bdcc40 | `CONDITIONAL_JUMP`
<a id="insn-00bdcc28"></a> `00bdcc28` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdcc2c"></a> `00bdcc2c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdcc30"></a> `00bdcc30` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdcc34"></a> `00bdcc34` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcc38"></a> `00bdcc38` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdcc3c"></a> `00bdcc3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdcc40"></a> `00bdcc40` | `a8 ec 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcb7c`](#insn-00bdcb7c) 範囲 `[['00bdcb7c', '00bdcc27']]`
  - `CONDITIONAL_JUMP` [`00bdcc24`](#insn-00bdcc24) → [`00bdcc40`](#insn-00bdcc40)
  - `FALL_THROUGH` [`00bdcc24`](#insn-00bdcc24) → [`00bdcc28`](#insn-00bdcc28)
- ブロック [`00bdcc28`](#insn-00bdcc28) 範囲 `[['00bdcc28', '00bdcc3f']]`
- ブロック [`00bdcc40`](#insn-00bdcc40) 範囲 `[['00bdcc40', '00bdcc43']]`

## 命令位置別の参照

- [`00bdcb80`](#insn-00bdcb80) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb84`](#insn-00bdcb84) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb88`](#insn-00bdcb88) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb8c`](#insn-00bdcb8c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbac`](#insn-00bdcbac) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbb0`](#insn-00bdcbb0) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbb4`](#insn-00bdcbb4) → [`00c5dd20`](../00c5d/00c5dd20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd20` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbd4`](#insn-00bdcbd4) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbd8`](#insn-00bdcbd8) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbdc`](#insn-00bdcbdc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbe0`](#insn-00bdcbe0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbe4`](#insn-00bdcbe4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbfc`](#insn-00bdcbfc) → [`00c5ddc0`](../00c5d/00c5ddc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddc0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc04`](#insn-00bdcc04) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc0c`](#insn-00bdcc0c) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc14`](#insn-00bdcc14) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc1c`](#insn-00bdcc1c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc24`](#insn-00bdcc24) → [`00bdcc40`](#insn-00bdcc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc28`](#insn-00bdcc28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc2c`](#insn-00bdcc2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc30`](#insn-00bdcc30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc34`](#insn-00bdcc34) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc40`](#insn-00bdcc40) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcb80`](#insn-00bdcb80)

~~~json
{
  "source": "00bdcb80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb84`](#insn-00bdcb84)

~~~json
{
  "source": "00bdcb84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb88`](#insn-00bdcb88)

~~~json
{
  "source": "00bdcb88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb8c`](#insn-00bdcb8c)

~~~json
{
  "source": "00bdcb8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbac`](#insn-00bdcbac)

~~~json
{
  "source": "00bdcbac",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbb0`](#insn-00bdcbb0)

~~~json
{
  "source": "00bdcbb0",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbb4`](#insn-00bdcbb4)

~~~json
{
  "source": "00bdcbb4",
  "target": "00c5dd20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcbd4`](#insn-00bdcbd4)

~~~json
{
  "source": "00bdcbd4",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcbd8`](#insn-00bdcbd8)

~~~json
{
  "source": "00bdcbd8",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbdc`](#insn-00bdcbdc)

~~~json
{
  "source": "00bdcbdc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbe0`](#insn-00bdcbe0)

~~~json
{
  "source": "00bdcbe0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbe4`](#insn-00bdcbe4)

~~~json
{
  "source": "00bdcbe4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbfc`](#insn-00bdcbfc)

~~~json
{
  "source": "00bdcbfc",
  "target": "00c5ddc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc04`](#insn-00bdcc04)

~~~json
{
  "source": "00bdcc04",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc0c`](#insn-00bdcc0c)

~~~json
{
  "source": "00bdcc0c",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc14`](#insn-00bdcc14)

~~~json
{
  "source": "00bdcc14",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc1c`](#insn-00bdcc1c)

~~~json
{
  "source": "00bdcc1c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc24`](#insn-00bdcc24)

~~~json
{
  "source": "00bdcc24",
  "target": "00bdcc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc28`](#insn-00bdcc28)

~~~json
{
  "source": "00bdcc28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc2c`](#insn-00bdcc2c)

~~~json
{
  "source": "00bdcc2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc30`](#insn-00bdcc30)

~~~json
{
  "source": "00bdcc30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc34`](#insn-00bdcc34)

~~~json
{
  "source": "00bdcc34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc40`](#insn-00bdcc40)

~~~json
{
  "source": "00bdcc40",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
