# 00bafeb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "302770a58ca522b40726bcfef82d003f3552741ec4758613d5ecd651a2b62f44"
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
