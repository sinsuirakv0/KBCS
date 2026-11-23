# 00af0dcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0164.md#review-f96e8172fd1c0600aec8d0cb24813328)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0dcc",
  "name": "FUN_00af0dcc",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13cdff8088af0a7b703442d50539c5d13d096c8a582c6287f0d266df84d7ba07",
  "source_text_sha256": "13cdff8088af0a7b703442d50539c5d13d096c8a582c6287f0d266df84d7ba07"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b9134](../008b9/008b9134.md)

## 疑似コード / UTF-8 947 bytes

~~~c

void FUN_00af0dcc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar2 = *param_2;
    uVar1 = FUN_0047acb4();
    FUN_0047cd94(uVar1,0xb,0);
    FUN_008b9134(uVar2);
    return;
  }
                    /* try { // try from 00af0e1c to 00bf0e1f has its CatchHandler @ 00af0e30 */
  if ((*param_3 == 5) && (*param_4 == 0)) {
                    /* catch() { ... } // from try @ 00af0c84 with catch @ 00af0e20
                       try { // try from 00af0e20 to 00bf0eab has its CatchHandler @ 00af0b98 */
                    /* catch() { ... } // from try @ 00af0c44 with catch @ 00af0e28 */
    *(undefined4 *)(*(long *)(param_1 + 8) + 0x4a86c) = 2;
  }
                    /* catch() { ... } // from try @ 00af0ca8 with catch @ 00af0e30
                       catch() { ... } // from try @ 00af0e1c with catch @ 00af0e30 */
  return;
}

~~~
