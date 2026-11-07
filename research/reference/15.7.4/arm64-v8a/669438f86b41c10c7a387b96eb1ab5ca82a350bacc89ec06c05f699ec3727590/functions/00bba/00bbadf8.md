# 00bbadf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbacec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbacec.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbadf8",
  "name": "_ZNKSt9bad_alloc4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "323a567f05491d6dd88d40b0687775744efbc2a37505ead74f633de0716d8a5c",
  "source_text_sha256": "323a567f05491d6dd88d40b0687775744efbc2a37505ead74f633de0716d8a5c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"std::bad_alloc"
~~~

## 疑似コード / UTF-8 332 bytes

~~~c

char * _ZNKSt9bad_alloc4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb58ec with catch @ 00bbadfc */
                    /* catch() { ... } // from try @ 00bb5904 with catch @ 00bbae00 */
                    /* catch() { ... } // from try @ 00bb5174 with catch @ 00bbae04 */
  return "std::bad_alloc";
}

~~~
