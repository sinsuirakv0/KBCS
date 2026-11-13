# 00bdda0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdda0c",
  "name": "_ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c904d7893f87d924a980a84bed0833f62ebb4284a89c6f55fe091bbae9f000e",
  "source_text_sha256": "9c904d7893f87d924a980a84bed0833f62ebb4284a89c6f55fe091bbae9f000e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 382 bytes

~~~c

void _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126f00 != 0) {
    if (DAT_01126f08 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126f08 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126f00);
    DAT_01126f00 = 0;
  }
  return;
}

~~~
