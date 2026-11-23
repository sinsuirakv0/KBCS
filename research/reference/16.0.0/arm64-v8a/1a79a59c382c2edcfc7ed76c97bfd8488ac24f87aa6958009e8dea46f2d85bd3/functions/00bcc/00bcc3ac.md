# 00bcc3ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5ceac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0066.md#compare-1af1b57bddb23032aa3d5c20e10d9898)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
