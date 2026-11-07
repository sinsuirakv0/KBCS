# 005bcdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `005bcdec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bc/005bcdec.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "005bcdec",
  "name": "FUN_005bcdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758",
  "source_text_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758"
}
~~~

## 呼び出し元

- [006ee6c8](../006ee/006ee6c8.md)
- [009f4ab8](../009f4/009f4ab8.md)
- [009f5650](../009f5/009f5650.md)

## 呼び出し先

- [005bc280](../005bc/005bc280.md)

## 疑似コード / UTF-8 95 bytes

~~~c

bool FUN_005bcdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005bc280();
  return iVar1 != -1;
}

~~~
