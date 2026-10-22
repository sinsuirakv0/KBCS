# 005bcdec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](005bcdec.md)

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
  "source_sha256": "4eba31452ea1bf2fce406d0a5bf0999c1c491ff7f6f83c9f1bc01c4b43daad38",
  "source_text_sha256": "4eba31452ea1bf2fce406d0a5bf0999c1c491ff7f6f83c9f1bc01c4b43daad38"
}
~~~
## 呼び出し元

- [006ee6c8](../006ee/006ee6c8.md)
- [009f4a74](../009f4/009f4a74.md)
- [009f560c](../009f5/009f560c.md)

## 呼び出し先

- [005bc280](../005bc/005bc280.md)

## 疑似コード 1/1 / UTF-8 105 bytes

~~~c

bool FUN_005bcdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005bc280();
  return iVar1 != -1;
}

~~~
