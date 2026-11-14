# 007fdbdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007fdbdc",
  "name": "FUN_007fdbdc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e4960e8c0b48b304aec8886ff5110f32c6769b1f09a340d2b54f902c77a7064",
  "source_text_sha256": "0e4960e8c0b48b304aec8886ff5110f32c6769b1f09a340d2b54f902c77a7064"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008524fc](../00852/008524fc.md)
- [008ba17c](../008ba/008ba17c.md)

## 疑似コード / UTF-8 897 bytes

~~~c

void FUN_007fdbdc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined4 uVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  if ((*param_3 == 2) && (*param_4 != -1)) {
    uVar4 = *param_2;
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,0xb,0);
    FUN_008ba17c(uVar4);
    return;
  }
  if ((*param_3 == 5) && (*param_4 == 0)) {
    lVar3 = FUN_008524fc();
    *(int *)((long)&fde_table_entry_00333de0.initial_loc + lVar3) =
         *(int *)((long)&fde_table_entry_00333de0.initial_loc + lVar3) + 1;
    lVar3 = FUN_008524fc();
    *(undefined4 *)((long)&fde_table_entry_00335f48.initial_loc + lVar3) = 0;
    lVar3 = FUN_008524fc();
    uVar1 = *(undefined4 *)(param_1 + 8);
    *(undefined4 *)(&uleb128_0029a6d8 + lVar3) = 0;
    lVar3 = FUN_008524fc();
    *(undefined4 *)((long)&fde_table_entry_00336eb0.initial_loc + lVar3) = uVar1;
  }
  return;
}

~~~
