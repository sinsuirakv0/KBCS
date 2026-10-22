# 00bbafac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbafac.md)

## 関数情報

~~~json
{
  "address": "00bbafac",
  "name": "std::type_info::~type_info",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98ea999d0ac2c7149a39fb429ce93f2503daf21ea739a70a3e1b0dc339294313",
  "source_text_sha256": "98ea999d0ac2c7149a39fb429ce93f2503daf21ea739a70a3e1b0dc339294313"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1da0](../00be1/00be1da0.md)

## 疑似コード 1/1 / UTF-8 169 bytes

~~~c

/* std::type_info::~type_info() */

void __thiscall std::type_info::~type_info(type_info *this)

{
  ~type_info(this);
  operator_delete(this);
  return;
}

~~~
