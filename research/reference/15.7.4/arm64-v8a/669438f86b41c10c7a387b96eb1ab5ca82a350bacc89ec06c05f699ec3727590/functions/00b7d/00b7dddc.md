# 00b7dddc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b7dcd0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcd0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00b7dddc",
  "name": "FUN_00b7dddc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a05f29a5900954c1d9a4d000f70270022a3733c60c2574c4721680a81abd4fe2",
  "source_text_sha256": "a05f29a5900954c1d9a4d000f70270022a3733c60c2574c4721680a81abd4fe2"
}
~~~

## 呼び出し元

- [00b7db58](../00b7d/00b7db58.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 216 bytes

~~~c

void FUN_00b7dddc(void)

{
                    /* try { // try from 00b7dde0 to 00c7ddfb has its CatchHandler @ 00b802ec */
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
