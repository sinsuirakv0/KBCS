# 00bebbe4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bebbe4",
  "name": "FUN_00bebbe4",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "65312db5a39fe3181047b0a1a04082fe8ff00ec24431f361275dff9074fef7e3",
  "source_text_sha256": "65312db5a39fe3181047b0a1a04082fe8ff00ec24431f361275dff9074fef7e3"
}
~~~

## 呼び出し元

- [00be5088](../00be5/00be5088.md)

## 呼び出し先

- [00bebe84](../00beb/00bebe84.md)

## 疑似コード / UTF-8 4030 bytes

~~~c

bool FUN_00bebbe4(uint *param_1,uint *param_2)

{
  uint uVar1;
  long lVar2;
  uint uVar3;
  uint uVar4;
  ulong uVar5;
  int iVar6;
  uint uVar7;
  uint *puVar8;
  long lVar9;
  uint uVar10;
  uint *puVar11;
  uint *puVar12;
  long lVar13;
  uint *puVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 2;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      uVar4 = *param_1;
      uVar10 = param_1[1];
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
      goto LAB_00bebe58;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00bebe84(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bebc74;
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
        goto joined_r0x00bebdf0;
      }
    }
    else {
      uVar7 = uVar1;
      if (uVar10 <= uVar1) goto LAB_00bebe08;
      *puVar12 = uVar1;
      *puVar8 = uVar10;
      puVar14 = puVar12;
      uVar3 = uVar10;
joined_r0x00bebdf0:
      uVar7 = uVar10;
      if (uVar4 <= uVar1) goto LAB_00bebe08;
    }
    *puVar11 = uVar1;
    *puVar14 = uVar4;
    uVar7 = uVar3;
LAB_00bebe08:
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
LAB_00bebe58:
    param_2[-1] = uVar4;
    return true;
  }
LAB_00bebc74:
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
      goto joined_r0x00bebd44;
    }
  }
  else {
    if (uVar10 <= uVar1) goto LAB_00bebd50;
    *puVar8 = uVar1;
    *puVar12 = uVar10;
    puVar14 = puVar8;
joined_r0x00bebd44:
    if (uVar4 <= uVar1) goto LAB_00bebd50;
  }
  *puVar11 = uVar1;
  *puVar14 = uVar4;
LAB_00bebd50:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 0xc;
    puVar11 = param_1 + 3;
    do {
      puVar8 = puVar11;
      uVar4 = *puVar8;
      uVar10 = *puVar12;
      lVar13 = lVar9;
      if (uVar4 < uVar10) {
        do {
          lVar2 = lVar13 + -4;
          *(uint *)((long)param_1 + lVar13) = uVar10;
          puVar11 = param_1;
          if (lVar2 == 0) goto LAB_00bebd6c;
          uVar10 = *(uint *)((long)param_1 + lVar13 + -8);
          lVar13 = lVar2;
        } while (uVar4 < uVar10);
        puVar11 = (uint *)((long)param_1 + lVar2);
LAB_00bebd6c:
        iVar6 = iVar6 + 1;
        *puVar11 = uVar4;
        if (iVar6 == 8) {
          return puVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 4;
      puVar11 = puVar8 + 1;
      puVar12 = puVar8;
    } while (puVar8 + 1 != param_2);
  }
  return true;
}

~~~
