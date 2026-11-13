# 00baeec4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "92b3ffa6532cff7e56f783344de888cf77e679b2beee79cc02ec4c122e7d88e4"
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
