# 00afbba0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbba0",
  "name": "FUN_00afbba0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efd86632ff69ed9d592df1539c26b8c5b82e630b34e2c8182b7ecc4df932351d",
  "source_text_sha256": "efd86632ff69ed9d592df1539c26b8c5b82e630b34e2c8182b7ecc4df932351d"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 978 bytes

~~~c

void FUN_00afbba0(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afbbcc to 00bfbc67 has its CatchHandler @ 00afbbcc
                       catch() { ... } // from try @ 00afbbcc with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbc80 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbd40 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbe0c with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbfa8 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afbff8 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afc0a4 with catch @ 00afbbcc
                       catch() { ... } // from try @ 00afc180 with catch @ 00afbbcc */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a24) = param_3 & 1;
  return;
}

~~~
