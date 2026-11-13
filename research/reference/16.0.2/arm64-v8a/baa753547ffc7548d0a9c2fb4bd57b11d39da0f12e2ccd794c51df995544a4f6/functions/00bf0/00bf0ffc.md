# 00bf0ffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf0ffc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305",
  "source_text_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305"
}
~~~

## 呼び出し元

- [00c5e120](../00c5e/00c5e120.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 191 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(byte *param_1)

{
  if ((*param_1 & 1) == 0) {
    return;
  }
  _ZdlPv(*(void **)(param_1 + 0x10));
  return;
}

~~~
