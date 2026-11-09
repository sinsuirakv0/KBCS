# 00afa4ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afa4ac",
  "name": "FUN_00afa4ac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2781fa79ab4d0938bae33234ed33149b0d7fa2a252ddfe648eb8b58019ec52af",
  "source_text_sha256": "2781fa79ab4d0938bae33234ed33149b0d7fa2a252ddfe648eb8b58019ec52af"
}
~~~

## 呼び出し元

- [00713ce4](../00713/00713ce4.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afa4ac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca0) != 0;
}

~~~
