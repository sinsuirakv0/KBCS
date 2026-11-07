# 00b5ceac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b5cda0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cda0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00b5ceac",
  "name": "_ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7191e079b324d53c022b08801d6e96d5f039e97b9f6411b1b91ca0e1c331372a",
  "source_text_sha256": "7191e079b324d53c022b08801d6e96d5f039e97b9f6411b1b91ca0e1c331372a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

## 疑似コード / UTF-8 392 bytes

~~~c

void _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a14c8 != 0) {
    if (DAT_010a14d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a14d0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a14c8);
    DAT_010a14c8 = 0;
  }
  return;
}

~~~
