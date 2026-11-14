# 00afae4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afae4c",
  "name": "FUN_00afae4c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ee27bd8fcc2229d4de27830353f66ac2c5b9de74bc40608f4761fc7102e39d9",
  "source_text_sha256": "4ee27bd8fcc2229d4de27830353f66ac2c5b9de74bc40608f4761fc7102e39d9"
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 559 bytes

~~~c

bool FUN_00afae4c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008524fc();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) != 0;
  }
                    /* catch() { ... } // from try @ 00afae40 with catch @ 00afaeb4 */
                    /* catch() { ... } // from try @ 00afadac with catch @ 00afaeb8 */
  return bVar1;
}

~~~
