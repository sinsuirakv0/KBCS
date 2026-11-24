# 00c1ffdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba3594`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0074.md#compare-e95a8b2d27c264d99bc05d88350add58)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c20404`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20404.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0088.md#compare-5d6487685452acdc31f7507bb955c987)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1ffdc",
  "name": "FUN_00c1ffdc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afcbfce993581fe1f346912f33a8c17e952282bd2df36d8f9a691596a07b500c",
  "source_text_sha256": "afcbfce993581fe1f346912f33a8c17e952282bd2df36d8f9a691596a07b500c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1ffdc",
        "00c200d7"
      ]
    ],
    "bytes_sha256": "fd478a33d796a95b05458e5b14959fa433e0596f5f9f0c93a7120f2a15e6edba",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c1f064](../00c1f/00c1f064.md)
- [00c21500](../00c21/00c21500.md)

## 呼び出し先

- [00c3561c](../00c35/00c3561c.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c5dae0](../00c5d/00c5dae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1435 bytes

~~~c

void FUN_00c1ffdc(long param_1,long param_2)

{
  undefined *puVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  undefined *local_48;
  undefined8 **local_40;
  undefined **local_38;
  
  puVar1 = PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838;
  local_48 = PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838;
  if (*(long *)PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838 != -1) {
    local_38 = &local_48;
    local_40 = &local_38;
                    /* try { // try from 00c20020 to 00d20027 has its CatchHandler @ 00c286c0 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838,&local_40,FUN_00c35b90);
  }
  uVar2 = (ulong)*(int *)(puVar1 + 8);
  uVar7 = uVar2 - 1;
  FUN_00c538b0(1,param_2 + 8);
  plVar5 = (long *)(param_1 + 0x10);
  lVar3 = *plVar5;
  uVar4 = *(long *)(param_1 + 0x18) - lVar3 >> 3;
  if (uVar4 <= uVar7) {
    if (uVar2 < uVar4 || uVar2 - uVar4 == 0) {
      if (uVar2 < uVar4) {
        *(ulong *)(param_1 + 0x18) = lVar3 + uVar2 * 8;
      }
    }
    else {
      FUN_00c3561c(plVar5,uVar2 - uVar4);
      lVar3 = *plVar5;
    }
  }
  plVar6 = *(long **)(lVar3 + uVar7 * 8);
  if ((plVar6 != (long *)0x0) && (lVar3 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar3 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
  }
  *(long *)(*plVar5 + uVar7 * 8) = param_2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1ffdc"></a> `00c1ffdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c1ffe0"></a> `00c1ffe0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c1ffe4"></a> `00c1ffe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1ffe8"></a> `00c1ffe8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1ffec"></a> `00c1ffec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1fff0"></a> `00c1fff0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00c1fff4"></a> `00c1fff4` | `f4 03 00 90` | adrp x20,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1fff8"></a> `00c1fff8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c1fffc"></a> `00c1fffc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c20000"></a> `00c20000` | `94 1e 44 f9` | ldr x20,[x20, #0x838] | `FALL_THROUGH`
<a id="insn-00c20004"></a> `00c20004` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c20008"></a> `00c20008` | `88 fe df c8` | ldar x8,[x20] | `FALL_THROUGH`
<a id="insn-00c2000c"></a> `00c2000c` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c20010"></a> `00c20010` | `60 01 00 54` | b.eq 0x00c2003c | `CONDITIONAL_JUMP`
<a id="insn-00c20014"></a> `00c20014` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c20018"></a> `00c20018` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c2001c"></a> `00c2001c` | `c0 03 00 f0` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c20020"></a> `00c20020` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c20024"></a> `00c20024` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c20028"></a> `00c20028` | `42 db 0a 10` | adr x2,0xc35b90 | `FALL_THROUGH`
<a id="insn-00c2002c"></a> `00c2002c` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c20030"></a> `00c20030` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c20034"></a> `00c20034` | `00 1c 44 f9` | ldr x0,[x0, #0x838] | `FALL_THROUGH`
<a id="insn-00c20038"></a> `00c20038` | `aa f6 00 94` | bl 0x00c5dae0 | `UNCONDITIONAL_CALL`
<a id="insn-00c2003c"></a> `00c2003c` | `88 0a 80 b9` | ldrsw x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c20040"></a> `00c20040` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00c20044"></a> `00c20044` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c20048"></a> `00c20048` | `16 05 00 d1` | sub x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c2004c"></a> `00c2004c` | `19 ce 00 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-00c20050"></a> `00c20050` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00c20054"></a> `00c20054` | `88 26 c1 a9` | ldp x8,x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00c20058"></a> `00c20058` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00c2005c"></a> `00c2005c` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00c20060"></a> `00c20060` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00c20064"></a> `00c20064` | `68 01 00 54` | b.hi 0x00c20090 | `CONDITIONAL_JUMP`
<a id="insn-00c20068"></a> `00c20068` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00c2006c"></a> `00c2006c` | `21 01 0a eb` | subs x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00c20070"></a> `00c20070` | `a9 00 00 54` | b.ls 0x00c20084 | `CONDITIONAL_JUMP`
<a id="insn-00c20074"></a> `00c20074` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c20078"></a> `00c20078` | `69 55 00 94` | bl 0x00c3561c | `UNCONDITIONAL_CALL`
<a id="insn-00c2007c"></a> `00c2007c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c20080"></a> `00c20080` | `04 00 00 14` | b 0x00c20090 | `UNCONDITIONAL_JUMP`
<a id="insn-00c20084"></a> `00c20084` | `62 00 00 54` | b.cs 0x00c20090 | `CONDITIONAL_JUMP`
<a id="insn-00c20088"></a> `00c20088` | `09 0d 09 8b` | add x9,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00c2008c"></a> `00c2008c` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c20090"></a> `00c20090` | `15 79 76 f8` | ldr x21,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c20094"></a> `00c20094` | `35 01 00 b4` | cbz x21,0x00c200b8 | `CONDITIONAL_JUMP`
<a id="insn-00c20098"></a> `00c20098` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00c2009c"></a> `00c2009c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00c200a0"></a> `00c200a0` | `10 ce 00 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00c200a4"></a> `00c200a4` | `a0 00 00 b5` | cbnz x0,0x00c200b8 | `CONDITIONAL_JUMP`
<a id="insn-00c200a8"></a> `00c200a8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c200ac"></a> `00c200ac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c200b0"></a> `00c200b0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00c200b4"></a> `00c200b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c200b8"></a> `00c200b8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c200bc"></a> `00c200bc` | `13 79 36 f8` | str x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c200c0"></a> `00c200c0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c200c4"></a> `00c200c4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c200c8"></a> `00c200c8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c200cc"></a> `00c200cc` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c200d0"></a> `00c200d0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c200d4"></a> `00c200d4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1ffdc`](#insn-00c1ffdc) 範囲 `[['00c1ffdc', '00c20013']]`
  - `CONDITIONAL_JUMP` [`00c20010`](#insn-00c20010) → [`00c2003c`](#insn-00c2003c)
  - `FALL_THROUGH` [`00c20010`](#insn-00c20010) → [`00c20014`](#insn-00c20014)
- ブロック [`00c20014`](#insn-00c20014) 範囲 `[['00c20014', '00c2001f']]`
  - `FALL_THROUGH` [`00c2001c`](#insn-00c2001c) → [`00c20020`](#insn-00c20020)
- ブロック [`00c20020`](#insn-00c20020) 範囲 `[['00c20020', '00c2003b']]`
  - `FALL_THROUGH` [`00c20038`](#insn-00c20038) → [`00c2003c`](#insn-00c2003c)
- ブロック [`00c2003c`](#insn-00c2003c) 範囲 `[['00c2003c', '00c20067']]`
  - `CONDITIONAL_JUMP` [`00c20064`](#insn-00c20064) → [`00c20090`](#insn-00c20090)
  - `FALL_THROUGH` [`00c20064`](#insn-00c20064) → [`00c20068`](#insn-00c20068)
- ブロック [`00c20068`](#insn-00c20068) 範囲 `[['00c20068', '00c20073']]`
  - `CONDITIONAL_JUMP` [`00c20070`](#insn-00c20070) → [`00c20084`](#insn-00c20084)
  - `FALL_THROUGH` [`00c20070`](#insn-00c20070) → [`00c20074`](#insn-00c20074)
- ブロック [`00c20074`](#insn-00c20074) 範囲 `[['00c20074', '00c20083']]`
  - `UNCONDITIONAL_JUMP` [`00c20080`](#insn-00c20080) → [`00c20090`](#insn-00c20090)
- ブロック [`00c20084`](#insn-00c20084) 範囲 `[['00c20084', '00c20087']]`
  - `CONDITIONAL_JUMP` [`00c20084`](#insn-00c20084) → [`00c20090`](#insn-00c20090)
  - `FALL_THROUGH` [`00c20084`](#insn-00c20084) → [`00c20088`](#insn-00c20088)
- ブロック [`00c20088`](#insn-00c20088) 範囲 `[['00c20088', '00c2008f']]`
  - `FALL_THROUGH` [`00c2008c`](#insn-00c2008c) → [`00c20090`](#insn-00c20090)
- ブロック [`00c20090`](#insn-00c20090) 範囲 `[['00c20090', '00c20097']]`
  - `CONDITIONAL_JUMP` [`00c20094`](#insn-00c20094) → [`00c200b8`](#insn-00c200b8)
  - `FALL_THROUGH` [`00c20094`](#insn-00c20094) → [`00c20098`](#insn-00c20098)
- ブロック [`00c20098`](#insn-00c20098) 範囲 `[['00c20098', '00c200a7']]`
  - `CONDITIONAL_JUMP` [`00c200a4`](#insn-00c200a4) → [`00c200b8`](#insn-00c200b8)
  - `FALL_THROUGH` [`00c200a4`](#insn-00c200a4) → [`00c200a8`](#insn-00c200a8)
- ブロック [`00c200a8`](#insn-00c200a8) 範囲 `[['00c200a8', '00c200b7']]`
  - `FALL_THROUGH` [`00c200b4`](#insn-00c200b4) → [`00c200b8`](#insn-00c200b8)
- ブロック [`00c200b8`](#insn-00c200b8) 範囲 `[['00c200b8', '00c200d7']]`

## 命令位置別の参照

- [`00c1ffe4`](#insn-00c1ffe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ffe8`](#insn-00c1ffe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ffec`](#insn-00c1ffec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20000`](#insn-00c20000) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c20004`](#insn-00c20004) → `01127a68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE` · 推定型 `undefined8`
- [`00c20004`](#insn-00c20004) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20008`](#insn-00c20008) → `01127a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE` · 推定型 `undefined8`
- [`00c20010`](#insn-00c20010) → [`00c2003c`](#insn-00c2003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20020`](#insn-00c20020) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20028`](#insn-00c20028) → [`00c35b90`](../00c35/00c35b90.md) · `PARAM` · `ANALYSIS` · 関数 `00c35b90` · 推定シンボル `None` · 推定型 `None`
- [`00c2002c`](#insn-00c2002c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20034`](#insn-00c20034) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c20034`](#insn-00c20034) → `01127a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE` · 推定型 `undefined8`
- [`00c20038`](#insn-00c20038) → [`00c5dae0`](../00c5d/00c5dae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dae0` · 推定シンボル `None` · 推定型 `None`
- [`00c2003c`](#insn-00c2003c) → `01127a70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c2004c`](#insn-00c2004c) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`00c20064`](#insn-00c20064) → [`00c20090`](#insn-00c20090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20070`](#insn-00c20070) → [`00c20084`](#insn-00c20084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20078`](#insn-00c20078) → [`00c3561c`](../00c35/00c3561c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3561c` · 推定シンボル `None` · 推定型 `None`
- [`00c20080`](#insn-00c20080) → [`00c20090`](#insn-00c20090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20084`](#insn-00c20084) → [`00c20090`](#insn-00c20090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c20094`](#insn-00c20094) → [`00c200b8`](#insn-00c200b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c200a0`](#insn-00c200a0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00c200a4`](#insn-00c200a4) → [`00c200b8`](#insn-00c200b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c200c0`](#insn-00c200c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c200c4`](#insn-00c200c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c200c8`](#insn-00c200c8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1ffe4`](#insn-00c1ffe4)

~~~json
{
  "source": "00c1ffe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ffe8`](#insn-00c1ffe8)

~~~json
{
  "source": "00c1ffe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ffec`](#insn-00c1ffec)

~~~json
{
  "source": "00c1ffec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20000`](#insn-00c20000)

~~~json
{
  "source": "00c20000",
  "target": "00c9b838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b838",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c20004`](#insn-00c20004)

~~~json
{
  "source": "00c20004",
  "target": "01127a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c20004`](#insn-00c20004)

~~~json
{
  "source": "00c20004",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20008`](#insn-00c20008)

~~~json
{
  "source": "00c20008",
  "target": "01127a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c20010`](#insn-00c20010)

~~~json
{
  "source": "00c20010",
  "target": "00c2003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20020`](#insn-00c20020)

~~~json
{
  "source": "00c20020",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20028`](#insn-00c20028)

~~~json
{
  "source": "00c20028",
  "target": "00c35b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2002c`](#insn-00c2002c)

~~~json
{
  "source": "00c2002c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20034`](#insn-00c20034)

~~~json
{
  "source": "00c20034",
  "target": "00c9b838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b838",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c20034`](#insn-00c20034)

~~~json
{
  "source": "00c20034",
  "target": "01127a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c20038`](#insn-00c20038)

~~~json
{
  "source": "00c20038",
  "target": "00c5dae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2003c`](#insn-00c2003c)

~~~json
{
  "source": "00c2003c",
  "target": "01127a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a70",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2004c`](#insn-00c2004c)

~~~json
{
  "source": "00c2004c",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c20064`](#insn-00c20064)

~~~json
{
  "source": "00c20064",
  "target": "00c20090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20070`](#insn-00c20070)

~~~json
{
  "source": "00c20070",
  "target": "00c20084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20078`](#insn-00c20078)

~~~json
{
  "source": "00c20078",
  "target": "00c3561c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c20080`](#insn-00c20080)

~~~json
{
  "source": "00c20080",
  "target": "00c20090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20084`](#insn-00c20084)

~~~json
{
  "source": "00c20084",
  "target": "00c20090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c20094`](#insn-00c20094)

~~~json
{
  "source": "00c20094",
  "target": "00c200b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c200a0`](#insn-00c200a0)

~~~json
{
  "source": "00c200a0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c200a4`](#insn-00c200a4)

~~~json
{
  "source": "00c200a4",
  "target": "00c200b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c200c0`](#insn-00c200c0)

~~~json
{
  "source": "00c200c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c200c4`](#insn-00c200c4)

~~~json
{
  "source": "00c200c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c200c8`](#insn-00c200c8)

~~~json
{
  "source": "00c200c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
