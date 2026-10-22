# 00bbaaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaaf4.md)

## 関数情報

~~~json
{
  "address": "00bbaaf4",
  "name": "FUN_00bbaaf4",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1beb45a6edd823c39df0df55d54bd22f8bae19c9a01fd52741f5164820e8eb8b",
  "source_text_sha256": "1beb45a6edd823c39df0df55d54bd22f8bae19c9a01fd52741f5164820e8eb8b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~
## 疑似コード 1/1 / UTF-8 437 bytes

~~~c

void FUN_00bbaaf4(void)

{
                    /* catch() { ... } // from try @ 00bb7aec with catch @ 00bbaaf8 */
                    /* catch() { ... } // from try @ 00bb369c with catch @ 00bbaafc */
                    /* catch() { ... } // from try @ 00bb36a8 with catch @ 00bbab0c */
  PTR_s_uncaught_00c248a0 = s_unexpected_002a1122;
                    /* WARNING: Subroutine does not return */
  std::terminate();
}

~~~
