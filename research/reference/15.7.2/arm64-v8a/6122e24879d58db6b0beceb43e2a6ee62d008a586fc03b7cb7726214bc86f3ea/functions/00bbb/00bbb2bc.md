# 00bbb2bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbb2bc.md)

## 関数情報

~~~json
{
  "address": "00bbb2bc",
  "name": "FUN_00bbb2bc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d73ed4d6cb8996b1841f8021b0397a3f780dba1bf59ffc1d4bbe27c3cdacfa6",
  "source_text_sha256": "0d73ed4d6cb8996b1841f8021b0397a3f780dba1bf59ffc1d4bbe27c3cdacfa6"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1d90](../00be1/00be1d90.md)

## 疑似コード 1/1 / UTF-8 131 bytes

~~~c

void FUN_00bbb2bc(type_info *param_1)

{
  std::type_info::~type_info(param_1);
  operator_delete(param_1);
  return;
}

~~~
