# 00afdbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdbc4",
  "name": "FUN_00afdbc4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8596dd132e5f6692774df78ab1b1168e433a802692a80b82e12db141ec15ce8f",
  "source_text_sha256": "8596dd132e5f6692774df78ab1b1168e433a802692a80b82e12db141ec15ce8f"
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 620 bytes

~~~c

undefined4 FUN_00afdbc4(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afd460 with catch @ 00afdbd4
                       catch() { ... } // from try @ 00afd544 with catch @ 00afdbd4 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd278 with catch @ 00afdbe4 */
                    /* catch() { ... } // from try @ 00afd234 with catch @ 00afdbfc
                       catch() { ... } // from try @ 00afd328 with catch @ 00afdbfc */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bd4);
}

~~~
