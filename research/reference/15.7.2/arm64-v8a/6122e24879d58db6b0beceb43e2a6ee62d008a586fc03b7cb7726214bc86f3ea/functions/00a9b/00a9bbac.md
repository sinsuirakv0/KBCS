# 00a9bbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a9bbac.md)

## 関数情報

~~~json
{
  "address": "00a9bbac",
  "name": "FUN_00a9bbac",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "669ae71e6857ec7db9ee705fb655b69fa53ac67f49cfbc7264e0958e54bde065",
  "source_text_sha256": "669ae71e6857ec7db9ee705fb655b69fa53ac67f49cfbc7264e0958e54bde065"
}
~~~
## 呼び出し元

- [005ced48](../005ce/005ced48.md)
- [005d6c3c](../005d6/005d6c3c.md)
- [006d6d04](../006d6/006d6d04.md)
- [006e4aec](../006e4/006e4aec.md)
- [006e79bc](../006e7/006e79bc.md)
- [006eccf4](../006ec/006eccf4.md)

## 呼び出し先

- [005bb5f0](../005bb/005bb5f0.md)
- [005bbbc8](../005bb/005bbbc8.md)
- [005bbc10](../005bb/005bbc10.md)
- [005bbc90](../005bb/005bbc90.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 1463 bytes

~~~c

void FUN_00a9bbac(int param_1,int param_2,int param_3)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  
  if (param_1 == 1) {
    uVar2 = FUN_005bbbc8();
    if ((uVar2 & 1) == 0) {
      if (param_2 != 0) goto LAB_00a9bc28;
    }
    else {
      iVar1 = FUN_005bbc10();
      if (iVar1 != param_2) goto LAB_00a9bc28;
    }
    uVar2 = FUN_005bbc90();
    if ((uVar2 & 1) != 0) {
      lVar3 = FUN_0081f580();
      FUN_005bb5f0(lVar3 + 0x898,1);
      return;
    }
  }
LAB_00a9bc28:
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x840cc) = *(int *)(lVar3 + 0x840cc) + param_3;
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84240) = *(int *)(lVar3 + 0x84240) + param_3;
  lVar3 = FUN_0081f580();
  if (((0 < *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288)) &&
      (lVar3 = FUN_0081f580(),
      *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288) < param_3)) &&
     (lVar3 = FUN_0081f580(),
     *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) == 0)) {
    lVar3 = FUN_0081f580();
    *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) = 1;
  }
  lVar3 = FUN_0081f580();
  *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84308) = 1;
  return;
}

~~~
