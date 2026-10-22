# 00bacbdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bacbdc.md)

## 関数情報

~~~json
{
  "address": "00bacbdc",
  "name": "std::__ndk1::codecvt<char32_t,char,mbstate_t>::do_unshift",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a01bad9cfc9a9ca119a97ce13013ec77bf8ff5e812167848ef070b777331efca",
  "source_text_sha256": "a01bad9cfc9a9ca119a97ce13013ec77bf8ff5e812167848ef070b777331efca"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 369 bytes

~~~c

/* std::__ndk1::codecvt<char32_t, char, mbstate_t>::do_unshift(mbstate_t&, char*, char*, char*&)
   const */

undefined8 __thiscall
std::__ndk1::codecvt<char32_t,char,mbstate_t>::do_unshift
          (codecvt<char32_t,char,mbstate_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4)

{
  *param_4 = param_2;
  return 3;
}

~~~
