# 00baebb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baebb8.md)

## 関数情報

~~~json
{
  "address": "00baebb8",
  "name": "std::__ndk1::__codecvt_utf8_utf16<char16_t>::do_out",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8803c06f53d0415f006963069a9bb8d5d0811b3d01fc2841f95123df20042e71",
  "source_text_sha256": "8803c06f53d0415f006963069a9bb8d5d0811b3d01fc2841f95123df20042e71"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babd60](../00bab/00babd60.md)

## 疑似コード 1/1 / UTF-8 914 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<char16_t>::do_out(mbstate_t&, char16_t const*, char16_t const*,
   char16_t const*&, char*, char*, char*&) const */

void __thiscall
std::__ndk1::__codecvt_utf8_utf16<char16_t>::do_out
          (__codecvt_utf8_utf16<char16_t> *this,mbstate_t *param_1,wchar16 *param_2,wchar16 *param_3
          ,wchar16 **param_4,char *param_5,char *param_6,char **param_7)

{
  char *local_30;
  wchar16 *pwStack_28;
  
                    /* try { // try from 00baebd8 to 00caebe3 has its CatchHandler @ 00baed6c */
  local_30 = param_5;
  pwStack_28 = param_2;
                    /* try { // try from 00baebfc to 00caec03 has its CatchHandler @ 00baed58 */
  FUN_00babd60(param_2,param_3,&pwStack_28,param_5,param_6,&local_30,*(undefined8 *)(this + 0x10),
               *(undefined4 *)(this + 0x18));
  *param_4 = pwStack_28;
  *param_7 = local_30;
  return;
}

~~~
