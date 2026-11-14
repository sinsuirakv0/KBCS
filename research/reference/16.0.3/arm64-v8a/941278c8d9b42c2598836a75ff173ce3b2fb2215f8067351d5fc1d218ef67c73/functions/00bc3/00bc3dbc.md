# 00bc3dbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc3dbc",
  "name": "_ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99874e3e67582ce47a28e281c1c824b1b1562c0e5f9eb04e27053b884b57684f",
  "source_text_sha256": "99874e3e67582ce47a28e281c1c824b1b1562c0e5f9eb04e27053b884b57684f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 432 bytes

~~~c

void _ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv
               (long *param_1)

{
  if (DAT_011276b8 != 0) {
    if (DAT_011276c0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011276c0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011276b8);
    DAT_011276b8 = 0;
  }
  return;
}

~~~
