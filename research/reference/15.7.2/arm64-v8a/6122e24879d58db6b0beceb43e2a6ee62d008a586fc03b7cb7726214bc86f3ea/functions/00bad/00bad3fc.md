# 00bad3fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bad3fc.md)

## 関数情報

~~~json
{
  "address": "00bad3fc",
  "name": "std::__ndk1::__codecvt_utf8<char16_t>::do_unshift",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c59e1c3e2de3f47b528069a9a16f07194a2b2a9a7b55a61b3fa118955a0220f9",
  "source_text_sha256": "c59e1c3e2de3f47b528069a9a16f07194a2b2a9a7b55a61b3fa118955a0220f9"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 339 bytes

~~~c

/* std::__ndk1::__codecvt_utf8<char16_t>::do_unshift(mbstate_t&, char*, char*, char*&) const */

undefined8 __thiscall
std::__ndk1::__codecvt_utf8<char16_t>::do_unshift
          (__codecvt_utf8<char16_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4)

{
  *param_4 = param_2;
  return 3;
}

~~~
