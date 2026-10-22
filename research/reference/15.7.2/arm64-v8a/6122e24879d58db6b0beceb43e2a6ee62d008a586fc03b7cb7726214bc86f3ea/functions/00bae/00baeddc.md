# 00baeddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baeddc.md)

## 関数情報

~~~json
{
  "address": "00baeddc",
  "name": "std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_unshift",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e6cce0003f4dd3c4b43bc2d18865c9187d8bd2f16ab53314ac3779113cdfe8a",
  "source_text_sha256": "2e6cce0003f4dd3c4b43bc2d18865c9187d8bd2f16ab53314ac3779113cdfe8a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 362 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_unshift(mbstate_t&, char*, char*, char*&) const
    */

undefined8 __thiscall
std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_unshift
          (__codecvt_utf8_utf16<char32_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4)

{
  *param_4 = param_2;
  return 3;
}

~~~
