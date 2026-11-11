# 00bccb1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bccb1c",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f85bb97ffd9868033fcc3d54220bc664ccc7e1bcfc6cb8f21fa0b642429667bb",
  "source_text_sha256": "f85bb97ffd9868033fcc3d54220bc664ccc7e1bcfc6cb8f21fa0b642429667bb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011267f0 != 0) {
    if (DAT_011267f8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011267f8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011267f0);
    DAT_011267f0 = 0;
  }
  return;
}

~~~
