# 00baeec4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baee28`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baee28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-f88486b0b08c860fba35a0589e1b6c8a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bafeb8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0014.md#compare-1aad86994332fc4a652873c33ff0dd2b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeec4",
  "name": "_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_",
  "size": 1304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92b3ffa6532cff7e56f783344de888cf77e679b2beee79cc02ec4c122e7d88e4",
  "source_text_sha256": "92b3ffa6532cff7e56f783344de888cf77e679b2beee79cc02ec4c122e7d88e4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeec4",
        "00baf3db"
      ]
    ],
    "bytes_sha256": "a36ed3904a74b7211b9ea8d3c3a18d9f21d26678d44da2ef61b80704547689e2",
    "instruction_count": 326,
    "instruction_bytes": 1304,
    "body_bytes": 1304,
    "indirect": 19,
    "unresolved": 18
  }
}
~~~

## 呼び出し元

- [00c5cec0](../00c5c/00c5cec0.md)

## 呼び出し先

- [00baf560](../00baf/00baf560.md)
- [00c5ccc0](../00c5c/00c5ccc0.md)
- [00c5ce80](../00c5c/00c5ce80.md)
- [00c5cec0](../00c5c/00c5cec0.md)
- [00c5d180](../00c5d/00c5d180.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9035 bytes

~~~c

void _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_
               (undefined1 (*param_1) [16],undefined1 (*param_2) [16],undefined8 *param_3)

{
  undefined1 (*pauVar1) [16];
  int iVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  undefined8 uVar6;
  undefined1 (*pauVar7) [16];
  undefined1 (*pauVar8) [16];
  undefined1 (*pauVar9) [16];
  undefined1 (*pauVar10) [16];
  undefined1 (*pauVar11) [16];
  undefined1 auVar12 [16];
  
LAB_00baeef0:
  pauVar9 = (undefined1 (*) [16])(param_2[-1] + 8);
  pauVar10 = param_1;
LAB_00baef04:
  param_1 = pauVar10;
  lVar5 = (long)param_2 - (long)param_1;
  uVar4 = lVar5 >> 3;
  switch(uVar4) {
  case 0:
  case 1:
    goto switchD_00baf268_caseD_0;
  case 2:
    uVar4 = (*(code *)*param_3)(*(undefined8 *)(param_2[-1] + 8),*(undefined8 *)*param_1);
    if ((uVar4 & 1) == 0) {
      return;
    }
    uVar6 = *(undefined8 *)*param_1;
    *(undefined8 *)*param_1 = *(undefined8 *)(param_2[-1] + 8);
    *(undefined8 *)(param_2[-1] + 8) = uVar6;
    return;
  case 3:
    uVar4 = (*(code *)*param_3)(*(undefined8 *)(*param_1 + 8),*(undefined8 *)*param_1);
    uVar3 = (*(code *)*param_3)(*(undefined8 *)(param_2[-1] + 8),*(undefined8 *)(*param_1 + 8));
    if ((uVar4 & 1) == 0) {
      if ((uVar3 & 1) == 0) {
        return;
      }
      uVar6 = *(undefined8 *)(*param_1 + 8);
      *(undefined8 *)(*param_1 + 8) = *(undefined8 *)(param_2[-1] + 8);
      *(undefined8 *)(param_2[-1] + 8) = uVar6;
      uVar4 = (*(code *)*param_3)(*(undefined8 *)(*param_1 + 8),*(undefined8 *)*param_1);
      if ((uVar4 & 1) == 0) {
        return;
      }
      auVar12 = NEON_ext(*param_1,*param_1,8,1);
      *(long *)(*param_1 + 8) = auVar12._8_8_;
      *(long *)*param_1 = auVar12._0_8_;
      return;
    }
    uVar6 = *(undefined8 *)*param_1;
    if ((uVar3 & 1) != 0) {
      *(undefined8 *)*param_1 = *(undefined8 *)(param_2[-1] + 8);
      *(undefined8 *)(param_2[-1] + 8) = uVar6;
      return;
    }
    *(undefined8 *)*param_1 = *(undefined8 *)(*param_1 + 8);
    *(undefined8 *)(*param_1 + 8) = uVar6;
    uVar4 = (*(code *)*param_3)(*(undefined8 *)(param_2[-1] + 8));
    if ((uVar4 & 1) == 0) {
      return;
    }
    uVar6 = *(undefined8 *)(*param_1 + 8);
    *(undefined8 *)(*param_1 + 8) = *(undefined8 *)(param_2[-1] + 8);
    *(undefined8 *)(param_2[-1] + 8) = uVar6;
    return;
  case 4:
    _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEjT0_SA_SA_SA_T_
              (param_1,*param_1 + 8,param_1 + 1,pauVar9,param_3);
    return;
  case 5:
    FUN_00baf560(param_1,*param_1 + 8,param_1 + 1,param_1[1] + 8,pauVar9,param_3);
    return;
  default:
    if (lVar5 < 0xf8) {
      _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_
                (param_1,param_2,param_3);
      return;
    }
    uVar3 = uVar4;
    if ((long)uVar4 < 0) {
      uVar3 = uVar4 + 1;
    }
    pauVar10 = (undefined1 (*) [16])(*param_1 + (uVar3 & 0x3ffffffffffffffe) * 4);
    if (lVar5 < 0x1f39) {
      uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar10,*(undefined8 *)*param_1);
      uVar3 = (*(code *)*param_3)(*(undefined8 *)*pauVar9,*(undefined8 *)*pauVar10);
      if ((uVar4 & 1) == 0) {
        if ((uVar3 & 1) == 0) {
          iVar2 = 0;
        }
        else {
          uVar6 = *(undefined8 *)*pauVar10;
          *(undefined8 *)*pauVar10 = *(undefined8 *)*pauVar9;
          *(undefined8 *)*pauVar9 = uVar6;
          uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar10,*(undefined8 *)*param_1);
          if ((uVar4 & 1) == 0) goto LAB_00baf1c0;
          uVar6 = *(undefined8 *)*param_1;
          *(undefined8 *)*param_1 = *(undefined8 *)*pauVar10;
          *(undefined8 *)*pauVar10 = uVar6;
LAB_00baf1b0:
          iVar2 = 2;
        }
      }
      else {
        uVar6 = *(undefined8 *)*param_1;
        if ((uVar3 & 1) == 0) {
          *(undefined8 *)*param_1 = *(undefined8 *)*pauVar10;
          *(undefined8 *)*pauVar10 = uVar6;
          uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar9);
          if ((uVar4 & 1) != 0) {
            uVar6 = *(undefined8 *)*pauVar10;
            *(undefined8 *)*pauVar10 = *(undefined8 *)*pauVar9;
            *(undefined8 *)*pauVar9 = uVar6;
            goto LAB_00baf1b0;
          }
LAB_00baf1c0:
          iVar2 = 1;
        }
        else {
          iVar2 = 1;
          *(undefined8 *)*param_1 = *(undefined8 *)*pauVar9;
          *(undefined8 *)*pauVar9 = uVar6;
        }
      }
    }
    else {
      uVar3 = uVar4 + 3;
      if (-1 < (long)uVar4) {
        uVar3 = uVar4;
      }
      lVar5 = (uVar3 & 0x7ffffffffffffffc) * 2;
      iVar2 = FUN_00baf560(param_1,*param_1 + lVar5,pauVar10,*pauVar10 + lVar5,pauVar9,param_3);
    }
    uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)*pauVar10);
    pauVar11 = pauVar9;
    pauVar8 = param_2 + -1;
    if ((uVar4 & 1) == 0) break;
    goto LAB_00baf008;
  }
  while (pauVar11 = pauVar8, param_1 != pauVar11) {
    uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar11,*(undefined8 *)*pauVar10);
    pauVar8 = (undefined1 (*) [16])(pauVar11[-1] + 8);
    if ((uVar4 & 1) != 0) goto code_r0x00baeff4;
  }
  pauVar11 = (undefined1 (*) [16])(*param_1 + 8);
  uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)*pauVar9);
  if ((uVar4 & 1) == 0) {
    if (pauVar11 == pauVar9) {
      return;
    }
    pauVar11 = param_1 + 1;
    while (uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)(pauVar11[-1] + 8)),
          (uVar4 & 1) == 0) {
      pauVar11 = (undefined1 (*) [16])(*pauVar11 + 8);
      if (param_2 == pauVar11) {
        return;
      }
    }
    uVar6 = *(undefined8 *)(pauVar11[-1] + 8);
    *(undefined8 *)(pauVar11[-1] + 8) = *(undefined8 *)*pauVar9;
    *(undefined8 *)*pauVar9 = uVar6;
  }
  pauVar8 = pauVar9;
  if (pauVar11 == pauVar9) {
    return;
  }
  while( true ) {
    pauVar10 = (undefined1 (*) [16])(pauVar11[-1] + 8);
    do {
      pauVar11 = pauVar10;
      pauVar10 = (undefined1 (*) [16])(*pauVar11 + 8);
      uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)*pauVar10);
    } while ((uVar4 & 1) == 0);
    pauVar11 = pauVar11 + 1;
    do {
      pauVar8 = (undefined1 (*) [16])(pauVar8[-1] + 8);
      uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)*pauVar8);
    } while ((uVar4 & 1) != 0);
    if (pauVar8 <= pauVar10) break;
    uVar6 = *(undefined8 *)*pauVar10;
    *(undefined8 *)*pauVar10 = *(undefined8 *)*pauVar8;
    *(undefined8 *)*pauVar8 = uVar6;
  }
  goto LAB_00baef04;
