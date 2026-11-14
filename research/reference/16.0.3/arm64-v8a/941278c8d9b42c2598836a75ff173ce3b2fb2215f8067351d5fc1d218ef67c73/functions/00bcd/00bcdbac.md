# 00bcdbac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcdbac",
  "name": "_ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea0da8c9284cd3253bf16edc590eca583992d10a9d432b0a3dfb3b7634f49433",
  "source_text_sha256": "ea0da8c9284cd3253bf16edc590eca583992d10a9d432b0a3dfb3b7634f49433"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 386 bytes

~~~c

void _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011278b0 != 0) {
    if (DAT_011278b8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278b8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278b0);
    DAT_011278b0 = 0;
  }
  return;
}

~~~
