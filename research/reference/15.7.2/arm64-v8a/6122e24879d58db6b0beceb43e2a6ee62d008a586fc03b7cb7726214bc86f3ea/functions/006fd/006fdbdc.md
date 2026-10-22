# 006fdbdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006fdbdc.md)

## 関数情報

~~~json
{
  "address": "006fdbdc",
  "name": "FUN_006fdbdc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2a1bbe342ac938cd74527a84fda73cd3f80bea8549fa46b1ba1052d4591f9a6",
  "source_text_sha256": "a2a1bbe342ac938cd74527a84fda73cd3f80bea8549fa46b1ba1052d4591f9a6"
}
~~~
## 呼び出し元

- [0067417c](../00674/0067417c.md)
- [00695904](../00695/00695904.md)
- [0070f364](../0070f/0070f364.md)
- [0070fd04](../0070f/0070fd04.md)
- [007317b0](../00731/007317b0.md)
- [00734374](../00734/00734374.md)
- [0073496c](../00734/0073496c.md)
- [00739a10](../00739/00739a10.md)
- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)
- [0075e798](../0075e/0075e798.md)
- [0075f8cc](../0075f/0075f8cc.md)
- [00761d08](../00761/00761d08.md)
- [007999cc](../00799/007999cc.md)
- [0081fa64](../0081f/0081fa64.md)
- [008336f0](../00833/008336f0.md)
- [00844bd8](../00844/00844bd8.md)
- [008673f0](../00867/008673f0.md)
- [0086b704](../0086b/0086b704.md)
- [009903e4](../00990/009903e4.md)
- [009d85c0](../009d8/009d85c0.md)
- [009d9f2c](../009d9/009d9f2c.md)
- [00a30514](../00a30/00a30514.md)
- [00a3d6c8](../00a3d/00a3d6c8.md)
- [00a42124](../00a42/00a42124.md)
- [00ade22c](../00ade/00ade22c.md)
- [00ade8c8](../00ade/00ade8c8.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 2164 bytes

~~~c

int FUN_006fdbdc(void)

{
  char *pcVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  
                    /* catch() { ... } // from try @ 006fd8c0 with catch @ 006fdbdc
                       catch() { ... } // from try @ 006fdb44 with catch @ 006fdbdc */
                    /* catch() { ... } // from try @ 006fd908 with catch @ 006fdbe4 */
  iVar5 = 0;
  iVar4 = 0;
  lVar6 = -300;
  lVar7 = 0xca3f;
  do {
    lVar3 = FUN_0081f580();
    pcVar1 = (char *)(lVar3 + lVar7);
    if (((*(char *)(lVar3 + 0xca66) == pcVar1[-1] && *(char *)(lVar3 + 0xca67) == *pcVar1) &&
        *(char *)(lVar3 + 0xca65) == pcVar1[-2]) && *(char *)(lVar3 + 0xca64) == pcVar1[-3]) {
      return iVar4;
    }
    lVar3 = FUN_0081f580();
    pbVar2 = (byte *)(lVar3 + lVar7);
    if (((uint)(*(byte *)(lVar3 + 0xca66) ^ pbVar2[-1]) << 0x10 |
         (uint)(*(byte *)(lVar3 + 0xca67) ^ *pbVar2) << 0x18 |
         (uint)(*(byte *)(lVar3 + 0xca65) ^ pbVar2[-2]) << 8 |
        (uint)(*(byte *)(lVar3 + 0xca64) ^ pbVar2[-3])) == 0x30) {
      iVar4 = (int)lVar6 + 400;
    }
    else {
      lVar3 = FUN_0081f580();
      pbVar2 = (byte *)(lVar3 + lVar7);
                    /* try { // try from 006fdc34 to 007fdf1f has its CatchHandler @ 006fdc34
                       catch() { ... } // from try @ 006fdc34 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe068 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe114 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe3a8 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe444 with catch @ 006fdc34 */
      iVar4 = (uint)(*(byte *)(lVar3 + 0xca64) ^ pbVar2[-3]) + iVar5 * 100 +
              (uint)(*(byte *)(lVar3 + 0xca65) ^ pbVar2[-2]) * 0x100 +
              (uint)(*(byte *)(lVar3 + 0xca66) ^ pbVar2[-1]) * 0x10000 +
              (uint)(*(byte *)(lVar3 + 0xca67) ^ *pbVar2) * 0x1000000;
    }
    lVar6 = lVar6 + 100;
    iVar5 = iVar5 + 1;
    lVar7 = lVar7 + 4;
  } while (lVar6 != 0);
  return iVar4;
}

~~~
