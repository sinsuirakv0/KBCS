# 00afaddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afaddc",
  "name": "FUN_00afaddc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c662995c24288112bd9009ff3b1642f402a918aececf5a66d4813b29107a4846",
  "source_text_sha256": "c662995c24288112bd9009ff3b1642f402a918aececf5a66d4813b29107a4846"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 542 bytes

~~~c

void FUN_00afaddc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a80) = param_3 & 1;
  }
                    /* try { // try from 00afae40 to 00bfae43 has its CatchHandler @ 00afaeb4 */
                    /* try { // try from 00afae44 to 00bfaedf has its CatchHandler @ 00afad10 */
  return;
}

~~~
