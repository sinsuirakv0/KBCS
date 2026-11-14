# 00bfaca8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfaca8",
  "name": "_ZNSt6__ndk16futureIvE3getEv",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8de37edde5b4f2c2adbca127bf913a7b4c2868870ef6822edd44a669a7e018ab",
  "source_text_sha256": "8de37edde5b4f2c2adbca127bf913a7b4c2868870ef6822edd44a669a7e018ab"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c54d90](../00c54/00c54d90.md)
- [00c5f300](../00c5f/00c5f300.md)

## 疑似コード / UTF-8 494 bytes

~~~c

void _ZNSt6__ndk16futureIvE3getEv(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)*param_1;
  *param_1 = 0;
  _ZNSt6__ndk117__assoc_sub_state4copyEv(plVar2);
  lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1);
  if (lVar1 != 0) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfad00. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar2 + 0x10))(plVar2);
  return;
}

~~~
