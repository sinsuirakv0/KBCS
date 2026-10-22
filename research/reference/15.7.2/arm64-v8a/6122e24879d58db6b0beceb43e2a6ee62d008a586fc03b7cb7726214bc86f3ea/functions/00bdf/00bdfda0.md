# 00bdfda0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfda0.md)

## 関数情報

~~~json
{
  "address": "00bdfda0",
  "name": "std::__ndk1::__sort<bool(*&)(flatbuffers::EnumDef_const*,flatbuffers::EnumDef_const*),flatbuffers::EnumDef**>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2c19ce4a8a5cf9c53f5cdcb74f9e7c513e7a6b73c479bc71d952d625cbb2eb5",
  "source_text_sha256": "a2c19ce4a8a5cf9c53f5cdcb74f9e7c513e7a6b73c479bc71d952d625cbb2eb5"
}
~~~
## 呼び出し元

- [00b28fc8](../00b28/00b28fc8.md)
- [00b4561c](../00b45/00b4561c.md)

## 呼び出し先

- [00b4561c](../00b45/00b4561c.md)

## 疑似コード 1/1 / UTF-8 381 bytes

~~~c

void std::__ndk1::
     __sort<bool(*&)(flatbuffers::EnumDef_const*,flatbuffers::EnumDef_const*),flatbuffers::EnumDef**>
               (EnumDef **param_1,EnumDef **param_2,_func_bool_EnumDef_ptr_EnumDef_ptr *param_3)

{
  (*(code *)
    PTR___sort<bool(*&)(flatbuffers::EnumDef_const*,flatbuffers::EnumDef_const*),flatbuffers::EnumDef**>_00c1e708
  )();
  return;
}

~~~
