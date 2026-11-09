# 00bd0dfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd0dfc",
  "name": "_ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8514e48819c18634b1a1c01969b5116d25e8b923bc152d18cc27b0a563ce6ce4",
  "source_text_sha256": "8514e48819c18634b1a1c01969b5116d25e8b923bc152d18cc27b0a563ce6ce4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 493 bytes

~~~c

void _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00bd0e00 to 00cd0f07 has its CatchHandler @ 00bd075c */
  if (DAT_011264c8 != 0) {
    if (DAT_011264d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011264d0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011264c8);
    DAT_011264c8 = 0;
  }
  return;
}

~~~
