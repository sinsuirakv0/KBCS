# 00bbabec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbabec",
  "name": "FUN_00bbabec",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92b7b5b26eab11bca475cffb74b0e274b80c3f388c89970a67b50e528d41b108",
  "source_text_sha256": "92b7b5b26eab11bca475cffb74b0e274b80c3f388c89970a67b50e528d41b108"
}
~~~

## 呼び出し元

- [00bba6c4](../00bba/00bba6c4.md)
- [00bbb0f4](../00bbb/00bbb0f4.md)

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 638 bytes

~~~c

void FUN_00bbabec(long *param_1)

{
  if (DAT_011263a8 != 0) {
    if (DAT_011263b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011263b0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011263a8);
    DAT_011263a8 = 0;
  }
  if (DAT_01126418 != 0) {
    if (DAT_01126420 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126420 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126418);
    DAT_01126418 = 0;
  }
  return;
}

~~~
