# 00a9cbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a9cbfc.md)

## 関数情報

~~~json
{
  "address": "00a9cbfc",
  "name": "FUN_00a9cbfc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "813a2665583b1c4393a6ad8465b4d66279cb28055239f919113b6f7d5a3fe335",
  "source_text_sha256": "813a2665583b1c4393a6ad8465b4d66279cb28055239f919113b6f7d5a3fe335"
}
~~~
## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 183 bytes

~~~c

bool FUN_00a9cbfc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84318) != 0;
}

~~~
