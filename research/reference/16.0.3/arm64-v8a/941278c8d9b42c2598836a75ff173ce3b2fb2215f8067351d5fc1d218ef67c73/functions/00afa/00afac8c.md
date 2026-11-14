# 00afac8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afac8c",
  "name": "FUN_00afac8c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "590cf423cbb1cc908154c8580d8c1813059da794dc47bfcc72211bb3ea432de6",
  "source_text_sha256": "590cf423cbb1cc908154c8580d8c1813059da794dc47bfcc72211bb3ea432de6"
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 907 bytes

~~~c

bool FUN_00afac8c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
                    /* catch() { ... } // from try @ 00afaa68 with catch @ 00afac94 */
  lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afaa98 with catch @ 00afacac */
                    /* catch() { ... } // from try @ 00afa9f0 with catch @ 00afacb0 */
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
                    /* catch() { ... } // from try @ 00afaa50 with catch @ 00afacc0 */
  }
  else {
                    /* catch() { ... } // from try @ 00afaa34 with catch @ 00afacc4 */
                    /* catch() { ... } // from try @ 00afa9d4 with catch @ 00afacc8 */
    lVar2 = FUN_008524fc();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) != 0;
  }
  return bVar1;
}

~~~
