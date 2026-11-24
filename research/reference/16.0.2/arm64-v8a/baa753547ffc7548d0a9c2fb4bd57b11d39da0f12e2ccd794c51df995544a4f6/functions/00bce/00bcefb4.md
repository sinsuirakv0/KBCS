# 00bcefb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcef18`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-a92c9291eeb2702969fa5d8d89b1a2d9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcffa8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcffa8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-c22d9223b014f1c70b439eb187a3819f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcefb4",
  "name": "_ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6073ffa1c6818ad8b7468d6c0f4f46c2ae7159ad5d8ecc59214a05860420774",
  "source_text_sha256": "d6073ffa1c6818ad8b7468d6c0f4f46c2ae7159ad5d8ecc59214a05860420774",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcefb4",
        "00bcf1eb"
      ]
    ],
    "bytes_sha256": "0b94208526c8800e73ae44d0cd57ecf597c73c6584f7b278f1a7bd8c4e479025",
    "instruction_count": 142,
    "instruction_bytes": 568,
    "body_bytes": 568,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580b0](../00c58/00c580b0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dc90](../00c5d/00c5dc90.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

## 関連文字列（未確認候補）

~~~text
"Empty email or password are not allowed."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3683 bytes

~~~c

void _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_
               (undefined8 param_1,long *param_2,char *param_3,char *param_4)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  size_t sVar4;
  long *plVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined4 uVar12;
  undefined8 *puVar13;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,7);
  if ((((param_3 == (char *)0x0) || (sVar4 = strlen(param_3), param_4 == (char *)0x0)) ||
      (sVar4 == 0)) || (sVar4 = strlen(param_4), sVar4 == 0)) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    uVar12 = 0x25;
    if (param_3 != (char *)0x0) {
      sVar4 = strlen(param_3);
      uVar12 = 0x25;
      if (sVar4 != 0) {
        uVar12 = 0x26;
      }
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,uVar12,"Empty email or password are not allowed.",auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  else {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
    uVar6 = (**(code **)(*plVar5 + 0x538))(plVar5,param_3);
    uVar7 = (**(code **)(*plVar5 + 0x538))(plVar5,param_4);
    uVar8 = FUN_00497874(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_011268b8,uVar6,uVar7);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar6);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar7);
    uVar9 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar5,lVar1,auStack_70);
    if ((uVar9 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar13 = (undefined8 *)*param_2;
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar13);
      lVar10 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar10,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
      ;
      *(undefined8 **)(lVar10 + 0x10) = puVar13;
      *(undefined **)(lVar10 + 0x18) = puVar3;
      if ((*(byte *)(puVar13 + 0x28) & 1) == 0) {
        lVar11 = (long)puVar13 + 0x141;
      }
      else {
        lVar11 = puVar13[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar8,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
                 ,lVar10,lVar11);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar5 + 0xb8))(plVar5,uVar8);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bcf1e8 to 00ccf1ef has its CatchHandler @ 00bcf1f0 */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcefb4"></a> `00bcefb4` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcefb8"></a> `00bcefb8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcefbc"></a> `00bcefbc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcefc0"></a> `00bcefc0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcefc4"></a> `00bcefc4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcefc8"></a> `00bcefc8` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcefcc"></a> `00bcefcc` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcefd0"></a> `00bcefd0` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcefd4"></a> `00bcefd4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcefd8"></a> `00bcefd8` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcefdc"></a> `00bcefdc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcefe0"></a> `00bcefe0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcefe4"></a> `00bcefe4` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00bcefe8"></a> `00bcefe8` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcefec"></a> `00bcefec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceff0"></a> `00bceff0` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bceff4"></a> `00bceff4` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bceff8"></a> `00bceff8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bceffc"></a> `00bceffc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf000"></a> `00bcf000` | `34 3b 02 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf004"></a> `00bcf004` | `77 08 00 b4` | cbz x23,0x00bcf110 | `CONDITIONAL_JUMP`
