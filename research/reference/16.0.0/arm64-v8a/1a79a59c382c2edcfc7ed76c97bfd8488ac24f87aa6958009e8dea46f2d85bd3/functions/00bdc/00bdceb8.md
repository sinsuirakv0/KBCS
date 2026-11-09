# 00bdceb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdceb8",
  "name": "_ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cac88589b26842049f81f8fe659552261781168481dd05ad72e9b91397e6470b",
  "source_text_sha256": "cac88589b26842049f81f8fe659552261781168481dd05ad72e9b91397e6470b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 378 bytes

~~~c

void _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126920 != 0) {
    if (DAT_01126928 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126928 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126920);
    DAT_01126920 = 0;
  }
  return;
}

~~~
