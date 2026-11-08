# 00bad0bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bad0bc",
  "name": "_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE9do_lengthERS1_PKDuS5_m",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21a7aba8c6ea152e075376a8cb5ad6d37441822ee25e70fe64fb167b706c3695",
  "source_text_sha256": "21a7aba8c6ea152e075376a8cb5ad6d37441822ee25e70fe64fb167b706c3695"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bacce8](../00bac/00bacce8.md)

## 疑似コード / UTF-8 350 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDiDu9mbstate_tE9do_lengthERS1_PKDuS5_m
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
                    /* catch() { ... } // from try @ 00bacf1c with catch @ 00bad0c0 */
  FUN_00bacce8(param_3,param_4,param_5,0x10ffff,0);
  return;
}

~~~
