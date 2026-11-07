# 00ba3eac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00ba3da0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba3/00ba3da0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00ba3eac",
  "name": "FUN_00ba3eac",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4464f4e206e1fd7bec586fd192a0e913dfeed4272346a817c13771c36c45b79c",
  "source_text_sha256": "4464f4e206e1fd7bec586fd192a0e913dfeed4272346a817c13771c36c45b79c"
}
~~~

## 呼び出し元

- [00ba261c](../00ba2/00ba261c.md)
- [00ba4ab8](../00ba4/00ba4ab8.md)

## 呼び出し先

- [00be18f0](../00be1/00be18f0.md)

## 疑似コード / UTF-8 599 bytes

~~~c

void FUN_00ba3eac(long *param_1,byte *param_2,long param_3)

{
  byte *pbVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk117moneypunct_bynameIcLb1EEE_00c1bf70 + 0x10);
  param_1[1] = param_3 + -1;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
  }
  _ZNSt6__ndk117moneypunct_bynameIcLb1EE4initEPKc(param_1,pbVar1);
  return;
}

~~~
