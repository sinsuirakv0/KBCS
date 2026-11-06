# 00ae0dec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00ae0dec",
  "name": "_ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc2d0f4df231ec5d8910e9d70f452c08fc255a5f9dc1e3b5b52befe5486fd4d9",
  "source_text_sha256": "bc2d0f4df231ec5d8910e9d70f452c08fc255a5f9dc1e3b5b52befe5486fd4d9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

## 疑似コード / UTF-8 404 bytes

~~~c

void _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a0118 != 0) {
    if (DAT_010a0120 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0120 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0118);
    DAT_010a0118 = 0;
  }
  return;
}

~~~
