# 00bbadb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbadb4",
  "name": "_ZNKSt9bad_alloc4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "458ec627df26c73102f8dca166fa0a81494999bd41199f497a8dc808005d0d1c",
  "source_text_sha256": "458ec627df26c73102f8dca166fa0a81494999bd41199f497a8dc808005d0d1c"
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
                    /* catch() { ... } // from try @ 00bb58a8 with catch @ 00bbadb8 */
                    /* catch() { ... } // from try @ 00bb58c0 with catch @ 00bbadbc */
                    /* catch() { ... } // from try @ 00bb5130 with catch @ 00bbadc0 */
  return "std::bad_alloc";
}

~~~
