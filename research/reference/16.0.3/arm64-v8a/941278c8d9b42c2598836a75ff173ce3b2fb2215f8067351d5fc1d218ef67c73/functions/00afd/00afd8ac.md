# 00afd8ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afd8ac",
  "name": "FUN_00afd8ac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37ba00998b5ff981e9dd9b08b2cce9f7ff06c57809b2eec295c6b26a44d84c55",
  "source_text_sha256": "37ba00998b5ff981e9dd9b08b2cce9f7ff06c57809b2eec295c6b26a44d84c55"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afd8ac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b7c) != 0;
}

~~~