<a id="insn-00bcf008"></a> `00bcf008` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcf00c"></a> `00bcf00c` | `29 24 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf010"></a> `00bcf010` | `18 08 00 b4` | cbz x24,0x00bcf110 | `CONDITIONAL_JUMP`
<a id="insn-00bcf014"></a> `00bcf014` | `e0 07 00 b4` | cbz x0,0x00bcf110 | `CONDITIONAL_JUMP`
<a id="insn-00bcf018"></a> `00bcf018` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcf01c"></a> `00bcf01c` | `25 24 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf020"></a> `00bcf020` | `80 07 00 b4` | cbz x0,0x00bcf110 | `CONDITIONAL_JUMP`
<a id="insn-00bcf024"></a> `00bcf024` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcf028"></a> `00bcf028` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcf02c"></a> `00bcf02c` | `49 30 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf030"></a> `00bcf030` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcf034"></a> `00bcf034` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcf038"></a> `00bcf038` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcf03c"></a> `00bcf03c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcf040"></a> `00bcf040` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf044"></a> `00bcf044` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcf048"></a> `00bcf048` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bcf04c"></a> `00bcf04c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcf050"></a> `00bcf050` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf054"></a> `00bcf054` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcf058"></a> `00bcf058` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf05c"></a> `00bcf05c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcf060"></a> `00bcf060` | `a9 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcf064"></a> `00bcf064` | `22 5d 44 f9` | ldr x2,[x9, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bcf068"></a> `00bcf068` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcf06c"></a> `00bcf06c` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcf070"></a> `00bcf070` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf074"></a> `00bcf074` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bcf078"></a> `00bcf078` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00bcf07c"></a> `00bcf07c` | `fe 21 e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf080"></a> `00bcf080` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcf084"></a> `00bcf084` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcf088"></a> `00bcf088` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcf08c"></a> `00bcf08c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf090"></a> `00bcf090` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bcf094"></a> `00bcf094` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf098"></a> `00bcf098` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcf09c"></a> `00bcf09c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcf0a0"></a> `00bcf0a0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf0a4"></a> `00bcf0a4` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcf0a8"></a> `00bcf0a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf0ac"></a> `00bcf0ac` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf0b0"></a> `00bcf0b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf0b4"></a> `00bcf0b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf0b8"></a> `00bcf0b8` | `3a 3b 02 94` | bl 0x00c5dda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf0bc"></a> `00bcf0bc` | `c0 08 00 37` | tbnz w0,#0x0,0x00bcf1d4 | `CONDITIONAL_JUMP`
<a id="insn-00bcf0c0"></a> `00bcf0c0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcf0c4"></a> `00bcf0c4` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf0c8"></a> `00bcf0c8` | `82 2f 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf0cc"></a> `00bcf0cc` | `d9 02 40 f9` | ldr x25,[x22] | `FALL_THROUGH`
<a id="insn-00bcf0d0"></a> `00bcf0d0` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00bcf0d4"></a> `00bcf0d4` | `1f 30 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf0d8"></a> `00bcf0d8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcf0dc"></a> `00bcf0dc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf0e0"></a> `00bcf0e0` | `a0 23 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf0e4"></a> `00bcf0e4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcf0e8"></a> `00bcf0e8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bcf0ec"></a> `00bcf0ec` | `79 2f 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf0f0"></a> `00bcf0f0` | `68 06 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcf0f4"></a> `00bcf0f4` | `08 79 45 f9` | ldr x8,[x8, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bcf0f8"></a> `00bcf0f8` | `19 23 01 a9` | stp x25,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf0fc"></a> `00bcf0fc` | `28 03 45 39` | ldrb w8,[x25, #0x140] | `FALL_THROUGH`
<a id="insn-00bcf100"></a> `00bcf100` | `e8 04 00 37` | tbnz w8,#0x0,0x00bcf19c | `CONDITIONAL_JUMP`
<a id="insn-00bcf104"></a> `00bcf104` | `28 03 05 91` | add x8,x25,#0x140 | `FALL_THROUGH`
<a id="insn-00bcf108"></a> `00bcf108` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf10c"></a> `00bcf10c` | `25 00 00 14` | b 0x00bcf1a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf110"></a> `00bcf110` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcf114"></a> `00bcf114` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf118"></a> `00bcf118` | `6e 2f 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf11c"></a> `00bcf11c` | `b5 04 80 52` | mov w21,#0x25 | `FALL_THROUGH`
<a id="insn-00bcf120"></a> `00bcf120` | `b7 00 00 b4` | cbz x23,0x00bcf134 | `CONDITIONAL_JUMP`
<a id="insn-00bcf124"></a> `00bcf124` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcf128"></a> `00bcf128` | `e2 23 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf12c"></a> `00bcf12c` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bcf130"></a> `00bcf130` | `b5 06 95 1a` | cinc w21,w21,ne | `FALL_THROUGH`
<a id="insn-00bcf134"></a> `00bcf134` | `e3 b6 ff b0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcf138"></a> `00bcf138` | `63 84 08 91` | add x3,x3,#0x221 | `FALL_THROUGH`
<a id="insn-00bcf13c"></a> `00bcf13c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcf140"></a> `00bcf140` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcf144"></a> `00bcf144` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf148"></a> `00bcf148` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bcf14c"></a> `00bcf14c` | `d1 3a 02 94` | bl 0x00c5dc90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf150"></a> `00bcf150` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcf154"></a> `00bcf154` | `83 2e 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf158"></a> `00bcf158` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf15c"></a> `00bcf15c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf160"></a> `00bcf160` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf164"></a> `00bcf164` | `27 3b 02 94` | bl 0x00c5de00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf168"></a> `00bcf168` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf16c"></a> `00bcf16c` | `7d 2e 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf170"></a> `00bcf170` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf174"></a> `00bcf174` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcf178"></a> `00bcf178` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf17c"></a> `00bcf17c` | `61 03 00 54` | b.ne 0x00bcf1e8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf180"></a> `00bcf180` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcf184"></a> `00bcf184` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcf188"></a> `00bcf188` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcf18c"></a> `00bcf18c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcf190"></a> `00bcf190` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcf194"></a> `00bcf194` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcf198"></a> `00bcf198` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf19c"></a> `00bcf19c` | `24 ab 40 f9` | ldr x4,[x25, #0x150] | `FALL_THROUGH`
<a id="insn-00bcf1a0"></a> `00bcf1a0` | `62 06 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcf1a4"></a> `00bcf1a4` | `42 68 45 f9` | ldr x2,[x2, #0xad0] | `FALL_THROUGH`
<a id="insn-00bcf1a8"></a> `00bcf1a8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcf1ac"></a> `00bcf1ac` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcf1b0"></a> `00bcf1b0` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcf1b4"></a> `00bcf1b4` | `97 2f 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf1b8"></a> `00bcf1b8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcf1bc"></a> `00bcf1bc` | `69 2e 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf1c0"></a> `00bcf1c0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcf1c4"></a> `00bcf1c4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcf1c8"></a> `00bcf1c8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf1cc"></a> `00bcf1cc` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcf1d0"></a> `00bcf1d0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf1d4"></a> `00bcf1d4` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf1d8"></a> `00bcf1d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf1dc"></a> `00bcf1dc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf1e0"></a> `00bcf1e0` | `08 3b 02 94` | bl 0x00c5de00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf1e4"></a> `00bcf1e4` | `e1 ff ff 17` | b 0x00bcf168 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf1e8"></a> `00bcf1e8` | `72 23 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcefb4`](#insn-00bcefb4) 範囲 `[['00bcefb4', '00bcf007']]`
  - `CONDITIONAL_JUMP` [`00bcf004`](#insn-00bcf004) → [`00bcf110`](#insn-00bcf110)
  - `FALL_THROUGH` [`00bcf004`](#insn-00bcf004) → [`00bcf008`](#insn-00bcf008)
- ブロック [`00bcf008`](#insn-00bcf008) 範囲 `[['00bcf008', '00bcf013']]`
  - `CONDITIONAL_JUMP` [`00bcf010`](#insn-00bcf010) → [`00bcf110`](#insn-00bcf110)
  - `FALL_THROUGH` [`00bcf010`](#insn-00bcf010) → [`00bcf014`](#insn-00bcf014)
- ブロック [`00bcf014`](#insn-00bcf014) 範囲 `[['00bcf014', '00bcf017']]`
  - `CONDITIONAL_JUMP` [`00bcf014`](#insn-00bcf014) → [`00bcf110`](#insn-00bcf110)
  - `FALL_THROUGH` [`00bcf014`](#insn-00bcf014) → [`00bcf018`](#insn-00bcf018)
- ブロック [`00bcf018`](#insn-00bcf018) 範囲 `[['00bcf018', '00bcf023']]`
  - `CONDITIONAL_JUMP` [`00bcf020`](#insn-00bcf020) → [`00bcf110`](#insn-00bcf110)
  - `FALL_THROUGH` [`00bcf020`](#insn-00bcf020) → [`00bcf024`](#insn-00bcf024)
- ブロック [`00bcf024`](#insn-00bcf024) 範囲 `[['00bcf024', '00bcf0bf']]`
  - `CONDITIONAL_JUMP` [`00bcf0bc`](#insn-00bcf0bc) → [`00bcf1d4`](#insn-00bcf1d4)
  - `FALL_THROUGH` [`00bcf0bc`](#insn-00bcf0bc) → [`00bcf0c0`](#insn-00bcf0c0)
- ブロック [`00bcf0c0`](#insn-00bcf0c0) 範囲 `[['00bcf0c0', '00bcf103']]`
  - `CONDITIONAL_JUMP` [`00bcf100`](#insn-00bcf100) → [`00bcf19c`](#insn-00bcf19c)
  - `FALL_THROUGH` [`00bcf100`](#insn-00bcf100) → [`00bcf104`](#insn-00bcf104)
- ブロック [`00bcf104`](#insn-00bcf104) 範囲 `[['00bcf104', '00bcf10f']]`
  - `UNCONDITIONAL_JUMP` [`00bcf10c`](#insn-00bcf10c) → [`00bcf1a0`](#insn-00bcf1a0)
- ブロック [`00bcf110`](#insn-00bcf110) 範囲 `[['00bcf110', '00bcf123']]`
  - `CONDITIONAL_JUMP` [`00bcf120`](#insn-00bcf120) → [`00bcf134`](#insn-00bcf134)
  - `FALL_THROUGH` [`00bcf120`](#insn-00bcf120) → [`00bcf124`](#insn-00bcf124)
- ブロック [`00bcf124`](#insn-00bcf124) 範囲 `[['00bcf124', '00bcf133']]`
  - `FALL_THROUGH` [`00bcf130`](#insn-00bcf130) → [`00bcf134`](#insn-00bcf134)
- ブロック [`00bcf134`](#insn-00bcf134) 範囲 `[['00bcf134', '00bcf167']]`
  - `FALL_THROUGH` [`00bcf164`](#insn-00bcf164) → [`00bcf168`](#insn-00bcf168)
- ブロック [`00bcf168`](#insn-00bcf168) 範囲 `[['00bcf168', '00bcf17f']]`
  - `CONDITIONAL_JUMP` [`00bcf17c`](#insn-00bcf17c) → [`00bcf1e8`](#insn-00bcf1e8)
  - `FALL_THROUGH` [`00bcf17c`](#insn-00bcf17c) → [`00bcf180`](#insn-00bcf180)
- ブロック [`00bcf180`](#insn-00bcf180) 範囲 `[['00bcf180', '00bcf19b']]`
- ブロック [`00bcf19c`](#insn-00bcf19c) 範囲 `[['00bcf19c', '00bcf19f']]`
  - `FALL_THROUGH` [`00bcf19c`](#insn-00bcf19c) → [`00bcf1a0`](#insn-00bcf1a0)
- ブロック [`00bcf1a0`](#insn-00bcf1a0) 範囲 `[['00bcf1a0', '00bcf1d3']]`
  - `FALL_THROUGH` [`00bcf1d0`](#insn-00bcf1d0) → [`00bcf1d4`](#insn-00bcf1d4)
- ブロック [`00bcf1d4`](#insn-00bcf1d4) 範囲 `[['00bcf1d4', '00bcf1e7']]`
  - `UNCONDITIONAL_JUMP` [`00bcf1e4`](#insn-00bcf1e4) → [`00bcf168`](#insn-00bcf168)
- ブロック [`00bcf1e8`](#insn-00bcf1e8) 範囲 `[['00bcf1e8', '00bcf1eb']]`

## 命令位置別の参照

- [`00bcefb8`](#insn-00bcefb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefbc`](#insn-00bcefbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefc0`](#insn-00bcefc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefc4`](#insn-00bcefc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefc8`](#insn-00bcefc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefe8`](#insn-00bcefe8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf000`](#insn-00bcf000) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf004`](#insn-00bcf004) → [`00bcf110`](#insn-00bcf110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf00c`](#insn-00bcf00c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf010`](#insn-00bcf010) → [`00bcf110`](#insn-00bcf110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf014`](#insn-00bcf014) → [`00bcf110`](#insn-00bcf110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf01c`](#insn-00bcf01c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf020`](#insn-00bcf020) → [`00bcf110`](#insn-00bcf110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf02c`](#insn-00bcf02c) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcf064`](#insn-00bcf064) → `011268b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcf07c`](#insn-00bcf07c) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0b8`](#insn-00bcf0b8) → [`00c5dda0`](../00c5d/00c5dda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dda0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0bc`](#insn-00bcf0bc) → [`00bcf1d4`](#insn-00bcf1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0c8`](#insn-00bcf0c8) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0d4`](#insn-00bcf0d4) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0e0`](#insn-00bcf0e0) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0ec`](#insn-00bcf0ec) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0f4`](#insn-00bcf0f4) → `00c9baf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcf0f8`](#insn-00bcf0f8) → [`00bd48c8`](../00bd4/00bd48c8.md) · `DATA` · `ANALYSIS` · 関数 `00bd48c8` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcf100`](#insn-00bcf100) → [`00bcf19c`](#insn-00bcf19c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf10c`](#insn-00bcf10c) → [`00bcf1a0`](#insn-00bcf1a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf118`](#insn-00bcf118) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf120`](#insn-00bcf120) → [`00bcf134`](#insn-00bcf134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf128`](#insn-00bcf128) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf138`](#insn-00bcf138) → `002ac221`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf14c`](#insn-00bcf14c) → [`00c5dc90`](../00c5d/00c5dc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc90` · 推定シンボル `None` · 推定型 `None`
- [`00bcf154`](#insn-00bcf154) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf164`](#insn-00bcf164) → [`00c5de00`](../00c5d/00c5de00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de00` · 推定シンボル `None` · 推定型 `None`
- [`00bcf16c`](#insn-00bcf16c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf174`](#insn-00bcf174) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf17c`](#insn-00bcf17c) → [`00bcf1e8`](#insn-00bcf1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf180`](#insn-00bcf180) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf184`](#insn-00bcf184) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf188`](#insn-00bcf188) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf18c`](#insn-00bcf18c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf190`](#insn-00bcf190) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1a4`](#insn-00bcf1a4) → `00c9bad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcf1a4`](#insn-00bcf1a4) → [`00bcfde0`](../00bcf/00bcfde0.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfde0` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcf1b4`](#insn-00bcf1b4) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1bc`](#insn-00bcf1bc) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1e0`](#insn-00bcf1e0) → [`00c5de00`](../00c5d/00c5de00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de00` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1e4`](#insn-00bcf1e4) → [`00bcf168`](#insn-00bcf168) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf1e8`](#insn-00bcf1e8) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcefb8`](#insn-00bcefb8)

~~~json
{
  "source": "00bcefb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefbc`](#insn-00bcefbc)

~~~json
{
  "source": "00bcefbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefc0`](#insn-00bcefc0)

~~~json
{
  "source": "00bcefc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefc4`](#insn-00bcefc4)

~~~json
{
  "source": "00bcefc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefc8`](#insn-00bcefc8)

~~~json
{
  "source": "00bcefc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefe8`](#insn-00bcefe8)

~~~json
{
  "source": "00bcefe8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf000`](#insn-00bcf000)

~~~json
{
  "source": "00bcf000",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf004`](#insn-00bcf004)

~~~json
{
  "source": "00bcf004",
  "target": "00bcf110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf00c`](#insn-00bcf00c)

~~~json
{
  "source": "00bcf00c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf010`](#insn-00bcf010)

~~~json
{
  "source": "00bcf010",
  "target": "00bcf110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf014`](#insn-00bcf014)

~~~json
{
  "source": "00bcf014",
  "target": "00bcf110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf01c`](#insn-00bcf01c)

~~~json
{
  "source": "00bcf01c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf020`](#insn-00bcf020)

~~~json
{
  "source": "00bcf020",
  "target": "00bcf110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf02c`](#insn-00bcf02c)

~~~json
{
  "source": "00bcf02c",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf064`](#insn-00bcf064)

~~~json
{
  "source": "00bcf064",
  "target": "011268b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcf07c`](#insn-00bcf07c)

~~~json
{
  "source": "00bcf07c",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0b8`](#insn-00bcf0b8)

~~~json
{
  "source": "00bcf0b8",
  "target": "00c5dda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0bc`](#insn-00bcf0bc)

~~~json
{
  "source": "00bcf0bc",
  "target": "00bcf1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0c8`](#insn-00bcf0c8)

~~~json
{
  "source": "00bcf0c8",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0d4`](#insn-00bcf0d4)

~~~json
{
  "source": "00bcf0d4",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0e0`](#insn-00bcf0e0)

~~~json
{
  "source": "00bcf0e0",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0ec`](#insn-00bcf0ec)

~~~json
{
  "source": "00bcf0ec",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf0f4`](#insn-00bcf0f4)

~~~json
{
  "source": "00bcf0f4",
  "target": "00c9baf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9baf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcf0f8`](#insn-00bcf0f8)

~~~json
{
  "source": "00bcf0f8",
  "target": "00bd48c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf100`](#insn-00bcf100)

~~~json
{
  "source": "00bcf100",
  "target": "00bcf19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf10c`](#insn-00bcf10c)

~~~json
{
  "source": "00bcf10c",
  "target": "00bcf1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf118`](#insn-00bcf118)

~~~json
{
  "source": "00bcf118",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf120`](#insn-00bcf120)

~~~json
{
  "source": "00bcf120",
  "target": "00bcf134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf128`](#insn-00bcf128)

~~~json
{
  "source": "00bcf128",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf138`](#insn-00bcf138)

~~~json
{
  "source": "00bcf138",
  "target": "002ac221",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac221",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "456d70747920656d61696c206f722070617373776f726420617265206e6f7420",
  "capture_start": "002ac221",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcf14c`](#insn-00bcf14c)

~~~json
{
  "source": "00bcf14c",
  "target": "00c5dc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf154`](#insn-00bcf154)

~~~json
{
  "source": "00bcf154",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf164`](#insn-00bcf164)

~~~json
{
  "source": "00bcf164",
  "target": "00c5de00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf16c`](#insn-00bcf16c)

~~~json
{
  "source": "00bcf16c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf174`](#insn-00bcf174)

~~~json
{
  "source": "00bcf174",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf17c`](#insn-00bcf17c)

~~~json
{
  "source": "00bcf17c",
  "target": "00bcf1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf180`](#insn-00bcf180)

~~~json
{
  "source": "00bcf180",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf184`](#insn-00bcf184)

~~~json
{
  "source": "00bcf184",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf188`](#insn-00bcf188)

~~~json
{
  "source": "00bcf188",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf18c`](#insn-00bcf18c)

~~~json
{
  "source": "00bcf18c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf190`](#insn-00bcf190)

~~~json
{
  "source": "00bcf190",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf1a4`](#insn-00bcf1a4)

~~~json
{
  "source": "00bcf1a4",
  "target": "00c9bad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bad0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcf1a4`](#insn-00bcf1a4)

~~~json
{
  "source": "00bcf1a4",
  "target": "00bcfde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf1b4`](#insn-00bcf1b4)

~~~json
{
  "source": "00bcf1b4",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf1bc`](#insn-00bcf1bc)

~~~json
{
  "source": "00bcf1bc",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf1e0`](#insn-00bcf1e0)

~~~json
{
  "source": "00bcf1e0",
  "target": "00c5de00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf1e4`](#insn-00bcf1e4)

~~~json
{
  "source": "00bcf1e4",
  "target": "00bcf168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf1e8`](#insn-00bcf1e8)

~~~json
{
  "source": "00bcf1e8",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
