# 00bfacbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfacbc",
  "name": "_ZNKSt6__ndk18ios_base6getlocEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fd838a63531509e635de8922dd7b932c1f7bde351e9e32fad00d816b41a251b",
  "source_text_sha256": "8fd838a63531509e635de8922dd7b932c1f7bde351e9e32fad00d816b41a251b"
}
~~~

## 呼び出し元

- [00c57e70](../00c57/00c57e70.md)

## 呼び出し先

- [00c5a3d0](../00c5a/00c5a3d0.md)

## 疑似コード / UTF-8 142 bytes

~~~c

void _ZNKSt6__ndk18ios_base6getlocEv(undefined8 param_1,long param_2)

{
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 0x30);
  return;
}

~~~
