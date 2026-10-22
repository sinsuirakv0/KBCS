# 00a9beac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a9beac.md)

## 関数情報

~~~json
{
  "address": "00a9beac",
  "name": "FUN_00a9beac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "34c23157072a9fb343e5f124aa1a86a780a2f8175b1da235abcbcefe5a274091",
  "source_text_sha256": "34c23157072a9fb343e5f124aa1a86a780a2f8175b1da235abcbcefe5a274091"
}
~~~
## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 193 bytes

~~~c

bool FUN_00a9beac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84170) != 0;
}

~~~
