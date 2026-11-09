# 00abccb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abccb8",
  "name": "FUN_00abccb8",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c8205d29d591b250d297ac7a7ed7dadb4349e5ece4746864e6eb3fefb490495",
  "source_text_sha256": "6c8205d29d591b250d297ac7a7ed7dadb4349e5ece4746864e6eb3fefb490495"
}
~~~

## 呼び出し元

- [00abc6dc](../00abc/00abc6dc.md)

## 呼び出し先

- [00800338](../00800/00800338.md)
- [008005ec](../00800/008005ec.md)
- [008056ac](../00805/008056ac.md)
- [008514b8](../00851/008514b8.md)
- [00a65bf4](../00a65/00a65bf4.md)

## 疑似コード / UTF-8 1548 bytes

~~~c

bool FUN_00abccb8(long param_1,undefined4 param_2)

{
  byte *pbVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  bool bVar9;
  long lVar10;
  
  iVar3 = FUN_00800338(param_2);
  iVar4 = FUN_008005ec(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_008056ac(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a65bf4(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00abcd60:
    bVar9 = false;
  }
  else {
    if (*(int *)(param_1 + 0x6c) == -1) {
      return true;
    }
    if (*(int *)(param_1 + 0x68) != -1) {
      return true;
    }
    if (iVar3 == -7) {
      iVar4 = iVar4 + 7;
    }
    else if (iVar3 != -2) {
      if (iVar3 != -3) goto LAB_00abcd60;
      iVar4 = iVar4 + 4;
    }
    FUN_008514b8();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd443;
    do {
      lVar6 = FUN_008514b8();
      lVar7 = lVar6 + (long)iVar4 * 200;
      pbVar1 = (byte *)(lVar6 + lVar8);
      uVar2 = (uint)(*(byte *)(lVar7 + 0xd506) ^ pbVar1[-1]) << 0x10 |
              (uint)(*(byte *)(lVar7 + 0xd507) ^ *pbVar1) << 0x18 |
              (uint)(*(byte *)(lVar7 + 0xd505) ^ pbVar1[-2]) << 8 |
              (uint)(*(byte *)(lVar7 + 0xd504) ^ pbVar1[-3]);
      bVar9 = *(int *)(param_1 + 0x6c) < (int)uVar2;
      if ((int)uVar2 <= *(int *)(param_1 + 0x6c)) {
        return bVar9;
      }
      FUN_008514b8();
      lVar10 = lVar10 + -1;
      lVar8 = lVar8 + 4;
    } while (lVar10 != 0);
  }
  return bVar9;
}

~~~
