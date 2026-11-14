# 00bcdef4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcdef4",
  "name": "_ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2fe16cec49703704218ea88259e7b889732b9debb5413c787a32e022dff4eb07",
  "source_text_sha256": "2fe16cec49703704218ea88259e7b889732b9debb5413c787a32e022dff4eb07"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 590 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bcdef4 to 00ccdf0b has its CatchHandler @ 00bcf958 */
                    /* try { // try from 00bcdf0c to 00ccdfbf has its CatchHandler @ 00bcd634 */
  if (DAT_011278d8 != 0) {
    if (DAT_011278e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278d8);
    DAT_011278d8 = 0;
  }
  return;
}

~~~
