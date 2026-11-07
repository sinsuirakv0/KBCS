# 00b7dddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b7dee8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b7dddc",
  "name": "_ZNSt6__ndk113random_deviceD2Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e62a244198d58329791df076882efe4b1e9a2d4fd9d89499753a099b8e5417e2",
  "source_text_sha256": "e62a244198d58329791df076882efe4b1e9a2d4fd9d89499753a099b8e5417e2"
}
~~~

## 呼び出し元

- [00bdb480](../00bdb/00bdb480.md)

## 呼び出し先

- [00bdc880](../00bdc/00bdc880.md)

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD2Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~
