# 00bdddd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdddd0.md)

## 関数情報

~~~json
{
  "address": "00bdddd0",
  "name": "std::__ndk1::__tree<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::__map_value_compare<unsigned_long,std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::less<unsigned_long>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>>>::destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10a383481a37fd40102a697c222de20fad86bf5c79cdbea02c91484157709333",
  "source_text_sha256": "10a383481a37fd40102a697c222de20fad86bf5c79cdbea02c91484157709333"
}
~~~
## 呼び出し元

- [00ae0434](../00ae0/00ae0434.md)
- [00afea18](../00afe/00afea18.md)

## 呼び出し先

- [00ae0434](../00ae0/00ae0434.md)

## 疑似コード 1/1 / UTF-8 800 bytes

~~~c

void __thiscall
std::__ndk1::
__tree<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::__map_value_compare<unsigned_long,std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::less<unsigned_long>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>>>
::destroy(__tree<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::__map_value_compare<unsigned_long,std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>,std::__ndk1::less<unsigned_long>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<unsigned_long,firebase::FutureBackingData*>>>
          *this,__tree_node *param_1)

{
  (*(code *)PTR_destroy_00c1d720)();
  return;
}

~~~
