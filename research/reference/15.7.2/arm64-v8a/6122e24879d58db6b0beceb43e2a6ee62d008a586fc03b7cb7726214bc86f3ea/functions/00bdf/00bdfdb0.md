# 00bdfdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfdb0.md)

## 関数情報

~~~json
{
  "address": "00bdfdb0",
  "name": "std::__ndk1::__sort<bool(*&)(flatbuffers::FieldDef_const*,flatbuffers::FieldDef_const*),flatbuffers::FieldDef**>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aff0b899a383f44f1db6d19fd2c6750750d6b10ffca53f1c2f05474f013ab3d2",
  "source_text_sha256": "aff0b899a383f44f1db6d19fd2c6750750d6b10ffca53f1c2f05474f013ab3d2"
}
~~~
## 呼び出し元

- [00b217a4](../00b21/00b217a4.md)
- [00b42fb4](../00b42/00b42fb4.md)

## 呼び出し先

- [00b42fb4](../00b42/00b42fb4.md)

## 疑似コード 1/1 / UTF-8 489 bytes

~~~c

void std::__ndk1::
     __sort<bool(*&)(flatbuffers::FieldDef_const*,flatbuffers::FieldDef_const*),flatbuffers::FieldDef**>
               (FieldDef **param_1,FieldDef **param_2,_func_bool_FieldDef_ptr_FieldDef_ptr *param_3)

{
                    /* try { // try from 00bdfdb0 to 00cdff63 has its CatchHandler @ 00bdfbd4 */
  (*(code *)
    PTR___sort<bool(*&)(flatbuffers::FieldDef_const*,flatbuffers::FieldDef_const*),flatbuffers::FieldDef**>_00c1e710
  )();
  return;
}

~~~
