# 00bb7fdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bb7fdc.md)

## 関数情報

~~~json
{
  "address": "00bb7fdc",
  "name": "FUN_00bb7fdc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "49acc878e99298959865a3523ac70c5bfd9e2c6333f71a7015d194f839d892f4",
  "source_text_sha256": "49acc878e99298959865a3523ac70c5bfd9e2c6333f71a7015d194f839d892f4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

## 疑似コード 1/1 / UTF-8 169 bytes

~~~c

void FUN_00bb7fdc(__shared_weak_count *param_1)

{
  std::__ndk1::__shared_weak_count::~__shared_weak_count(param_1);
  operator_delete(param_1);
  return;
}

~~~
