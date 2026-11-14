# 00afc3dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afc3dc",
  "name": "FUN_00afc3dc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c14002711c92c25083703920e7fd63e90fd6ad142caaedcdd047ea7c4753f8c",
  "source_text_sha256": "2c14002711c92c25083703920e7fd63e90fd6ad142caaedcdd047ea7c4753f8c"
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 441 bytes

~~~c

bool FUN_00afc3dc(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc058 with catch @ 00afc3dc
                       catch() { ... } // from try @ 00afc134 with catch @ 00afc3dc */
                    /* catch() { ... } // from try @ 00afbdc0 with catch @ 00afc3ec */
  lVar1 = FUN_008524fc();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b94) != 0;
}

~~~
