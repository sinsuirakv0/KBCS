# 00afda0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afda0c",
  "name": "FUN_00afda0c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e393149512a81e6017562975e813c2b5d45ec37e887727ac144c1ef64bcc080",
  "source_text_sha256": "7e393149512a81e6017562975e813c2b5d45ec37e887727ac144c1ef64bcc080"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 565 bytes

~~~c

void FUN_00afda0c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afd478 with catch @ 00afda10 */
                    /* catch() { ... } // from try @ 00afd364 with catch @ 00afda14 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd254 with catch @ 00afda30 */
                    /* catch() { ... } // from try @ 00afd138 with catch @ 00afda34 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc4) = param_3;
  return;
}

~~~