code_r0x00baeff4:
  uVar6 = *(undefined8 *)*param_1;
  iVar2 = iVar2 + 1;
  *(undefined8 *)*param_1 = *(undefined8 *)*pauVar11;
  *(undefined8 *)*pauVar11 = uVar6;
LAB_00baf008:
  pauVar8 = (undefined1 (*) [16])(*param_1 + 8);
  pauVar7 = pauVar8;
  pauVar1 = pauVar10;
  if (pauVar8 < pauVar11) {
    while( true ) {
      pauVar10 = pauVar1;
      pauVar8 = (undefined1 (*) [16])(pauVar7[-1] + 8);
      do {
        pauVar7 = pauVar8;
        pauVar8 = (undefined1 (*) [16])(*pauVar7 + 8);
        uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar8,*(undefined8 *)*pauVar10);
      } while ((uVar4 & 1) != 0);
      pauVar7 = pauVar7 + 1;
      do {
        pauVar11 = (undefined1 (*) [16])(pauVar11[-1] + 8);
        uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar11,*(undefined8 *)*pauVar10);
      } while ((uVar4 & 1) == 0);
      if (pauVar11 < pauVar8) break;
      uVar6 = *(undefined8 *)*pauVar8;
      iVar2 = iVar2 + 1;
      *(undefined8 *)*pauVar8 = *(undefined8 *)*pauVar11;
      *(undefined8 *)*pauVar11 = uVar6;
      pauVar1 = pauVar11;
      if (pauVar10 != pauVar8) {
        pauVar1 = pauVar10;
      }
    }
  }
  if ((pauVar8 != pauVar10) &&
     (uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar10,*(undefined8 *)*pauVar8),
     (uVar4 & 1) != 0)) {
    uVar6 = *(undefined8 *)*pauVar8;
    iVar2 = iVar2 + 1;
    *(undefined8 *)*pauVar8 = *(undefined8 *)*pauVar10;
    *(undefined8 *)*pauVar10 = uVar6;
  }
  if (iVar2 == 0) {
    uVar4 = _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_
                      (param_1,pauVar8,param_3);
    uVar3 = _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_
                      ((undefined1 (*) [16])(*pauVar8 + 8),param_2,param_3);
    if ((uVar3 & 1) != 0) goto LAB_00baf248;
    pauVar10 = (undefined1 (*) [16])(*pauVar8 + 8);
    if ((uVar4 & 1) != 0) goto LAB_00baef04;
  }
  if ((long)param_2 - (long)pauVar8 <= (long)pauVar8 - (long)param_1) {
    _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_
              ((long)*pauVar8 + 8,param_2,param_3);
    param_2 = pauVar8;
    goto LAB_00baeef0;
  }
  _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_(param_1,pauVar8,param_3);
  pauVar10 = (undefined1 (*) [16])(*pauVar8 + 8);
  goto LAB_00baef04;
LAB_00baf248:
  param_2 = pauVar8;
  if ((uVar4 & 1) != 0) {
switchD_00baf268_caseD_0:
    return;
  }
  goto LAB_00baeef0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baeec4"></a> `00baeec4` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00baeec8"></a> `00baeec8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeecc"></a> `00baeecc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baeed0"></a> `00baeed0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baeed4"></a> `00baeed4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baeed8"></a> `00baeed8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baeedc"></a> `00baeedc` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baeee0"></a> `00baeee0` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00baeee4"></a> `00baeee4` | `fa 03 01 aa` | mov x26,x1 | `FALL_THROUGH`
