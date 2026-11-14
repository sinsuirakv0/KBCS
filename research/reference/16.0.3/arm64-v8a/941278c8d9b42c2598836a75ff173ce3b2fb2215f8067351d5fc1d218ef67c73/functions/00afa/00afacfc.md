# 00afacfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afacfc",
  "name": "FUN_00afacfc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea17b44cb1ddd2d1712ab153a740655ee88bfd1f8135a585c567974cf12edf84",
  "source_text_sha256": "ea17b44cb1ddd2d1712ab153a740655ee88bfd1f8135a585c567974cf12edf84"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 697 bytes

~~~c

void FUN_00afacfc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
                    /* try { // try from 00afad10 to 00bfadab has its CatchHandler @ 00afad10
                       catch() { ... } // from try @ 00afad10 with catch @ 00afad10
                       catch() { ... } // from try @ 00afadb0 with catch @ 00afad10
                       catch() { ... } // from try @ 00afae44 with catch @ 00afad10 */
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) = param_3 & 1;
  }
  return;
}

~~~
