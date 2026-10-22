# 00babfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00babfbc.md)

## 関数情報

~~~json
{
  "address": "00babfbc",
  "name": "std::__ndk1::codecvt<char16_t,char,mbstate_t>::do_in",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c01e51d6dd1abe6e85f3b5f275a6d013b228a21d3f71bd936a46216536bf0e8d",
  "source_text_sha256": "c01e51d6dd1abe6e85f3b5f275a6d013b228a21d3f71bd936a46216536bf0e8d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac024](../00bac/00bac024.md)

## 疑似コード 1/1 / UTF-8 660 bytes

~~~c

/* std::__ndk1::codecvt<char16_t, char, mbstate_t>::do_in(mbstate_t&, char const*, char const*, char
   const*&, char16_t*, char16_t*, char16_t*&) const */

void __thiscall
std::__ndk1::codecvt<char16_t,char,mbstate_t>::do_in
          (codecvt<char16_t,char,mbstate_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4,wchar16 *param_5,wchar16 *param_6,wchar16 **param_7)

{
  wchar16 *local_30;
  char *pcStack_28;
  
  local_30 = param_5;
  pcStack_28 = param_2;
  FUN_00bac024(param_2,param_3,&pcStack_28,param_5,param_6,&local_30,0x10ffff,0);
  *param_4 = pcStack_28;
  *param_7 = local_30;
  return;
}

~~~
