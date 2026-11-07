# 00aa1aac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aa1a68`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa1/00aa1a68.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aa1aac",
  "name": "FUN_00aa1aac",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f5a7834c95c2f55525a1f699f3595ce1c742c995c07ad82e51427d7b37300ee",
  "source_text_sha256": "2f5a7834c95c2f55525a1f699f3595ce1c742c995c07ad82e51427d7b37300ee"
}
~~~

## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c70](../00aa2/00aa2c70.md)

## 疑似コード / UTF-8 2410 bytes

~~~c

undefined8 FUN_00aa1aac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* catch() { ... } // from try @ 00aa04dc with catch @ 00aa1aac */
                    /* catch() { ... } // from try @ 00aa0484 with catch @ 00aa1ab0 */
                    /* catch() { ... } // from try @ 00aa0380 with catch @ 00aa1ab4 */
                    /* catch() { ... } // from try @ 00aa027c with catch @ 00aa1ab8 */
                    /* catch() { ... } // from try @ 00aa03f0 with catch @ 00aa1abc */
                    /* catch() { ... } // from try @ 00aa03dc with catch @ 00aa1ac0 */
                    /* catch() { ... } // from try @ 00aa03c4 with catch @ 00aa1ac4 */
                    /* catch() { ... } // from try @ 00aa0ecc with catch @ 00aa1ac8 */
  lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0f68 with catch @ 00aa1acc */
                    /* catch() { ... } // from try @ 00a9ff74 with catch @ 00aa1ad0 */
                    /* catch() { ... } // from try @ 00a9ff64 with catch @ 00aa1ad4 */
                    /* catch() { ... } // from try @ 00aa0314 with catch @ 00aa1ad8 */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar2 & 1) == 0) {
    uVar3 = 0;
  }
  else {
    lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0300 with catch @ 00aa1af0 */
                    /* catch() { ... } // from try @ 00aa0f74 with catch @ 00aa1b08 */
                    /* catch() { ... } // from try @ 00a9ffc8 with catch @ 00aa1b0c */
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9fdc4) == 0) {
                    /* catch() { ... } // from try @ 00aa052c with catch @ 00aa1b28 */
                    /* catch() { ... } // from try @ 00aa0020 with catch @ 00aa1b2c */
                    /* catch() { ... } // from try @ 00aa0674 with catch @ 00aa1b30 */
                    /* catch() { ... } // from try @ 00aa1774 with catch @ 00aa1b34 */
                    /* catch() { ... } // from try @ 00aa0984 with catch @ 00aa1b38 */
                    /* catch() { ... } // from try @ 00aa0108 with catch @ 00aa1b3c */
      uVar3 = FUN_00aa2c70(lVar1,param_2,param_3,5);
      return uVar3;
    }
                    /* catch() { ... } // from try @ 00a9feb4 with catch @ 00aa1b10 */
    uVar3 = 1;
  }
  return uVar3;
}

~~~
