# 00bd0edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bd0edc",
  "name": "_ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e12f77748a9b9e1e09a16306b075bb4296727f30fbe83b9aac4e3a48f92517d8",
  "source_text_sha256": "e12f77748a9b9e1e09a16306b075bb4296727f30fbe83b9aac4e3a48f92517d8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

## 疑似コード / UTF-8 499 bytes

~~~c

void _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bd0ee4 to 00cd0f7b has its CatchHandler @ 00bd0958 */
  if (DAT_011268a8 != 0) {
    if (DAT_011268b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011268b0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011268a8);
    DAT_011268a8 = 0;
  }
  return;
}

~~~
