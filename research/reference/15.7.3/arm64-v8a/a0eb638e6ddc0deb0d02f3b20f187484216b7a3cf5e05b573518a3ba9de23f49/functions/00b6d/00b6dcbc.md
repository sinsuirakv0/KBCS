# 00b6dcbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b6dcbc",
  "name": "_ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df05ed018abb53657572f276326b55acf02e43aae0a64be9063215cbaed6a632",
  "source_text_sha256": "df05ed018abb53657572f276326b55acf02e43aae0a64be9063215cbaed6a632"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 疑似コード / UTF-8 382 bytes

~~~c

void _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a1a68 != 0) {
    if (DAT_010a1a70 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a1a70 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a1a68);
    DAT_010a1a68 = 0;
  }
  return;
}

~~~
