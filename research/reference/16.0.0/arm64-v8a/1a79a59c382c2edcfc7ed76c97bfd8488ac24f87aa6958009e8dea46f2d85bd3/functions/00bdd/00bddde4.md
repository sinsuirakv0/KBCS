# 00bddde4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bddde4",
  "name": "_ZN8firebase4auth4UserC1ERKS1_",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3b9685558555ef792fa4e2e89aa898f8d7f6223f0ab9febcc81a56e3c714b5b",
  "source_text_sha256": "a3b9685558555ef792fa4e2e89aa898f8d7f6223f0ab9febcc81a56e3c714b5b"
}
~~~

## 呼び出し元

- [00c5a640](../00c5a/00c5a640.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 581 bytes

~~~c

void _ZN8firebase4auth4UserC1ERKS1_(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[1] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[0x13] = *(long *)(param_2 + 0x98);
  return;
}

~~~
