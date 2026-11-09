# 005cebdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005cebdc",
  "name": "FUN_005cebdc",
  "size": 864,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dd083a7170e688349530cb757efe52d5f2d7df68324f3c75467748f3b8a04d9",
  "source_text_sha256": "7dd083a7170e688349530cb757efe52d5f2d7df68324f3c75467748f3b8a04d9"
}
~~~

## 呼び出し元

- [005ce48c](../005ce/005ce48c.md)
- [005ce52c](../005ce/005ce52c.md)
- [005d582c](../005d5/005d582c.md)

## 呼び出し先

- [005d4b08](../005d4/005d4b08.md)
- [005d4c48](../005d4/005d4c48.md)
- [005d4c94](../005d4/005d4c94.md)

## 疑似コード / UTF-8 3928 bytes

~~~c

byte * FUN_005cebdc(long param_1,byte *param_2,byte *param_3,undefined8 param_4,undefined4 param_5,
                   undefined4 param_6)

{
  uint uVar1;
  byte bVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  long lVar6;
  undefined8 uVar7;
  uint uVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *pbVar11;
  
  if (param_2 == param_3) {
    return param_2;
  }
  bVar2 = *param_2;
  uVar1 = *(uint *)(param_1 + 0x18) & 0x1f0;
  if (bVar2 < 0x3f) {
    if (bVar2 == 0x2a) {
      pbVar11 = param_2 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        pbVar11 = param_2 + 2;
        lVar5 = 0;
LAB_005ced60:
        lVar6 = -1;
LAB_005ced98:
        uVar7 = 0;
        goto LAB_005cef20;
      }
      lVar5 = 0;
    }
    else {
      if (bVar2 != 0x2b) {
        return param_2;
      }
      pbVar11 = param_2 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        pbVar11 = param_2 + 2;
        lVar5 = 1;
        goto LAB_005ced60;
      }
      lVar5 = 1;
    }
LAB_005cedbc:
    lVar6 = -1;
  }
  else if (bVar2 == 0x3f) {
    pbVar11 = param_2 + 1;
    if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
      pbVar11 = param_2 + 2;
      lVar5 = 0;
      lVar6 = 1;
      goto LAB_005ced98;
    }
    lVar5 = 0;
    lVar6 = 1;
  }
  else {
    if (bVar2 != 0x7b) {
      return param_2;
    }
    pbVar11 = param_2 + 1;
    if ((pbVar11 == param_3) ||
       ((bVar2 = *pbVar11, (bVar2 & 0xf8) != 0x30 && ((bVar2 & 0xfe) != 0x38)))) {
LAB_005cef34:
                    /* WARNING: Subroutine does not return */
      FUN_005d4c48();
    }
    uVar8 = (uint)bVar2;
    for (param_2 = param_2 + 2;
        (iVar3 = uVar8 - 0x30, pbVar9 = param_3, param_2 != param_3 &&
        ((bVar2 = *param_2, (bVar2 & 0xf8) == 0x30 || (pbVar9 = param_2, (bVar2 & 0xfe) == 0x38))));
        param_2 = param_2 + 1) {
      if (0xccccccb < iVar3) goto LAB_005cef34;
      uVar8 = (uint)bVar2 + iVar3 * 10;
    }
    if (pbVar9 == pbVar11) goto LAB_005cef34;
    if (pbVar9 == param_3) goto LAB_005cef38;
    if (*pbVar9 == 0x2c) {
      pbVar11 = pbVar9 + 1;
      if (pbVar11 == param_3) goto LAB_005cef34;
      bVar2 = *pbVar11;
      if (bVar2 == 0x7d) {
        pbVar11 = pbVar9 + 2;
        if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
          lVar5 = (long)iVar3;
          pbVar11 = pbVar9 + 3;
          goto LAB_005ced60;
        }
        lVar5 = (long)iVar3;
        goto LAB_005cedbc;
      }
      uVar8 = (uint)bVar2;
      if (((bVar2 & 0xf8) != 0x30) && ((uVar8 & 0xfe) != 0x38)) {
LAB_005cef38:
                    /* WARNING: Subroutine does not return */
        FUN_005d4c94();
      }
      for (pbVar9 = pbVar9 + 2;
          (iVar4 = uVar8 - 0x30, pbVar10 = param_3, pbVar9 != param_3 &&
          ((bVar2 = *pbVar9, (bVar2 & 0xf8) == 0x30 || (pbVar10 = pbVar9, (bVar2 & 0xfe) == 0x38))))
          ; pbVar9 = pbVar9 + 1) {
        if (0xccccccb < iVar4) goto LAB_005cef34;
        uVar8 = (uint)bVar2 + iVar4 * 10;
      }
      if (((pbVar10 == pbVar11) || (pbVar10 == param_3)) || (*pbVar10 != 0x7d)) goto LAB_005cef38;
      if (iVar4 < iVar3) goto LAB_005cef34;
      pbVar11 = pbVar10 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        lVar5 = (long)iVar3;
        lVar6 = (long)iVar4;
        pbVar11 = pbVar10 + 2;
        goto LAB_005ced98;
      }
      lVar5 = (long)iVar3;
      lVar6 = (long)iVar4;
    }
    else {
      if (*pbVar9 != 0x7d) goto LAB_005cef34;
      pbVar11 = pbVar9 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        lVar5 = (long)iVar3;
        pbVar11 = pbVar9 + 2;
        lVar6 = lVar5;
        goto LAB_005ced98;
      }
      lVar5 = (long)iVar3;
      lVar6 = lVar5;
    }
  }
  uVar7 = 1;
LAB_005cef20:
  FUN_005d4b08(param_1,lVar5,lVar6,param_4,param_5,param_6,uVar7);
  return pbVar11;
}

~~~
