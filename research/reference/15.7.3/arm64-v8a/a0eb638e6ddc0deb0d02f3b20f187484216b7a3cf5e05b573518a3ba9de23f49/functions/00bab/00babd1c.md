# 00babd1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00babd1c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab5b8fb3ac083131cbeae40af3da646fa25145be096031b831711115492a527f",
  "source_text_sha256": "ab5b8fb3ac083131cbeae40af3da646fa25145be096031b831711115492a527f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1530](../00be1/00be1530.md)
- [00be1b40](../00be1/00be1b40.md)

## 疑似コード / UTF-8 851 bytes

~~~c

ulong _ZNKSt6__ndk17codecvtIwc9mbstate_tE13do_max_lengthEv(long param_1)

{
  __locale_t __dataset;
  size_t sVar1;
  
                    /* catch() { ... } // from try @ 00bab7ec with catch @ 00babd20 */
                    /* catch() { ... } // from try @ 00bab7bc with catch @ 00babd28 */
                    /* catch() { ... } // from try @ 00bab954 with catch @ 00babd30 */
                    /* catch() { ... } // from try @ 00babac8 with catch @ 00babd34 */
  if (*(__locale_t *)(param_1 + 0x10) == (__locale_t)0x0) {
    sVar1 = 1;
  }
  else {
    __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
                    /* catch() { ... } // from try @ 00bab80c with catch @ 00babd44 */
    sVar1 = __ctype_get_mb_cur_max();
    if (__dataset != (__locale_t)0x0) {
      uselocale(__dataset);
    }
  }
  return sVar1 & 0xffffffff;
}

~~~
