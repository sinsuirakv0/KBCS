# 00bbacec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbacec.md)

## 関数情報

~~~json
{
  "address": "00bbacec",
  "name": "std::bad_alloc::what",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9021d813b65d0c8dad87be97698d59a59c18794a435eed4b6bde0556f1304c7",
  "source_text_sha256": "f9021d813b65d0c8dad87be97698d59a59c18794a435eed4b6bde0556f1304c7"
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
## 疑似コード 1/1 / UTF-8 377 bytes

~~~c

/* std::bad_alloc::what() const */

char * std::bad_alloc::what(void)

{
                    /* catch() { ... } // from try @ 00bb57e0 with catch @ 00bbacf0 */
                    /* catch() { ... } // from try @ 00bb57f8 with catch @ 00bbacf4 */
                    /* catch() { ... } // from try @ 00bb5068 with catch @ 00bbacf8 */
  return "std::bad_alloc";
}

~~~
