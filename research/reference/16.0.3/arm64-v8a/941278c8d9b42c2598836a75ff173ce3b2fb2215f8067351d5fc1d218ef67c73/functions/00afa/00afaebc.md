# 00afaebc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afaebc",
  "name": "FUN_00afaebc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "320c2ea425f59d224fc88c94bd1286f5fdf336962d7774b1b4ad3351ab356a1a",
  "source_text_sha256": "320c2ea425f59d224fc88c94bd1286f5fdf336962d7774b1b4ad3351ab356a1a"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 1537 bytes

~~~c

void FUN_00afaebc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afaee0 to 00bfafd3 has its CatchHandler @ 00afaee0
                       catch() { ... } // from try @ 00afaee0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afaffc with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb080 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb0d0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb244 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb2ec with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb33c with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb404 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb4e0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb610 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb6dc with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb820 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb8ec with catch @ 00afaee0 */
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) = param_3 & 1;
  }
  return;
}

~~~
