# 00bbcee0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