<a id="insn-00baeee8"></a> `00baeee8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baeeec"></a> `00baeeec` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00baeef0"></a> `00baeef0` | `56 23 00 d1` | sub x22,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00baeef4"></a> `00baeef4` | `5b 43 00 d1` | sub x27,x26,#0x10 | `FALL_THROUGH`
<a id="insn-00baeef8"></a> `00baeef8` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00baeefc"></a> `00baeefc` | `02 00 00 14` | b 0x00baef04 | `UNCONDITIONAL_JUMP`
<a id="insn-00baef00"></a> `00baef00` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00baef04"></a> `00baef04` | `49 03 17 cb` | sub x9,x26,x23 | `FALL_THROUGH`
<a id="insn-00baef08"></a> `00baef08` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00baef0c"></a> `00baef0c` | `f3 03 17 aa` | mov x19,x23 | `FALL_THROUGH`
<a id="insn-00baef10"></a> `00baef10` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00baef14"></a> `00baef14` | `09 1a 00 54` | b.ls 0x00baf254 | `CONDITIONAL_JUMP`
<a id="insn-00baef18"></a> `00baef18` | `3f dd 03 f1` | cmp x9,#0xf7 | `FALL_THROUGH`
<a id="insn-00baef1c"></a> `00baef1c` | `6d 1b 00 54` | b.le 0x00baf288 | `CONDITIONAL_JUMP`
<a id="insn-00baef20"></a> `00baef20` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00baef24"></a> `00baef24` | `0a a5 88 9a` | cinc x10,x8,lt | `FALL_THROUGH`
<a id="insn-00baef28"></a> `00baef28` | `4a f5 7e d3` | lsl x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00baef2c"></a> `00baef2c` | `4a f1 7d 92` | and x10,x10,#-0x8 | `FALL_THROUGH`
<a id="insn-00baef30"></a> `00baef30` | `3f 01 19 eb` | cmp x9,x25 | `FALL_THROUGH`
<a id="insn-00baef34"></a> `00baef34` | `77 02 0a 8b` | add x23,x19,x10 | `FALL_THROUGH`
<a id="insn-00baef38"></a> `00baef38` | `ab 02 00 54` | b.lt 0x00baef8c | `CONDITIONAL_JUMP`
<a id="insn-00baef3c"></a> `00baef3c` | `09 0d 00 91` | add x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baef40"></a> `00baef40` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00baef44"></a> `00baef44` | `28 b1 88 9a` | csel x8,x9,x8,lt | `FALL_THROUGH`
<a id="insn-00baef48"></a> `00baef48` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baef4c"></a> `00baef4c` | `08 f1 7d 92` | and x8,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00baef50"></a> `00baef50` | `61 02 08 8b` | add x1,x19,x8 | `FALL_THROUGH`
<a id="insn-00baef54"></a> `00baef54` | `e3 02 08 8b` | add x3,x23,x8 | `FALL_THROUGH`
<a id="insn-00baef58"></a> `00baef58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baef5c"></a> `00baef5c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00baef60"></a> `00baef60` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00baef64"></a> `00baef64` | `e5 03 15 aa` | mov x5,x21 | `FALL_THROUGH`
<a id="insn-00baef68"></a> `00baef68` | `7e 01 00 94` | bl 0x00baf560 | `UNCONDITIONAL_CALL`
<a id="insn-00baef6c"></a> `00baef6c` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baef70"></a> `00baef70` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baef74"></a> `00baef74` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baef78"></a> `00baef78` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baef7c"></a> `00baef7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baef80"></a> `00baef80` | `a0 02 00 36` | tbz w0,#0x0,0x00baefd4 | `CONDITIONAL_JUMP`
<a id="insn-00baef84"></a> `00baef84` | `fc 03 16 aa` | mov x28,x22 | `FALL_THROUGH`
<a id="insn-00baef88"></a> `00baef88` | `20 00 00 14` | b 0x00baf008 | `UNCONDITIONAL_JUMP`
<a id="insn-00baef8c"></a> `00baef8c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baef90"></a> `00baef90` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baef94"></a> `00baef94` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baef98"></a> `00baef98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baef9c"></a> `00baef9c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baefa0"></a> `00baefa0` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00baefa4"></a> `00baefa4` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baefa8"></a> `00baefa8` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baefac"></a> `00baefac` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baefb0"></a> `00baefb0` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baefb4"></a> `00baefb4` | `b8 0c 00 36` | tbz w24,#0x0,0x00baf148 | `CONDITIONAL_JUMP`
<a id="insn-00baefb8"></a> `00baefb8` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baefbc"></a> `00baefbc` | `40 0e 00 36` | tbz w0,#0x0,0x00baf184 | `CONDITIONAL_JUMP`
<a id="insn-00baefc0"></a> `00baefc0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baefc4"></a> `00baefc4` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baefc8"></a> `00baefc8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baefcc"></a> `00baefcc` | `c1 02 00 f9` | str x1,[x22] | `FALL_THROUGH`
<a id="insn-00baefd0"></a> `00baefd0` | `e8 ff ff 17` | b 0x00baef70 | `UNCONDITIONAL_JUMP`
<a id="insn-00baefd4"></a> `00baefd4` | `fc 03 1b aa` | mov x28,x27 | `FALL_THROUGH`
<a id="insn-00baefd8"></a> `00baefd8` | `7f 02 1c eb` | cmp x19,x28 | `FALL_THROUGH`
<a id="insn-00baefdc"></a> `00baefdc` | `20 09 00 54` | b.eq 0x00baf100 | `CONDITIONAL_JUMP`
<a id="insn-00baefe0"></a> `00baefe0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baefe4"></a> `00baefe4` | `80 87 5f f8` | ldr x0,[x28], #-0x8 | `FALL_THROUGH`
<a id="insn-00baefe8"></a> `00baefe8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baefec"></a> `00baefec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baeff0"></a> `00baeff0` | `40 ff 07 36` | tbz w0,#0x0,0x00baefd8 | `CONDITIONAL_JUMP`
<a id="insn-00baeff4"></a> `00baeff4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baeff8"></a> `00baeff8` | `89 8f 40 f8` | ldr x9,[x28, #0x8]! | `FALL_THROUGH`
<a id="insn-00baeffc"></a> `00baeffc` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf000"></a> `00baf000` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf004"></a> `00baf004` | `88 03 00 f9` | str x8,[x28] | `FALL_THROUGH`
<a id="insn-00baf008"></a> `00baf008` | `74 22 00 91` | add x20,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00baf00c"></a> `00baf00c` | `9f 02 1c eb` | cmp x20,x28 | `FALL_THROUGH`
<a id="insn-00baf010"></a> `00baf010` | `22 03 00 54` | b.cs 0x00baf074 | `CONDITIONAL_JUMP`
<a id="insn-00baf014"></a> `00baf014` | `99 22 00 d1` | sub x25,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00baf018"></a> `00baf018` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf01c"></a> `00baf01c` | `20 8f 40 f8` | ldr x0,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00baf020"></a> `00baf020` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baf024"></a> `00baf024` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf028"></a> `00baf028` | `80 ff 07 37` | tbnz w0,#0x0,0x00baf018 | `CONDITIONAL_JUMP`
<a id="insn-00baf02c"></a> `00baf02c` | `34 23 00 91` | add x20,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00baf030"></a> `00baf030` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf034"></a> `00baf034` | `80 8f 5f f8` | ldr x0,[x28, #-0x8]! | `FALL_THROUGH`
<a id="insn-00baf038"></a> `00baf038` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baf03c"></a> `00baf03c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf040"></a> `00baf040` | `80 ff 07 36` | tbz w0,#0x0,0x00baf030 | `CONDITIONAL_JUMP`
<a id="insn-00baf044"></a> `00baf044` | `3f 03 1c eb` | cmp x25,x28 | `FALL_THROUGH`
<a id="insn-00baf048"></a> `00baf048` | `28 01 00 54` | b.hi 0x00baf06c | `CONDITIONAL_JUMP`
<a id="insn-00baf04c"></a> `00baf04c` | `88 03 40 f9` | ldr x8,[x28] | `FALL_THROUGH`
<a id="insn-00baf050"></a> `00baf050` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-00baf054"></a> `00baf054` | `ff 02 19 eb` | cmp x23,x25 | `FALL_THROUGH`
<a id="insn-00baf058"></a> `00baf058` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf05c"></a> `00baf05c` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00baf060"></a> `00baf060` | `89 03 00 f9` | str x9,[x28] | `FALL_THROUGH`
<a id="insn-00baf064"></a> `00baf064` | `97 03 97 9a` | csel x23,x28,x23,eq | `FALL_THROUGH`
<a id="insn-00baf068"></a> `00baf068` | `eb ff ff 17` | b 0x00baf014 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf06c"></a> `00baf06c` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00baf070"></a> `00baf070` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00baf074"></a> `00baf074` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00baf078"></a> `00baf078` | `60 01 00 54` | b.eq 0x00baf0a4 | `CONDITIONAL_JUMP`
<a id="insn-00baf07c"></a> `00baf07c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf080"></a> `00baf080` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baf084"></a> `00baf084` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf088"></a> `00baf088` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf08c"></a> `00baf08c` | `c0 00 00 36` | tbz w0,#0x0,0x00baf0a4 | `CONDITIONAL_JUMP`
<a id="insn-00baf090"></a> `00baf090` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf094"></a> `00baf094` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00baf098"></a> `00baf098` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf09c"></a> `00baf09c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf0a0"></a> `00baf0a0` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf0a4"></a> `00baf0a4` | `b8 01 00 35` | cbnz w24,0x00baf0d8 | `CONDITIONAL_JUMP`
<a id="insn-00baf0a8"></a> `00baf0a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf0ac"></a> `00baf0ac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00baf0b0"></a> `00baf0b0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baf0b4"></a> `00baf0b4` | `73 b7 02 94` | bl 0x00c5ce80 | `UNCONDITIONAL_CALL`
<a id="insn-00baf0b8"></a> `00baf0b8` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00baf0bc"></a> `00baf0bc` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baf0c0"></a> `00baf0c0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00baf0c4"></a> `00baf0c4` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00baf0c8"></a> `00baf0c8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baf0cc"></a> `00baf0cc` | `6d b7 02 94` | bl 0x00c5ce80 | `UNCONDITIONAL_CALL`
<a id="insn-00baf0d0"></a> `00baf0d0` | `c0 0b 00 37` | tbnz w0,#0x0,0x00baf248 | `CONDITIONAL_JUMP`
<a id="insn-00baf0d4"></a> `00baf0d4` | `98 f1 07 37` | tbnz w24,#0x0,0x00baef04 | `CONDITIONAL_JUMP`
<a id="insn-00baf0d8"></a> `00baf0d8` | `88 02 13 cb` | sub x8,x20,x19 | `FALL_THROUGH`
<a id="insn-00baf0dc"></a> `00baf0dc` | `49 03 14 cb` | sub x9,x26,x20 | `FALL_THROUGH`
<a id="insn-00baf0e0"></a> `00baf0e0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baf0e4"></a> `00baf0e4` | `6a 0a 00 54` | b.ge 0x00baf230 | `CONDITIONAL_JUMP`
<a id="insn-00baf0e8"></a> `00baf0e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf0ec"></a> `00baf0ec` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00baf0f0"></a> `00baf0f0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baf0f4"></a> `00baf0f4` | `73 b7 02 94` | bl 0x00c5cec0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf0f8"></a> `00baf0f8` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00baf0fc"></a> `00baf0fc` | `82 ff ff 17` | b 0x00baef04 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf100"></a> `00baf100` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00baf104"></a> `00baf104` | `00 87 40 f8` | ldr x0,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00baf108"></a> `00baf108` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf10c"></a> `00baf10c` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00baf110"></a> `00baf110` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf114"></a> `00baf114` | `20 06 00 37` | tbnz w0,#0x0,0x00baf1d8 | `CONDITIONAL_JUMP`
<a id="insn-00baf118"></a> `00baf118` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baf11c"></a> `00baf11c` | `80 0a 00 54` | b.eq 0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf120"></a> `00baf120` | `78 42 00 91` | add x24,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00baf124"></a> `00baf124` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf128"></a> `00baf128` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf12c"></a> `00baf12c` | `01 83 5f f8` | ldur x1,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf130"></a> `00baf130` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf134"></a> `00baf134` | `a0 04 00 37` | tbnz w0,#0x0,0x00baf1c8 | `CONDITIONAL_JUMP`
<a id="insn-00baf138"></a> `00baf138` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00baf13c"></a> `00baf13c` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-00baf140"></a> `00baf140` | `21 ff ff 54` | b.ne 0x00baf124 | `CONDITIONAL_JUMP`
<a id="insn-00baf144"></a> `00baf144` | `4a 00 00 14` | b 0x00baf26c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf148"></a> `00baf148` | `80 03 00 36` | tbz w0,#0x0,0x00baf1b8 | `CONDITIONAL_JUMP`
<a id="insn-00baf14c"></a> `00baf14c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf150"></a> `00baf150` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf154"></a> `00baf154` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf158"></a> `00baf158` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf15c"></a> `00baf15c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf160"></a> `00baf160` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baf164"></a> `00baf164` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf168"></a> `00baf168` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf16c"></a> `00baf16c` | `a0 02 00 36` | tbz w0,#0x0,0x00baf1c0 | `CONDITIONAL_JUMP`
<a id="insn-00baf170"></a> `00baf170` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf174"></a> `00baf174` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf178"></a> `00baf178` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf17c"></a> `00baf17c` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf180"></a> `00baf180` | `0c 00 00 14` | b 0x00baf1b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf184"></a> `00baf184` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf188"></a> `00baf188` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf18c"></a> `00baf18c` | `e1 02 00 f9` | str x1,[x23] | `FALL_THROUGH`
<a id="insn-00baf190"></a> `00baf190` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf194"></a> `00baf194` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00baf198"></a> `00baf198` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf19c"></a> `00baf19c` | `20 01 00 36` | tbz w0,#0x0,0x00baf1c0 | `CONDITIONAL_JUMP`
<a id="insn-00baf1a0"></a> `00baf1a0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf1a4"></a> `00baf1a4` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf1a8"></a> `00baf1a8` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf1ac"></a> `00baf1ac` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf1b0"></a> `00baf1b0` | `58 00 80 52` | mov w24,#0x2 | `FALL_THROUGH`
<a id="insn-00baf1b4"></a> `00baf1b4` | `6f ff ff 17` | b 0x00baef70 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf1b8"></a> `00baf1b8` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00baf1bc"></a> `00baf1bc` | `6d ff ff 17` | b 0x00baef70 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf1c0"></a> `00baf1c0` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baf1c4"></a> `00baf1c4` | `6b ff ff 17` | b 0x00baef70 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf1c8"></a> `00baf1c8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baf1cc"></a> `00baf1cc` | `09 83 5f f8` | ldur x9,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf1d0"></a> `00baf1d0` | `08 83 1f f8` | stur x8,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf1d4"></a> `00baf1d4` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00baf1d8"></a> `00baf1d8` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baf1dc"></a> `00baf1dc` | `80 04 00 54` | b.eq 0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf1e0"></a> `00baf1e0` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00baf1e4"></a> `00baf1e4` | `17 23 00 d1` | sub x23,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00baf1e8"></a> `00baf1e8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf1ec"></a> `00baf1ec` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf1f0"></a> `00baf1f0` | `e1 8e 40 f8` | ldr x1,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00baf1f4"></a> `00baf1f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf1f8"></a> `00baf1f8` | `80 ff 07 36` | tbz w0,#0x0,0x00baf1e8 | `CONDITIONAL_JUMP`
<a id="insn-00baf1fc"></a> `00baf1fc` | `f8 22 00 91` | add x24,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00baf200"></a> `00baf200` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf204"></a> `00baf204` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf208"></a> `00baf208` | `21 8f 5f f8` | ldr x1,[x25, #-0x8]! | `FALL_THROUGH`
<a id="insn-00baf20c"></a> `00baf20c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf210"></a> `00baf210` | `80 ff 07 37` | tbnz w0,#0x0,0x00baf200 | `CONDITIONAL_JUMP`
<a id="insn-00baf214"></a> `00baf214` | `ff 02 19 eb` | cmp x23,x25 | `FALL_THROUGH`
<a id="insn-00baf218"></a> `00baf218` | `42 e7 ff 54` | b.cs 0x00baef00 | `CONDITIONAL_JUMP`
<a id="insn-00baf21c"></a> `00baf21c` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00baf220"></a> `00baf220` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00baf224"></a> `00baf224` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00baf228"></a> `00baf228` | `29 03 00 f9` | str x9,[x25] | `FALL_THROUGH`
<a id="insn-00baf22c"></a> `00baf22c` | `ee ff ff 17` | b 0x00baf1e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf230"></a> `00baf230` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00baf234"></a> `00baf234` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00baf238"></a> `00baf238` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baf23c"></a> `00baf23c` | `21 b7 02 94` | bl 0x00c5cec0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf240"></a> `00baf240` | `fa 03 14 aa` | mov x26,x20 | `FALL_THROUGH`
<a id="insn-00baf244"></a> `00baf244` | `2b ff ff 17` | b 0x00baeef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf248"></a> `00baf248` | `fa 03 14 aa` | mov x26,x20 | `FALL_THROUGH`
<a id="insn-00baf24c"></a> `00baf24c` | `38 e5 07 36` | tbz w24,#0x0,0x00baeef0 | `CONDITIONAL_JUMP`
<a id="insn-00baf250"></a> `00baf250` | `07 00 00 14` | b 0x00baf26c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf254"></a> `00baf254` | `e9 ba ff f0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00baf258"></a> `00baf258` | `29 61 09 91` | add x9,x9,#0x258 | `FALL_THROUGH`
<a id="insn-00baf25c"></a> `00baf25c` | `8a 00 00 10` | adr x10,0xbaf26c | `FALL_THROUGH`
<a id="insn-00baf260"></a> `00baf260` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baf264"></a> `00baf264` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00baf268"></a> `00baf268` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00baf26c"></a> `00baf26c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf270"></a> `00baf270` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf274"></a> `00baf274` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf278"></a> `00baf278` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf27c"></a> `00baf27c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf280"></a> `00baf280` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baf284"></a> `00baf284` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baf288"></a> `00baf288` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf28c"></a> `00baf28c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00baf290"></a> `00baf290` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baf294"></a> `00baf294` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf298"></a> `00baf298` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf29c"></a> `00baf29c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf2a0"></a> `00baf2a0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf2a4"></a> `00baf2a4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf2a8"></a> `00baf2a8` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baf2ac"></a> `00baf2ac` | `85 b6 02 14` | b 0x00c5ccc0 | `CALL_TERMINATOR`
<a id="insn-00baf2b0"></a> `00baf2b0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf2b4"></a> `00baf2b4` | `40 83 5f f8` | ldur x0,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf2b8"></a> `00baf2b8` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf2bc"></a> `00baf2bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf2c0"></a> `00baf2c0` | `60 fd 07 36` | tbz w0,#0x0,0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf2c4"></a> `00baf2c4` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf2c8"></a> `00baf2c8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf2cc"></a> `00baf2cc` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf2d0"></a> `00baf2d0` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf2d4"></a> `00baf2d4` | `e6 ff ff 17` | b 0x00baf26c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf2d8"></a> `00baf2d8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf2dc"></a> `00baf2dc` | `61 02 40 a9` | ldp x1,x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf2e0"></a> `00baf2e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf2e4"></a> `00baf2e4` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf2e8"></a> `00baf2e8` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00baf2ec"></a> `00baf2ec` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf2f0"></a> `00baf2f0` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00baf2f4"></a> `00baf2f4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baf2f8"></a> `00baf2f8` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baf2fc"></a> `00baf2fc` | `16 04 00 36` | tbz w22,#0x0,0x00baf37c | `CONDITIONAL_JUMP`
<a id="insn-00baf300"></a> `00baf300` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf304"></a> `00baf304` | `60 05 00 36` | tbz w0,#0x0,0x00baf3b0 | `CONDITIONAL_JUMP`
<a id="insn-00baf308"></a> `00baf308` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf30c"></a> `00baf30c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf310"></a> `00baf310` | `41 83 1f f8` | stur x1,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf314"></a> `00baf314` | `d6 ff ff 17` | b 0x00baf26c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf318"></a> `00baf318` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00baf31c"></a> `00baf31c` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00baf320"></a> `00baf320` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf324"></a> `00baf324` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00baf328"></a> `00baf328` | `e4 03 15 aa` | mov x4,x21 | `FALL_THROUGH`
<a id="insn-00baf32c"></a> `00baf32c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf330"></a> `00baf330` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf334"></a> `00baf334` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf338"></a> `00baf338` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf33c"></a> `00baf33c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf340"></a> `00baf340` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baf344"></a> `00baf344` | `8f b7 02 14` | b 0x00c5d180 | `CALL_TERMINATOR`
<a id="insn-00baf348"></a> `00baf348` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00baf34c"></a> `00baf34c` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00baf350"></a> `00baf350` | `63 62 00 91` | add x3,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00baf354"></a> `00baf354` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf358"></a> `00baf358` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00baf35c"></a> `00baf35c` | `e5 03 15 aa` | mov x5,x21 | `FALL_THROUGH`
<a id="insn-00baf360"></a> `00baf360` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf364"></a> `00baf364` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf368"></a> `00baf368` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf36c"></a> `00baf36c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf370"></a> `00baf370` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf374"></a> `00baf374` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baf378"></a> `00baf378` | `7a 00 00 14` | b 0x00baf560 | `CALL_TERMINATOR`
<a id="insn-00baf37c"></a> `00baf37c` | `80 f7 07 36` | tbz w0,#0x0,0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf380"></a> `00baf380` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf384"></a> `00baf384` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf388"></a> `00baf388` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf38c"></a> `00baf38c` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf390"></a> `00baf390` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf394"></a> `00baf394` | `61 02 40 a9` | ldp x1,x0,[x19] | `FALL_THROUGH`
<a id="insn-00baf398"></a> `00baf398` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf39c"></a> `00baf39c` | `80 f6 07 36` | tbz w0,#0x0,0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf3a0"></a> `00baf3a0` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00baf3a4"></a> `00baf3a4` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00baf3a8"></a> `00baf3a8` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00baf3ac"></a> `00baf3ac` | `b0 ff ff 17` | b 0x00baf26c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf3b0"></a> `00baf3b0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf3b4"></a> `00baf3b4` | `68 06 00 a9` | stp x8,x1,[x19] | `FALL_THROUGH`
<a id="insn-00baf3b8"></a> `00baf3b8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baf3bc"></a> `00baf3bc` | `40 83 5f f8` | ldur x0,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf3c0"></a> `00baf3c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf3c4"></a> `00baf3c4` | `40 f5 07 36` | tbz w0,#0x0,0x00baf26c | `CONDITIONAL_JUMP`
<a id="insn-00baf3c8"></a> `00baf3c8` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf3cc"></a> `00baf3cc` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf3d0"></a> `00baf3d0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baf3d4"></a> `00baf3d4` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00baf3d8"></a> `00baf3d8` | `a5 ff ff 17` | b 0x00baf26c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00baeec4`](#insn-00baeec4) 範囲 `[['00baeec4', '00baeeef']]`
  - `FALL_THROUGH` [`00baeeec`](#insn-00baeeec) → [`00baeef0`](#insn-00baeef0)
- ブロック [`00baeef0`](#insn-00baeef0) 範囲 `[['00baeef0', '00baeeff']]`
  - `UNCONDITIONAL_JUMP` [`00baeefc`](#insn-00baeefc) → [`00baef04`](#insn-00baef04)
- ブロック [`00baef00`](#insn-00baef00) 範囲 `[['00baef00', '00baef03']]`
  - `FALL_THROUGH` [`00baef00`](#insn-00baef00) → [`00baef04`](#insn-00baef04)
- ブロック [`00baef04`](#insn-00baef04) 範囲 `[['00baef04', '00baef17']]`
  - `CONDITIONAL_JUMP` [`00baef14`](#insn-00baef14) → [`00baf254`](#insn-00baf254)
  - `FALL_THROUGH` [`00baef14`](#insn-00baef14) → [`00baef18`](#insn-00baef18)
- ブロック [`00baef18`](#insn-00baef18) 範囲 `[['00baef18', '00baef1f']]`
  - `CONDITIONAL_JUMP` [`00baef1c`](#insn-00baef1c) → [`00baf288`](#insn-00baf288)
  - `FALL_THROUGH` [`00baef1c`](#insn-00baef1c) → [`00baef20`](#insn-00baef20)
- ブロック [`00baef20`](#insn-00baef20) 範囲 `[['00baef20', '00baef3b']]`
  - `CONDITIONAL_JUMP` [`00baef38`](#insn-00baef38) → [`00baef8c`](#insn-00baef8c)
  - `FALL_THROUGH` [`00baef38`](#insn-00baef38) → [`00baef3c`](#insn-00baef3c)
- ブロック [`00baef3c`](#insn-00baef3c) 範囲 `[['00baef3c', '00baef6f']]`
  - `FALL_THROUGH` [`00baef6c`](#insn-00baef6c) → [`00baef70`](#insn-00baef70)
- ブロック [`00baef70`](#insn-00baef70) 範囲 `[['00baef70', '00baef83']]`
  - `CONDITIONAL_JUMP` [`00baef80`](#insn-00baef80) → [`00baefd4`](#insn-00baefd4)
  - `FALL_THROUGH` [`00baef80`](#insn-00baef80) → [`00baef84`](#insn-00baef84)
- ブロック [`00baef84`](#insn-00baef84) 範囲 `[['00baef84', '00baef8b']]`
  - `UNCONDITIONAL_JUMP` [`00baef88`](#insn-00baef88) → [`00baf008`](#insn-00baf008)
- ブロック [`00baef8c`](#insn-00baef8c) 範囲 `[['00baef8c', '00baefb7']]`
  - `CONDITIONAL_JUMP` [`00baefb4`](#insn-00baefb4) → [`00baf148`](#insn-00baf148)
  - `FALL_THROUGH` [`00baefb4`](#insn-00baefb4) → [`00baefb8`](#insn-00baefb8)
- ブロック [`00baefb8`](#insn-00baefb8) 範囲 `[['00baefb8', '00baefbf']]`
  - `CONDITIONAL_JUMP` [`00baefbc`](#insn-00baefbc) → [`00baf184`](#insn-00baf184)
  - `FALL_THROUGH` [`00baefbc`](#insn-00baefbc) → [`00baefc0`](#insn-00baefc0)
- ブロック [`00baefc0`](#insn-00baefc0) 範囲 `[['00baefc0', '00baefd3']]`
  - `UNCONDITIONAL_JUMP` [`00baefd0`](#insn-00baefd0) → [`00baef70`](#insn-00baef70)
- ブロック [`00baefd4`](#insn-00baefd4) 範囲 `[['00baefd4', '00baefd7']]`
  - `FALL_THROUGH` [`00baefd4`](#insn-00baefd4) → [`00baefd8`](#insn-00baefd8)
- ブロック [`00baefd8`](#insn-00baefd8) 範囲 `[['00baefd8', '00baefdf']]`
  - `CONDITIONAL_JUMP` [`00baefdc`](#insn-00baefdc) → [`00baf100`](#insn-00baf100)
  - `FALL_THROUGH` [`00baefdc`](#insn-00baefdc) → [`00baefe0`](#insn-00baefe0)
- ブロック [`00baefe0`](#insn-00baefe0) 範囲 `[['00baefe0', '00baeff3']]`
  - `CONDITIONAL_JUMP` [`00baeff0`](#insn-00baeff0) → [`00baefd8`](#insn-00baefd8)
  - `FALL_THROUGH` [`00baeff0`](#insn-00baeff0) → [`00baeff4`](#insn-00baeff4)
- ブロック [`00baeff4`](#insn-00baeff4) 範囲 `[['00baeff4', '00baf007']]`
  - `FALL_THROUGH` [`00baf004`](#insn-00baf004) → [`00baf008`](#insn-00baf008)
- ブロック [`00baf008`](#insn-00baf008) 範囲 `[['00baf008', '00baf013']]`
  - `CONDITIONAL_JUMP` [`00baf010`](#insn-00baf010) → [`00baf074`](#insn-00baf074)
  - `FALL_THROUGH` [`00baf010`](#insn-00baf010) → [`00baf014`](#insn-00baf014)
- ブロック [`00baf014`](#insn-00baf014) 範囲 `[['00baf014', '00baf017']]`
  - `FALL_THROUGH` [`00baf014`](#insn-00baf014) → [`00baf018`](#insn-00baf018)
- ブロック [`00baf018`](#insn-00baf018) 範囲 `[['00baf018', '00baf02b']]`
  - `CONDITIONAL_JUMP` [`00baf028`](#insn-00baf028) → [`00baf018`](#insn-00baf018)
  - `FALL_THROUGH` [`00baf028`](#insn-00baf028) → [`00baf02c`](#insn-00baf02c)
- ブロック [`00baf02c`](#insn-00baf02c) 範囲 `[['00baf02c', '00baf02f']]`
  - `FALL_THROUGH` [`00baf02c`](#insn-00baf02c) → [`00baf030`](#insn-00baf030)
- ブロック [`00baf030`](#insn-00baf030) 範囲 `[['00baf030', '00baf043']]`
  - `CONDITIONAL_JUMP` [`00baf040`](#insn-00baf040) → [`00baf030`](#insn-00baf030)
  - `FALL_THROUGH` [`00baf040`](#insn-00baf040) → [`00baf044`](#insn-00baf044)
- ブロック [`00baf044`](#insn-00baf044) 範囲 `[['00baf044', '00baf04b']]`
  - `CONDITIONAL_JUMP` [`00baf048`](#insn-00baf048) → [`00baf06c`](#insn-00baf06c)
  - `FALL_THROUGH` [`00baf048`](#insn-00baf048) → [`00baf04c`](#insn-00baf04c)
- ブロック [`00baf04c`](#insn-00baf04c) 範囲 `[['00baf04c', '00baf06b']]`
  - `UNCONDITIONAL_JUMP` [`00baf068`](#insn-00baf068) → [`00baf014`](#insn-00baf014)
- ブロック [`00baf06c`](#insn-00baf06c) 範囲 `[['00baf06c', '00baf073']]`
  - `FALL_THROUGH` [`00baf070`](#insn-00baf070) → [`00baf074`](#insn-00baf074)
- ブロック [`00baf074`](#insn-00baf074) 範囲 `[['00baf074', '00baf07b']]`
  - `CONDITIONAL_JUMP` [`00baf078`](#insn-00baf078) → [`00baf0a4`](#insn-00baf0a4)
  - `FALL_THROUGH` [`00baf078`](#insn-00baf078) → [`00baf07c`](#insn-00baf07c)
- ブロック [`00baf07c`](#insn-00baf07c) 範囲 `[['00baf07c', '00baf08f']]`
  - `CONDITIONAL_JUMP` [`00baf08c`](#insn-00baf08c) → [`00baf0a4`](#insn-00baf0a4)
  - `FALL_THROUGH` [`00baf08c`](#insn-00baf08c) → [`00baf090`](#insn-00baf090)
- ブロック [`00baf090`](#insn-00baf090) 範囲 `[['00baf090', '00baf0a3']]`
  - `FALL_THROUGH` [`00baf0a0`](#insn-00baf0a0) → [`00baf0a4`](#insn-00baf0a4)
- ブロック [`00baf0a4`](#insn-00baf0a4) 範囲 `[['00baf0a4', '00baf0a7']]`
  - `CONDITIONAL_JUMP` [`00baf0a4`](#insn-00baf0a4) → [`00baf0d8`](#insn-00baf0d8)
  - `FALL_THROUGH` [`00baf0a4`](#insn-00baf0a4) → [`00baf0a8`](#insn-00baf0a8)
- ブロック [`00baf0a8`](#insn-00baf0a8) 範囲 `[['00baf0a8', '00baf0d3']]`
  - `CONDITIONAL_JUMP` [`00baf0d0`](#insn-00baf0d0) → [`00baf248`](#insn-00baf248)
  - `FALL_THROUGH` [`00baf0d0`](#insn-00baf0d0) → [`00baf0d4`](#insn-00baf0d4)
- ブロック [`00baf0d4`](#insn-00baf0d4) 範囲 `[['00baf0d4', '00baf0d7']]`
  - `CONDITIONAL_JUMP` [`00baf0d4`](#insn-00baf0d4) → [`00baef04`](#insn-00baef04)
  - `FALL_THROUGH` [`00baf0d4`](#insn-00baf0d4) → [`00baf0d8`](#insn-00baf0d8)
- ブロック [`00baf0d8`](#insn-00baf0d8) 範囲 `[['00baf0d8', '00baf0e7']]`
  - `CONDITIONAL_JUMP` [`00baf0e4`](#insn-00baf0e4) → [`00baf230`](#insn-00baf230)
  - `FALL_THROUGH` [`00baf0e4`](#insn-00baf0e4) → [`00baf0e8`](#insn-00baf0e8)
- ブロック [`00baf0e8`](#insn-00baf0e8) 範囲 `[['00baf0e8', '00baf0ff']]`
  - `UNCONDITIONAL_JUMP` [`00baf0fc`](#insn-00baf0fc) → [`00baef04`](#insn-00baef04)
- ブロック [`00baf100`](#insn-00baf100) 範囲 `[['00baf100', '00baf117']]`
  - `CONDITIONAL_JUMP` [`00baf114`](#insn-00baf114) → [`00baf1d8`](#insn-00baf1d8)
  - `FALL_THROUGH` [`00baf114`](#insn-00baf114) → [`00baf118`](#insn-00baf118)
- ブロック [`00baf118`](#insn-00baf118) 範囲 `[['00baf118', '00baf11f']]`
  - `CONDITIONAL_JUMP` [`00baf11c`](#insn-00baf11c) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf11c`](#insn-00baf11c) → [`00baf120`](#insn-00baf120)
- ブロック [`00baf120`](#insn-00baf120) 範囲 `[['00baf120', '00baf123']]`
  - `FALL_THROUGH` [`00baf120`](#insn-00baf120) → [`00baf124`](#insn-00baf124)
- ブロック [`00baf124`](#insn-00baf124) 範囲 `[['00baf124', '00baf137']]`
  - `CONDITIONAL_JUMP` [`00baf134`](#insn-00baf134) → [`00baf1c8`](#insn-00baf1c8)
  - `FALL_THROUGH` [`00baf134`](#insn-00baf134) → [`00baf138`](#insn-00baf138)
- ブロック [`00baf138`](#insn-00baf138) 範囲 `[['00baf138', '00baf143']]`
  - `CONDITIONAL_JUMP` [`00baf140`](#insn-00baf140) → [`00baf124`](#insn-00baf124)
  - `FALL_THROUGH` [`00baf140`](#insn-00baf140) → [`00baf144`](#insn-00baf144)
- ブロック [`00baf144`](#insn-00baf144) 範囲 `[['00baf144', '00baf147']]`
  - `UNCONDITIONAL_JUMP` [`00baf144`](#insn-00baf144) → [`00baf26c`](#insn-00baf26c)
- ブロック [`00baf148`](#insn-00baf148) 範囲 `[['00baf148', '00baf14b']]`
  - `CONDITIONAL_JUMP` [`00baf148`](#insn-00baf148) → [`00baf1b8`](#insn-00baf1b8)
  - `FALL_THROUGH` [`00baf148`](#insn-00baf148) → [`00baf14c`](#insn-00baf14c)
- ブロック [`00baf14c`](#insn-00baf14c) 範囲 `[['00baf14c', '00baf16f']]`
  - `CONDITIONAL_JUMP` [`00baf16c`](#insn-00baf16c) → [`00baf1c0`](#insn-00baf1c0)
  - `FALL_THROUGH` [`00baf16c`](#insn-00baf16c) → [`00baf170`](#insn-00baf170)
- ブロック [`00baf170`](#insn-00baf170) 範囲 `[['00baf170', '00baf183']]`
  - `UNCONDITIONAL_JUMP` [`00baf180`](#insn-00baf180) → [`00baf1b0`](#insn-00baf1b0)
- ブロック [`00baf184`](#insn-00baf184) 範囲 `[['00baf184', '00baf19f']]`
  - `CONDITIONAL_JUMP` [`00baf19c`](#insn-00baf19c) → [`00baf1c0`](#insn-00baf1c0)
  - `FALL_THROUGH` [`00baf19c`](#insn-00baf19c) → [`00baf1a0`](#insn-00baf1a0)
- ブロック [`00baf1a0`](#insn-00baf1a0) 範囲 `[['00baf1a0', '00baf1af']]`
  - `FALL_THROUGH` [`00baf1ac`](#insn-00baf1ac) → [`00baf1b0`](#insn-00baf1b0)
- ブロック [`00baf1b0`](#insn-00baf1b0) 範囲 `[['00baf1b0', '00baf1b7']]`
  - `UNCONDITIONAL_JUMP` [`00baf1b4`](#insn-00baf1b4) → [`00baef70`](#insn-00baef70)
- ブロック [`00baf1b8`](#insn-00baf1b8) 範囲 `[['00baf1b8', '00baf1bf']]`
  - `UNCONDITIONAL_JUMP` [`00baf1bc`](#insn-00baf1bc) → [`00baef70`](#insn-00baef70)
- ブロック [`00baf1c0`](#insn-00baf1c0) 範囲 `[['00baf1c0', '00baf1c7']]`
  - `UNCONDITIONAL_JUMP` [`00baf1c4`](#insn-00baf1c4) → [`00baef70`](#insn-00baef70)
- ブロック [`00baf1c8`](#insn-00baf1c8) 範囲 `[['00baf1c8', '00baf1d7']]`
  - `FALL_THROUGH` [`00baf1d4`](#insn-00baf1d4) → [`00baf1d8`](#insn-00baf1d8)
- ブロック [`00baf1d8`](#insn-00baf1d8) 範囲 `[['00baf1d8', '00baf1df']]`
  - `CONDITIONAL_JUMP` [`00baf1dc`](#insn-00baf1dc) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf1dc`](#insn-00baf1dc) → [`00baf1e0`](#insn-00baf1e0)
- ブロック [`00baf1e0`](#insn-00baf1e0) 範囲 `[['00baf1e0', '00baf1e3']]`
  - `FALL_THROUGH` [`00baf1e0`](#insn-00baf1e0) → [`00baf1e4`](#insn-00baf1e4)
- ブロック [`00baf1e4`](#insn-00baf1e4) 範囲 `[['00baf1e4', '00baf1e7']]`
  - `FALL_THROUGH` [`00baf1e4`](#insn-00baf1e4) → [`00baf1e8`](#insn-00baf1e8)
- ブロック [`00baf1e8`](#insn-00baf1e8) 範囲 `[['00baf1e8', '00baf1fb']]`
  - `CONDITIONAL_JUMP` [`00baf1f8`](#insn-00baf1f8) → [`00baf1e8`](#insn-00baf1e8)
  - `FALL_THROUGH` [`00baf1f8`](#insn-00baf1f8) → [`00baf1fc`](#insn-00baf1fc)
- ブロック [`00baf1fc`](#insn-00baf1fc) 範囲 `[['00baf1fc', '00baf1ff']]`
  - `FALL_THROUGH` [`00baf1fc`](#insn-00baf1fc) → [`00baf200`](#insn-00baf200)
- ブロック [`00baf200`](#insn-00baf200) 範囲 `[['00baf200', '00baf213']]`
  - `CONDITIONAL_JUMP` [`00baf210`](#insn-00baf210) → [`00baf200`](#insn-00baf200)
  - `FALL_THROUGH` [`00baf210`](#insn-00baf210) → [`00baf214`](#insn-00baf214)
- ブロック [`00baf214`](#insn-00baf214) 範囲 `[['00baf214', '00baf21b']]`
  - `CONDITIONAL_JUMP` [`00baf218`](#insn-00baf218) → [`00baef00`](#insn-00baef00)
  - `FALL_THROUGH` [`00baf218`](#insn-00baf218) → [`00baf21c`](#insn-00baf21c)
- ブロック [`00baf21c`](#insn-00baf21c) 範囲 `[['00baf21c', '00baf22f']]`
  - `UNCONDITIONAL_JUMP` [`00baf22c`](#insn-00baf22c) → [`00baf1e4`](#insn-00baf1e4)
- ブロック [`00baf230`](#insn-00baf230) 範囲 `[['00baf230', '00baf247']]`
  - `UNCONDITIONAL_JUMP` [`00baf244`](#insn-00baf244) → [`00baeef0`](#insn-00baeef0)
- ブロック [`00baf248`](#insn-00baf248) 範囲 `[['00baf248', '00baf24f']]`
  - `CONDITIONAL_JUMP` [`00baf24c`](#insn-00baf24c) → [`00baeef0`](#insn-00baeef0)
  - `FALL_THROUGH` [`00baf24c`](#insn-00baf24c) → [`00baf250`](#insn-00baf250)
- ブロック [`00baf250`](#insn-00baf250) 範囲 `[['00baf250', '00baf253']]`
  - `UNCONDITIONAL_JUMP` [`00baf250`](#insn-00baf250) → [`00baf26c`](#insn-00baf26c)
- ブロック [`00baf254`](#insn-00baf254) 範囲 `[['00baf254', '00baf267']]`
  - `FALL_THROUGH` [`00baf264`](#insn-00baf264) → [`00baf268`](#insn-00baf268)
- ブロック [`00baf268`](#insn-00baf268) 範囲 `[['00baf268', '00baf26b']]`
  - `COMPUTED_JUMP` [`00baf268`](#insn-00baf268) → [`00baf26c`](#insn-00baf26c)
  - `COMPUTED_JUMP` [`00baf268`](#insn-00baf268) → [`00baf2b0`](#insn-00baf2b0)
  - `COMPUTED_JUMP` [`00baf268`](#insn-00baf268) → [`00baf2d8`](#insn-00baf2d8)
  - `COMPUTED_JUMP` [`00baf268`](#insn-00baf268) → [`00baf318`](#insn-00baf318)
  - `COMPUTED_JUMP` [`00baf268`](#insn-00baf268) → [`00baf348`](#insn-00baf348)
- ブロック [`00baf26c`](#insn-00baf26c) 範囲 `[['00baf26c', '00baf287']]`
- ブロック [`00baf288`](#insn-00baf288) 範囲 `[['00baf288', '00baf2af']]`
- ブロック [`00baf2b0`](#insn-00baf2b0) 範囲 `[['00baf2b0', '00baf2c3']]`
  - `CONDITIONAL_JUMP` [`00baf2c0`](#insn-00baf2c0) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf2c0`](#insn-00baf2c0) → [`00baf2c4`](#insn-00baf2c4)
- ブロック [`00baf2c4`](#insn-00baf2c4) 範囲 `[['00baf2c4', '00baf2d7']]`
  - `UNCONDITIONAL_JUMP` [`00baf2d4`](#insn-00baf2d4) → [`00baf26c`](#insn-00baf26c)
- ブロック [`00baf2d8`](#insn-00baf2d8) 範囲 `[['00baf2d8', '00baf2ff']]`
  - `CONDITIONAL_JUMP` [`00baf2fc`](#insn-00baf2fc) → [`00baf37c`](#insn-00baf37c)
  - `FALL_THROUGH` [`00baf2fc`](#insn-00baf2fc) → [`00baf300`](#insn-00baf300)
- ブロック [`00baf300`](#insn-00baf300) 範囲 `[['00baf300', '00baf307']]`
  - `CONDITIONAL_JUMP` [`00baf304`](#insn-00baf304) → [`00baf3b0`](#insn-00baf3b0)
  - `FALL_THROUGH` [`00baf304`](#insn-00baf304) → [`00baf308`](#insn-00baf308)
- ブロック [`00baf308`](#insn-00baf308) 範囲 `[['00baf308', '00baf317']]`
  - `UNCONDITIONAL_JUMP` [`00baf314`](#insn-00baf314) → [`00baf26c`](#insn-00baf26c)
- ブロック [`00baf318`](#insn-00baf318) 範囲 `[['00baf318', '00baf347']]`
- ブロック [`00baf348`](#insn-00baf348) 範囲 `[['00baf348', '00baf37b']]`
- ブロック [`00baf37c`](#insn-00baf37c) 範囲 `[['00baf37c', '00baf37f']]`
  - `CONDITIONAL_JUMP` [`00baf37c`](#insn-00baf37c) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf37c`](#insn-00baf37c) → [`00baf380`](#insn-00baf380)
- ブロック [`00baf380`](#insn-00baf380) 範囲 `[['00baf380', '00baf39f']]`
  - `CONDITIONAL_JUMP` [`00baf39c`](#insn-00baf39c) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf39c`](#insn-00baf39c) → [`00baf3a0`](#insn-00baf3a0)
- ブロック [`00baf3a0`](#insn-00baf3a0) 範囲 `[['00baf3a0', '00baf3af']]`
  - `UNCONDITIONAL_JUMP` [`00baf3ac`](#insn-00baf3ac) → [`00baf26c`](#insn-00baf26c)
- ブロック [`00baf3b0`](#insn-00baf3b0) 範囲 `[['00baf3b0', '00baf3c7']]`
  - `CONDITIONAL_JUMP` [`00baf3c4`](#insn-00baf3c4) → [`00baf26c`](#insn-00baf26c)
  - `FALL_THROUGH` [`00baf3c4`](#insn-00baf3c4) → [`00baf3c8`](#insn-00baf3c8)
- ブロック [`00baf3c8`](#insn-00baf3c8) 範囲 `[['00baf3c8', '00baf3db']]`
  - `UNCONDITIONAL_JUMP` [`00baf3d8`](#insn-00baf3d8) → [`00baf26c`](#insn-00baf26c)

## 命令位置別の参照

- [`00baeec4`](#insn-00baeec4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeec8`](#insn-00baeec8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeecc`](#insn-00baeecc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeed0`](#insn-00baeed0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeed4`](#insn-00baeed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeed8`](#insn-00baeed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeefc`](#insn-00baeefc) → [`00baef04`](#insn-00baef04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef14`](#insn-00baef14) → [`00baf254`](#insn-00baf254) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef1c`](#insn-00baef1c) → [`00baf288`](#insn-00baf288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef38`](#insn-00baef38) → [`00baef8c`](#insn-00baef8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef68`](#insn-00baef68) → [`00baf560`](../00baf/00baf560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00baf560` · 推定シンボル `None` · 推定型 `None`
- [`00baef80`](#insn-00baef80) → [`00baefd4`](#insn-00baefd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef88`](#insn-00baef88) → [`00baf008`](#insn-00baf008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefb4`](#insn-00baefb4) → [`00baf148`](#insn-00baf148) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefbc`](#insn-00baefbc) → [`00baf184`](#insn-00baf184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefd0`](#insn-00baefd0) → [`00baef70`](#insn-00baef70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baefdc`](#insn-00baefdc) → [`00baf100`](#insn-00baf100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeff0`](#insn-00baeff0) → [`00baefd8`](#insn-00baefd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf010`](#insn-00baf010) → [`00baf074`](#insn-00baf074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf028`](#insn-00baf028) → [`00baf018`](#insn-00baf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf040`](#insn-00baf040) → [`00baf030`](#insn-00baf030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf048`](#insn-00baf048) → [`00baf06c`](#insn-00baf06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf068`](#insn-00baf068) → [`00baf014`](#insn-00baf014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf078`](#insn-00baf078) → [`00baf0a4`](#insn-00baf0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf08c`](#insn-00baf08c) → [`00baf0a4`](#insn-00baf0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf0a4`](#insn-00baf0a4) → [`00baf0d8`](#insn-00baf0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf0b4`](#insn-00baf0b4) → [`00c5ce80`](../00c5c/00c5ce80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce80` · 推定シンボル `None` · 推定型 `None`
- [`00baf0cc`](#insn-00baf0cc) → [`00c5ce80`](../00c5c/00c5ce80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce80` · 推定シンボル `None` · 推定型 `None`
- [`00baf0d0`](#insn-00baf0d0) → [`00baf248`](#insn-00baf248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf0d4`](#insn-00baf0d4) → [`00baef04`](#insn-00baef04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf0e4`](#insn-00baf0e4) → [`00baf230`](#insn-00baf230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf0f4`](#insn-00baf0f4) → [`00c5cec0`](../00c5c/00c5cec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cec0` · 推定シンボル `None` · 推定型 `None`
- [`00baf0fc`](#insn-00baf0fc) → [`00baef04`](#insn-00baef04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf114`](#insn-00baf114) → [`00baf1d8`](#insn-00baf1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf11c`](#insn-00baf11c) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf134`](#insn-00baf134) → [`00baf1c8`](#insn-00baf1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf140`](#insn-00baf140) → [`00baf124`](#insn-00baf124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf144`](#insn-00baf144) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf148`](#insn-00baf148) → [`00baf1b8`](#insn-00baf1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf16c`](#insn-00baf16c) → [`00baf1c0`](#insn-00baf1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf180`](#insn-00baf180) → [`00baf1b0`](#insn-00baf1b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf19c`](#insn-00baf19c) → [`00baf1c0`](#insn-00baf1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf1b4`](#insn-00baf1b4) → [`00baef70`](#insn-00baef70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf1bc`](#insn-00baf1bc) → [`00baef70`](#insn-00baef70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf1c4`](#insn-00baf1c4) → [`00baef70`](#insn-00baef70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf1dc`](#insn-00baf1dc) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf1f8`](#insn-00baf1f8) → [`00baf1e8`](#insn-00baf1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf210`](#insn-00baf210) → [`00baf200`](#insn-00baf200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf218`](#insn-00baf218) → [`00baef00`](#insn-00baef00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf22c`](#insn-00baf22c) → [`00baf1e4`](#insn-00baf1e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf23c`](#insn-00baf23c) → [`00c5cec0`](../00c5c/00c5cec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cec0` · 推定シンボル `None` · 推定型 `None`
- [`00baf244`](#insn-00baf244) → [`00baeef0`](#insn-00baeef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf24c`](#insn-00baf24c) → [`00baeef0`](#insn-00baeef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf250`](#insn-00baf250) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf260`](#insn-00baf260) → `0030e258`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::switchdataD_0030e258` · 推定型 `byte`
- [`00baf268`](#insn-00baf268) → [`00baf26c`](#insn-00baf26c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf268`](#insn-00baf268) → [`00baf2b0`](#insn-00baf2b0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_2` · 推定型 `None`
- [`00baf268`](#insn-00baf268) → [`00baf2d8`](#insn-00baf2d8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_3` · 推定型 `None`
- [`00baf268`](#insn-00baf268) → [`00baf318`](#insn-00baf318) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_4` · 推定型 `None`
- [`00baf268`](#insn-00baf268) → [`00baf348`](#insn-00baf348) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_5` · 推定型 `None`
- [`00baf26c`](#insn-00baf26c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf270`](#insn-00baf270) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf274`](#insn-00baf274) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf278`](#insn-00baf278) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf27c`](#insn-00baf27c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf294`](#insn-00baf294) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf298`](#insn-00baf298) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf29c`](#insn-00baf29c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2a0`](#insn-00baf2a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2a4`](#insn-00baf2a4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2ac`](#insn-00baf2ac) → [`00c5ccc0`](../00c5c/00c5ccc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ccc0` · 推定シンボル `None` · 推定型 `None`
- [`00baf2c0`](#insn-00baf2c0) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf2d4`](#insn-00baf2d4) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf2fc`](#insn-00baf2fc) → [`00baf37c`](#insn-00baf37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf304`](#insn-00baf304) → [`00baf3b0`](#insn-00baf3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf314`](#insn-00baf314) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf32c`](#insn-00baf32c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf330`](#insn-00baf330) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf334`](#insn-00baf334) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf338`](#insn-00baf338) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf33c`](#insn-00baf33c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf344`](#insn-00baf344) → [`00c5d180`](../00c5d/00c5d180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d180` · 推定シンボル `None` · 推定型 `None`
- [`00baf360`](#insn-00baf360) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf364`](#insn-00baf364) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf368`](#insn-00baf368) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf36c`](#insn-00baf36c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf370`](#insn-00baf370) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf378`](#insn-00baf378) → [`00baf560`](../00baf/00baf560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00baf560` · 推定シンボル `None` · 推定型 `None`
- [`00baf37c`](#insn-00baf37c) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf39c`](#insn-00baf39c) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf3ac`](#insn-00baf3ac) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf3c4`](#insn-00baf3c4) → [`00baf26c`](#insn-00baf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`
- [`00baf3d8`](#insn-00baf3d8) → [`00baf26c`](#insn-00baf26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baf268::caseD_0` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeec4`](#insn-00baeec4)

~~~json
{
  "source": "00baeec4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeec8`](#insn-00baeec8)

~~~json
{
  "source": "00baeec8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeecc`](#insn-00baeecc)

~~~json
{
  "source": "00baeecc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeed0`](#insn-00baeed0)

~~~json
{
  "source": "00baeed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeed4`](#insn-00baeed4)

~~~json
{
  "source": "00baeed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeed8`](#insn-00baeed8)

~~~json
{
  "source": "00baeed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeefc`](#insn-00baeefc)

~~~json
{
  "source": "00baeefc",
  "target": "00baef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef14`](#insn-00baef14)

~~~json
{
  "source": "00baef14",
  "target": "00baf254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef1c`](#insn-00baef1c)

~~~json
{
  "source": "00baef1c",
  "target": "00baf288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef38`](#insn-00baef38)

~~~json
{
  "source": "00baef38",
  "target": "00baef8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef68`](#insn-00baef68)

~~~json
{
  "source": "00baef68",
  "target": "00baf560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baef80`](#insn-00baef80)

~~~json
{
  "source": "00baef80",
  "target": "00baefd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef88`](#insn-00baef88)

~~~json
{
  "source": "00baef88",
  "target": "00baf008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefb4`](#insn-00baefb4)

~~~json
{
  "source": "00baefb4",
  "target": "00baf148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefbc`](#insn-00baefbc)

~~~json
{
  "source": "00baefbc",
  "target": "00baf184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefd0`](#insn-00baefd0)

~~~json
{
  "source": "00baefd0",
  "target": "00baef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baefdc`](#insn-00baefdc)

~~~json
{
  "source": "00baefdc",
  "target": "00baf100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeff0`](#insn-00baeff0)

~~~json
{
  "source": "00baeff0",
  "target": "00baefd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf010`](#insn-00baf010)

~~~json
{
  "source": "00baf010",
  "target": "00baf074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf028`](#insn-00baf028)

~~~json
{
  "source": "00baf028",
  "target": "00baf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf040`](#insn-00baf040)

~~~json
{
  "source": "00baf040",
  "target": "00baf030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf048`](#insn-00baf048)

~~~json
{
  "source": "00baf048",
  "target": "00baf06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf068`](#insn-00baf068)

~~~json
{
  "source": "00baf068",
  "target": "00baf014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf078`](#insn-00baf078)

~~~json
{
  "source": "00baf078",
  "target": "00baf0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf08c`](#insn-00baf08c)

~~~json
{
  "source": "00baf08c",
  "target": "00baf0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf0a4`](#insn-00baf0a4)

~~~json
{
  "source": "00baf0a4",
  "target": "00baf0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf0b4`](#insn-00baf0b4)

~~~json
{
  "source": "00baf0b4",
  "target": "00c5ce80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf0cc`](#insn-00baf0cc)

~~~json
{
  "source": "00baf0cc",
  "target": "00c5ce80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf0d0`](#insn-00baf0d0)

~~~json
{
  "source": "00baf0d0",
  "target": "00baf248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf0d4`](#insn-00baf0d4)

~~~json
{
  "source": "00baf0d4",
  "target": "00baef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf0e4`](#insn-00baf0e4)

~~~json
{
  "source": "00baf0e4",
  "target": "00baf230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf0f4`](#insn-00baf0f4)

~~~json
{
  "source": "00baf0f4",
  "target": "00c5cec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf0fc`](#insn-00baf0fc)

~~~json
{
  "source": "00baf0fc",
  "target": "00baef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf114`](#insn-00baf114)

~~~json
{
  "source": "00baf114",
  "target": "00baf1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf11c`](#insn-00baf11c)

~~~json
{
  "source": "00baf11c",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf134`](#insn-00baf134)

~~~json
{
  "source": "00baf134",
  "target": "00baf1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf140`](#insn-00baf140)

~~~json
{
  "source": "00baf140",
  "target": "00baf124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf144`](#insn-00baf144)

~~~json
{
  "source": "00baf144",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf148`](#insn-00baf148)

~~~json
{
  "source": "00baf148",
  "target": "00baf1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf16c`](#insn-00baf16c)

~~~json
{
  "source": "00baf16c",
  "target": "00baf1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf180`](#insn-00baf180)

~~~json
{
  "source": "00baf180",
  "target": "00baf1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf19c`](#insn-00baf19c)

~~~json
{
  "source": "00baf19c",
  "target": "00baf1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf1b4`](#insn-00baf1b4)

~~~json
{
  "source": "00baf1b4",
  "target": "00baef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf1bc`](#insn-00baf1bc)

~~~json
{
  "source": "00baf1bc",
  "target": "00baef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf1c4`](#insn-00baf1c4)

~~~json
{
  "source": "00baf1c4",
  "target": "00baef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf1dc`](#insn-00baf1dc)

~~~json
{
  "source": "00baf1dc",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf1f8`](#insn-00baf1f8)

~~~json
{
  "source": "00baf1f8",
  "target": "00baf1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf210`](#insn-00baf210)

~~~json
{
  "source": "00baf210",
  "target": "00baf200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf218`](#insn-00baf218)

~~~json
{
  "source": "00baf218",
  "target": "00baef00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf22c`](#insn-00baf22c)

~~~json
{
  "source": "00baf22c",
  "target": "00baf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf23c`](#insn-00baf23c)

~~~json
{
  "source": "00baf23c",
  "target": "00c5cec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf244`](#insn-00baf244)

~~~json
{
  "source": "00baf244",
  "target": "00baeef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf24c`](#insn-00baf24c)

~~~json
{
  "source": "00baf24c",
  "target": "00baeef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf250`](#insn-00baf250)

~~~json
{
  "source": "00baf250",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf260`](#insn-00baf260)

~~~json
{
  "source": "00baf260",
  "target": "0030e258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e258",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e258",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baf268`](#insn-00baf268)

~~~json
{
  "source": "00baf268",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf268`](#insn-00baf268)

~~~json
{
  "source": "00baf268",
  "target": "00baf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf268`](#insn-00baf268)

~~~json
{
  "source": "00baf268",
  "target": "00baf2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf268`](#insn-00baf268)

~~~json
{
  "source": "00baf268",
  "target": "00baf318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf268`](#insn-00baf268)

~~~json
{
  "source": "00baf268",
  "target": "00baf348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf26c`](#insn-00baf26c)

~~~json
{
  "source": "00baf26c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf270`](#insn-00baf270)

~~~json
{
  "source": "00baf270",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf274`](#insn-00baf274)

~~~json
{
  "source": "00baf274",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf278`](#insn-00baf278)

~~~json
{
  "source": "00baf278",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf27c`](#insn-00baf27c)

~~~json
{
  "source": "00baf27c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf294`](#insn-00baf294)

~~~json
{
  "source": "00baf294",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf298`](#insn-00baf298)

~~~json
{
  "source": "00baf298",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf29c`](#insn-00baf29c)

~~~json
{
  "source": "00baf29c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2a0`](#insn-00baf2a0)

~~~json
{
  "source": "00baf2a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2a4`](#insn-00baf2a4)

~~~json
{
  "source": "00baf2a4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2ac`](#insn-00baf2ac)

~~~json
{
  "source": "00baf2ac",
  "target": "00c5ccc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf2c0`](#insn-00baf2c0)

~~~json
{
  "source": "00baf2c0",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2d4`](#insn-00baf2d4)

~~~json
{
  "source": "00baf2d4",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2fc`](#insn-00baf2fc)

~~~json
{
  "source": "00baf2fc",
  "target": "00baf37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf304`](#insn-00baf304)

~~~json
{
  "source": "00baf304",
  "target": "00baf3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf314`](#insn-00baf314)

~~~json
{
  "source": "00baf314",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf32c`](#insn-00baf32c)

~~~json
{
  "source": "00baf32c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf330`](#insn-00baf330)

~~~json
{
  "source": "00baf330",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf334`](#insn-00baf334)

~~~json
{
  "source": "00baf334",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf338`](#insn-00baf338)

~~~json
{
  "source": "00baf338",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf33c`](#insn-00baf33c)

~~~json
{
  "source": "00baf33c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf344`](#insn-00baf344)

~~~json
{
  "source": "00baf344",
  "target": "00c5d180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf360`](#insn-00baf360)

~~~json
{
  "source": "00baf360",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf364`](#insn-00baf364)

~~~json
{
  "source": "00baf364",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf368`](#insn-00baf368)

~~~json
{
  "source": "00baf368",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf36c`](#insn-00baf36c)

~~~json
{
  "source": "00baf36c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf370`](#insn-00baf370)

~~~json
{
  "source": "00baf370",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf378`](#insn-00baf378)

~~~json
{
  "source": "00baf378",
  "target": "00baf560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf37c`](#insn-00baf37c)

~~~json
{
  "source": "00baf37c",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf39c`](#insn-00baf39c)

~~~json
{
  "source": "00baf39c",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3ac`](#insn-00baf3ac)

~~~json
{
  "source": "00baf3ac",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3c4`](#insn-00baf3c4)

~~~json
{
  "source": "00baf3c4",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3d8`](#insn-00baf3d8)

~~~json
{
  "source": "00baf3d8",
  "target": "00baf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
