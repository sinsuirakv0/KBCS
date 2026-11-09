# 00bef5cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bef5cc",
  "name": "_ZNSt6__ndk16chrono12system_clock11from_time_tEl",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733",
  "source_text_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733"
}
~~~

## 呼び出し元

- [00c58610](../00c58/00c58610.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 103 bytes

~~~c

long _ZNSt6__ndk16chrono12system_clock11from_time_tEl(long param_1)

{
  return param_1 * 1000000;
}

~~~
