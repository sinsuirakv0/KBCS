# 00bbbbe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbbbe0",
  "name": "FUN_00bbbbe0",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d216a75d614d10ff5756f9bffc7d281d25bf84bf53889d1805c40d7a035b8369",
  "source_text_sha256": "d216a75d614d10ff5756f9bffc7d281d25bf84bf53889d1805c40d7a035b8369"
}
~~~

## 呼び出し元

- [00bbb6b8](../00bbb/00bbb6b8.md)
- [00bbc0e8](../00bbc/00bbc0e8.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 638 bytes

~~~c

void FUN_00bbbbe0(long *param_1)

{
  if (DAT_01127368 != 0) {
    if (DAT_01127370 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127370 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127368);
    DAT_01127368 = 0;
  }
  if (DAT_011273d8 != 0) {
    if (DAT_011273e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011273e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011273d8);
    DAT_011273d8 = 0;
  }
  return;
}

~~~
