# 00bd5dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd5dbc",
  "name": "_ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e09abc1f6546c77e96b1972e47d79522dfae1940c7168ab8baa23a1e6ab6446",
  "source_text_sha256": "6e09abc1f6546c77e96b1972e47d79522dfae1940c7168ab8baa23a1e6ab6446"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 385 bytes

~~~c

void _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126bc8 != 0) {
    if (DAT_01126bd0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126bd0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126bc8);
    DAT_01126bc8 = 0;
  }
  return;
}

~~~
