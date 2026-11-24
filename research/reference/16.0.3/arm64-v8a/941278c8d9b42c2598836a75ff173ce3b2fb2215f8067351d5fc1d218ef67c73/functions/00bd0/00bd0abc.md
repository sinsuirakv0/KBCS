# 00bd0abc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcfac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-7165fc8528fdf4f503e02a9e51c6545b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0abc",
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
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0abc",
        "00bd0b7b"
      ]
    ],
    "bytes_sha256": "46a4ea9b05a8c3b20bc7051a713f2cfeed79530166f9f9aae260dd8ff2f9f552",
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

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5ec40](../00c5e/00c5ec40.md)
- [00c5edc0](../00c5e/00c5edc0.md)

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
<a id="insn-00bd0abc"></a> `00bd0abc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bd0ac0"></a> `00bd0ac0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bd0ac4"></a> `00bd0ac4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bd0ac8"></a> `00bd0ac8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bd0acc"></a> `00bd0acc` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bd0ad0"></a> `00bd0ad0` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bd0ad4"></a> `00bd0ad4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bd0ad8"></a> `00bd0ad8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0adc"></a> `00bd0adc` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bd0ae0"></a> `00bd0ae0` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bd0ae4"></a> `00bd0ae4` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bd0ae8"></a> `00bd0ae8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bd0aec"></a> `00bd0aec` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bd0af0"></a> `00bd0af0` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bd0af4"></a> `00bd0af4` | `b3 38 02 94` | bl 0x00c5edc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0af8"></a> `00bd0af8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0afc"></a> `00bd0afc` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bd0b00"></a> `00bd0b00` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0b04"></a> `00bd0b04` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd0b08"></a> `00bd0b08` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0b0c"></a> `00bd0b0c` | `e5 2c 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0b10"></a> `00bd0b10` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bd0b14"></a> `00bd0b14` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0b18"></a> `00bd0b18` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bd0b1c"></a> `00bd0b1c` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0b20"></a> `00bd0b20` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0b24"></a> `00bd0b24` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd0b28"></a> `00bd0b28` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd0b2c"></a> `00bd0b2c` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bd0b30"></a> `00bd0b30` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bd0b34"></a> `00bd0b34` | `43 38 02 94` | bl 0x00c5ec40 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0b38"></a> `00bd0b38` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd0b3c"></a> `00bd0b3c` | `fd 2b 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0b40"></a> `00bd0b40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0b44"></a> `00bd0b44` | `fb 2b 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0b48"></a> `00bd0b48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd0b4c"></a> `00bd0b4c` | `01 21 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0b50"></a> `00bd0b50` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0b54"></a> `00bd0b54` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bd0b58"></a> `00bd0b58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd0b5c"></a> `00bd0b5c` | `e1 00 00 54` | b.ne 0x00bd0b78 | `CONDITIONAL_JUMP`
<a id="insn-00bd0b60"></a> `00bd0b60` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bd0b64"></a> `00bd0b64` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bd0b68"></a> `00bd0b68` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bd0b6c"></a> `00bd0b6c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bd0b70"></a> `00bd0b70` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bd0b74"></a> `00bd0b74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd0b78"></a> `00bd0b78` | `02 21 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0abc`](#insn-00bd0abc) 範囲 `[['00bd0abc', '00bd0b5f']]`
  - `CONDITIONAL_JUMP` [`00bd0b5c`](#insn-00bd0b5c) → [`00bd0b78`](#insn-00bd0b78)
  - `FALL_THROUGH` [`00bd0b5c`](#insn-00bd0b5c) → [`00bd0b60`](#insn-00bd0b60)
- ブロック [`00bd0b60`](#insn-00bd0b60) 範囲 `[['00bd0b60', '00bd0b77']]`
- ブロック [`00bd0b78`](#insn-00bd0b78) 範囲 `[['00bd0b78', '00bd0b7b']]`

## 命令位置別の参照

- [`00bd0ac0`](#insn-00bd0ac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ac4`](#insn-00bd0ac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ac8`](#insn-00bd0ac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0acc`](#insn-00bd0acc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0aec`](#insn-00bd0aec) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0af0`](#insn-00bd0af0) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0af4`](#insn-00bd0af4) → [`00c5edc0`](../00c5e/00c5edc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edc0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b0c`](#insn-00bd0b0c) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b10`](#insn-00bd0b10) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b14`](#insn-00bd0b14) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b18`](#insn-00bd0b18) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b1c`](#insn-00bd0b1c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b34`](#insn-00bd0b34) → [`00c5ec40`](../00c5e/00c5ec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec40` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b3c`](#insn-00bd0b3c) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b44`](#insn-00bd0b44) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b4c`](#insn-00bd0b4c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b54`](#insn-00bd0b54) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b5c`](#insn-00bd0b5c) → [`00bd0b78`](#insn-00bd0b78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b60`](#insn-00bd0b60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b64`](#insn-00bd0b64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b68`](#insn-00bd0b68) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b6c`](#insn-00bd0b6c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0b78`](#insn-00bd0b78) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0ac0`](#insn-00bd0ac0)

~~~json
{
  "source": "00bd0ac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ac4`](#insn-00bd0ac4)

~~~json
{
  "source": "00bd0ac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ac8`](#insn-00bd0ac8)

~~~json
{
  "source": "00bd0ac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0acc`](#insn-00bd0acc)

~~~json
{
  "source": "00bd0acc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0aec`](#insn-00bd0aec)

~~~json
{
  "source": "00bd0aec",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0af0`](#insn-00bd0af0)

~~~json
{
  "source": "00bd0af0",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0af4`](#insn-00bd0af4)

~~~json
{
  "source": "00bd0af4",
  "target": "00c5edc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b0c`](#insn-00bd0b0c)

~~~json
{
  "source": "00bd0b0c",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b10`](#insn-00bd0b10)

~~~json
{
  "source": "00bd0b10",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b14`](#insn-00bd0b14)

~~~json
{
  "source": "00bd0b14",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b18`](#insn-00bd0b18)

~~~json
{
  "source": "00bd0b18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b1c`](#insn-00bd0b1c)

~~~json
{
  "source": "00bd0b1c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b34`](#insn-00bd0b34)

~~~json
{
  "source": "00bd0b34",
  "target": "00c5ec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b3c`](#insn-00bd0b3c)

~~~json
{
  "source": "00bd0b3c",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b44`](#insn-00bd0b44)

~~~json
{
  "source": "00bd0b44",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b4c`](#insn-00bd0b4c)

~~~json
{
  "source": "00bd0b4c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0b54`](#insn-00bd0b54)

~~~json
{
  "source": "00bd0b54",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b5c`](#insn-00bd0b5c)

~~~json
{
  "source": "00bd0b5c",
  "target": "00bd0b78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b60`](#insn-00bd0b60)

~~~json
{
  "source": "00bd0b60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b64`](#insn-00bd0b64)

~~~json
{
  "source": "00bd0b64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b68`](#insn-00bd0b68)

~~~json
{
  "source": "00bd0b68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b6c`](#insn-00bd0b6c)

~~~json
{
  "source": "00bd0b6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0b78`](#insn-00bd0b78)

~~~json
{
  "source": "00bd0b78",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
