# 00aaefdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aaf0e8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf0e8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aaefdc",
  "name": "FUN_00aaefdc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18a316590f89e48711067541018de778bf8f65b796131c55c9ad510006c232b2",
  "source_text_sha256": "18a316590f89e48711067541018de778bf8f65b796131c55c9ad510006c232b2"
}
~~~

## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d518](../0045d/0045d518.md)

## 疑似コード / UTF-8 206 bytes

~~~c

void FUN_00aaefdc(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  
  uVar1 = FUN_0045d518(param_2);
  *param_1 = uVar1;
  uVar1 = FUN_0045d518(param_2);
  param_1[1] = uVar1;
  return;
}

~~~
