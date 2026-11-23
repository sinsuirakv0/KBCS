# 00afc8cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0019.md#review-e0dace160e8984d29ee1fd37d4efcdcc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc8cc",
  "name": "FUN_00afc8cc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9db48495f1681376fffa10ddce01002b27285bd9051141faf644fb37ad32507b",
  "source_text_sha256": "9db48495f1681376fffa10ddce01002b27285bd9051141faf644fb37ad32507b"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 444 bytes

~~~c

bool FUN_00afc8cc(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbea4 with catch @ 00afc8d8 */
                    /* catch() { ... } // from try @ 00afb88c with catch @ 00afc8dc */
  lVar1 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00afb840 with catch @ 00afc8f8 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c34) != 0;
}

~~~
