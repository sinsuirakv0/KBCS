# 00babcf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00babcf8.md)

## 関数情報

~~~json
{
  "address": "00babcf8",
  "name": "std::__ndk1::codecvt<char16_t,char,mbstate_t>::do_out",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0146089c40d45d33317655978523aa070fc47e39464a0b069fe600a24001d50",
  "source_text_sha256": "a0146089c40d45d33317655978523aa070fc47e39464a0b069fe600a24001d50"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babd60](../00bab/00babd60.md)

## 疑似コード 1/1 / UTF-8 1015 bytes

~~~c

/* std::__ndk1::codecvt<char16_t, char, mbstate_t>::do_out(mbstate_t&, char16_t const*, char16_t
   const*, char16_t const*&, char*, char*, char*&) const */

void __thiscall
std::__ndk1::codecvt<char16_t,char,mbstate_t>::do_out
          (codecvt<char16_t,char,mbstate_t> *this,mbstate_t *param_1,wchar16 *param_2,
          wchar16 *param_3,wchar16 **param_4,char *param_5,char *param_6,char **param_7)

{
  char *local_30;
  wchar16 *pwStack_28;
  
  local_30 = param_5;
  pwStack_28 = param_2;
                    /* try { // try from 00babd3c to 00cabf0b has its CatchHandler @ 00babd3c
                       catch() { ... } // from try @ 00babd3c with catch @ 00babd3c
                       catch() { ... } // from try @ 00babf28 with catch @ 00babd3c
                       catch() { ... } // from try @ 00bac1c4 with catch @ 00babd3c */
  FUN_00babd60(param_2,param_3,&pwStack_28,param_5,param_6,&local_30,0x10ffff,0);
  *param_4 = pwStack_28;
  *param_7 = local_30;
  return;
}

~~~
