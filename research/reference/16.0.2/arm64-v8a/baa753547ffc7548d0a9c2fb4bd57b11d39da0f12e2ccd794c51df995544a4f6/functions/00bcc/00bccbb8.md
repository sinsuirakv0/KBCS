# 00bccbb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bccbb8",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "337d113a295d567bbc23e8f60d6900aa02ac669f0c349e69d8b076ec4e9d438d",
  "source_text_sha256": "337d113a295d567bbc23e8f60d6900aa02ac669f0c349e69d8b076ec4e9d438d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011268f0 != 0) {
    if (DAT_011268f8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011268f8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011268f0);
    DAT_011268f0 = 0;
  }
  return;
}

~~~
