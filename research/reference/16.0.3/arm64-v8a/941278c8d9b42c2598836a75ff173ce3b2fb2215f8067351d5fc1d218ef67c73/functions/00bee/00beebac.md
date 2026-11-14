# 00beebac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00beebac",
  "name": "FUN_00beebac",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16c0bfdb5a054746e8bc483993d9729f218c1e7569eb0d9be8521aec2dee3651",
  "source_text_sha256": "16c0bfdb5a054746e8bc483993d9729f218c1e7569eb0d9be8521aec2dee3651"
}
~~~

## 呼び出し元

- [00be81a0](../00be8/00be81a0.md)

## 呼び出し先

- [00beee4c](../00bee/00beee4c.md)

## 疑似コード / UTF-8 4555 bytes

~~~c

bool FUN_00beebac(ulong *param_1,ulong *param_2)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  int iVar4;
  ulong uVar5;
  ulong *puVar6;
  long lVar7;
  ulong uVar8;
  ulong *puVar9;
  ulong *puVar10;
  ulong uVar11;
  long lVar12;
  ulong *puVar13;
  
  uVar3 = (long)param_2 - (long)param_1 >> 3;
  if (2 < (long)uVar3) {
    if (uVar3 == 3) {
      uVar3 = *param_1;
      uVar5 = param_1[1];
      uVar11 = param_2[-1];
      if (uVar3 <= uVar5) {
        if (uVar5 <= uVar11) {
          return true;
        }
        param_1[1] = uVar11;
        param_2[-1] = uVar5;
        uVar3 = *param_1;
        if (param_1[1] < uVar3) {
          *param_1 = param_1[1];
          param_1[1] = uVar3;
          return true;
        }
        return true;
      }
      if (uVar11 < uVar5) {
        *param_1 = uVar11;
      }
      else {
        *param_1 = uVar5;
        param_1[1] = uVar3;
        if (uVar3 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00beee20;
    }
    if (uVar3 != 4) {
      if (uVar3 == 5) {
        FUN_00beee4c(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beec3c;
    }
    uVar5 = *param_1;
    puVar10 = param_1 + 1;
    uVar3 = *puVar10;
    puVar6 = param_1 + 2;
    uVar11 = *puVar6;
    puVar9 = param_1;
    if (uVar3 < uVar5) {
      uVar2 = uVar5;
      puVar13 = puVar6;
                    /* try { // try from 00beeca8 to 00ceecaf has its CatchHandler @ 00beed00 */
      if (uVar3 <= uVar11) {
                    /* try { // try from 00beecb0 to 00ceedf3 has its CatchHandler @ 00bee9e0 */
        *param_1 = uVar3;
        param_1[1] = uVar5;
        uVar3 = uVar11;
        puVar9 = puVar10;
        goto joined_r0x00beedb8;
      }
    }
    else {
      uVar8 = uVar11;
      if (uVar3 <= uVar11) goto LAB_00beedd0;
      *puVar10 = uVar11;
      *puVar6 = uVar3;
      puVar13 = puVar10;
      uVar2 = uVar3;
joined_r0x00beedb8:
      uVar8 = uVar3;
      if (uVar5 <= uVar11) goto LAB_00beedd0;
    }
    *puVar9 = uVar11;
    *puVar13 = uVar5;
    uVar8 = uVar2;
LAB_00beedd0:
                    /* catch() { ... } // from try @ 00beea90 with catch @ 00beedd4 */
    if (uVar8 <= param_2[-1]) {
      return true;
    }
    *puVar6 = param_2[-1];
    param_2[-1] = uVar8;
    uVar5 = *puVar6;
    uVar3 = *puVar10;
    if (uVar5 < uVar3) {
      uVar11 = *param_1;
      param_1[1] = uVar5;
      param_1[2] = uVar3;
      if (uVar5 < uVar11) {
        *param_1 = uVar5;
        param_1[1] = uVar11;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar3 < 2) {
    return true;
  }
  if (uVar3 == 2) {
    uVar3 = *param_1;
    if (uVar3 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00beee20:
    param_2[-1] = uVar3;
    return true;
  }
LAB_00beec3c:
  uVar3 = *param_1;
  puVar6 = param_1 + 1;
  uVar11 = *puVar6;
  puVar10 = param_1 + 2;
  uVar5 = *puVar10;
  puVar9 = param_1;
  if (uVar11 < uVar3) {
    puVar13 = puVar10;
    if (uVar11 <= uVar5) {
      *param_1 = uVar11;
      param_1[1] = uVar3;
      puVar9 = puVar6;
      goto joined_r0x00beed0c;
    }
  }
  else {
    if (uVar11 <= uVar5) goto LAB_00beed18;
                    /* catch() { ... } // from try @ 00beeca8 with catch @ 00beed00 */
    *puVar6 = uVar5;
    *puVar10 = uVar11;
    puVar13 = puVar6;
joined_r0x00beed0c:
    if (uVar3 <= uVar5) goto LAB_00beed18;
  }
  *puVar9 = uVar5;
  *puVar13 = uVar3;
LAB_00beed18:
  if (param_1 + 3 != param_2) {
    iVar4 = 0;
    lVar7 = 0x18;
    puVar9 = param_1 + 3;
    do {
      puVar6 = puVar9;
      uVar5 = *puVar6;
      uVar3 = *puVar10;
      lVar12 = lVar7;
      if (uVar5 < uVar3) {
        do {
          lVar1 = lVar12 + -8;
          *(ulong *)((long)param_1 + lVar12) = uVar3;
          puVar9 = param_1;
          if (lVar1 == 0) goto LAB_00beed34;
          uVar3 = *(ulong *)((long)param_1 + lVar12 + -0x10);
          lVar12 = lVar1;
        } while (uVar5 < uVar3);
        puVar9 = (ulong *)((long)param_1 + lVar1);
LAB_00beed34:
        iVar4 = iVar4 + 1;
                    /* catch() { ... } // from try @ 00beea84 with catch @ 00beed38 */
        *puVar9 = uVar5;
        if (iVar4 == 8) {
          return puVar6 + 1 == param_2;
        }
      }
                    /* catch() { ... } // from try @ 00beeacc with catch @ 00beed48 */
      lVar7 = lVar7 + 8;
      puVar9 = puVar6 + 1;
      puVar10 = puVar6;
    } while (puVar6 + 1 != param_2);
  }
  return true;
}

~~~
