# 00af4fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0015.md#review-23b524bd51dbc327a49563b5042b8614)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af4fdc",
  "name": "FUN_00af4fdc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "692a798fd25675e838ca81b367e63f2b422323a4d8ed217efce5fa9e7b18ccc4",
  "source_text_sha256": "692a798fd25675e838ca81b367e63f2b422323a4d8ed217efce5fa9e7b18ccc4"
}
~~~

## 呼び出し元

- [0066b684](../0066b/0066b684.md)
- [00716a50](../00716/00716a50.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 508 bytes

~~~c

void FUN_00af4fdc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af4fdc to 00bf4fe3 has its CatchHandler @ 00af51c8 */
                    /* try { // try from 00af4fe4 to 00bf4ffb has its CatchHandler @ 00af51dc */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00af4ffc to 00bf5043 has its CatchHandler @ 00af51e4 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848f0) = param_3;
  return;
}

~~~
