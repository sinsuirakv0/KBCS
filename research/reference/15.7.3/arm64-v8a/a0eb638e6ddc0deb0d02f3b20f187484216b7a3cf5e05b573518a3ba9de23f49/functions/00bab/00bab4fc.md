# 00bab4fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bab4fc",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_",
  "size": 668,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "31cb74985d58b875f3df37e6341c9102894a3fa943baaae52575e0e7dff5f013",
  "source_text_sha256": "31cb74985d58b875f3df37e6341c9102894a3fa943baaae52575e0e7dff5f013"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1530](../00be1/00be1530.md)
- [00be1af0](../00be1/00be1af0.md)
- [00be1b00](../00be1/00be1b00.md)

## 疑似コード / UTF-8 3426 bytes

~~~c

undefined1
_ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_
          (long param_1,mbstate_t *param_2,wchar_t *param_3,wchar_t *param_4,wchar_t **param_5,
          char *param_6,char *param_7,long *param_8)

{
  wchar_t *pwVar1;
  wchar_t __wc;
  char cVar2;
  __locale_t p_Var3;
  size_t sVar4;
  char *pcVar5;
  char *pcVar6;
  wchar_t *pwVar7;
  char acStack_74 [4];
  mbstate_t local_70;
  __locale_t local_68;
  
  pwVar7 = param_3;
  for (pwVar1 = param_3; (pwVar1 != param_4 && (pwVar7 = pwVar1, *pwVar1 != L'\0'));
      pwVar1 = pwVar1 + 1) {
    pwVar7 = param_4;
  }
  *param_8 = (long)param_6;
  *param_5 = param_3;
  while( true ) {
    if ((param_3 == param_4) || (param_6 == param_7)) goto LAB_00bab764;
    local_70 = *param_2;
    p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
    local_68 = p_Var3;
    sVar4 = wcsnrtombs(param_6,param_5,(long)pwVar7 - (long)param_3 >> 2,
                       (long)param_7 - (long)param_6,param_2);
    if (p_Var3 != (__locale_t)0x0) {
      uselocale(p_Var3);
    }
    if (sVar4 == 0) {
      return true;
    }
    if (sVar4 == 0xffffffffffffffff) {
      *param_8 = (long)param_6;
      if (param_3 == *param_5) goto LAB_00bab74c;
      goto LAB_00bab6ec;
    }
    param_6 = (char *)(*param_8 + sVar4);
    *param_8 = (long)param_6;
    if (param_6 == param_7) break;
    if (pwVar7 == param_4) {
      param_3 = *param_5;
      pwVar7 = param_4;
    }
    else {
      p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
      local_68 = p_Var3;
      sVar4 = wcrtomb(acStack_74,L'\0',param_2);
      if (p_Var3 != (__locale_t)0x0) {
        uselocale(p_Var3);
      }
      if (sVar4 == 0xffffffffffffffff) {
        return 2;
      }
      if ((ulong)((long)param_7 - *param_8) < sVar4) {
        return true;
      }
      if (sVar4 != 0) {
        pcVar5 = acStack_74;
        do {
          pcVar6 = (char *)*param_8;
          cVar2 = *pcVar5;
          sVar4 = sVar4 - 1;
          *param_8 = (long)(pcVar6 + 1);
          *pcVar6 = cVar2;
          pcVar5 = pcVar5 + 1;
        } while (sVar4 != 0);
      }
      param_3 = *param_5 + 1;
      *param_5 = param_3;
      for (pwVar1 = param_3;
          (pwVar7 = param_4, pwVar1 != param_4 && (pwVar7 = pwVar1, *pwVar1 != L'\0'));
          pwVar1 = pwVar1 + 1) {
      }
      param_6 = (char *)*param_8;
    }
  }
  param_3 = *param_5;
LAB_00bab764:
  return param_3 != param_4;
  while( true ) {
    param_3 = param_3 + 1;
    param_6 = (char *)(*param_8 + sVar4);
    *param_8 = (long)param_6;
                    /* try { // try from 00bab744 to 00cab7bb has its CatchHandler @ 00bab744
                       catch() { ... } // from try @ 00bab744 with catch @ 00bab744
                       catch() { ... } // from try @ 00bab85c with catch @ 00bab744
                       catch() { ... } // from try @ 00bab9ac with catch @ 00bab744
                       catch() { ... } // from try @ 00babb2c with catch @ 00bab744
                       catch() { ... } // from try @ 00babc48 with catch @ 00bab744 */
    if (param_3 == *param_5) break;
LAB_00bab6ec:
    __wc = *param_3;
    p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
    local_68 = p_Var3;
    sVar4 = wcrtomb(param_6,__wc,&local_70);
    if (p_Var3 != (__locale_t)0x0) {
      uselocale(p_Var3);
    }
    if (sVar4 == 0xffffffffffffffff) break;
  }
LAB_00bab74c:
  *param_5 = param_3;
  return 2;
}

~~~
