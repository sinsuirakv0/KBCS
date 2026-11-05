# 00bbacec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbacec.md)

## 関数情報

~~~json
{
  "address": "00bbacec",
  "name": "_ZNKSt9bad_alloc4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89542cb3da142e704930f11ce8804fce6a9c4aed036007c6f36bd424e1da6be3",
  "source_text_sha256": "89542cb3da142e704930f11ce8804fce6a9c4aed036007c6f36bd424e1da6be3"
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
## 疑似コード 1/1 / UTF-8 332 bytes

~~~c

char * _ZNKSt9bad_alloc4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb57e0 with catch @ 00bbacf0 */
                    /* catch() { ... } // from try @ 00bb57f8 with catch @ 00bbacf4 */
                    /* catch() { ... } // from try @ 00bb5068 with catch @ 00bbacf8 */
  return "std::bad_alloc";
}

~~~
