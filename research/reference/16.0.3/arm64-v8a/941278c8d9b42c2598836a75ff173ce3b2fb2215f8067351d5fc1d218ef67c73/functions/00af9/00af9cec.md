# 00af9cec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af9cec",
  "name": "FUN_00af9cec",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44b4ba221680d0c6d8fd333f82a3857452a871ee828d6dd43076ba5d83e64427",
  "source_text_sha256": "44b4ba221680d0c6d8fd333f82a3857452a871ee828d6dd43076ba5d83e64427"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00af9cec(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84cb0) = param_3;
  return;
}

~~~
