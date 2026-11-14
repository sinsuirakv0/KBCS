# 00afcb8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcb8c",
  "name": "FUN_00afcb8c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f8e7a3fa2f8b8c43940aa86c6e9503b86c48d66349b254a22c99cea1d8f8456",
  "source_text_sha256": "3f8e7a3fa2f8b8c43940aa86c6e9503b86c48d66349b254a22c99cea1d8f8456"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [007106e0](../00710/007106e0.md)
- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00afcb8c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afcbac to 00bfcbbf has its CatchHandler @ 00afdcb0 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849d0) = param_3;
  return;
}

~~~
