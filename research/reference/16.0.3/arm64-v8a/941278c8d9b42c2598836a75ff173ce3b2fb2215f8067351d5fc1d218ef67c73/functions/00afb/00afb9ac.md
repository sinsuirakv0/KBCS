# 00afb9ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afb9ac",
  "name": "FUN_00afb9ac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5b318924ebcfb257dd54c1c65a9b436509c605d2802e5319cf2bae6e9237746",
  "source_text_sha256": "c5b318924ebcfb257dd54c1c65a9b436509c605d2802e5319cf2bae6e9237746"
}
~~~

## 呼び出し元

- [0071412c](../00714/0071412c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afb9ac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afb1c8 with catch @ 00afb9cc */
                    /* catch() { ... } // from try @ 00afb138 with catch @ 00afb9d0 */
                    /* catch() { ... } // from try @ 00afb8c8 with catch @ 00afb9d8 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca0);
}

~~~
