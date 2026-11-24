# 00bc5fbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc4fc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-711be5cb413614bf45b797c805c804dc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc5fbc",
  "name": "_ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "daf4995367100d2be558fc84dabd8182e6ca13a2f8746310ad59684107cccd05",
  "source_text_sha256": "daf4995367100d2be558fc84dabd8182e6ca13a2f8746310ad59684107cccd05",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc5fbc",
        "00bc60d7"
      ]
    ],
    "bytes_sha256": "5033c0486679cc5661f270216799aaba16d9b7988968624af2462feea1ef3bd1",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc60ec](../00bc6/00bc60ec.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5e970](../00c5e/00c5e970.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2047 bytes

~~~c

void _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,long param_2,int param_3,undefined8 param_4,undefined8 *param_5)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  undefined8 uVar6;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 auStack_70 [16];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  if ((param_2 != 0) && (param_3 == 0)) {
                    /* try { // try from 00bc5ff4 to 00cc5fff has its CatchHandler @ 00bc6504 */
    FUN_00bc60ec(param_1,param_2,&local_88);
  }
                    /* try { // try from 00bc6000 to 00cc6553 has its CatchHandler @ 00bc4ce4 */
  uVar6 = *param_5;
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_70,param_5 + 1);
  uStack_58 = uStack_80;
  local_60 = local_88;
  local_50 = local_78;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS3_E_EEvS7_iS9_RKT0_
            (uVar6,auStack_70,param_3 != 0,param_4,&local_60);
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  pbVar5 = (byte *)param_5[4];
  if (pbVar5 != (byte *)0x0) {
    pbVar4 = (byte *)param_5[5];
    pbVar3 = pbVar5;
    if (pbVar4 != pbVar5) {
      bVar1 = pbVar4[-0x18];
      pbVar3 = pbVar4 + -0x18;
      while( true ) {
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(pbVar4 + -8));
        }
        if (pbVar5 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar4 = pbVar3;
        pbVar3 = pbVar3 + -0x18;
      }
      pbVar3 = (byte *)param_5[4];
    }
    param_5[5] = pbVar5;
    _ZdlPv(pbVar3);
  }
  _ZN8firebase12FutureHandleD2Ev(param_5 + 1);
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
<a id="insn-00bc5fbc"></a> `00bc5fbc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bc5fc0"></a> `00bc5fc0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc5fc4"></a> `00bc5fc4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc5fc8"></a> `00bc5fc8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc5fcc"></a> `00bc5fcc` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc5fd0"></a> `00bc5fd0` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bc5fd4"></a> `00bc5fd4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bc5fd8"></a> `00bc5fd8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bc5fdc"></a> `00bc5fdc` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bc5fe0"></a> `00bc5fe0` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bc5fe4"></a> `00bc5fe4` | `f6 03 02 2a` | mov w22,w2 | `FALL_THROUGH`
<a id="insn-00bc5fe8"></a> `00bc5fe8` | `a8 83 1c f8` | stur x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bc5fec"></a> `00bc5fec` | `81 00 00 b4` | cbz x1,0x00bc5ffc | `CONDITIONAL_JUMP`
<a id="insn-00bc5ff0"></a> `00bc5ff0` | `76 00 00 35` | cbnz w22,0x00bc5ffc | `CONDITIONAL_JUMP`
<a id="insn-00bc5ff4"></a> `00bc5ff4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bc5ff8"></a> `00bc5ff8` | `3d 00 00 94` | bl 0x00bc60ec | `UNCONDITIONAL_CALL`
<a id="insn-00bc5ffc"></a> `00bc5ffc` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bc6000"></a> `00bc6000` | `97 86 40 f8` | ldr x23,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00bc6004"></a> `00bc6004` | `df 02 00 71` | cmp w22,#0x0 | `FALL_THROUGH`
<a id="insn-00bc6008"></a> `00bc6008` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc600c"></a> `00bc600c` | `f6 07 9f 1a` | cset w22,ne | `FALL_THROUGH`
<a id="insn-00bc6010"></a> `00bc6010` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc6014"></a> `00bc6014` | `a3 57 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6018"></a> `00bc6018` | `e0 83 c0 3c` | ldur q0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc601c"></a> `00bc601c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bc6020"></a> `00bc6020` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc6024"></a> `00bc6024` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc6028"></a> `00bc6028` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc602c"></a> `00bc602c` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc6030"></a> `00bc6030` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bc6034"></a> `00bc6034` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bc6038"></a> `00bc6038` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bc603c"></a> `00bc603c` | `4d 62 02 94` | bl 0x00c5e970 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6040"></a> `00bc6040` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc6044"></a> `00bc6044` | `bb 56 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6048"></a> `00bc6048` | `75 12 40 f9` | ldr x21,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc604c"></a> `00bc604c` | `95 02 00 b4` | cbz x21,0x00bc609c | `CONDITIONAL_JUMP`
<a id="insn-00bc6050"></a> `00bc6050` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bc6054"></a> `00bc6054` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bc6058"></a> `00bc6058` | `c0 01 00 54` | b.eq 0x00bc6090 | `CONDITIONAL_JUMP`
<a id="insn-00bc605c"></a> `00bc605c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bc6060"></a> `00bc6060` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc6064"></a> `00bc6064` | `c9 00 00 37` | tbnz w9,#0x0,0x00bc607c | `CONDITIONAL_JUMP`
<a id="insn-00bc6068"></a> `00bc6068` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00bc606c"></a> `00bc606c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bc6070"></a> `00bc6070` | `c0 00 00 54` | b.eq 0x00bc6088 | `CONDITIONAL_JUMP`
<a id="insn-00bc6074"></a> `00bc6074` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc6078"></a> `00bc6078` | `89 ff 07 36` | tbz w9,#0x0,0x00bc6068 | `CONDITIONAL_JUMP`
<a id="insn-00bc607c"></a> `00bc607c` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc6080"></a> `00bc6080` | `b4 4b 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6084"></a> `00bc6084` | `f9 ff ff 17` | b 0x00bc6068 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6088"></a> `00bc6088` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc608c"></a> `00bc608c` | `02 00 00 14` | b 0x00bc6094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6090"></a> `00bc6090` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc6094"></a> `00bc6094` | `75 16 00 f9` | str x21,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bc6098"></a> `00bc6098` | `ae 4b 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc609c"></a> `00bc609c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc60a0"></a> `00bc60a0` | `a4 56 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc60a4"></a> `00bc60a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc60a8"></a> `00bc60a8` | `aa 4b 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc60ac"></a> `00bc60ac` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bc60b0"></a> `00bc60b0` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bc60b4"></a> `00bc60b4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc60b8"></a> `00bc60b8` | `e1 00 00 54` | b.ne 0x00bc60d4 | `CONDITIONAL_JUMP`
<a id="insn-00bc60bc"></a> `00bc60bc` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc60c0"></a> `00bc60c0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc60c4"></a> `00bc60c4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc60c8"></a> `00bc60c8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc60cc"></a> `00bc60cc` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bc60d0"></a> `00bc60d0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc60d4"></a> `00bc60d4` | `ab 4b 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc5fbc`](#insn-00bc5fbc) 範囲 `[['00bc5fbc', '00bc5fef']]`
  - `CONDITIONAL_JUMP` [`00bc5fec`](#insn-00bc5fec) → [`00bc5ffc`](#insn-00bc5ffc)
  - `FALL_THROUGH` [`00bc5fec`](#insn-00bc5fec) → [`00bc5ff0`](#insn-00bc5ff0)
- ブロック [`00bc5ff0`](#insn-00bc5ff0) 範囲 `[['00bc5ff0', '00bc5ff3']]`
  - `CONDITIONAL_JUMP` [`00bc5ff0`](#insn-00bc5ff0) → [`00bc5ffc`](#insn-00bc5ffc)
  - `FALL_THROUGH` [`00bc5ff0`](#insn-00bc5ff0) → [`00bc5ff4`](#insn-00bc5ff4)
- ブロック [`00bc5ff4`](#insn-00bc5ff4) 範囲 `[['00bc5ff4', '00bc5ffb']]`
  - `FALL_THROUGH` [`00bc5ff8`](#insn-00bc5ff8) → [`00bc5ffc`](#insn-00bc5ffc)
- ブロック [`00bc5ffc`](#insn-00bc5ffc) 範囲 `[['00bc5ffc', '00bc5fff']]`
  - `FALL_THROUGH` [`00bc5ffc`](#insn-00bc5ffc) → [`00bc6000`](#insn-00bc6000)
- ブロック [`00bc6000`](#insn-00bc6000) 範囲 `[['00bc6000', '00bc604f']]`
  - `CONDITIONAL_JUMP` [`00bc604c`](#insn-00bc604c) → [`00bc609c`](#insn-00bc609c)
  - `FALL_THROUGH` [`00bc604c`](#insn-00bc604c) → [`00bc6050`](#insn-00bc6050)
- ブロック [`00bc6050`](#insn-00bc6050) 範囲 `[['00bc6050', '00bc605b']]`
  - `CONDITIONAL_JUMP` [`00bc6058`](#insn-00bc6058) → [`00bc6090`](#insn-00bc6090)
  - `FALL_THROUGH` [`00bc6058`](#insn-00bc6058) → [`00bc605c`](#insn-00bc605c)
- ブロック [`00bc605c`](#insn-00bc605c) 範囲 `[['00bc605c', '00bc6067']]`
  - `CONDITIONAL_JUMP` [`00bc6064`](#insn-00bc6064) → [`00bc607c`](#insn-00bc607c)
  - `FALL_THROUGH` [`00bc6064`](#insn-00bc6064) → [`00bc6068`](#insn-00bc6068)
- ブロック [`00bc6068`](#insn-00bc6068) 範囲 `[['00bc6068', '00bc6073']]`
  - `CONDITIONAL_JUMP` [`00bc6070`](#insn-00bc6070) → [`00bc6088`](#insn-00bc6088)
  - `FALL_THROUGH` [`00bc6070`](#insn-00bc6070) → [`00bc6074`](#insn-00bc6074)
- ブロック [`00bc6074`](#insn-00bc6074) 範囲 `[['00bc6074', '00bc607b']]`
  - `CONDITIONAL_JUMP` [`00bc6078`](#insn-00bc6078) → [`00bc6068`](#insn-00bc6068)
  - `FALL_THROUGH` [`00bc6078`](#insn-00bc6078) → [`00bc607c`](#insn-00bc607c)
- ブロック [`00bc607c`](#insn-00bc607c) 範囲 `[['00bc607c', '00bc6087']]`
  - `UNCONDITIONAL_JUMP` [`00bc6084`](#insn-00bc6084) → [`00bc6068`](#insn-00bc6068)
- ブロック [`00bc6088`](#insn-00bc6088) 範囲 `[['00bc6088', '00bc608f']]`
  - `UNCONDITIONAL_JUMP` [`00bc608c`](#insn-00bc608c) → [`00bc6094`](#insn-00bc6094)
- ブロック [`00bc6090`](#insn-00bc6090) 範囲 `[['00bc6090', '00bc6093']]`
  - `FALL_THROUGH` [`00bc6090`](#insn-00bc6090) → [`00bc6094`](#insn-00bc6094)
- ブロック [`00bc6094`](#insn-00bc6094) 範囲 `[['00bc6094', '00bc609b']]`
  - `FALL_THROUGH` [`00bc6098`](#insn-00bc6098) → [`00bc609c`](#insn-00bc609c)
- ブロック [`00bc609c`](#insn-00bc609c) 範囲 `[['00bc609c', '00bc60bb']]`
  - `CONDITIONAL_JUMP` [`00bc60b8`](#insn-00bc60b8) → [`00bc60d4`](#insn-00bc60d4)
  - `FALL_THROUGH` [`00bc60b8`](#insn-00bc60b8) → [`00bc60bc`](#insn-00bc60bc)
- ブロック [`00bc60bc`](#insn-00bc60bc) 範囲 `[['00bc60bc', '00bc60d3']]`
- ブロック [`00bc60d4`](#insn-00bc60d4) 範囲 `[['00bc60d4', '00bc60d7']]`

## 命令位置別の参照

- [`00bc5fc0`](#insn-00bc5fc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fc4`](#insn-00bc5fc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fc8`](#insn-00bc5fc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fcc`](#insn-00bc5fcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fe8`](#insn-00bc5fe8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fec`](#insn-00bc5fec) → [`00bc5ffc`](#insn-00bc5ffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ff0`](#insn-00bc5ff0) → [`00bc5ffc`](#insn-00bc5ffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ff8`](#insn-00bc5ff8) → [`00bc60ec`](../00bc6/00bc60ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc60ec` · 推定シンボル `None` · 推定型 `None`
- [`00bc6014`](#insn-00bc6014) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6018`](#insn-00bc6018) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc601c`](#insn-00bc601c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6020`](#insn-00bc6020) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6024`](#insn-00bc6024) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc603c`](#insn-00bc603c) → [`00c5e970`](../00c5e/00c5e970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e970` · 推定シンボル `None` · 推定型 `None`
- [`00bc6044`](#insn-00bc6044) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc604c`](#insn-00bc604c) → [`00bc609c`](#insn-00bc609c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6058`](#insn-00bc6058) → [`00bc6090`](#insn-00bc6090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6064`](#insn-00bc6064) → [`00bc607c`](#insn-00bc607c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6070`](#insn-00bc6070) → [`00bc6088`](#insn-00bc6088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6078`](#insn-00bc6078) → [`00bc6068`](#insn-00bc6068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6080`](#insn-00bc6080) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc6084`](#insn-00bc6084) → [`00bc6068`](#insn-00bc6068) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc608c`](#insn-00bc608c) → [`00bc6094`](#insn-00bc6094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6098`](#insn-00bc6098) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc60a0`](#insn-00bc60a0) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc60a8`](#insn-00bc60a8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc60b0`](#insn-00bc60b0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60b8`](#insn-00bc60b8) → [`00bc60d4`](#insn-00bc60d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60bc`](#insn-00bc60bc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60c0`](#insn-00bc60c0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60c4`](#insn-00bc60c4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60c8`](#insn-00bc60c8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60d4`](#insn-00bc60d4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc5fc0`](#insn-00bc5fc0)

~~~json
{
  "source": "00bc5fc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fc4`](#insn-00bc5fc4)

~~~json
{
  "source": "00bc5fc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fc8`](#insn-00bc5fc8)

~~~json
{
  "source": "00bc5fc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fcc`](#insn-00bc5fcc)

~~~json
{
  "source": "00bc5fcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fe8`](#insn-00bc5fe8)

~~~json
{
  "source": "00bc5fe8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fec`](#insn-00bc5fec)

~~~json
{
  "source": "00bc5fec",
  "target": "00bc5ffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ff0`](#insn-00bc5ff0)

~~~json
{
  "source": "00bc5ff0",
  "target": "00bc5ffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ff8`](#insn-00bc5ff8)

~~~json
{
  "source": "00bc5ff8",
  "target": "00bc60ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6014`](#insn-00bc6014)

~~~json
{
  "source": "00bc6014",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6018`](#insn-00bc6018)

~~~json
{
  "source": "00bc6018",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc601c`](#insn-00bc601c)

~~~json
{
  "source": "00bc601c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6020`](#insn-00bc6020)

~~~json
{
  "source": "00bc6020",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6024`](#insn-00bc6024)

~~~json
{
  "source": "00bc6024",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc603c`](#insn-00bc603c)

~~~json
{
  "source": "00bc603c",
  "target": "00c5e970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6044`](#insn-00bc6044)

~~~json
{
  "source": "00bc6044",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc604c`](#insn-00bc604c)

~~~json
{
  "source": "00bc604c",
  "target": "00bc609c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6058`](#insn-00bc6058)

~~~json
{
  "source": "00bc6058",
  "target": "00bc6090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6064`](#insn-00bc6064)

~~~json
{
  "source": "00bc6064",
  "target": "00bc607c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6070`](#insn-00bc6070)

~~~json
{
  "source": "00bc6070",
  "target": "00bc6088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6078`](#insn-00bc6078)

~~~json
{
  "source": "00bc6078",
  "target": "00bc6068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6080`](#insn-00bc6080)

~~~json
{
  "source": "00bc6080",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6084`](#insn-00bc6084)

~~~json
{
  "source": "00bc6084",
  "target": "00bc6068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc608c`](#insn-00bc608c)

~~~json
{
  "source": "00bc608c",
  "target": "00bc6094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6098`](#insn-00bc6098)

~~~json
{
  "source": "00bc6098",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc60a0`](#insn-00bc60a0)

~~~json
{
  "source": "00bc60a0",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc60a8`](#insn-00bc60a8)

~~~json
{
  "source": "00bc60a8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc60b0`](#insn-00bc60b0)

~~~json
{
  "source": "00bc60b0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60b8`](#insn-00bc60b8)

~~~json
{
  "source": "00bc60b8",
  "target": "00bc60d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60bc`](#insn-00bc60bc)

~~~json
{
  "source": "00bc60bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60c0`](#insn-00bc60c0)

~~~json
{
  "source": "00bc60c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60c4`](#insn-00bc60c4)

~~~json
{
  "source": "00bc60c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60c8`](#insn-00bc60c8)

~~~json
{
  "source": "00bc60c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60d4`](#insn-00bc60d4)

~~~json
{
  "source": "00bc60d4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
