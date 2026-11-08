# 00acd8ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acd8ec",
  "name": "FUN_00acd8ec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0c3bba4e26fdf266eed18918aa3604d61944705925992e02ae82e8c071b6b2f",
  "source_text_sha256": "a0c3bba4e26fdf266eed18918aa3604d61944705925992e02ae82e8c071b6b2f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 149 bytes

~~~c

void FUN_00acd8ec(long param_1)

{
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    return;
  }
  _ZdlPv(*(void **)(param_1 + 0x20));
  return;
}

~~~
