# 00beae3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00beae3c",
  "name": "FUN_00beae3c",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d1aafcb64aeaeab9acee9ec736366369bbacc0bf842e4ca385b91aeb41feb22",
  "source_text_sha256": "5d1aafcb64aeaeab9acee9ec736366369bbacc0bf842e4ca385b91aeb41feb22"
}
~~~

## 呼び出し元

- [00be4234](../00be4/00be4234.md)

## 呼び出し先

- [00beb0fc](../00beb/00beb0fc.md)

## 疑似コード / UTF-8 4056 bytes

~~~c

bool FUN_00beae3c(ushort *param_1,ushort *param_2)

{
  ushort uVar1;
  long lVar2;
  ushort uVar3;
  ushort uVar4;
  ulong uVar5;
  int iVar6;
  ushort uVar7;
  ushort *puVar8;
  long lVar9;
  ushort uVar10;
  ushort *puVar11;
  ushort *puVar12;
  long lVar13;
  ushort *puVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 1;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      uVar10 = param_1[1];
      uVar4 = *param_1;
      uVar1 = param_2[-1];
      if (uVar4 <= uVar10) {
        if (uVar10 <= uVar1) {
          return true;
        }
        param_1[1] = uVar1;
        param_2[-1] = uVar10;
        uVar4 = *param_1;
        if (param_1[1] < uVar4) {
          *param_1 = param_1[1];
          param_1[1] = uVar4;
          return true;
        }
        return true;
      }
      if (uVar1 < uVar10) {
        *param_1 = uVar1;
      }
      else {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        if (uVar4 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00beb0d0;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00beb0fc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beaed0;
    }
    uVar4 = *param_1;
    puVar12 = param_1 + 1;
    uVar10 = *puVar12;
    puVar8 = param_1 + 2;
    uVar1 = *puVar8;
    puVar11 = param_1;
    if (uVar10 < uVar4) {
      puVar14 = puVar8;
      uVar3 = uVar4;
      if (uVar10 <= uVar1) {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        uVar10 = uVar1;
        puVar11 = puVar12;
        goto joined_r0x00beb05c;
      }
    }
    else {
      uVar7 = uVar1;
      if (uVar10 <= uVar1) goto LAB_00beb074;
      *puVar12 = uVar1;
      *puVar8 = uVar10;
      puVar14 = puVar12;
      uVar3 = uVar10;
joined_r0x00beb05c:
      uVar7 = uVar10;
      if (uVar4 <= uVar1) goto LAB_00beb074;
    }
    *puVar11 = uVar1;
    *puVar14 = uVar4;
    uVar7 = uVar3;
LAB_00beb074:
    if (uVar7 <= param_2[-1]) {
      return true;
    }
    *puVar8 = param_2[-1];
    param_2[-1] = uVar7;
    uVar4 = *puVar8;
    uVar10 = *puVar12;
    if (uVar4 < uVar10) {
      uVar1 = *param_1;
      param_1[1] = uVar4;
      param_1[2] = uVar10;
      if (uVar4 < uVar1) {
        *param_1 = uVar4;
        param_1[1] = uVar1;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar5 < 2) {
    return true;
  }
  if (uVar5 == 2) {
    uVar4 = *param_1;
    if (uVar4 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00beb0d0:
    param_2[-1] = uVar4;
    return true;
  }
LAB_00beaed0:
  uVar4 = *param_1;
  puVar8 = param_1 + 1;
  uVar10 = *puVar8;
  puVar12 = param_1 + 2;
  uVar1 = *puVar12;
  puVar11 = param_1;
  if (uVar10 < uVar4) {
    puVar14 = puVar12;
    if (uVar10 <= uVar1) {
      *param_1 = uVar10;
      param_1[1] = uVar4;
      puVar11 = puVar8;
      goto joined_r0x00beafb0;
    }
  }
  else {
    if (uVar10 <= uVar1) goto LAB_00beafbc;
    *puVar8 = uVar1;
    *puVar12 = uVar10;
    puVar14 = puVar8;
joined_r0x00beafb0:
    if (uVar4 <= uVar1) goto LAB_00beafbc;
  }
  *puVar11 = uVar1;
  *puVar14 = uVar4;
LAB_00beafbc:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 6;
    puVar11 = param_1 + 3;
    do {
      puVar8 = puVar11;
      uVar4 = *puVar8;
      uVar10 = *puVar12;
      lVar13 = lVar9;
      if (uVar4 < uVar10) {
        do {
          lVar2 = lVar13 + -2;
          *(ushort *)((long)param_1 + lVar13) = uVar10;
          puVar11 = param_1;
          if (lVar2 == 0) goto LAB_00beafd8;
          uVar10 = *(ushort *)((long)param_1 + lVar13 + -4);
          lVar13 = lVar2;
        } while (uVar4 < uVar10);
        puVar11 = (ushort *)((long)param_1 + lVar2);
LAB_00beafd8:
        iVar6 = iVar6 + 1;
        *puVar11 = uVar4;
        if (iVar6 == 8) {
          return puVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 2;
      puVar11 = puVar8 + 1;
      puVar12 = puVar8;
    } while (puVar8 + 1 != param_2);
  }
  return true;
}

~~~
