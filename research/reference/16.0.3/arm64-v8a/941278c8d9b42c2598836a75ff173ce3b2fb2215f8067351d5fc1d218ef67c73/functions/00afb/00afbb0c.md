# 00afbb0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbb0c",
  "name": "FUN_00afbb0c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb628c7f0c4e454a534b7c3276a3e7cd3383c0898566f54975022da2241d4e9a",
  "source_text_sha256": "eb628c7f0c4e454a534b7c3276a3e7cd3383c0898566f54975022da2241d4e9a"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 725 bytes

~~~c

void FUN_00afbb0c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb3b8 with catch @ 00afbb0c
                       catch() { ... } // from try @ 00afb494 with catch @ 00afbb0c */
                    /* catch() { ... } // from try @ 00afb7f8 with catch @ 00afbb10 */
                    /* catch() { ... } // from try @ 00afb7bc with catch @ 00afbb28
                       catch() { ... } // from try @ 00afb8a0 with catch @ 00afbb28 */
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a20) = param_3 & 1;
                    /* catch() { ... } // from try @ 00afb1e4 with catch @ 00afbb54 */
  return;
}

~~~
