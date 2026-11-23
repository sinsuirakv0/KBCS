# 00bbcee0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0174.md#review-c27574d01304dc947549adfee5afed6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcee0",
  "name": "FUN_00bbcee0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bac9ffd4c7ac5959aa460cf182b19bc8dcf07e200894612c67c9cde30c53b9c2",
  "source_text_sha256": "bac9ffd4c7ac5959aa460cf182b19bc8dcf07e200894612c67c9cde30c53b9c2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbcd98](../00bbc/00bbcd98.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5cfc0](../00c5c/00c5cfc0.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void FUN_00bbcee0(undefined8 param_1)

{
  long lVar1;
  
  lVar1 = DAT_01125f70;
  if (DAT_01125f70 != 0) {
    _ZN8firebase5Mutex7AcquireEv(DAT_01125f70);
    DAT_01126008 = 1;
    FUN_00bbcd98();
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  _ZN8firebase9messaging36NotifyListenerOnRegistrationReceivedEPKc(param_1);
  return;
}

~~~
