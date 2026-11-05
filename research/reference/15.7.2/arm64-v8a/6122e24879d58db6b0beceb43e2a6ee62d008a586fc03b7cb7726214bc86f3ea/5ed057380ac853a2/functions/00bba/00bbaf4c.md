# 00bbaf4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaf4c.md)

## 関数情報

~~~json
{
  "address": "00bbaf4c",
  "name": "_ZNSt14overflow_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3169f3ea017d25c70550165623ba4a8f60eb88a3ca5ebd74c757473b5290f40",
  "source_text_sha256": "c3169f3ea017d25c70550165623ba4a8f60eb88a3ca5ebd74c757473b5290f40"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be0e70](../00be0/00be0e70.md)

## 疑似コード 1/1 / UTF-8 113 bytes

~~~c

void _ZNSt14overflow_errorD0Ev(void *param_1)

{
  _ZNSt14overflow_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
