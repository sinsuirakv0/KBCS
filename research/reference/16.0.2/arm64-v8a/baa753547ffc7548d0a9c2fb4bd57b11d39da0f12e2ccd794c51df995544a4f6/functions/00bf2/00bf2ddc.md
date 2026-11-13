# 00bf2ddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf2ddc",
  "name": "_ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d",
  "source_text_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58520](../00c58/00c58520.md)

## 疑似コード / UTF-8 848 bytes

~~~c

long _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm
               (byte *param_1,wchar_t *param_2,ulong param_3,size_t param_4)

{
  ulong uVar1;
  byte *pbVar2;
  wchar_t *pwVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  uVar1 = (ulong)(*param_1 >> 1);
  pbVar2 = param_1 + 4;
  if ((*param_1 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
    pbVar2 = *(byte **)(param_1 + 0x10);
  }
  if (param_3 < uVar1) {
    pwVar4 = (wchar_t *)(pbVar2 + param_3 * 4);
    if (param_4 == 0) {
LAB_00bf2e58:
      return (long)pwVar4 - (long)pbVar2 >> 2;
    }
    lVar5 = uVar1 * 4 + param_3 * -4;
    do {
      pwVar3 = wmemchr(param_2,*pwVar4,param_4);
      if (pwVar3 == (wchar_t *)0x0) goto LAB_00bf2e58;
      lVar5 = lVar5 + -4;
      pwVar4 = pwVar4 + 1;
    } while (lVar5 != 0);
  }
  return -1;
}

~~~
