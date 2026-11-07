# 007bfcdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `007bfcdc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007bf/007bfcdc.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "007bfcdc",
  "name": "FUN_007bfcdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef",
  "source_text_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef"
}
~~~

## 呼び出し元

- [0078cd14](../0078c/0078cd14.md)
- [00796d74](../00796/00796d74.md)
- [007da86c](../007da/007da86c.md)
- [007dbc94](../007db/007dbc94.md)
- [007dc0fc](../007dc/007dc0fc.md)
- [009a3648](../009a3/009a3648.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_007bfcdc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
