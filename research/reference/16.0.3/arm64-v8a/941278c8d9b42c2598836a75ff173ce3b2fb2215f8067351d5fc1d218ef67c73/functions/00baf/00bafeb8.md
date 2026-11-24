# 00bafeb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baeec4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0014.md#compare-1aad86994332fc4a652873c33ff0dd2b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafeb8",
  "name": "_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_",
  "size": 1304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "302770a58ca522b40726bcfef82d003f3552741ec4758613d5ecd651a2b62f44",
  "source_text_sha256": "302770a58ca522b40726bcfef82d003f3552741ec4758613d5ecd651a2b62f44",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafeb8",
        "00bb03cf"
      ]
    ],
    "bytes_sha256": "cf2f9c0ee89ab31a50dbfa1a5cae49dce49caaf69119b934d82f88f617c6cb1a",
    "instruction_count": 326,
    "instruction_bytes": 1304,
    "body_bytes": 1304,
    "indirect": 19,
    "unresolved": 18
  }
}
~~~

## 呼び出し元

- [00c5de90](../00c5d/00c5de90.md)

## 呼び出し先

- [00bb0554](../00bb0/00bb0554.md)
- [00c5dc90](../00c5d/00c5dc90.md)
- [00c5de50](../00c5d/00c5de50.md)
- [00c5de90](../00c5d/00c5de90.md)
- [00c5e150](../00c5e/00c5e150.md)

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
  
LAB_00bafee4:
  pauVar9 = (undefined1 (*) [16])(param_2[-1] + 8);
  pauVar10 = param_1;
LAB_00bafef8:
  param_1 = pauVar10;
  lVar5 = (long)param_2 - (long)param_1;
  uVar4 = lVar5 >> 3;
  switch(uVar4) {
  case 0:
  case 1:
    goto switchD_00bb025c_caseD_0;
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
    FUN_00bb0554(param_1,*param_1 + 8,param_1 + 1,param_1[1] + 8,pauVar9,param_3);
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
          if ((uVar4 & 1) == 0) goto LAB_00bb01b4;
          uVar6 = *(undefined8 *)*param_1;
          *(undefined8 *)*param_1 = *(undefined8 *)*pauVar10;
          *(undefined8 *)*pauVar10 = uVar6;
LAB_00bb01a4:
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
            goto LAB_00bb01a4;
          }
LAB_00bb01b4:
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
      iVar2 = FUN_00bb0554(param_1,*param_1 + lVar5,pauVar10,*pauVar10 + lVar5,pauVar9,param_3);
    }
    uVar4 = (*(code *)*param_3)(*(undefined8 *)*param_1,*(undefined8 *)*pauVar10);
    pauVar11 = pauVar9;
    pauVar8 = param_2 + -1;
    if ((uVar4 & 1) == 0) break;
    goto LAB_00bafffc;
  }
  while (pauVar11 = pauVar8, param_1 != pauVar11) {
    uVar4 = (*(code *)*param_3)(*(undefined8 *)*pauVar11,*(undefined8 *)*pauVar10);
    pauVar8 = (undefined1 (*) [16])(pauVar11[-1] + 8);
    if ((uVar4 & 1) != 0) goto code_r0x00baffe8;
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
  goto LAB_00bafef8;
code_r0x00baffe8:
  uVar6 = *(undefined8 *)*param_1;
  iVar2 = iVar2 + 1;
  *(undefined8 *)*param_1 = *(undefined8 *)*pauVar11;
  *(undefined8 *)*pauVar11 = uVar6;
LAB_00bafffc:
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
    if ((uVar3 & 1) != 0) goto LAB_00bb023c;
    pauVar10 = (undefined1 (*) [16])(*pauVar8 + 8);
    if ((uVar4 & 1) != 0) goto LAB_00bafef8;
  }
  if ((long)param_2 - (long)pauVar8 <= (long)pauVar8 - (long)param_1) {
    _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_
              ((long)*pauVar8 + 8,param_2,param_3);
    param_2 = pauVar8;
    goto LAB_00bafee4;
  }
  _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_(param_1,pauVar8,param_3);
  pauVar10 = (undefined1 (*) [16])(*pauVar8 + 8);
  goto LAB_00bafef8;
