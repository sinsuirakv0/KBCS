# 00bbaa5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbaa5c",
  "name": "_ZSt15get_new_handlerv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "283548e1d42701c0b083c1595b0dc48e0badd092f6f7ddc10da1873cd034228d",
  "source_text_sha256": "283548e1d42701c0b083c1595b0dc48e0badd092f6f7ddc10da1873cd034228d"
}
~~~

## 呼び出し元

- [00be1dd0](../00be1/00be1dd0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 277 bytes

~~~c

undefined8 _ZSt15get_new_handlerv(void)

{
                    /* catch() { ... } // from try @ 00bb3480 with catch @ 00bbaa68 */
                    /* catch() { ... } // from try @ 00bb344c with catch @ 00bbaa6c */
  return *(undefined8 *)PTR___cxa_new_handler_00c1bfb8;
}

~~~
