# 00bd2ecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd2ecc",
  "name": "_ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2e30ea70d08032fea850d9a96dba6da7b77451c200b33889c01621c4126e733",
  "source_text_sha256": "d2e30ea70d08032fea850d9a96dba6da7b77451c200b33889c01621c4126e733"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 402 bytes

~~~c

void _ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126608 != 0) {
    if (DAT_01126610 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126610 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126608);
    DAT_01126608 = 0;
  }
  return;
}

~~~
