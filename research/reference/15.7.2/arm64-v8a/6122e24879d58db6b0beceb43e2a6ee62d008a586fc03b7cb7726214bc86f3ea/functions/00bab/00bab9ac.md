# 00bab9ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bab9ac",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d938319d40ff8ac555a4534e2d3d1a199eedd1fe340293917a61ca9d142d1fd6",
  "source_text_sha256": "d938319d40ff8ac555a4534e2d3d1a199eedd1fe340293917a61ca9d142d1fd6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a50](../00be1/00be1a50.md)

## 疑似コード / UTF-8 1336 bytes

~~~c

undefined8
_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_
          (long param_1,mbstate_t *param_2,long param_3,long param_4,long *param_5)

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
  
  *param_5 = param_3;
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  local_38 = __dataset;
  sVar2 = wcrtomb(acStack_3c,L'\0',param_2);
  if (__dataset != (__locale_t)0x0) {
                    /* try { // try from 00baba00 to 00caba17 has its CatchHandler @ 00babc6c */
    uselocale(__dataset);
  }
  if (sVar2 + 1 < 2) {
    uVar3 = 2;
  }
  else {
    uVar4 = sVar2 - 1;
    if ((ulong)(param_4 - *param_5) < uVar4) {
      uVar3 = 1;
    }
    else {
      if (uVar4 != 0) {
        pcVar5 = acStack_3c;
        do {
          pcVar6 = (char *)*param_5;
          cVar1 = *pcVar5;
                    /* try { // try from 00baba44 to 00caba63 has its CatchHandler @ 00babbfc */
          uVar4 = uVar4 - 1;
          *param_5 = (long)(pcVar6 + 1);
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
