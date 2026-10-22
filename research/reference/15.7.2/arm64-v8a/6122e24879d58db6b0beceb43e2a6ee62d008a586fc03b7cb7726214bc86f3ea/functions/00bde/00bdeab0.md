# 00bdeab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeab0.md)

## 関数情報

~~~json
{
  "address": "00bdeab0",
  "name": "std::__ndk1::__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>::destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afdebd25cc0cbb68a9f076ddbb56bfb0f618cb6a075f7648c8648b3123e3b82a",
  "source_text_sha256": "afdebd25cc0cbb68a9f076ddbb56bfb0f618cb6a075f7648c8648b3123e3b82a"
}
~~~
## 呼び出し元

- [00b0a3b0](../00b0a/00b0a3b0.md)
- [00b0d4a8](../00b0d/00b0d4a8.md)
- [00b1cedc](../00b1c/00b1cedc.md)
- [00b2e664](../00b2e/00b2e664.md)

## 呼び出し先

- [00b0d4a8](../00b0d/00b0d4a8.md)

## 疑似コード 1/1 / UTF-8 1538 bytes

~~~c

void __thiscall
std::__ndk1::
__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
::destroy(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
          *this,__tree_node *param_1)

{
  (*(code *)PTR_destroy_00c1dd90)();
  return;
}

~~~
