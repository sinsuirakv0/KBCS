# 00bbac5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbac5c.md)

## 関数情報

~~~json
{
  "address": "00bbac5c",
  "name": "std::exception::what",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2332d78d75b0dadb15d93797ee31bdfeb113f20de27e7b0bd2abc8fc5afa12ea",
  "source_text_sha256": "2332d78d75b0dadb15d93797ee31bdfeb113f20de27e7b0bd2abc8fc5afa12ea"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"std::exception"
~~~
## 疑似コード 1/1 / UTF-8 632 bytes

~~~c

/* std::exception::what() const */

char * std::exception::what(void)

{
                    /* catch() { ... } // from try @ 00bba128 with catch @ 00bbac60
                       catch() { ... } // from try @ 00bba278 with catch @ 00bbac60 */
                    /* catch() { ... } // from try @ 00bba110 with catch @ 00bbac64
                       catch() { ... } // from try @ 00bba260 with catch @ 00bbac64 */
                    /* catch() { ... } // from try @ 00bba0f8 with catch @ 00bbac68
                       catch() { ... } // from try @ 00bba248 with catch @ 00bbac68 */
  return "std::exception";
}

~~~
