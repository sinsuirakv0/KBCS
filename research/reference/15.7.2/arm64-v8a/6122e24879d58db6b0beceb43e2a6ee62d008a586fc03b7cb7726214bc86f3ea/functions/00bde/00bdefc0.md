# 00bdefc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdefc0.md)

## 関数情報

~~~json
{
  "address": "00bdefc0",
  "name": "reflection::EnumBuilder::add_is_union",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9df5d83229ee7ff6d4716cf18ab8a53d3014a9592ab6d5a39ec869d00844adbf",
  "source_text_sha256": "9df5d83229ee7ff6d4716cf18ab8a53d3014a9592ab6d5a39ec869d00844adbf"
}
~~~
## 呼び出し元

- [00b29390](../00b29/00b29390.md)

## 呼び出し先

- [00b34f54](../00b34/00b34f54.md)

## 疑似コード 1/1 / UTF-8 165 bytes

~~~c

void __thiscall reflection::EnumBuilder::add_is_union(EnumBuilder *this,bool param_1)

{
  (*(code *)PTR_add_is_union_00c1e018)(this,param_1);
  return;
}

~~~
