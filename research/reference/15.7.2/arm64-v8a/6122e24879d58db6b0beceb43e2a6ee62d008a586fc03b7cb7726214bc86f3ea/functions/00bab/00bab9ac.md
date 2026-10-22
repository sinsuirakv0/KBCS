# 00bab9ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bab9ac.md)

## 関数情報

~~~json
{
  "address": "00bab9ac",
  "name": "std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_unshift",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ce9f8fe37cc445c8c9a600ede28e63a60b2ac86c560a81ed2dd1463c5b46b0c",
  "source_text_sha256": "5ce9f8fe37cc445c8c9a600ede28e63a60b2ac86c560a81ed2dd1463c5b46b0c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a50](../00be1/00be1a50.md)

## 疑似コード 1/1 / UTF-8 1539 bytes

~~~c

/* std::__ndk1::codecvt<wchar_t, char, mbstate_t>::do_unshift(mbstate_t&, char*, char*, char*&)
   const */

undefined8 __thiscall
std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_unshift
          (codecvt<wchar_t,char,mbstate_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4)

{
  char cVar1;
  __locale_t __dataset;
  size_t sVar2;
  undefined8 uVar3;
  ulong uVar4;
  char *pcVar5;
  char *pcVar6;
  char acStack_3c [4];
  __locale_t local_38;
  
  *param_4 = param_2;
  __dataset = uselocale(*(__locale_t *)(this + 0x10));
  local_38 = __dataset;
  sVar2 = wcrtomb(acStack_3c,L'\0',param_1);
  if (__dataset != (__locale_t)0x0) {
                    /* try { // try from 00baba00 to 00caba17 has its CatchHandler @ 00babc6c */
    uselocale(__dataset);
  }
  if (sVar2 + 1 < 2) {
    uVar3 = 2;
  }
  else {
    uVar4 = sVar2 - 1;
    if ((ulong)((long)param_3 - (long)*param_4) < uVar4) {
      uVar3 = 1;
    }
    else {
      if (uVar4 != 0) {
        pcVar5 = acStack_3c;
        do {
          pcVar6 = *param_4;
          cVar1 = *pcVar5;
                    /* try { // try from 00baba44 to 00caba63 has its CatchHandler @ 00babbfc */
          uVar4 = uVar4 - 1;
          *param_4 = pcVar6 + 1;
          *pcVar6 = cVar1;
          pcVar5 = pcVar5 + 1;
        } while (uVar4 != 0);
      }
      uVar3 = 0;
    }
  }
                    /* try { // try from 00baba64 to 00cabb57 has its CatchHandler @ 00bab67c */
  return uVar3;
}

~~~
