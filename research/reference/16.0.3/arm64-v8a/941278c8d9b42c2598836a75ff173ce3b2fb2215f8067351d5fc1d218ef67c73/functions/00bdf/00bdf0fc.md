# 00bdf0fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdf0fc",
  "name": "_ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbf5b7f51af542bf84fa86114c26cf2ec725b0d29759004f9df1cc47e8b10519",
  "source_text_sha256": "bbf5b7f51af542bf84fa86114c26cf2ec725b0d29759004f9df1cc47e8b10519"
}
~~~

## 呼び出し元

- [00c5ed10](../00c5e/00c5ed10.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 1555 bytes

~~~c

void _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv(long *param_1)

{
  if (DAT_01127dc0 != 0) {
    if (DAT_01127dc8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127dc8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127dc0);
    DAT_01127dc0 = 0;
  }
  if (DAT_01127de0 != 0) {
    if (DAT_01127de8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127de8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127de0);
    DAT_01127de0 = 0;
  }
  if (DAT_01127e70 != 0) {
    if (DAT_01127e78 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127e78 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127e70);
    DAT_01127e70 = 0;
  }
  if (DAT_01127ec0 != 0) {
    if (DAT_01127ec8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127ec8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127ec0);
    DAT_01127ec0 = 0;
  }
  if (DAT_01127ee8 != 0) {
    if (DAT_01127ef0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127ef0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127ee8);
    DAT_01127ee8 = 0;
  }
  return;
}

~~~
