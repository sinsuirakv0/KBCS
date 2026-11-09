# 00bcc3ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcc3ac",
  "name": "_ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b6fcbb7167ff29f2696e9a243b1fc681f393d9240e8133ae0f0a7684b7efa26",
  "source_text_sha256": "2b6fcbb7167ff29f2696e9a243b1fc681f393d9240e8133ae0f0a7684b7efa26"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab60](../00c5a/00c5ab60.md)

## 疑似コード / UTF-8 2589 bytes

~~~c

void _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_011263d0 != 0) {
                    /* try { // try from 00bcc3d4 to 00ccc53b has its CatchHandler @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc3d4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc560 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc5c8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc6a4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc770 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc840 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc90c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcc9d8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcca40 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccb1c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccbe8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcccac with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccd7c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcce98 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bccf70 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd140 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd208 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd368 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd71c with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcd9c0 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdcb8 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcddc4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdec4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bcdfd4 with catch @ 00bcc3d4
                       catch() { ... } // from try @ 00bce040 with catch @ 00bcc3d4 */
    if (DAT_011263d8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011263d8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011263d0);
    DAT_011263d0 = 0;
  }
  return;
}

~~~
