# 00aa1afc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aa1afc.md)

## 関数情報

~~~json
{
  "address": "00aa1afc",
  "name": "FUN_00aa1afc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9dcf82014844b7ed90a7839bae9ff09fd11f31b4baf556b38ea013e9af737d23",
  "source_text_sha256": "9dcf82014844b7ed90a7839bae9ff09fd11f31b4baf556b38ea013e9af737d23"
}
~~~
## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [006a0ab4](../006a0/006a0ab4.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

## 疑似コード 1/1 / UTF-8 5498 bytes

~~~c

undefined8 FUN_00aa1afc(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* catch() { ... } // from try @ 00aa0f74 with catch @ 00aa1b08 */
                    /* catch() { ... } // from try @ 00a9ffc8 with catch @ 00aa1b0c */
                    /* catch() { ... } // from try @ 00a9feb4 with catch @ 00aa1b10 */
  lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa052c with catch @ 00aa1b28 */
                    /* catch() { ... } // from try @ 00aa0020 with catch @ 00aa1b2c */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
                    /* catch() { ... } // from try @ 00aa0674 with catch @ 00aa1b30 */
  if ((uVar2 & 1) == 0) {
                    /* catch() { ... } // from try @ 00aa1774 with catch @ 00aa1b34 */
    uVar3 = 0;
                    /* catch() { ... } // from try @ 00aa0984 with catch @ 00aa1b38 */
  }
  else {
                    /* catch() { ... } // from try @ 00aa0108 with catch @ 00aa1b3c */
    lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0708 with catch @ 00aa1b40 */
                    /* catch() { ... } // from try @ 00aa16e4 with catch @ 00aa1b44 */
                    /* catch() { ... } // from try @ 00a9ffa8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0018 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0224 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa032c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0408 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0524 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa05b0 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0654 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa06c8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa08e4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0a8c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0b4c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0b9c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0c3c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0c8c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0ce4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0e00 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0e54 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0ec4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0f9c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1004 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa105c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa10b4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa110c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1164 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa11bc with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1214 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1294 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa12ec with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1344 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa13ac with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1404 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa145c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa14b4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa150c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1564 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa15bc with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1614 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa166c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa170c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa179c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa17f8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1860 with catch @ 00aa1b48 */
                    /* catch() { ... } // from try @ 00aa07f0 with catch @ 00aa1b4c */
                    /* catch() { ... } // from try @ 00aa0114 with catch @ 00aa1b50 */
                    /* catch() { ... } // from try @ 00aa093c with catch @ 00aa1b54 */
                    /* catch() { ... } // from try @ 00aa07fc with catch @ 00aa1b58 */
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9fddc) == 0) {
      uVar3 = FUN_00aa2c2c(lVar1,param_2,param_3,6);
      return uVar3;
    }
    uVar3 = 1;
  }
  return uVar3;
}

~~~
