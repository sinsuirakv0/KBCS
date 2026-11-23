# 00aa3cac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aa3cac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa3/00aa3cac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0025.md#compare-55348e70423a42f7b1a1b3b89be38b17)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3cac",
  "name": "FUN_00aa3cac",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f365afc45f9c337870f4ffbf799b40dcccd9f26554705ba5819e08785d1d432",
  "source_text_sha256": "8f365afc45f9c337870f4ffbf799b40dcccd9f26554705ba5819e08785d1d432"
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [006a4d58](../006a4/006a4d58.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

## 疑似コード / UTF-8 887 bytes

~~~c

undefined8 FUN_00aa3cac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* try { // try from 00aa3cc8 to 00ba3cd7 has its CatchHandler @ 00aa5998 */
  lVar1 = FUN_0081f580();
                    /* try { // try from 00aa3cd8 to 00ba3ceb has its CatchHandler @ 00aa5970 */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar2 & 1) == 0) {
    uVar3 = 0;
  }
  else {
    lVar1 = FUN_0081f580();
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9feec) == 0) {
      uVar3 = FUN_00aa2c2c(lVar1,param_2,param_3,0x3f);
      return uVar3;
    }
    uVar3 = 1;
  }
                    /* try { // try from 00aa3d18 to 00ba3d1f has its CatchHandler @ 00aa5a58 */
                    /* try { // try from 00aa3d20 to 00ba3d5b has its CatchHandler @ 00aa5a70 */
  return uVar3;
}

~~~
