# 00bcca3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d53c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0066.md#compare-328442f7b77a52e8f33bafc81606a261)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
