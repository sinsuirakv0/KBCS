# 00bcca3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcca3c",
  "name": "_ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9677dc3e9f3b9fa04a5c464c9c08d3f26d01aa09d42f7fe390a0b34d2ad816e1",
  "source_text_sha256": "9677dc3e9f3b9fa04a5c464c9c08d3f26d01aa09d42f7fe390a0b34d2ad816e1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 493 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bcca40 to 00cccb03 has its CatchHandler @ 00bcc3d4 */
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
