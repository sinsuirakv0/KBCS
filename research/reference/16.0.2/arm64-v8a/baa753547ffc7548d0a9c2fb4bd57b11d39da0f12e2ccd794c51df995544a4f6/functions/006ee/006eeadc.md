# 006eeadc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006eeadc",
  "name": "FUN_006eeadc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea308394b9be220edcabf06fb329efbae43f7c889698e383ecbbec128a7ec67e",
  "source_text_sha256": "ea308394b9be220edcabf06fb329efbae43f7c889698e383ecbbec128a7ec67e"
}
~~~

## 呼び出し元

- [006eed04](../006ee/006eed04.md)

## 呼び出し先

- [0046d7f0](../0046d/0046d7f0.md)
- [006e4440](../006e4/006e4440.md)
- [006e4b1c](../006e4/006e4b1c.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 2245 bytes

~~~c

int FUN_006eeadc(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  int iVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  int iVar12;
  int iVar13;
  
  uVar7 = FUN_0046d7f0(10000);
  uVar8 = FUN_006e4b1c(uVar7,*(undefined4 *)(param_1 + 0x1f88),7);
  iVar3 = FUN_006e4b1c(uVar8,*(undefined4 *)(param_1 + 0x1f88),7);
  uVar4 = FUN_006e4440();
  lVar9 = FUN_00851550();
  if (uVar4 < 0x47) {
    lVar9 = FUN_00851550();
    iVar5 = *(int *)(BYTE_ARRAY_0043ade1 + lVar9 + (ulong)uVar4 * 4 + 0x13);
  }
  else {
    iVar5 = 0;
  }
  iVar12 = 0;
  iVar13 = 0;
  iVar1 = 0;
  if (iVar5 + iVar3 != 0) {
    iVar1 = ((int)uVar8 * 100) / (iVar5 + iVar3);
  }
  iVar3 = 0x12;
  do {
    uVar8 = FUN_006e4b1c(lVar9,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -9);
    uVar10 = FUN_006e4b1c(uVar8,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -10);
    iVar2 = (int)uVar10;
    iVar5 = FUN_006e4b1c(uVar10,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -6);
    lVar9 = FUN_00851550();
    iVar5 = (*(int *)(BYTE_ARRAY_0043a5a9 + lVar9 + (long)*(int *)(param_1 + 0x1f9c) * 0x10 + 0x2f)
            * iVar5) / 100;
    if (iVar3 == 0x2a) {
      if ((int)uVar8 == 0x16) {
LAB_006eec40:
        iVar5 = (iVar5 + iVar2) * iVar1;
LAB_006eec58:
        iVar5 = iVar5 / 100;
      }
      else {
        iVar5 = iVar5 + iVar2;
      }
      iVar13 = iVar5 + iVar13;
    }
    else {
      uVar10 = FUN_006e4b1c(lVar9,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -3);
      uVar11 = FUN_006e4b1c(uVar10,*(undefined4 *)(param_1 + 0x1f88),iVar3 + -4);
      iVar6 = FUN_006e4b1c(uVar11,*(undefined4 *)(param_1 + 0x1f88),iVar3);
      lVar9 = FUN_00851550();
      if ((int)uVar8 == 0x16) goto LAB_006eec40;
      iVar13 = iVar5 + iVar2 + iVar13;
      if ((int)uVar10 == 0x16) {
        iVar5 = ((*(int *)(BYTE_ARRAY_0043a5a9 +
                          lVar9 + (long)*(int *)(param_1 + 0x1f9c) * 0x10 + 0x2f) * iVar6) / 100 +
                (int)uVar11) * (100 - iVar1);
        goto LAB_006eec58;
      }
    }
    if ((int)uVar7 < iVar13) {
      return iVar12;
    }
    iVar3 = iVar3 + 6;
    iVar12 = iVar12 + 1;
    if (iVar3 == 0x30) {
      return -1;
    }
  } while( true );
}

~~~
