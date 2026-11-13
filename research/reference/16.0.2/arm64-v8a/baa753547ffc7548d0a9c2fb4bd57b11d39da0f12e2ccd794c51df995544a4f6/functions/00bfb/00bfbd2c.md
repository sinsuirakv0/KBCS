# 00bfbd2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbd2c",
  "name": "_ZNKSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6getlocEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b37cebe5881f12c5102417f7da44c9e1ebb868dbc485425e7b1aeca72b186c6",
  "source_text_sha256": "7b37cebe5881f12c5102417f7da44c9e1ebb868dbc485425e7b1aeca72b186c6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a8a0](../00c5a/00c5a8a0.md)

## 疑似コード / UTF-8 170 bytes

~~~c

void _ZNKSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6getlocEv(undefined8 param_1,long param_2)

{
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 8);
  return;
}

~~~
