# 00bcef9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5fa9c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0067.md#compare-8f11c7eb64d4c25042d9c286d07daaa5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcef9c",
  "name": "_ZN8firebase4auth4Auth14UseAppLanguageEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11",
  "source_text_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 643 bytes

~~~c

void _ZN8firebase4auth4Auth14UseAppLanguageEv(long *param_1)

{
  undefined8 uVar1;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
                    /* try { // try from 00bcefbc to 00ccf247 has its CatchHandler @ 00bcefbc
                       catch() { ... } // from try @ 00bcefbc with catch @ 00bcefbc
                       catch() { ... } // from try @ 00bcf250 with catch @ 00bcefbc */
    FUN_00574cac(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126358);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
    return;
  }
  return;
}

~~~
