# 00bba9fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bba9fc",
  "name": "_ZSt10unexpectedv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43635d2ec0a2edc94267a5b96bf85e34d4f74cc1d16010853b6b087df98289fe",
  "source_text_sha256": "43635d2ec0a2edc94267a5b96bf85e34d4f74cc1d16010853b6b087df98289fe"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bba9e0](../00bba/00bba9e0.md)

## 疑似コード / UTF-8 348 bytes

~~~c

undefined8 _ZSt10unexpectedv(void)

{
                    /* catch() { ... } // from try @ 00bb3cd0 with catch @ 00bbaa00 */
                    /* catch() { ... } // from try @ 00bb3930 with catch @ 00bbaa04 */
  FUN_00bba9e0(*(undefined8 *)PTR___cxa_unexpected_handler_00c1bfa8);
  return *(undefined8 *)PTR___cxa_terminate_handler_00c1bfb0;
}

~~~
