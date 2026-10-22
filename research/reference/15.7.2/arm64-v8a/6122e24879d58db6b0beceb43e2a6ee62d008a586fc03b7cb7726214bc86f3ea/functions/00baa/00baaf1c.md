# 00baaf1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaf1c.md)

## 関数情報

~~~json
{
  "address": "00baaf1c",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_tolower",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96ccf0e9adaa85d1aee32404954c54592b7ca54596bdb3553aa9b51ef115ecc3",
  "source_text_sha256": "96ccf0e9adaa85d1aee32404954c54592b7ca54596bdb3553aa9b51ef115ecc3"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be19f0](../00be1/00be19f0.md)

## 疑似コード 1/1 / UTF-8 294 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_tolower(wchar_t) const */

wint_t __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_tolower(ctype_byname<wchar_t> *this,wchar_t param_1)

{
  wint_t wVar1;
  
  wVar1 = towlower_l(param_1,*(__locale_t *)(this + 0x10));
  return wVar1;
}

~~~
