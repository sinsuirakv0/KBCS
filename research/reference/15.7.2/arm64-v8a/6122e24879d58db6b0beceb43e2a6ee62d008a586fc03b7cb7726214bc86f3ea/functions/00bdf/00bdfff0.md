# 00bdfff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfff0.md)

## 関数情報

~~~json
{
  "address": "00bdfff0",
  "name": "std::__ndk1::__sort3<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Enum>&,flatbuffers::Offset<reflection::Enum>*>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df4c7b8c3d95c2b30e8a4bf04bbb83d2e994ba282701d807d6e603053b7ee9a9",
  "source_text_sha256": "df4c7b8c3d95c2b30e8a4bf04bbb83d2e994ba282701d807d6e603053b7ee9a9"
}
~~~
## 呼び出し元

- [00b3c354](../00b3c/00b3c354.md)
- [00b3cce4](../00b3c/00b3cce4.md)
- [00b3d140](../00b3d/00b3d140.md)
- [00b3d2dc](../00b3d/00b3d2dc.md)

## 呼び出し先

- [00b3ca98](../00b3c/00b3ca98.md)

## 疑似コード 1/1 / UTF-8 480 bytes

~~~c

uint std::__ndk1::
     __sort3<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Enum>&,flatbuffers::Offset<reflection::Enum>*>
               (Offset *param_1,Offset *param_2,Offset *param_3,TableKeyComparator *param_4)

{
  uint uVar1;
  
  uVar1 = (*(code *)
            PTR___sort3<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Enum>&,flatbuffers::Offset<reflection::Enum>*>_00c1e830
          )((int)param_1);
  return uVar1;
}

~~~
