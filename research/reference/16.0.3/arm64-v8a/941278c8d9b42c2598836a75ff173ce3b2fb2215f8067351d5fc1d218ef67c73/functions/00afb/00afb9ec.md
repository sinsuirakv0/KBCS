# 00afb9ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afb9ec",
  "name": "FUN_00afb9ec",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e007265a18f29f8607a7ea158480179f1d22ce42dafbca85ccaba35e35b488ce",
  "source_text_sha256": "e007265a18f29f8607a7ea158480179f1d22ce42dafbca85ccaba35e35b488ce"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 565 bytes

~~~c

void FUN_00afb9ec(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb7d4 with catch @ 00afb9f4 */
                    /* catch() { ... } // from try @ 00afb6bc with catch @ 00afb9f8 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afb5d0 with catch @ 00afba14 */
                    /* catch() { ... } // from try @ 00afb4bc with catch @ 00afba18 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca0) = param_3;
  return;
}

~~~
