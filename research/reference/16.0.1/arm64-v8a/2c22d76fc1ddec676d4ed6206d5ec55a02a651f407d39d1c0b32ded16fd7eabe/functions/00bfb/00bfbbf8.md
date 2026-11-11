# 00bfbbf8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbbf8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41b4d203cf3c54ca646692d8ca9bd67db7d023522f886897c9b509547d82994d",
  "source_text_sha256": "41b4d203cf3c54ca646692d8ca9bd67db7d023522f886897c9b509547d82994d"
}
~~~

## 呼び出し元

- [00c5e350](../00c5e/00c5e350.md)

## 呼び出し先

- [00c58290](../00c58/00c58290.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b848 + 0x10);
  _ZNSt6__ndk16localeD1Ev(param_1 + 1);
  return;
}

~~~
