# 00baed6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baed6c.md)

## 関数情報

~~~json
{
  "address": "00baed6c",
  "name": "std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_in",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f97a292f1987551e4fce4f2a0af15328ce61a47339773a13d6bb37d30abb146a",
  "source_text_sha256": "f97a292f1987551e4fce4f2a0af15328ce61a47339773a13d6bb37d30abb146a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae8c8](../00bae/00bae8c8.md)

## 疑似コード 1/1 / UTF-8 980 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_in(mbstate_t&, char const*, char const*, char
   const*&, char32_t*, char32_t*, char32_t*&) const */

void __thiscall
std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_in
          (__codecvt_utf8_utf16<char32_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4,wchar32 *param_5,wchar32 *param_6,wchar32 **param_7)

{
  wchar32 *local_30;
  char *pcStack_28;
  
                    /* catch() { ... } // from try @ 00baeb68 with catch @ 00baed7c */
                    /* catch() { ... } // from try @ 00baeb34 with catch @ 00baed90 */
                    /* catch() { ... } // from try @ 00baeb74 with catch @ 00baed98 */
  local_30 = param_5;
  pcStack_28 = param_2;
  FUN_00bae8c8(param_2,param_3,&pcStack_28,param_5,param_6,&local_30,*(undefined8 *)(this + 0x10),
               *(undefined4 *)(this + 0x18));
  *param_4 = pcStack_28;
  *param_7 = local_30;
  return;
}

~~~
