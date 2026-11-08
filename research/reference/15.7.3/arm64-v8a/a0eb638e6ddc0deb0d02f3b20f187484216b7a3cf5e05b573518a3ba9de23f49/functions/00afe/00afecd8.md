# 00afecd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afecd8",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD0Ev",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c8f648fec4c251e6cd585207d4df6c56b6cc15c23dbc67fd43ea875e32c8bfd",
  "source_text_sha256": "1c8f648fec4c251e6cd585207d4df6c56b6cc15c23dbc67fd43ea875e32c8bfd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdedd0](../00bde/00bdedd0.md)

## 疑似コード / UTF-8 325 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00afdb30 with catch @ 00afecd8 */
                    /* catch() { ... } // from try @ 00af6fb0 with catch @ 00afecdc */
  _ZN8firebase26ReferenceCountedFutureImplD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
