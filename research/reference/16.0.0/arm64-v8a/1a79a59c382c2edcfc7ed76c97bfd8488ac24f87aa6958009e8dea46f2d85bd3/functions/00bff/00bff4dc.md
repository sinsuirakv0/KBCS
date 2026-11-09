# 00bff4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bff4dc",
  "name": "_ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0675f1093c5dd1ccfd0efc5d0e433303f4e6d8e18590362d760f2b58a90eef84",
  "source_text_sha256": "0675f1093c5dd1ccfd0efc5d0e433303f4e6d8e18590362d760f2b58a90eef84"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5cce0](../00c5c/00c5cce0.md)

## 疑似コード / UTF-8 250 bytes

~~~c

void _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev(long *param_1)

{
  void *__ptr;
  
  __ptr = (void *)((long)param_1 + *(long *)(*param_1 + -0x18));
  _ZNSt6__ndk18ios_baseD1Ev((long)__ptr + 0x18);
  _ZdlPv(__ptr);
  return;
}

~~~
