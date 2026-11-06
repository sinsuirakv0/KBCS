# 00baef1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baef1c",
  "name": "_ZNSt6__ndk18numpunctIwEC2Em",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "011ac845cff15c6a87662bd3df46817877a99719792cb98f6a4912b46bd5ce03",
  "source_text_sha256": "011ac845cff15c6a87662bd3df46817877a99719792cb98f6a4912b46bd5ce03"
}
~~~

## 呼び出し元

- [00be1720](../00be1/00be1720.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk18numpunctIwEC2Em(long *param_1,long param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bec0;
  lVar1 = DAT_002b2b98;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  param_1[2] = lVar1;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~
