# 00baeef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baeffc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baeffc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baeef0",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09b384e18a6609c00cca071b8e35e0a93c16a6eb388a516e91789b0591b160d7",
  "source_text_sha256": "09b384e18a6609c00cca071b8e35e0a93c16a6eb388a516e91789b0591b160d7"
}
~~~

## 呼び出し元

- [00be1710](../00be1/00be1710.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c1beb8;
  *(undefined2 *)(param_1 + 2) = 0x2c2e;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~
