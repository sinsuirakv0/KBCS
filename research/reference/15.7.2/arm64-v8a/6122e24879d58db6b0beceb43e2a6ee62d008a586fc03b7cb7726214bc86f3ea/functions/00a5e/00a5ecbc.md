# 00a5ecbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a5ecbc.md)

## 関数情報

~~~json
{
  "address": "00a5ecbc",
  "name": "FUN_00a5ecbc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b235aa318aec76b86c48616690500cb2b0d9845546e9ef022c0068ad1be58cdf",
  "source_text_sha256": "b235aa318aec76b86c48616690500cb2b0d9845546e9ef022c0068ad1be58cdf"
}
~~~
## 呼び出し元

- [00a5e6e0](../00a5e/00a5e6e0.md)

## 呼び出し先

- [007cd2ac](../007cd/007cd2ac.md)
- [007cd560](../007cd/007cd560.md)
- [007d22d4](../007d2/007d22d4.md)
- [0081f580](../0081f/0081f580.md)
- [00a08564](../00a08/00a08564.md)

## 疑似コード 1/1 / UTF-8 1612 bytes

~~~c

bool FUN_00a5ecbc(long param_1,undefined4 param_2)

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
  
  iVar3 = FUN_007cd2ac(param_2);
  iVar4 = FUN_007cd560(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_007d22d4(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a08564(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00a5ed64:
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
      if (iVar3 != -3) goto LAB_00a5ed64;
      iVar4 = iVar4 + 4;
    }
    FUN_0081f580();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd28b;
    do {
      lVar6 = FUN_0081f580();
      lVar7 = lVar6 + (long)iVar4 * 200;
      pbVar1 = (byte *)(lVar6 + lVar8);
      uVar2 = (uint)(*(byte *)(lVar7 + 0xd34e) ^ pbVar1[-1]) << 0x10 |
              (uint)(*(byte *)(lVar7 + 0xd34f) ^ *pbVar1) << 0x18 |
              (uint)(*(byte *)(lVar7 + 0xd34d) ^ pbVar1[-2]) << 8 |
              (uint)(*(byte *)(lVar7 + 0xd34c) ^ pbVar1[-3]);
      bVar9 = *(int *)(param_1 + 0x6c) < (int)uVar2;
      if ((int)uVar2 <= *(int *)(param_1 + 0x6c)) {
        return bVar9;
      }
      FUN_0081f580();
      lVar10 = lVar10 + -1;
      lVar8 = lVar8 + 4;
    } while (lVar10 != 0);
  }
  return bVar9;
}

~~~
