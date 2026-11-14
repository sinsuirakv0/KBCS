# 00afbbec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbbec",
  "name": "FUN_00afbbec",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c03efab653cbf849a66f0d74f4aab58c72373d7570052a91031b1904989cd0a",
  "source_text_sha256": "5c03efab653cbf849a66f0d74f4aab58c72373d7570052a91031b1904989cd0a"
}
~~~

## 呼び出し元

- [007106e0](../00710/007106e0.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afbbec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a28) != 0;
}

~~~
