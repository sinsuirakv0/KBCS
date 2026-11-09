# 008daaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008daaac",
  "name": "FUN_008daaac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac4b5a66de0a59e422baaef1204e54ceb8a2170f6558ad1bff368c0b9fd9e4a9",
  "source_text_sha256": "ac4b5a66de0a59e422baaef1204e54ceb8a2170f6558ad1bff368c0b9fd9e4a9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 243 bytes

~~~c

long FUN_008daaac(long param_1,long param_2)

{
  param_1 = param_1 + 0x10;
  if (*(char **)(param_2 + 8) !=
      "ZN10NyankoClub19requestCurrentStateENSt6__ndk18functionIFvNS_6ResultEiEEEbE3$_0") {
    param_1 = 0;
  }
  return param_1;
}

~~~
