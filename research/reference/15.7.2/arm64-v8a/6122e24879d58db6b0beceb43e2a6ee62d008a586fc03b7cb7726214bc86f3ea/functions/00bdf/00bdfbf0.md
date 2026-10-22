# 00bdfbf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfbf0.md)

## 関数情報

~~~json
{
  "address": "00bdfbf0",
  "name": "std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::__append_forward_unsafe<char_const*>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e41d8b067216463ad8d200b55a33d89efa849dcd402c7a0cb7944254915ae768",
  "source_text_sha256": "e41d8b067216463ad8d200b55a33d89efa849dcd402c7a0cb7944254915ae768"
}
~~~
## 呼び出し元

- [00b0f740](../00b0f/00b0f740.md)

## 呼び出し先

- [00b3eca0](../00b3e/00b3eca0.md)

## 疑似コード 1/1 / UTF-8 449 bytes

~~~c

basic_string * __thiscall
std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
__append_forward_unsafe<char_const*>
          (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *this,
          char *param_1,char *param_2)

{
  basic_string *pbVar1;
  
  pbVar1 = (basic_string *)(*(code *)PTR___append_forward_unsafe<char_const*>_00c1e630)();
  return pbVar1;
}

~~~
