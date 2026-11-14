# 00bc4adc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc4adc",
  "name": "_ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74d6906b100a44facdfca7509fc3650dad0d416f021dbdc697afda88cd3f8c86",
  "source_text_sha256": "74d6906b100a44facdfca7509fc3650dad0d416f021dbdc697afda88cd3f8c86"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 542 bytes

~~~c

void _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv
               (long *param_1)

{
  if (DAT_01127758 != 0) {
    if (DAT_01127760 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127760 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bc4b30 to 00cc4ce3 has its CatchHandler @ 00bc4954 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127758);
    DAT_01127758 = 0;
  }
  return;
}

~~~
