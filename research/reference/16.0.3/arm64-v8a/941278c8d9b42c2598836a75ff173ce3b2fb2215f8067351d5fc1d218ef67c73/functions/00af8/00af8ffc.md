# 00af8ffc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af8ffc",
  "name": "FUN_00af8ffc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "561020b9b33895de455c4722dd0a9c31225f02820e60442de8e348868b48d1fe",
  "source_text_sha256": "561020b9b33895de455c4722dd0a9c31225f02820e60442de8e348868b48d1fe"
}
~~~

## 呼び出し元

- [007106e0](../00710/007106e0.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 288 bytes

~~~c

undefined4 FUN_00af8ffc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00af9030 to 00bf903b has its CatchHandler @ 00af9538 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af0);
}

~~~
