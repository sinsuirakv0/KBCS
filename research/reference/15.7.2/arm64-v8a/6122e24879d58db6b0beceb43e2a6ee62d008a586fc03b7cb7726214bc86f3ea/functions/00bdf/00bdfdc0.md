# 00bdfdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfdc0.md)

## 関数情報

~~~json
{
  "address": "00bdfdc0",
  "name": "std::__ndk1::__sort<bool(*&)(flatbuffers::StructDef_const*,flatbuffers::StructDef_const*),flatbuffers::StructDef**>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5cadf1c53bc125747e28f76da8ab193b9b79231ffb240dac73388f59e0ceee",
  "source_text_sha256": "9d5cadf1c53bc125747e28f76da8ab193b9b79231ffb240dac73388f59e0ceee"
}
~~~
## 呼び出し元

- [00b28e9c](../00b28/00b28e9c.md)
- [00b44938](../00b44/00b44938.md)

## 呼び出し先

- [00b44938](../00b44/00b44938.md)

## 疑似コード 1/1 / UTF-8 418 bytes

~~~c

void std::__ndk1::
     __sort<bool(*&)(flatbuffers::StructDef_const*,flatbuffers::StructDef_const*),flatbuffers::StructDef**>
               (StructDef **param_1,StructDef **param_2,
               _func_bool_StructDef_ptr_StructDef_ptr *param_3)

{
  (*(code *)
    PTR___sort<bool(*&)(flatbuffers::StructDef_const*,flatbuffers::StructDef_const*),flatbuffers::StructDef**>_00c1e718
  )();
  return;
}

~~~