LAB_00bb023c:
  param_2 = pauVar8;
  if ((uVar4 & 1) != 0) {
switchD_00bb025c_caseD_0:
    return;
  }
  goto LAB_00bafee4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafeb8"></a> `00bafeb8` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bafebc"></a> `00bafebc` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafec0"></a> `00bafec0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafec4"></a> `00bafec4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafec8"></a> `00bafec8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafecc"></a> `00bafecc` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafed0"></a> `00bafed0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bafed4"></a> `00bafed4` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bafed8"></a> `00bafed8` | `fa 03 01 aa` | mov x26,x1 | `FALL_THROUGH`
<a id="insn-00bafedc"></a> `00bafedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafee0"></a> `00bafee0` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00bafee4"></a> `00bafee4` | `56 23 00 d1` | sub x22,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00bafee8"></a> `00bafee8` | `5b 43 00 d1` | sub x27,x26,#0x10 | `FALL_THROUGH`
<a id="insn-00bafeec"></a> `00bafeec` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00bafef0"></a> `00bafef0` | `02 00 00 14` | b 0x00bafef8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafef4"></a> `00bafef4` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00bafef8"></a> `00bafef8` | `49 03 17 cb` | sub x9,x26,x23 | `FALL_THROUGH`
<a id="insn-00bafefc"></a> `00bafefc` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00baff00"></a> `00baff00` | `f3 03 17 aa` | mov x19,x23 | `FALL_THROUGH`
<a id="insn-00baff04"></a> `00baff04` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00baff08"></a> `00baff08` | `09 1a 00 54` | b.ls 0x00bb0248 | `CONDITIONAL_JUMP`
<a id="insn-00baff0c"></a> `00baff0c` | `3f dd 03 f1` | cmp x9,#0xf7 | `FALL_THROUGH`
<a id="insn-00baff10"></a> `00baff10` | `6d 1b 00 54` | b.le 0x00bb027c | `CONDITIONAL_JUMP`
<a id="insn-00baff14"></a> `00baff14` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00baff18"></a> `00baff18` | `0a a5 88 9a` | cinc x10,x8,lt | `FALL_THROUGH`
<a id="insn-00baff1c"></a> `00baff1c` | `4a f5 7e d3` | lsl x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00baff20"></a> `00baff20` | `4a f1 7d 92` | and x10,x10,#-0x8 | `FALL_THROUGH`
<a id="insn-00baff24"></a> `00baff24` | `3f 01 19 eb` | cmp x9,x25 | `FALL_THROUGH`
<a id="insn-00baff28"></a> `00baff28` | `77 02 0a 8b` | add x23,x19,x10 | `FALL_THROUGH`
<a id="insn-00baff2c"></a> `00baff2c` | `ab 02 00 54` | b.lt 0x00baff80 | `CONDITIONAL_JUMP`
<a id="insn-00baff30"></a> `00baff30` | `09 0d 00 91` | add x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baff34"></a> `00baff34` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00baff38"></a> `00baff38` | `28 b1 88 9a` | csel x8,x9,x8,lt | `FALL_THROUGH`
<a id="insn-00baff3c"></a> `00baff3c` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baff40"></a> `00baff40` | `08 f1 7d 92` | and x8,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00baff44"></a> `00baff44` | `61 02 08 8b` | add x1,x19,x8 | `FALL_THROUGH`
<a id="insn-00baff48"></a> `00baff48` | `e3 02 08 8b` | add x3,x23,x8 | `FALL_THROUGH`
<a id="insn-00baff4c"></a> `00baff4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baff50"></a> `00baff50` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00baff54"></a> `00baff54` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00baff58"></a> `00baff58` | `e5 03 15 aa` | mov x5,x21 | `FALL_THROUGH`
<a id="insn-00baff5c"></a> `00baff5c` | `7e 01 00 94` | bl 0x00bb0554 | `UNCONDITIONAL_CALL`
<a id="insn-00baff60"></a> `00baff60` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baff64"></a> `00baff64` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baff68"></a> `00baff68` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00baff6c"></a> `00baff6c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baff70"></a> `00baff70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baff74"></a> `00baff74` | `a0 02 00 36` | tbz w0,#0x0,0x00baffc8 | `CONDITIONAL_JUMP`
<a id="insn-00baff78"></a> `00baff78` | `fc 03 16 aa` | mov x28,x22 | `FALL_THROUGH`
<a id="insn-00baff7c"></a> `00baff7c` | `20 00 00 14` | b 0x00bafffc | `UNCONDITIONAL_JUMP`
<a id="insn-00baff80"></a> `00baff80` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baff84"></a> `00baff84` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baff88"></a> `00baff88` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baff8c"></a> `00baff8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baff90"></a> `00baff90` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baff94"></a> `00baff94` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00baff98"></a> `00baff98` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baff9c"></a> `00baff9c` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00baffa0"></a> `00baffa0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baffa4"></a> `00baffa4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baffa8"></a> `00baffa8` | `b8 0c 00 36` | tbz w24,#0x0,0x00bb013c | `CONDITIONAL_JUMP`
<a id="insn-00baffac"></a> `00baffac` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00baffb0"></a> `00baffb0` | `40 0e 00 36` | tbz w0,#0x0,0x00bb0178 | `CONDITIONAL_JUMP`
<a id="insn-00baffb4"></a> `00baffb4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00baffb8"></a> `00baffb8` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00baffbc"></a> `00baffbc` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00baffc0"></a> `00baffc0` | `c1 02 00 f9` | str x1,[x22] | `FALL_THROUGH`
<a id="insn-00baffc4"></a> `00baffc4` | `e8 ff ff 17` | b 0x00baff64 | `UNCONDITIONAL_JUMP`
<a id="insn-00baffc8"></a> `00baffc8` | `fc 03 1b aa` | mov x28,x27 | `FALL_THROUGH`
<a id="insn-00baffcc"></a> `00baffcc` | `7f 02 1c eb` | cmp x19,x28 | `FALL_THROUGH`
<a id="insn-00baffd0"></a> `00baffd0` | `20 09 00 54` | b.eq 0x00bb00f4 | `CONDITIONAL_JUMP`
<a id="insn-00baffd4"></a> `00baffd4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baffd8"></a> `00baffd8` | `80 87 5f f8` | ldr x0,[x28], #-0x8 | `FALL_THROUGH`
<a id="insn-00baffdc"></a> `00baffdc` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baffe0"></a> `00baffe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baffe4"></a> `00baffe4` | `40 ff 07 36` | tbz w0,#0x0,0x00baffcc | `CONDITIONAL_JUMP`
<a id="insn-00baffe8"></a> `00baffe8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baffec"></a> `00baffec` | `89 8f 40 f8` | ldr x9,[x28, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafff0"></a> `00bafff0` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bafff4"></a> `00bafff4` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bafff8"></a> `00bafff8` | `88 03 00 f9` | str x8,[x28] | `FALL_THROUGH`
<a id="insn-00bafffc"></a> `00bafffc` | `74 22 00 91` | add x20,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0000"></a> `00bb0000` | `9f 02 1c eb` | cmp x20,x28 | `FALL_THROUGH`
<a id="insn-00bb0004"></a> `00bb0004` | `22 03 00 54` | b.cs 0x00bb0068 | `CONDITIONAL_JUMP`
<a id="insn-00bb0008"></a> `00bb0008` | `99 22 00 d1` | sub x25,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bb000c"></a> `00bb000c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0010"></a> `00bb0010` | `20 8f 40 f8` | ldr x0,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00bb0014"></a> `00bb0014` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00bb0018"></a> `00bb0018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb001c"></a> `00bb001c` | `80 ff 07 37` | tbnz w0,#0x0,0x00bb000c | `CONDITIONAL_JUMP`
<a id="insn-00bb0020"></a> `00bb0020` | `34 23 00 91` | add x20,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0024"></a> `00bb0024` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0028"></a> `00bb0028` | `80 8f 5f f8` | ldr x0,[x28, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bb002c"></a> `00bb002c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00bb0030"></a> `00bb0030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0034"></a> `00bb0034` | `80 ff 07 36` | tbz w0,#0x0,0x00bb0024 | `CONDITIONAL_JUMP`
<a id="insn-00bb0038"></a> `00bb0038` | `3f 03 1c eb` | cmp x25,x28 | `FALL_THROUGH`
<a id="insn-00bb003c"></a> `00bb003c` | `28 01 00 54` | b.hi 0x00bb0060 | `CONDITIONAL_JUMP`
<a id="insn-00bb0040"></a> `00bb0040` | `88 03 40 f9` | ldr x8,[x28] | `FALL_THROUGH`
<a id="insn-00bb0044"></a> `00bb0044` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-00bb0048"></a> `00bb0048` | `ff 02 19 eb` | cmp x23,x25 | `FALL_THROUGH`
<a id="insn-00bb004c"></a> `00bb004c` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0050"></a> `00bb0050` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00bb0054"></a> `00bb0054` | `89 03 00 f9` | str x9,[x28] | `FALL_THROUGH`
<a id="insn-00bb0058"></a> `00bb0058` | `97 03 97 9a` | csel x23,x28,x23,eq | `FALL_THROUGH`
<a id="insn-00bb005c"></a> `00bb005c` | `eb ff ff 17` | b 0x00bb0008 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0060"></a> `00bb0060` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00bb0064"></a> `00bb0064` | `39 e7 83 52` | mov w25,#0x1f39 | `FALL_THROUGH`
<a id="insn-00bb0068"></a> `00bb0068` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00bb006c"></a> `00bb006c` | `60 01 00 54` | b.eq 0x00bb0098 | `CONDITIONAL_JUMP`
<a id="insn-00bb0070"></a> `00bb0070` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0074"></a> `00bb0074` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00bb0078"></a> `00bb0078` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bb007c"></a> `00bb007c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0080"></a> `00bb0080` | `c0 00 00 36` | tbz w0,#0x0,0x00bb0098 | `CONDITIONAL_JUMP`
<a id="insn-00bb0084"></a> `00bb0084` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb0088"></a> `00bb0088` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bb008c"></a> `00bb008c` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0090"></a> `00bb0090` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bb0094"></a> `00bb0094` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb0098"></a> `00bb0098` | `b8 01 00 35` | cbnz w24,0x00bb00cc | `CONDITIONAL_JUMP`
<a id="insn-00bb009c"></a> `00bb009c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb00a0"></a> `00bb00a0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bb00a4"></a> `00bb00a4` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb00a8"></a> `00bb00a8` | `6a b7 02 94` | bl 0x00c5de50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00ac"></a> `00bb00ac` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bb00b0"></a> `00bb00b0` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00bb00b4"></a> `00bb00b4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bb00b8"></a> `00bb00b8` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bb00bc"></a> `00bb00bc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb00c0"></a> `00bb00c0` | `64 b7 02 94` | bl 0x00c5de50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00c4"></a> `00bb00c4` | `c0 0b 00 37` | tbnz w0,#0x0,0x00bb023c | `CONDITIONAL_JUMP`
<a id="insn-00bb00c8"></a> `00bb00c8` | `98 f1 07 37` | tbnz w24,#0x0,0x00bafef8 | `CONDITIONAL_JUMP`
<a id="insn-00bb00cc"></a> `00bb00cc` | `88 02 13 cb` | sub x8,x20,x19 | `FALL_THROUGH`
<a id="insn-00bb00d0"></a> `00bb00d0` | `49 03 14 cb` | sub x9,x26,x20 | `FALL_THROUGH`
<a id="insn-00bb00d4"></a> `00bb00d4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bb00d8"></a> `00bb00d8` | `6a 0a 00 54` | b.ge 0x00bb0224 | `CONDITIONAL_JUMP`
<a id="insn-00bb00dc"></a> `00bb00dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb00e0"></a> `00bb00e0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bb00e4"></a> `00bb00e4` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb00e8"></a> `00bb00e8` | `6a b7 02 94` | bl 0x00c5de90 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00ec"></a> `00bb00ec` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bb00f0"></a> `00bb00f0` | `82 ff ff 17` | b 0x00bafef8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00f4"></a> `00bb00f4` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00bb00f8"></a> `00bb00f8` | `00 87 40 f8` | ldr x0,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bb00fc"></a> `00bb00fc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0100"></a> `00bb0100` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00bb0104"></a> `00bb0104` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0108"></a> `00bb0108` | `20 06 00 37` | tbnz w0,#0x0,0x00bb01cc | `CONDITIONAL_JUMP`
<a id="insn-00bb010c"></a> `00bb010c` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bb0110"></a> `00bb0110` | `80 0a 00 54` | b.eq 0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb0114"></a> `00bb0114` | `78 42 00 91` | add x24,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bb0118"></a> `00bb0118` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb011c"></a> `00bb011c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb0120"></a> `00bb0120` | `01 83 5f f8` | ldur x1,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb0124"></a> `00bb0124` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0128"></a> `00bb0128` | `a0 04 00 37` | tbnz w0,#0x0,0x00bb01bc | `CONDITIONAL_JUMP`
<a id="insn-00bb012c"></a> `00bb012c` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0130"></a> `00bb0130` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-00bb0134"></a> `00bb0134` | `21 ff ff 54` | b.ne 0x00bb0118 | `CONDITIONAL_JUMP`
<a id="insn-00bb0138"></a> `00bb0138` | `4a 00 00 14` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb013c"></a> `00bb013c` | `80 03 00 36` | tbz w0,#0x0,0x00bb01ac | `CONDITIONAL_JUMP`
<a id="insn-00bb0140"></a> `00bb0140` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb0144"></a> `00bb0144` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb0148"></a> `00bb0148` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb014c"></a> `00bb014c` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00bb0150"></a> `00bb0150` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0154"></a> `00bb0154` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00bb0158"></a> `00bb0158` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00bb015c"></a> `00bb015c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0160"></a> `00bb0160` | `a0 02 00 36` | tbz w0,#0x0,0x00bb01b4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0164"></a> `00bb0164` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb0168"></a> `00bb0168` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bb016c"></a> `00bb016c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bb0170"></a> `00bb0170` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb0174"></a> `00bb0174` | `0c 00 00 14` | b 0x00bb01a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0178"></a> `00bb0178` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb017c"></a> `00bb017c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bb0180"></a> `00bb0180` | `e1 02 00 f9` | str x1,[x23] | `FALL_THROUGH`
<a id="insn-00bb0184"></a> `00bb0184` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0188"></a> `00bb0188` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00bb018c"></a> `00bb018c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0190"></a> `00bb0190` | `20 01 00 36` | tbz w0,#0x0,0x00bb01b4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0194"></a> `00bb0194` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb0198"></a> `00bb0198` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb019c"></a> `00bb019c` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb01a0"></a> `00bb01a0` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00bb01a4"></a> `00bb01a4` | `58 00 80 52` | mov w24,#0x2 | `FALL_THROUGH`
<a id="insn-00bb01a8"></a> `00bb01a8` | `6f ff ff 17` | b 0x00baff64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb01ac"></a> `00bb01ac` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00bb01b0"></a> `00bb01b0` | `6d ff ff 17` | b 0x00baff64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb01b4"></a> `00bb01b4` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bb01b8"></a> `00bb01b8` | `6b ff ff 17` | b 0x00baff64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb01bc"></a> `00bb01bc` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb01c0"></a> `00bb01c0` | `09 83 5f f8` | ldur x9,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb01c4"></a> `00bb01c4` | `08 83 1f f8` | stur x8,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb01c8"></a> `00bb01c8` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00bb01cc"></a> `00bb01cc` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bb01d0"></a> `00bb01d0` | `80 04 00 54` | b.eq 0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb01d4"></a> `00bb01d4` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00bb01d8"></a> `00bb01d8` | `17 23 00 d1` | sub x23,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bb01dc"></a> `00bb01dc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb01e0"></a> `00bb01e0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb01e4"></a> `00bb01e4` | `e1 8e 40 f8` | ldr x1,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00bb01e8"></a> `00bb01e8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb01ec"></a> `00bb01ec` | `80 ff 07 36` | tbz w0,#0x0,0x00bb01dc | `CONDITIONAL_JUMP`
<a id="insn-00bb01f0"></a> `00bb01f0` | `f8 22 00 91` | add x24,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bb01f4"></a> `00bb01f4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb01f8"></a> `00bb01f8` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb01fc"></a> `00bb01fc` | `21 8f 5f f8` | ldr x1,[x25, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bb0200"></a> `00bb0200` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0204"></a> `00bb0204` | `80 ff 07 37` | tbnz w0,#0x0,0x00bb01f4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0208"></a> `00bb0208` | `ff 02 19 eb` | cmp x23,x25 | `FALL_THROUGH`
<a id="insn-00bb020c"></a> `00bb020c` | `42 e7 ff 54` | b.cs 0x00bafef4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0210"></a> `00bb0210` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00bb0214"></a> `00bb0214` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb0218"></a> `00bb0218` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb021c"></a> `00bb021c` | `29 03 00 f9` | str x9,[x25] | `FALL_THROUGH`
<a id="insn-00bb0220"></a> `00bb0220` | `ee ff ff 17` | b 0x00bb01d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0224"></a> `00bb0224` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0228"></a> `00bb0228` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bb022c"></a> `00bb022c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb0230"></a> `00bb0230` | `18 b7 02 94` | bl 0x00c5de90 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0234"></a> `00bb0234` | `fa 03 14 aa` | mov x26,x20 | `FALL_THROUGH`
<a id="insn-00bb0238"></a> `00bb0238` | `2b ff ff 17` | b 0x00bafee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb023c"></a> `00bb023c` | `fa 03 14 aa` | mov x26,x20 | `FALL_THROUGH`
<a id="insn-00bb0240"></a> `00bb0240` | `38 e5 07 36` | tbz w24,#0x0,0x00bafee4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0244"></a> `00bb0244` | `07 00 00 14` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0248"></a> `00bb0248` | `e9 ba ff d0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00bb024c"></a> `00bb024c` | `29 61 0a 91` | add x9,x9,#0x298 | `FALL_THROUGH`
<a id="insn-00bb0250"></a> `00bb0250` | `8a 00 00 10` | adr x10,0xbb0260 | `FALL_THROUGH`
<a id="insn-00bb0254"></a> `00bb0254` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bb0258"></a> `00bb0258` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bb025c"></a> `00bb025c` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00bb0260"></a> `00bb0260` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb0264"></a> `00bb0264` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb0268"></a> `00bb0268` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb026c"></a> `00bb026c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb0270"></a> `00bb0270` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0274"></a> `00bb0274` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb0278"></a> `00bb0278` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb027c"></a> `00bb027c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb0280"></a> `00bb0280` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bb0284"></a> `00bb0284` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bb0288"></a> `00bb0288` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb028c"></a> `00bb028c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb0290"></a> `00bb0290` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb0294"></a> `00bb0294` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb0298"></a> `00bb0298` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb029c"></a> `00bb029c` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb02a0"></a> `00bb02a0` | `7c b6 02 14` | b 0x00c5dc90 | `CALL_TERMINATOR`
<a id="insn-00bb02a4"></a> `00bb02a4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb02a8"></a> `00bb02a8` | `40 83 5f f8` | ldur x0,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb02ac"></a> `00bb02ac` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00bb02b0"></a> `00bb02b0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb02b4"></a> `00bb02b4` | `60 fd 07 36` | tbz w0,#0x0,0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb02b8"></a> `00bb02b8` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb02bc"></a> `00bb02bc` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bb02c0"></a> `00bb02c0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bb02c4"></a> `00bb02c4` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb02c8"></a> `00bb02c8` | `e6 ff ff 17` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb02cc"></a> `00bb02cc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb02d0"></a> `00bb02d0` | `61 02 40 a9` | ldp x1,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb02d4"></a> `00bb02d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb02d8"></a> `00bb02d8` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb02dc"></a> `00bb02dc` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bb02e0"></a> `00bb02e0` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb02e4"></a> `00bb02e4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bb02e8"></a> `00bb02e8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb02ec"></a> `00bb02ec` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bb02f0"></a> `00bb02f0` | `16 04 00 36` | tbz w22,#0x0,0x00bb0370 | `CONDITIONAL_JUMP`
<a id="insn-00bb02f4"></a> `00bb02f4` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00bb02f8"></a> `00bb02f8` | `60 05 00 36` | tbz w0,#0x0,0x00bb03a4 | `CONDITIONAL_JUMP`
<a id="insn-00bb02fc"></a> `00bb02fc` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb0300"></a> `00bb0300` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bb0304"></a> `00bb0304` | `41 83 1f f8` | stur x1,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb0308"></a> `00bb0308` | `d6 ff ff 17` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb030c"></a> `00bb030c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0310"></a> `00bb0310` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bb0314"></a> `00bb0314` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb0318"></a> `00bb0318` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bb031c"></a> `00bb031c` | `e4 03 15 aa` | mov x4,x21 | `FALL_THROUGH`
<a id="insn-00bb0320"></a> `00bb0320` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb0324"></a> `00bb0324` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb0328"></a> `00bb0328` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb032c"></a> `00bb032c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb0330"></a> `00bb0330` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0334"></a> `00bb0334` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb0338"></a> `00bb0338` | `86 b7 02 14` | b 0x00c5e150 | `CALL_TERMINATOR`
<a id="insn-00bb033c"></a> `00bb033c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0340"></a> `00bb0340` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bb0344"></a> `00bb0344` | `63 62 00 91` | add x3,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bb0348"></a> `00bb0348` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb034c"></a> `00bb034c` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00bb0350"></a> `00bb0350` | `e5 03 15 aa` | mov x5,x21 | `FALL_THROUGH`
<a id="insn-00bb0354"></a> `00bb0354` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb0358"></a> `00bb0358` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb035c"></a> `00bb035c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb0360"></a> `00bb0360` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb0364"></a> `00bb0364` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0368"></a> `00bb0368` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb036c"></a> `00bb036c` | `7a 00 00 14` | b 0x00bb0554 | `CALL_TERMINATOR`
<a id="insn-00bb0370"></a> `00bb0370` | `80 f7 07 36` | tbz w0,#0x0,0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb0374"></a> `00bb0374` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb0378"></a> `00bb0378` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb037c"></a> `00bb037c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0380"></a> `00bb0380` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb0384"></a> `00bb0384` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb0388"></a> `00bb0388` | `61 02 40 a9` | ldp x1,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bb038c"></a> `00bb038c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb0390"></a> `00bb0390` | `80 f6 07 36` | tbz w0,#0x0,0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb0394"></a> `00bb0394` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00bb0398"></a> `00bb0398` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00bb039c"></a> `00bb039c` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bb03a0"></a> `00bb03a0` | `b0 ff ff 17` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb03a4"></a> `00bb03a4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb03a8"></a> `00bb03a8` | `68 06 00 a9` | stp x8,x1,[x19] | `FALL_THROUGH`
<a id="insn-00bb03ac"></a> `00bb03ac` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb03b0"></a> `00bb03b0` | `40 83 5f f8` | ldur x0,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb03b4"></a> `00bb03b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb03b8"></a> `00bb03b8` | `40 f5 07 36` | tbz w0,#0x0,0x00bb0260 | `CONDITIONAL_JUMP`
<a id="insn-00bb03bc"></a> `00bb03bc` | `48 83 5f f8` | ldur x8,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb03c0"></a> `00bb03c0` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb03c4"></a> `00bb03c4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bb03c8"></a> `00bb03c8` | `49 83 1f f8` | stur x9,[x26, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb03cc"></a> `00bb03cc` | `a5 ff ff 17` | b 0x00bb0260 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bafeb8`](#insn-00bafeb8) 範囲 `[['00bafeb8', '00bafee3']]`
  - `FALL_THROUGH` [`00bafee0`](#insn-00bafee0) → [`00bafee4`](#insn-00bafee4)
- ブロック [`00bafee4`](#insn-00bafee4) 範囲 `[['00bafee4', '00bafef3']]`
  - `UNCONDITIONAL_JUMP` [`00bafef0`](#insn-00bafef0) → [`00bafef8`](#insn-00bafef8)
- ブロック [`00bafef4`](#insn-00bafef4) 範囲 `[['00bafef4', '00bafef7']]`
  - `FALL_THROUGH` [`00bafef4`](#insn-00bafef4) → [`00bafef8`](#insn-00bafef8)
- ブロック [`00bafef8`](#insn-00bafef8) 範囲 `[['00bafef8', '00baff0b']]`
  - `CONDITIONAL_JUMP` [`00baff08`](#insn-00baff08) → [`00bb0248`](#insn-00bb0248)
  - `FALL_THROUGH` [`00baff08`](#insn-00baff08) → [`00baff0c`](#insn-00baff0c)
- ブロック [`00baff0c`](#insn-00baff0c) 範囲 `[['00baff0c', '00baff13']]`
  - `CONDITIONAL_JUMP` [`00baff10`](#insn-00baff10) → [`00bb027c`](#insn-00bb027c)
  - `FALL_THROUGH` [`00baff10`](#insn-00baff10) → [`00baff14`](#insn-00baff14)
- ブロック [`00baff14`](#insn-00baff14) 範囲 `[['00baff14', '00baff2f']]`
  - `CONDITIONAL_JUMP` [`00baff2c`](#insn-00baff2c) → [`00baff80`](#insn-00baff80)
  - `FALL_THROUGH` [`00baff2c`](#insn-00baff2c) → [`00baff30`](#insn-00baff30)
- ブロック [`00baff30`](#insn-00baff30) 範囲 `[['00baff30', '00baff63']]`
  - `FALL_THROUGH` [`00baff60`](#insn-00baff60) → [`00baff64`](#insn-00baff64)
- ブロック [`00baff64`](#insn-00baff64) 範囲 `[['00baff64', '00baff77']]`
  - `CONDITIONAL_JUMP` [`00baff74`](#insn-00baff74) → [`00baffc8`](#insn-00baffc8)
  - `FALL_THROUGH` [`00baff74`](#insn-00baff74) → [`00baff78`](#insn-00baff78)
- ブロック [`00baff78`](#insn-00baff78) 範囲 `[['00baff78', '00baff7f']]`
  - `UNCONDITIONAL_JUMP` [`00baff7c`](#insn-00baff7c) → [`00bafffc`](#insn-00bafffc)
- ブロック [`00baff80`](#insn-00baff80) 範囲 `[['00baff80', '00baffab']]`
  - `CONDITIONAL_JUMP` [`00baffa8`](#insn-00baffa8) → [`00bb013c`](#insn-00bb013c)
  - `FALL_THROUGH` [`00baffa8`](#insn-00baffa8) → [`00baffac`](#insn-00baffac)
- ブロック [`00baffac`](#insn-00baffac) 範囲 `[['00baffac', '00baffb3']]`
  - `CONDITIONAL_JUMP` [`00baffb0`](#insn-00baffb0) → [`00bb0178`](#insn-00bb0178)
  - `FALL_THROUGH` [`00baffb0`](#insn-00baffb0) → [`00baffb4`](#insn-00baffb4)
- ブロック [`00baffb4`](#insn-00baffb4) 範囲 `[['00baffb4', '00baffc7']]`
  - `UNCONDITIONAL_JUMP` [`00baffc4`](#insn-00baffc4) → [`00baff64`](#insn-00baff64)
- ブロック [`00baffc8`](#insn-00baffc8) 範囲 `[['00baffc8', '00baffcb']]`
  - `FALL_THROUGH` [`00baffc8`](#insn-00baffc8) → [`00baffcc`](#insn-00baffcc)
- ブロック [`00baffcc`](#insn-00baffcc) 範囲 `[['00baffcc', '00baffd3']]`
  - `CONDITIONAL_JUMP` [`00baffd0`](#insn-00baffd0) → [`00bb00f4`](#insn-00bb00f4)
  - `FALL_THROUGH` [`00baffd0`](#insn-00baffd0) → [`00baffd4`](#insn-00baffd4)
- ブロック [`00baffd4`](#insn-00baffd4) 範囲 `[['00baffd4', '00baffe7']]`
  - `CONDITIONAL_JUMP` [`00baffe4`](#insn-00baffe4) → [`00baffcc`](#insn-00baffcc)
  - `FALL_THROUGH` [`00baffe4`](#insn-00baffe4) → [`00baffe8`](#insn-00baffe8)
- ブロック [`00baffe8`](#insn-00baffe8) 範囲 `[['00baffe8', '00bafffb']]`
  - `FALL_THROUGH` [`00bafff8`](#insn-00bafff8) → [`00bafffc`](#insn-00bafffc)
- ブロック [`00bafffc`](#insn-00bafffc) 範囲 `[['00bafffc', '00bb0007']]`
  - `CONDITIONAL_JUMP` [`00bb0004`](#insn-00bb0004) → [`00bb0068`](#insn-00bb0068)
  - `FALL_THROUGH` [`00bb0004`](#insn-00bb0004) → [`00bb0008`](#insn-00bb0008)
- ブロック [`00bb0008`](#insn-00bb0008) 範囲 `[['00bb0008', '00bb000b']]`
  - `FALL_THROUGH` [`00bb0008`](#insn-00bb0008) → [`00bb000c`](#insn-00bb000c)
- ブロック [`00bb000c`](#insn-00bb000c) 範囲 `[['00bb000c', '00bb001f']]`
  - `CONDITIONAL_JUMP` [`00bb001c`](#insn-00bb001c) → [`00bb000c`](#insn-00bb000c)
  - `FALL_THROUGH` [`00bb001c`](#insn-00bb001c) → [`00bb0020`](#insn-00bb0020)
- ブロック [`00bb0020`](#insn-00bb0020) 範囲 `[['00bb0020', '00bb0023']]`
  - `FALL_THROUGH` [`00bb0020`](#insn-00bb0020) → [`00bb0024`](#insn-00bb0024)
- ブロック [`00bb0024`](#insn-00bb0024) 範囲 `[['00bb0024', '00bb0037']]`
  - `CONDITIONAL_JUMP` [`00bb0034`](#insn-00bb0034) → [`00bb0024`](#insn-00bb0024)
  - `FALL_THROUGH` [`00bb0034`](#insn-00bb0034) → [`00bb0038`](#insn-00bb0038)
- ブロック [`00bb0038`](#insn-00bb0038) 範囲 `[['00bb0038', '00bb003f']]`
  - `CONDITIONAL_JUMP` [`00bb003c`](#insn-00bb003c) → [`00bb0060`](#insn-00bb0060)
  - `FALL_THROUGH` [`00bb003c`](#insn-00bb003c) → [`00bb0040`](#insn-00bb0040)
- ブロック [`00bb0040`](#insn-00bb0040) 範囲 `[['00bb0040', '00bb005f']]`
  - `UNCONDITIONAL_JUMP` [`00bb005c`](#insn-00bb005c) → [`00bb0008`](#insn-00bb0008)
- ブロック [`00bb0060`](#insn-00bb0060) 範囲 `[['00bb0060', '00bb0067']]`
  - `FALL_THROUGH` [`00bb0064`](#insn-00bb0064) → [`00bb0068`](#insn-00bb0068)
- ブロック [`00bb0068`](#insn-00bb0068) 範囲 `[['00bb0068', '00bb006f']]`
  - `CONDITIONAL_JUMP` [`00bb006c`](#insn-00bb006c) → [`00bb0098`](#insn-00bb0098)
  - `FALL_THROUGH` [`00bb006c`](#insn-00bb006c) → [`00bb0070`](#insn-00bb0070)
- ブロック [`00bb0070`](#insn-00bb0070) 範囲 `[['00bb0070', '00bb0083']]`
  - `CONDITIONAL_JUMP` [`00bb0080`](#insn-00bb0080) → [`00bb0098`](#insn-00bb0098)
  - `FALL_THROUGH` [`00bb0080`](#insn-00bb0080) → [`00bb0084`](#insn-00bb0084)
- ブロック [`00bb0084`](#insn-00bb0084) 範囲 `[['00bb0084', '00bb0097']]`
  - `FALL_THROUGH` [`00bb0094`](#insn-00bb0094) → [`00bb0098`](#insn-00bb0098)
- ブロック [`00bb0098`](#insn-00bb0098) 範囲 `[['00bb0098', '00bb009b']]`
  - `CONDITIONAL_JUMP` [`00bb0098`](#insn-00bb0098) → [`00bb00cc`](#insn-00bb00cc)
  - `FALL_THROUGH` [`00bb0098`](#insn-00bb0098) → [`00bb009c`](#insn-00bb009c)
- ブロック [`00bb009c`](#insn-00bb009c) 範囲 `[['00bb009c', '00bb00c7']]`
  - `CONDITIONAL_JUMP` [`00bb00c4`](#insn-00bb00c4) → [`00bb023c`](#insn-00bb023c)
  - `FALL_THROUGH` [`00bb00c4`](#insn-00bb00c4) → [`00bb00c8`](#insn-00bb00c8)
- ブロック [`00bb00c8`](#insn-00bb00c8) 範囲 `[['00bb00c8', '00bb00cb']]`
  - `CONDITIONAL_JUMP` [`00bb00c8`](#insn-00bb00c8) → [`00bafef8`](#insn-00bafef8)
  - `FALL_THROUGH` [`00bb00c8`](#insn-00bb00c8) → [`00bb00cc`](#insn-00bb00cc)
- ブロック [`00bb00cc`](#insn-00bb00cc) 範囲 `[['00bb00cc', '00bb00db']]`
  - `CONDITIONAL_JUMP` [`00bb00d8`](#insn-00bb00d8) → [`00bb0224`](#insn-00bb0224)
  - `FALL_THROUGH` [`00bb00d8`](#insn-00bb00d8) → [`00bb00dc`](#insn-00bb00dc)
- ブロック [`00bb00dc`](#insn-00bb00dc) 範囲 `[['00bb00dc', '00bb00f3']]`
  - `UNCONDITIONAL_JUMP` [`00bb00f0`](#insn-00bb00f0) → [`00bafef8`](#insn-00bafef8)
- ブロック [`00bb00f4`](#insn-00bb00f4) 範囲 `[['00bb00f4', '00bb010b']]`
  - `CONDITIONAL_JUMP` [`00bb0108`](#insn-00bb0108) → [`00bb01cc`](#insn-00bb01cc)
  - `FALL_THROUGH` [`00bb0108`](#insn-00bb0108) → [`00bb010c`](#insn-00bb010c)
- ブロック [`00bb010c`](#insn-00bb010c) 範囲 `[['00bb010c', '00bb0113']]`
  - `CONDITIONAL_JUMP` [`00bb0110`](#insn-00bb0110) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb0110`](#insn-00bb0110) → [`00bb0114`](#insn-00bb0114)
- ブロック [`00bb0114`](#insn-00bb0114) 範囲 `[['00bb0114', '00bb0117']]`
  - `FALL_THROUGH` [`00bb0114`](#insn-00bb0114) → [`00bb0118`](#insn-00bb0118)
- ブロック [`00bb0118`](#insn-00bb0118) 範囲 `[['00bb0118', '00bb012b']]`
  - `CONDITIONAL_JUMP` [`00bb0128`](#insn-00bb0128) → [`00bb01bc`](#insn-00bb01bc)
  - `FALL_THROUGH` [`00bb0128`](#insn-00bb0128) → [`00bb012c`](#insn-00bb012c)
- ブロック [`00bb012c`](#insn-00bb012c) 範囲 `[['00bb012c', '00bb0137']]`
  - `CONDITIONAL_JUMP` [`00bb0134`](#insn-00bb0134) → [`00bb0118`](#insn-00bb0118)
  - `FALL_THROUGH` [`00bb0134`](#insn-00bb0134) → [`00bb0138`](#insn-00bb0138)
- ブロック [`00bb0138`](#insn-00bb0138) 範囲 `[['00bb0138', '00bb013b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0138`](#insn-00bb0138) → [`00bb0260`](#insn-00bb0260)
- ブロック [`00bb013c`](#insn-00bb013c) 範囲 `[['00bb013c', '00bb013f']]`
  - `CONDITIONAL_JUMP` [`00bb013c`](#insn-00bb013c) → [`00bb01ac`](#insn-00bb01ac)
  - `FALL_THROUGH` [`00bb013c`](#insn-00bb013c) → [`00bb0140`](#insn-00bb0140)
- ブロック [`00bb0140`](#insn-00bb0140) 範囲 `[['00bb0140', '00bb0163']]`
  - `CONDITIONAL_JUMP` [`00bb0160`](#insn-00bb0160) → [`00bb01b4`](#insn-00bb01b4)
  - `FALL_THROUGH` [`00bb0160`](#insn-00bb0160) → [`00bb0164`](#insn-00bb0164)
- ブロック [`00bb0164`](#insn-00bb0164) 範囲 `[['00bb0164', '00bb0177']]`
  - `UNCONDITIONAL_JUMP` [`00bb0174`](#insn-00bb0174) → [`00bb01a4`](#insn-00bb01a4)
- ブロック [`00bb0178`](#insn-00bb0178) 範囲 `[['00bb0178', '00bb0193']]`
  - `CONDITIONAL_JUMP` [`00bb0190`](#insn-00bb0190) → [`00bb01b4`](#insn-00bb01b4)
  - `FALL_THROUGH` [`00bb0190`](#insn-00bb0190) → [`00bb0194`](#insn-00bb0194)
- ブロック [`00bb0194`](#insn-00bb0194) 範囲 `[['00bb0194', '00bb01a3']]`
  - `FALL_THROUGH` [`00bb01a0`](#insn-00bb01a0) → [`00bb01a4`](#insn-00bb01a4)
- ブロック [`00bb01a4`](#insn-00bb01a4) 範囲 `[['00bb01a4', '00bb01ab']]`
  - `UNCONDITIONAL_JUMP` [`00bb01a8`](#insn-00bb01a8) → [`00baff64`](#insn-00baff64)
- ブロック [`00bb01ac`](#insn-00bb01ac) 範囲 `[['00bb01ac', '00bb01b3']]`
  - `UNCONDITIONAL_JUMP` [`00bb01b0`](#insn-00bb01b0) → [`00baff64`](#insn-00baff64)
- ブロック [`00bb01b4`](#insn-00bb01b4) 範囲 `[['00bb01b4', '00bb01bb']]`
  - `UNCONDITIONAL_JUMP` [`00bb01b8`](#insn-00bb01b8) → [`00baff64`](#insn-00baff64)
- ブロック [`00bb01bc`](#insn-00bb01bc) 範囲 `[['00bb01bc', '00bb01cb']]`
  - `FALL_THROUGH` [`00bb01c8`](#insn-00bb01c8) → [`00bb01cc`](#insn-00bb01cc)
- ブロック [`00bb01cc`](#insn-00bb01cc) 範囲 `[['00bb01cc', '00bb01d3']]`
  - `CONDITIONAL_JUMP` [`00bb01d0`](#insn-00bb01d0) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb01d0`](#insn-00bb01d0) → [`00bb01d4`](#insn-00bb01d4)
- ブロック [`00bb01d4`](#insn-00bb01d4) 範囲 `[['00bb01d4', '00bb01d7']]`
  - `FALL_THROUGH` [`00bb01d4`](#insn-00bb01d4) → [`00bb01d8`](#insn-00bb01d8)
- ブロック [`00bb01d8`](#insn-00bb01d8) 範囲 `[['00bb01d8', '00bb01db']]`
  - `FALL_THROUGH` [`00bb01d8`](#insn-00bb01d8) → [`00bb01dc`](#insn-00bb01dc)
- ブロック [`00bb01dc`](#insn-00bb01dc) 範囲 `[['00bb01dc', '00bb01ef']]`
  - `CONDITIONAL_JUMP` [`00bb01ec`](#insn-00bb01ec) → [`00bb01dc`](#insn-00bb01dc)
  - `FALL_THROUGH` [`00bb01ec`](#insn-00bb01ec) → [`00bb01f0`](#insn-00bb01f0)
- ブロック [`00bb01f0`](#insn-00bb01f0) 範囲 `[['00bb01f0', '00bb01f3']]`
  - `FALL_THROUGH` [`00bb01f0`](#insn-00bb01f0) → [`00bb01f4`](#insn-00bb01f4)
- ブロック [`00bb01f4`](#insn-00bb01f4) 範囲 `[['00bb01f4', '00bb0207']]`
  - `CONDITIONAL_JUMP` [`00bb0204`](#insn-00bb0204) → [`00bb01f4`](#insn-00bb01f4)
  - `FALL_THROUGH` [`00bb0204`](#insn-00bb0204) → [`00bb0208`](#insn-00bb0208)
- ブロック [`00bb0208`](#insn-00bb0208) 範囲 `[['00bb0208', '00bb020f']]`
  - `CONDITIONAL_JUMP` [`00bb020c`](#insn-00bb020c) → [`00bafef4`](#insn-00bafef4)
  - `FALL_THROUGH` [`00bb020c`](#insn-00bb020c) → [`00bb0210`](#insn-00bb0210)
- ブロック [`00bb0210`](#insn-00bb0210) 範囲 `[['00bb0210', '00bb0223']]`
  - `UNCONDITIONAL_JUMP` [`00bb0220`](#insn-00bb0220) → [`00bb01d8`](#insn-00bb01d8)
- ブロック [`00bb0224`](#insn-00bb0224) 範囲 `[['00bb0224', '00bb023b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0238`](#insn-00bb0238) → [`00bafee4`](#insn-00bafee4)
- ブロック [`00bb023c`](#insn-00bb023c) 範囲 `[['00bb023c', '00bb0243']]`
  - `CONDITIONAL_JUMP` [`00bb0240`](#insn-00bb0240) → [`00bafee4`](#insn-00bafee4)
  - `FALL_THROUGH` [`00bb0240`](#insn-00bb0240) → [`00bb0244`](#insn-00bb0244)
- ブロック [`00bb0244`](#insn-00bb0244) 範囲 `[['00bb0244', '00bb0247']]`
  - `UNCONDITIONAL_JUMP` [`00bb0244`](#insn-00bb0244) → [`00bb0260`](#insn-00bb0260)
- ブロック [`00bb0248`](#insn-00bb0248) 範囲 `[['00bb0248', '00bb025b']]`
  - `FALL_THROUGH` [`00bb0258`](#insn-00bb0258) → [`00bb025c`](#insn-00bb025c)
- ブロック [`00bb025c`](#insn-00bb025c) 範囲 `[['00bb025c', '00bb025f']]`
  - `COMPUTED_JUMP` [`00bb025c`](#insn-00bb025c) → [`00bb0260`](#insn-00bb0260)
  - `COMPUTED_JUMP` [`00bb025c`](#insn-00bb025c) → [`00bb02a4`](#insn-00bb02a4)
  - `COMPUTED_JUMP` [`00bb025c`](#insn-00bb025c) → [`00bb02cc`](#insn-00bb02cc)
  - `COMPUTED_JUMP` [`00bb025c`](#insn-00bb025c) → [`00bb030c`](#insn-00bb030c)
  - `COMPUTED_JUMP` [`00bb025c`](#insn-00bb025c) → [`00bb033c`](#insn-00bb033c)
- ブロック [`00bb0260`](#insn-00bb0260) 範囲 `[['00bb0260', '00bb027b']]`
- ブロック [`00bb027c`](#insn-00bb027c) 範囲 `[['00bb027c', '00bb02a3']]`
- ブロック [`00bb02a4`](#insn-00bb02a4) 範囲 `[['00bb02a4', '00bb02b7']]`
  - `CONDITIONAL_JUMP` [`00bb02b4`](#insn-00bb02b4) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb02b4`](#insn-00bb02b4) → [`00bb02b8`](#insn-00bb02b8)
- ブロック [`00bb02b8`](#insn-00bb02b8) 範囲 `[['00bb02b8', '00bb02cb']]`
  - `UNCONDITIONAL_JUMP` [`00bb02c8`](#insn-00bb02c8) → [`00bb0260`](#insn-00bb0260)
- ブロック [`00bb02cc`](#insn-00bb02cc) 範囲 `[['00bb02cc', '00bb02f3']]`
  - `CONDITIONAL_JUMP` [`00bb02f0`](#insn-00bb02f0) → [`00bb0370`](#insn-00bb0370)
  - `FALL_THROUGH` [`00bb02f0`](#insn-00bb02f0) → [`00bb02f4`](#insn-00bb02f4)
- ブロック [`00bb02f4`](#insn-00bb02f4) 範囲 `[['00bb02f4', '00bb02fb']]`
  - `CONDITIONAL_JUMP` [`00bb02f8`](#insn-00bb02f8) → [`00bb03a4`](#insn-00bb03a4)
  - `FALL_THROUGH` [`00bb02f8`](#insn-00bb02f8) → [`00bb02fc`](#insn-00bb02fc)
- ブロック [`00bb02fc`](#insn-00bb02fc) 範囲 `[['00bb02fc', '00bb030b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0308`](#insn-00bb0308) → [`00bb0260`](#insn-00bb0260)
- ブロック [`00bb030c`](#insn-00bb030c) 範囲 `[['00bb030c', '00bb033b']]`
- ブロック [`00bb033c`](#insn-00bb033c) 範囲 `[['00bb033c', '00bb036f']]`
- ブロック [`00bb0370`](#insn-00bb0370) 範囲 `[['00bb0370', '00bb0373']]`
  - `CONDITIONAL_JUMP` [`00bb0370`](#insn-00bb0370) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb0370`](#insn-00bb0370) → [`00bb0374`](#insn-00bb0374)
- ブロック [`00bb0374`](#insn-00bb0374) 範囲 `[['00bb0374', '00bb0393']]`
  - `CONDITIONAL_JUMP` [`00bb0390`](#insn-00bb0390) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb0390`](#insn-00bb0390) → [`00bb0394`](#insn-00bb0394)
- ブロック [`00bb0394`](#insn-00bb0394) 範囲 `[['00bb0394', '00bb03a3']]`
  - `UNCONDITIONAL_JUMP` [`00bb03a0`](#insn-00bb03a0) → [`00bb0260`](#insn-00bb0260)
- ブロック [`00bb03a4`](#insn-00bb03a4) 範囲 `[['00bb03a4', '00bb03bb']]`
  - `CONDITIONAL_JUMP` [`00bb03b8`](#insn-00bb03b8) → [`00bb0260`](#insn-00bb0260)
  - `FALL_THROUGH` [`00bb03b8`](#insn-00bb03b8) → [`00bb03bc`](#insn-00bb03bc)
- ブロック [`00bb03bc`](#insn-00bb03bc) 範囲 `[['00bb03bc', '00bb03cf']]`
  - `UNCONDITIONAL_JUMP` [`00bb03cc`](#insn-00bb03cc) → [`00bb0260`](#insn-00bb0260)

## 命令位置別の参照

- [`00bafeb8`](#insn-00bafeb8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafebc`](#insn-00bafebc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec0`](#insn-00bafec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec4`](#insn-00bafec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec8`](#insn-00bafec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafecc`](#insn-00bafecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafef0`](#insn-00bafef0) → [`00bafef8`](#insn-00bafef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff08`](#insn-00baff08) → [`00bb0248`](#insn-00bb0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff10`](#insn-00baff10) → [`00bb027c`](#insn-00bb027c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff2c`](#insn-00baff2c) → [`00baff80`](#insn-00baff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff5c`](#insn-00baff5c) → [`00bb0554`](../00bb0/00bb0554.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb0554` · 推定シンボル `None` · 推定型 `None`
- [`00baff74`](#insn-00baff74) → [`00baffc8`](#insn-00baffc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff7c`](#insn-00baff7c) → [`00bafffc`](#insn-00bafffc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffa8`](#insn-00baffa8) → [`00bb013c`](#insn-00bb013c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffb0`](#insn-00baffb0) → [`00bb0178`](#insn-00bb0178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffc4`](#insn-00baffc4) → [`00baff64`](#insn-00baff64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffd0`](#insn-00baffd0) → [`00bb00f4`](#insn-00bb00f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffe4`](#insn-00baffe4) → [`00baffcc`](#insn-00baffcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0004`](#insn-00bb0004) → [`00bb0068`](#insn-00bb0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb001c`](#insn-00bb001c) → [`00bb000c`](#insn-00bb000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0034`](#insn-00bb0034) → [`00bb0024`](#insn-00bb0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb003c`](#insn-00bb003c) → [`00bb0060`](#insn-00bb0060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb005c`](#insn-00bb005c) → [`00bb0008`](#insn-00bb0008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb006c`](#insn-00bb006c) → [`00bb0098`](#insn-00bb0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0080`](#insn-00bb0080) → [`00bb0098`](#insn-00bb0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0098`](#insn-00bb0098) → [`00bb00cc`](#insn-00bb00cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00a8`](#insn-00bb00a8) → [`00c5de50`](../00c5d/00c5de50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de50` · 推定シンボル `None` · 推定型 `None`
- [`00bb00c0`](#insn-00bb00c0) → [`00c5de50`](../00c5d/00c5de50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de50` · 推定シンボル `None` · 推定型 `None`
- [`00bb00c4`](#insn-00bb00c4) → [`00bb023c`](#insn-00bb023c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00c8`](#insn-00bb00c8) → [`00bafef8`](#insn-00bafef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00d8`](#insn-00bb00d8) → [`00bb0224`](#insn-00bb0224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00e8`](#insn-00bb00e8) → [`00c5de90`](../00c5d/00c5de90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de90` · 推定シンボル `None` · 推定型 `None`
- [`00bb00f0`](#insn-00bb00f0) → [`00bafef8`](#insn-00bafef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0108`](#insn-00bb0108) → [`00bb01cc`](#insn-00bb01cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0110`](#insn-00bb0110) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb0128`](#insn-00bb0128) → [`00bb01bc`](#insn-00bb01bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0134`](#insn-00bb0134) → [`00bb0118`](#insn-00bb0118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0138`](#insn-00bb0138) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb013c`](#insn-00bb013c) → [`00bb01ac`](#insn-00bb01ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0160`](#insn-00bb0160) → [`00bb01b4`](#insn-00bb01b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0174`](#insn-00bb0174) → [`00bb01a4`](#insn-00bb01a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0190`](#insn-00bb0190) → [`00bb01b4`](#insn-00bb01b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb01a8`](#insn-00bb01a8) → [`00baff64`](#insn-00baff64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb01b0`](#insn-00bb01b0) → [`00baff64`](#insn-00baff64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb01b8`](#insn-00bb01b8) → [`00baff64`](#insn-00baff64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb01d0`](#insn-00bb01d0) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb01ec`](#insn-00bb01ec) → [`00bb01dc`](#insn-00bb01dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0204`](#insn-00bb0204) → [`00bb01f4`](#insn-00bb01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb020c`](#insn-00bb020c) → [`00bafef4`](#insn-00bafef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0220`](#insn-00bb0220) → [`00bb01d8`](#insn-00bb01d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0230`](#insn-00bb0230) → [`00c5de90`](../00c5d/00c5de90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de90` · 推定シンボル `None` · 推定型 `None`
- [`00bb0238`](#insn-00bb0238) → [`00bafee4`](#insn-00bafee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0240`](#insn-00bb0240) → [`00bafee4`](#insn-00bafee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0244`](#insn-00bb0244) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb0254`](#insn-00bb0254) → `0030e298`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::switchdataD_0030e298` · 推定型 `byte`
- [`00bb025c`](#insn-00bb025c) → [`00bb0260`](#insn-00bb0260) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb025c`](#insn-00bb025c) → [`00bb02a4`](#insn-00bb02a4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_2` · 推定型 `None`
- [`00bb025c`](#insn-00bb025c) → [`00bb02cc`](#insn-00bb02cc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_3` · 推定型 `None`
- [`00bb025c`](#insn-00bb025c) → [`00bb030c`](#insn-00bb030c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_4` · 推定型 `None`
- [`00bb025c`](#insn-00bb025c) → [`00bb033c`](#insn-00bb033c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_5` · 推定型 `None`
- [`00bb0260`](#insn-00bb0260) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0264`](#insn-00bb0264) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0268`](#insn-00bb0268) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb026c`](#insn-00bb026c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0270`](#insn-00bb0270) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0288`](#insn-00bb0288) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb028c`](#insn-00bb028c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0290`](#insn-00bb0290) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0294`](#insn-00bb0294) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0298`](#insn-00bb0298) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb02a0`](#insn-00bb02a0) → [`00c5dc90`](../00c5d/00c5dc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc90` · 推定シンボル `None` · 推定型 `None`
- [`00bb02b4`](#insn-00bb02b4) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb02c8`](#insn-00bb02c8) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb02f0`](#insn-00bb02f0) → [`00bb0370`](#insn-00bb0370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb02f8`](#insn-00bb02f8) → [`00bb03a4`](#insn-00bb03a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0308`](#insn-00bb0308) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb0320`](#insn-00bb0320) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0324`](#insn-00bb0324) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0328`](#insn-00bb0328) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb032c`](#insn-00bb032c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0330`](#insn-00bb0330) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0338`](#insn-00bb0338) → [`00c5e150`](../00c5e/00c5e150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e150` · 推定シンボル `None` · 推定型 `None`
- [`00bb0354`](#insn-00bb0354) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0358`](#insn-00bb0358) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb035c`](#insn-00bb035c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0360`](#insn-00bb0360) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0364`](#insn-00bb0364) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb036c`](#insn-00bb036c) → [`00bb0554`](../00bb0/00bb0554.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb0554` · 推定シンボル `None` · 推定型 `None`
- [`00bb0370`](#insn-00bb0370) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb0390`](#insn-00bb0390) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb03a0`](#insn-00bb03a0) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb03b8`](#insn-00bb03b8) → [`00bb0260`](#insn-00bb0260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`
- [`00bb03cc`](#insn-00bb03cc) → [`00bb0260`](#insn-00bb0260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bb025c::caseD_0` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafeb8`](#insn-00bafeb8)

~~~json
{
  "source": "00bafeb8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafebc`](#insn-00bafebc)

~~~json
{
  "source": "00bafebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec0`](#insn-00bafec0)

~~~json
{
  "source": "00bafec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec4`](#insn-00bafec4)

~~~json
{
  "source": "00bafec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec8`](#insn-00bafec8)

~~~json
{
  "source": "00bafec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafecc`](#insn-00bafecc)

~~~json
{
  "source": "00bafecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafef0`](#insn-00bafef0)

~~~json
{
  "source": "00bafef0",
  "target": "00bafef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff08`](#insn-00baff08)

~~~json
{
  "source": "00baff08",
  "target": "00bb0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff10`](#insn-00baff10)

~~~json
{
  "source": "00baff10",
  "target": "00bb027c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff2c`](#insn-00baff2c)

~~~json
{
  "source": "00baff2c",
  "target": "00baff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff5c`](#insn-00baff5c)

~~~json
{
  "source": "00baff5c",
  "target": "00bb0554",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baff74`](#insn-00baff74)

~~~json
{
  "source": "00baff74",
  "target": "00baffc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff7c`](#insn-00baff7c)

~~~json
{
  "source": "00baff7c",
  "target": "00bafffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffa8`](#insn-00baffa8)

~~~json
{
  "source": "00baffa8",
  "target": "00bb013c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffb0`](#insn-00baffb0)

~~~json
{
  "source": "00baffb0",
  "target": "00bb0178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffc4`](#insn-00baffc4)

~~~json
{
  "source": "00baffc4",
  "target": "00baff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffd0`](#insn-00baffd0)

~~~json
{
  "source": "00baffd0",
  "target": "00bb00f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffe4`](#insn-00baffe4)

~~~json
{
  "source": "00baffe4",
  "target": "00baffcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0004`](#insn-00bb0004)

~~~json
{
  "source": "00bb0004",
  "target": "00bb0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb001c`](#insn-00bb001c)

~~~json
{
  "source": "00bb001c",
  "target": "00bb000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0034`](#insn-00bb0034)

~~~json
{
  "source": "00bb0034",
  "target": "00bb0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb003c`](#insn-00bb003c)

~~~json
{
  "source": "00bb003c",
  "target": "00bb0060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb005c`](#insn-00bb005c)

~~~json
{
  "source": "00bb005c",
  "target": "00bb0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb006c`](#insn-00bb006c)

~~~json
{
  "source": "00bb006c",
  "target": "00bb0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0080`](#insn-00bb0080)

~~~json
{
  "source": "00bb0080",
  "target": "00bb0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0098`](#insn-00bb0098)

~~~json
{
  "source": "00bb0098",
  "target": "00bb00cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00a8`](#insn-00bb00a8)

~~~json
{
  "source": "00bb00a8",
  "target": "00c5de50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00c0`](#insn-00bb00c0)

~~~json
{
  "source": "00bb00c0",
  "target": "00c5de50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00c4`](#insn-00bb00c4)

~~~json
{
  "source": "00bb00c4",
  "target": "00bb023c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00c8`](#insn-00bb00c8)

~~~json
{
  "source": "00bb00c8",
  "target": "00bafef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00d8`](#insn-00bb00d8)

~~~json
{
  "source": "00bb00d8",
  "target": "00bb0224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00e8`](#insn-00bb00e8)

~~~json
{
  "source": "00bb00e8",
  "target": "00c5de90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00f0`](#insn-00bb00f0)

~~~json
{
  "source": "00bb00f0",
  "target": "00bafef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0108`](#insn-00bb0108)

~~~json
{
  "source": "00bb0108",
  "target": "00bb01cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0110`](#insn-00bb0110)

~~~json
{
  "source": "00bb0110",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0128`](#insn-00bb0128)

~~~json
{
  "source": "00bb0128",
  "target": "00bb01bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0134`](#insn-00bb0134)

~~~json
{
  "source": "00bb0134",
  "target": "00bb0118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0138`](#insn-00bb0138)

~~~json
{
  "source": "00bb0138",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb013c`](#insn-00bb013c)

~~~json
{
  "source": "00bb013c",
  "target": "00bb01ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0160`](#insn-00bb0160)

~~~json
{
  "source": "00bb0160",
  "target": "00bb01b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0174`](#insn-00bb0174)

~~~json
{
  "source": "00bb0174",
  "target": "00bb01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0190`](#insn-00bb0190)

~~~json
{
  "source": "00bb0190",
  "target": "00bb01b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb01a8`](#insn-00bb01a8)

~~~json
{
  "source": "00bb01a8",
  "target": "00baff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb01b0`](#insn-00bb01b0)

~~~json
{
  "source": "00bb01b0",
  "target": "00baff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb01b8`](#insn-00bb01b8)

~~~json
{
  "source": "00bb01b8",
  "target": "00baff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb01d0`](#insn-00bb01d0)

~~~json
{
  "source": "00bb01d0",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb01ec`](#insn-00bb01ec)

~~~json
{
  "source": "00bb01ec",
  "target": "00bb01dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0204`](#insn-00bb0204)

~~~json
{
  "source": "00bb0204",
  "target": "00bb01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb020c`](#insn-00bb020c)

~~~json
{
  "source": "00bb020c",
  "target": "00bafef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0220`](#insn-00bb0220)

~~~json
{
  "source": "00bb0220",
  "target": "00bb01d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0230`](#insn-00bb0230)

~~~json
{
  "source": "00bb0230",
  "target": "00c5de90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0238`](#insn-00bb0238)

~~~json
{
  "source": "00bb0238",
  "target": "00bafee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0240`](#insn-00bb0240)

~~~json
{
  "source": "00bb0240",
  "target": "00bafee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0244`](#insn-00bb0244)

~~~json
{
  "source": "00bb0244",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0254`](#insn-00bb0254)

~~~json
{
  "source": "00bb0254",
  "target": "0030e298",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e298",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e298",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb025c`](#insn-00bb025c)

~~~json
{
  "source": "00bb025c",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb025c`](#insn-00bb025c)

~~~json
{
  "source": "00bb025c",
  "target": "00bb02a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb025c`](#insn-00bb025c)

~~~json
{
  "source": "00bb025c",
  "target": "00bb02cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb025c`](#insn-00bb025c)

~~~json
{
  "source": "00bb025c",
  "target": "00bb030c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb025c`](#insn-00bb025c)

~~~json
{
  "source": "00bb025c",
  "target": "00bb033c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0260`](#insn-00bb0260)

~~~json
{
  "source": "00bb0260",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0264`](#insn-00bb0264)

~~~json
{
  "source": "00bb0264",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0268`](#insn-00bb0268)

~~~json
{
  "source": "00bb0268",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb026c`](#insn-00bb026c)

~~~json
{
  "source": "00bb026c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0270`](#insn-00bb0270)

~~~json
{
  "source": "00bb0270",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0288`](#insn-00bb0288)

~~~json
{
  "source": "00bb0288",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb028c`](#insn-00bb028c)

~~~json
{
  "source": "00bb028c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0290`](#insn-00bb0290)

~~~json
{
  "source": "00bb0290",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0294`](#insn-00bb0294)

~~~json
{
  "source": "00bb0294",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0298`](#insn-00bb0298)

~~~json
{
  "source": "00bb0298",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb02a0`](#insn-00bb02a0)

~~~json
{
  "source": "00bb02a0",
  "target": "00c5dc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb02b4`](#insn-00bb02b4)

~~~json
{
  "source": "00bb02b4",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb02c8`](#insn-00bb02c8)

~~~json
{
  "source": "00bb02c8",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb02f0`](#insn-00bb02f0)

~~~json
{
  "source": "00bb02f0",
  "target": "00bb0370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb02f8`](#insn-00bb02f8)

~~~json
{
  "source": "00bb02f8",
  "target": "00bb03a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0308`](#insn-00bb0308)

~~~json
{
  "source": "00bb0308",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0320`](#insn-00bb0320)

~~~json
{
  "source": "00bb0320",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0324`](#insn-00bb0324)

~~~json
{
  "source": "00bb0324",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0328`](#insn-00bb0328)

~~~json
{
  "source": "00bb0328",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb032c`](#insn-00bb032c)

~~~json
{
  "source": "00bb032c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0330`](#insn-00bb0330)

~~~json
{
  "source": "00bb0330",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0338`](#insn-00bb0338)

~~~json
{
  "source": "00bb0338",
  "target": "00c5e150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0354`](#insn-00bb0354)

~~~json
{
  "source": "00bb0354",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0358`](#insn-00bb0358)

~~~json
{
  "source": "00bb0358",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb035c`](#insn-00bb035c)

~~~json
{
  "source": "00bb035c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0360`](#insn-00bb0360)

~~~json
{
  "source": "00bb0360",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0364`](#insn-00bb0364)

~~~json
{
  "source": "00bb0364",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb036c`](#insn-00bb036c)

~~~json
{
  "source": "00bb036c",
  "target": "00bb0554",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0370`](#insn-00bb0370)

~~~json
{
  "source": "00bb0370",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0390`](#insn-00bb0390)

~~~json
{
  "source": "00bb0390",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb03a0`](#insn-00bb03a0)

~~~json
{
  "source": "00bb03a0",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb03b8`](#insn-00bb03b8)

~~~json
{
  "source": "00bb03b8",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb03cc`](#insn-00bb03cc)

~~~json
{
  "source": "00bb03cc",
  "target": "00bb0260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
