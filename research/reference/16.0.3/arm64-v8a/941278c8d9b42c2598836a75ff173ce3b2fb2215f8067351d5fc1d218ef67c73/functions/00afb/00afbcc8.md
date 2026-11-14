# 00afbcc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbcc8",
  "name": "FUN_00afbcc8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f90ebe15a2edfc22cce08d54613679f53edd40a486bbd3e75e4bb95c75b40f40",
  "source_text_sha256": "f90ebe15a2edfc22cce08d54613679f53edd40a486bbd3e75e4bb95c75b40f40"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afbcc8(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a2c) = param_3 & 1;
  return;
}

~~~
