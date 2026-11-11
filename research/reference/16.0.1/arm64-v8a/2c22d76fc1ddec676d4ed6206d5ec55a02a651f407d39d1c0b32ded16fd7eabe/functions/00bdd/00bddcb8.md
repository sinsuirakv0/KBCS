# 00bddcb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bddcb8",
  "name": "_ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52cf5ef26b879e371e7b6ac9c07303a986176badc92a2e47b370e397cf0ee899",
  "source_text_sha256": "52cf5ef26b879e371e7b6ac9c07303a986176badc92a2e47b370e397cf0ee899"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

## 疑似コード / UTF-8 393 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126e28 != 0) {
    if (DAT_01126e30 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126e30 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126e28);
    DAT_01126e28 = 0;
  }
  return;
}

~~~
