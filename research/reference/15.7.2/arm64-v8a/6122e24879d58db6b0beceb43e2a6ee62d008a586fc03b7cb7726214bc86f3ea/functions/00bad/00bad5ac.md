# 00bad5ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bad5ac.md)

## 関数情報

~~~json
{
  "address": "00bad5ac",
  "name": "std::__ndk1::__codecvt_utf8<char32_t>::do_out",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17b1abdfbc7f2fbbbd1d79b4f103c1d112a13a40bfe5433296882cf4ffa5c430",
  "source_text_sha256": "17b1abdfbc7f2fbbbd1d79b4f103c1d112a13a40bfe5433296882cf4ffa5c430"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac7a8](../00bac/00bac7a8.md)

## 疑似コード 1/1 / UTF-8 700 bytes

~~~c

/* std::__ndk1::__codecvt_utf8<char32_t>::do_out(mbstate_t&, char32_t const*, char32_t const*,
   char32_t const*&, char*, char*, char*&) const */

void __thiscall
std::__ndk1::__codecvt_utf8<char32_t>::do_out
          (__codecvt_utf8<char32_t> *this,mbstate_t *param_1,wchar32 *param_2,wchar32 *param_3,
          wchar32 **param_4,char *param_5,char *param_6,char **param_7)

{
  char *local_30;
  wchar32 *pwStack_28;
  
  local_30 = param_5;
  pwStack_28 = param_2;
  FUN_00bac7a8(param_2,param_3,&pwStack_28,param_5,param_6,&local_30,*(undefined8 *)(this + 0x10),
               *(undefined4 *)(this + 0x18));
  *param_4 = pwStack_28;
  *param_7 = local_30;
  return;
}

~~~
