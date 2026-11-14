# 00afd3dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afd3dc",
  "name": "FUN_00afd3dc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0101e8fa9b244f8ff9ecb83ef5d72bcf99d5c9bbc509eac76f14cf3db379b35",
  "source_text_sha256": "b0101e8fa9b244f8ff9ecb83ef5d72bcf99d5c9bbc509eac76f14cf3db379b35"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afd3dc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84ae0) = *(int *)(lVar1 + 0x84ae0) + param_3;
  return;
}

~~~
