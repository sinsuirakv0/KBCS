# 00afaaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0168.md#review-eeba5e23c83d51395a37e825499cb6f7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaac",
  "name": "FUN_00afaaac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68231e94d94b7338fdbc373d4bae2a219ec77b92280f9f77904d4ae7019cf451",
  "source_text_sha256": "68231e94d94b7338fdbc373d4bae2a219ec77b92280f9f77904d4ae7019cf451"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 377 bytes

~~~c

bool FUN_00afaaac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afaacc to 00bfaae3 has its CatchHandler @ 00afb218 */
                    /* try { // try from 00afaae4 to 00bfab07 has its CatchHandler @ 00afaa30 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) != 0;
}

~~~
