# 00bbaf4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaf4c.md)

## 関数情報

~~~json
{
  "address": "00bbaf4c",
  "name": "std::overflow_error::~overflow_error",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "935d097077441c1ddde1b3f1f0275a2f284d94956b5a423cb320ce898e90505b",
  "source_text_sha256": "935d097077441c1ddde1b3f1f0275a2f284d94956b5a423cb320ce898e90505b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be0e70](../00be0/00be0e70.md)

## 疑似コード 1/1 / UTF-8 199 bytes

~~~c

/* std::overflow_error::~overflow_error() */

void __thiscall std::overflow_error::~overflow_error(overflow_error *this)

{
  ~overflow_error(this);
  operator_delete(this);
  return;
}

~~~
