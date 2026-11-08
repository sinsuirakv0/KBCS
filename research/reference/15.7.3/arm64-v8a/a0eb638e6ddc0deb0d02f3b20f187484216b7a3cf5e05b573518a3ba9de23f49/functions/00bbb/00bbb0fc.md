# 00bbb0fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbb0fc",
  "name": "_ZNSt10bad_typeidC2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85d3dba937f5c34052585b88762d7cf3d7fb2a6c1d5dc10d9c79a3ab3bb3fb0b",
  "source_text_sha256": "85d3dba937f5c34052585b88762d7cf3d7fb2a6c1d5dc10d9c79a3ab3bb3fb0b"
}
~~~

## 呼び出し元

- [00be1d60](../00be1/00be1d60.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 120 bytes

~~~c

void _ZNSt10bad_typeidC2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVSt10bad_typeid_00c1bff0 + 0x10);
  return;
}

~~~
