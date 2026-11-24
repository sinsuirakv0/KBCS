# 00bddc0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcc18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-1cd584640bd208e1bef1166de9f36055)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddc0c",
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
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddc0c",
        "00bddcd3"
      ]
    ],
    "bytes_sha256": "ab088d540a5dc0f5536ea40baa4ddbb21b6c71f141385a5bb16e94fa4bbd345d",
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

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5edc0](../00c5e/00c5edc0.md)
- [00c5ee60](../00c5e/00c5ee60.md)

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
<a id="insn-00bddc0c"></a> `00bddc0c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bddc10"></a> `00bddc10` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bddc14"></a> `00bddc14` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bddc18"></a> `00bddc18` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bddc1c"></a> `00bddc1c` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bddc20"></a> `00bddc20` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bddc24"></a> `00bddc24` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bddc28"></a> `00bddc28` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bddc2c"></a> `00bddc2c` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bddc30"></a> `00bddc30` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bddc34"></a> `00bddc34` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bddc38"></a> `00bddc38` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bddc3c"></a> `00bddc3c` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bddc40"></a> `00bddc40` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bddc44"></a> `00bddc44` | `5f 04 02 94` | bl 0x00c5edc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc48"></a> `00bddc48` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc4c"></a> `00bddc4c` | `1f 1c 00 71` | cmp w0,#0x7 | `FALL_THROUGH`
<a id="insn-00bddc50"></a> `00bddc50` | `69 07 80 52` | mov w9,#0x3b | `FALL_THROUGH`
<a id="insn-00bddc54"></a> `00bddc54` | `36 01 80 1a` | csel w22,w9,w0,eq | `FALL_THROUGH`
<a id="insn-00bddc58"></a> `00bddc58` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddc5c"></a> `00bddc5c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bddc60"></a> `00bddc60` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bddc64"></a> `00bddc64` | `8f f8 01 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc68"></a> `00bddc68` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bddc6c"></a> `00bddc6c` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bddc70"></a> `00bddc70` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bddc74"></a> `00bddc74` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc78"></a> `00bddc78` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddc7c"></a> `00bddc7c` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bddc80"></a> `00bddc80` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bddc84"></a> `00bddc84` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bddc88"></a> `00bddc88` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bddc8c"></a> `00bddc8c` | `75 04 02 94` | bl 0x00c5ee60 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc90"></a> `00bddc90` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddc94"></a> `00bddc94` | `a7 f7 01 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc98"></a> `00bddc98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddc9c"></a> `00bddc9c` | `a5 f7 01 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bddca0"></a> `00bddca0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddca4"></a> `00bddca4` | `ab ec 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bddca8"></a> `00bddca8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bddcac"></a> `00bddcac` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bddcb0"></a> `00bddcb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bddcb4"></a> `00bddcb4` | `e1 00 00 54` | b.ne 0x00bddcd0 | `CONDITIONAL_JUMP`
<a id="insn-00bddcb8"></a> `00bddcb8` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bddcbc"></a> `00bddcbc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bddcc0"></a> `00bddcc0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bddcc4"></a> `00bddcc4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bddcc8"></a> `00bddcc8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bddccc"></a> `00bddccc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bddcd0"></a> `00bddcd0` | `ac ec 01 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddc0c`](#insn-00bddc0c) 範囲 `[['00bddc0c', '00bddcb7']]`
  - `CONDITIONAL_JUMP` [`00bddcb4`](#insn-00bddcb4) → [`00bddcd0`](#insn-00bddcd0)
  - `FALL_THROUGH` [`00bddcb4`](#insn-00bddcb4) → [`00bddcb8`](#insn-00bddcb8)
- ブロック [`00bddcb8`](#insn-00bddcb8) 範囲 `[['00bddcb8', '00bddccf']]`
- ブロック [`00bddcd0`](#insn-00bddcd0) 範囲 `[['00bddcd0', '00bddcd3']]`

## 命令位置別の参照

- [`00bddc10`](#insn-00bddc10) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc14`](#insn-00bddc14) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc18`](#insn-00bddc18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc1c`](#insn-00bddc1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc3c`](#insn-00bddc3c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc40`](#insn-00bddc40) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc44`](#insn-00bddc44) → [`00c5edc0`](../00c5e/00c5edc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5edc0` · 推定シンボル `None` · 推定型 `None`
- [`00bddc64`](#insn-00bddc64) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bddc68`](#insn-00bddc68) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc6c`](#insn-00bddc6c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc70`](#insn-00bddc70) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc74`](#insn-00bddc74) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc8c`](#insn-00bddc8c) → [`00c5ee60`](../00c5e/00c5ee60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ee60` · 推定シンボル `None` · 推定型 `None`
- [`00bddc94`](#insn-00bddc94) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bddc9c`](#insn-00bddc9c) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bddca4`](#insn-00bddca4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bddcac`](#insn-00bddcac) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcb4`](#insn-00bddcb4) → [`00bddcd0`](#insn-00bddcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcb8`](#insn-00bddcb8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcbc`](#insn-00bddcbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcc0`](#insn-00bddcc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcc4`](#insn-00bddcc4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcd0`](#insn-00bddcd0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddc10`](#insn-00bddc10)

~~~json
{
  "source": "00bddc10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc14`](#insn-00bddc14)

~~~json
{
  "source": "00bddc14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc18`](#insn-00bddc18)

~~~json
{
  "source": "00bddc18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc1c`](#insn-00bddc1c)

~~~json
{
  "source": "00bddc1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc3c`](#insn-00bddc3c)

~~~json
{
  "source": "00bddc3c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc40`](#insn-00bddc40)

~~~json
{
  "source": "00bddc40",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc44`](#insn-00bddc44)

~~~json
{
  "source": "00bddc44",
  "target": "00c5edc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc64`](#insn-00bddc64)

~~~json
{
  "source": "00bddc64",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc68`](#insn-00bddc68)

~~~json
{
  "source": "00bddc68",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc6c`](#insn-00bddc6c)

~~~json
{
  "source": "00bddc6c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc70`](#insn-00bddc70)

~~~json
{
  "source": "00bddc70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc74`](#insn-00bddc74)

~~~json
{
  "source": "00bddc74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc8c`](#insn-00bddc8c)

~~~json
{
  "source": "00bddc8c",
  "target": "00c5ee60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc94`](#insn-00bddc94)

~~~json
{
  "source": "00bddc94",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc9c`](#insn-00bddc9c)

~~~json
{
  "source": "00bddc9c",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddca4`](#insn-00bddca4)

~~~json
{
  "source": "00bddca4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddcac`](#insn-00bddcac)

~~~json
{
  "source": "00bddcac",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcb4`](#insn-00bddcb4)

~~~json
{
  "source": "00bddcb4",
  "target": "00bddcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcb8`](#insn-00bddcb8)

~~~json
{
  "source": "00bddcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcbc`](#insn-00bddcbc)

~~~json
{
  "source": "00bddcbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcc0`](#insn-00bddcc0)

~~~json
{
  "source": "00bddcc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcc4`](#insn-00bddcc4)

~~~json
{
  "source": "00bddcc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcd0`](#insn-00bddcd0)

~~~json
{
  "source": "00bddcd0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
