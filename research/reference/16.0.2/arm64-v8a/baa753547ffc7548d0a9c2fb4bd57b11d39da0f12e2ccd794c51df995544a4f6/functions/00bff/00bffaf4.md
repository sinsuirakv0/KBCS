# 00bffaf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bffaf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d",
  "source_text_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d"
}
~~~

## 呼び出し元

- [00c5e490](../00c5e/00c5e490.md)
- [00c5e4a0](../00c5e/00c5e4a0.md)

## 呼び出し先

- [00c58360](../00c58/00c58360.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bc00 + 0x10);
  _ZNSt6__ndk16localeD1Ev(param_1 + 1);
  return;
}

~~~
