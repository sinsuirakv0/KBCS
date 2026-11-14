# 00afdea4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdea4",
  "name": "FUN_00afdea4",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a6ffd7fb1fd60994d7dfbe345810a9aa275f8a8b0138550ebc0b063bc070d76",
  "source_text_sha256": "5a6ffd7fb1fd60994d7dfbe345810a9aa275f8a8b0138550ebc0b063bc070d76"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afdea4(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84c70) = *(int *)(lVar1 + 0x84c70) + param_3;
  return;
}

~~~
