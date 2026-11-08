# 00bbaddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbaddc",
  "name": "_ZNSt20bad_array_new_lengthD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a80914d12dacfc9e757b7252b5e6e74e3502f084c762ef55eb87ad43b8f3d17",
  "source_text_sha256": "8a80914d12dacfc9e757b7252b5e6e74e3502f084c762ef55eb87ad43b8f3d17"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb1a0](../00bdb/00bdb1a0.md)

## 疑似コード / UTF-8 647 bytes

~~~c

void _ZNSt20bad_array_new_lengthD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb45b0 with catch @ 00bbadf0 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb764c with catch @ 00bbadf4 */
                    /* catch() { ... } // from try @ 00bb729c with catch @ 00bbadf8 */
                    /* catch() { ... } // from try @ 00bb6ee8 with catch @ 00bbadfc */
                    /* catch() { ... } // from try @ 00bb6b34 with catch @ 00bbae00 */
                    /* catch() { ... } // from try @ 00bb6780 with catch @ 00bbae04 */
  _ZdlPv(param_1);
  return;
}

~~~
