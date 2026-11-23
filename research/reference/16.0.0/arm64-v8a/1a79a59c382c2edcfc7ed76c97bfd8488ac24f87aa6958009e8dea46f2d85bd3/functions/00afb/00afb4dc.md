# 00afb4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0169.md#review-561e2992e8b88fcff55959f90ce9c861)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb4dc",
  "name": "FUN_00afb4dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06",
  "source_text_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afb4dc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afb4f4 to 00bfb4ff has its CatchHandler @ 00afc9b4 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afb500 to 00bfb513 has its CatchHandler @ 00afc994 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b8) = param_3 & 1;
  return;
}

~~~
