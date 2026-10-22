# 00bdfce0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfce0.md)

## 関数情報

~~~json
{
  "address": "00bdfce0",
  "name": "std::__ndk1::__insertion_sort_incomplete<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Object>&,flatbuffers::Offset<reflection::Object>*>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe350703c7720ed9e3ecea000e2c120ae8767f0f2fe95774d85aae0400a5172f",
  "source_text_sha256": "fe350703c7720ed9e3ecea000e2c120ae8767f0f2fe95774d85aae0400a5172f"
}
~~~
## 呼び出し元

- [00b3b02c](../00b3b/00b3b02c.md)

## 呼び出し先

- [00b3bfb4](../00b3b/00b3bfb4.md)

## 疑似コード 1/1 / UTF-8 531 bytes

~~~c

bool std::__ndk1::
     __insertion_sort_incomplete<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Object>&,flatbuffers::Offset<reflection::Object>*>
               (Offset *param_1,Offset *param_2,TableKeyComparator *param_3)

{
  bool bVar1;
  
  bVar1 = (bool)(*(code *)
                  PTR___insertion_sort_incomplete<flatbuffers::FlatBufferBuilder::TableKeyComparator<reflection::Object>&,flatbuffers::Offset<reflection::Object>*>_00c1e6a8
                )((char)param_1);
  return bVar1;
}

~~~
