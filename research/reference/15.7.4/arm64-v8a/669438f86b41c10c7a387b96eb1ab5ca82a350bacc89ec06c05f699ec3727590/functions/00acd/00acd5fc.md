# 00acd5fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00acd4f0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd4f0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00acd5fc",
  "name": "FUN_00acd5fc",
  "size": 508,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f8813b9b84fba773d9703e789bfdbb270512179b49dd1bdcbcb7d792b34b132",
  "source_text_sha256": "2f8813b9b84fba773d9703e789bfdbb270512179b49dd1bdcbcb7d792b34b132"
}
~~~

## 呼び出し元

- [00acc598](../00acc/00acc598.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00acd800](../00acd/00acd800.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード / UTF-8 3402 bytes

~~~c

long FUN_00acd5fc(long *param_1,long *param_2)

{
  ulong uVar1;
  long *plVar2;
  void *__ptr;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long lVar8;
  ulong uVar9;
  long lVar10;
  long *plVar11;
  long lVar12;
  long *plVar13;
  
  plVar13 = (long *)*param_1;
  plVar11 = (long *)param_1[1];
  lVar12 = (long)plVar11 - (long)plVar13;
  lVar3 = lVar12 >> 4;
  uVar1 = lVar3 * -0x5555555555555555 + 1;
  if (0x555555555555555 < uVar1) {
    FUN_00acd800(param_1);
LAB_00acd7f4:
                    /* WARNING: Subroutine does not return */
    FUN_0041e380();
  }
  lVar8 = param_1[2] - (long)plVar13 >> 4;
  uVar9 = lVar8 * 0x5555555555555556;
  if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
    uVar9 = uVar1;
  }
  if (0x2aaaaaaaaaaaaa9 < (ulong)(lVar8 * -0x5555555555555555)) {
    uVar9 = 0x555555555555555;
  }
  if (uVar9 == 0) {
    lVar8 = 0;
  }
  else {
    if (0x555555555555555 < uVar9) goto LAB_00acd7f4;
    lVar8 = _Znwm(uVar9 * 0x30);
  }
  lVar10 = lVar8 + lVar3 * 0x10;
  plVar2 = param_2 + 4;
  plVar5 = (long *)*plVar2;
  if (plVar5 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00accb6c with catch @ 00acd6c0 */
    plVar2 = (long *)(lVar10 + 0x20);
LAB_00acd6c4:
                    /* catch() { ... } // from try @ 00accaec with catch @ 00acd6c4 */
    *plVar2 = 0;
                    /* catch() { ... } // from try @ 00acca7c with catch @ 00acd6c8 */
                    /* catch() { ... } // from try @ 00acca74 with catch @ 00acd6cc */
    if (plVar13 == plVar11) goto LAB_00acd7ac;
  }
  else {
    if (plVar5 != param_2) {
      *(long **)(lVar10 + 0x20) = plVar5;
      goto LAB_00acd6c4;
    }
    lVar12 = *param_2;
    *(long *)(lVar10 + 0x20) = lVar10;
                    /* catch() { ... } // from try @ 00acc0ac with catch @ 00acd6e0 */
                    /* catch() { ... } // from try @ 00acc0bc with catch @ 00acd6e8 */
    (**(code **)(lVar12 + 0x18))(param_2,lVar10);
    plVar13 = (long *)*param_1;
    plVar11 = (long *)param_1[1];
    lVar12 = (long)plVar11 - (long)plVar13;
    if (plVar13 == plVar11) goto LAB_00acd7ac;
  }
                    /* catch() { ... } // from try @ 00acacb0 with catch @ 00acd710 */
  plVar2 = (long *)(lVar3 * 0x10 + (lVar12 >> 4) * -0x10 + lVar8 + 0x20);
  plVar5 = plVar13;
  do {
    plVar4 = plVar5 + 4;
    plVar6 = (long *)*plVar4;
    plVar7 = plVar2;
    if (plVar6 == (long *)0x0) {
LAB_00acd72c:
      *plVar7 = 0;
    }
    else {
      if (plVar5 != plVar6) {
                    /* catch() { ... } // from try @ 00aca7d4 with catch @ 00acd728 */
        *plVar2 = (long)plVar6;
        plVar7 = plVar4;
        goto LAB_00acd72c;
      }
      *plVar2 = (long)(plVar2 + -4);
      (**(code **)(*(long *)*plVar4 + 0x18))();
    }
    plVar5 = plVar5 + 6;
    plVar2 = plVar2 + 6;
  } while (plVar5 != plVar11);
  do {
    plVar2 = (long *)plVar13[4];
    if (plVar13 == plVar2) {
      lVar3 = 0x20;
      plVar2 = plVar13;
LAB_00acd77c:
      (**(code **)(*plVar2 + lVar3))();
    }
    else if (plVar2 != (long *)0x0) {
      lVar3 = 0x28;
      goto LAB_00acd77c;
    }
    plVar13 = plVar13 + 6;
  } while (plVar13 != plVar11);
LAB_00acd7ac:
  __ptr = (void *)*param_1;
  *param_1 = lVar10 - lVar12;
  param_1[1] = lVar10 + 0x30;
  param_1[2] = lVar8 + uVar9 * 0x30;
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
  }
  return lVar10 + 0x30;
}

~~~
