# 00afb6dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afb6dc",
  "name": "FUN_00afb6dc",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fb167a795ade8fc4dd55c5233f7c30b6907f99e8dbec20249240b697e7a2c95",
  "source_text_sha256": "3fb167a795ade8fc4dd55c5233f7c30b6907f99e8dbec20249240b697e7a2c95"
}
~~~

## 呼び出し元

- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 492 bytes

~~~c

undefined4 FUN_00afb6dc(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00afb6dc to 00bfb7bb has its CatchHandler @ 00afaee0 */
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_008524fc();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c0c);
  }
  return uVar1;
}

~~~
