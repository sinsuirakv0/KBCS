# 00afcacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afcacc",
  "name": "FUN_00afcacc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32b9d613465bec2e58f55d712010ef5a96996ef9cdb1127621fb173f7348e4ce",
  "source_text_sha256": "32b9d613465bec2e58f55d712010ef5a96996ef9cdb1127621fb173f7348e4ce"
}
~~~

## 呼び出し元

- [00710298](../00710/00710298.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00afcacc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbcd8 with catch @ 00afcadc */
  lVar1 = FUN_008514b8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc778 with catch @ 00afcafc */
  *(int *)(lVar1 + 0x84ca8) = *(int *)(lVar1 + 0x84ca8) + param_3;
                    /* catch() { ... } // from try @ 00afba10 with catch @ 00afcb14 */
  return;
}

~~~
