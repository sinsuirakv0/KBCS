# 00afbac4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbac4",
  "name": "FUN_00afbac4",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd814ee285e267aaa4d8e4d68210b682bcd0dad369818ddcd135d30a0fe11ff9",
  "source_text_sha256": "cd814ee285e267aaa4d8e4d68210b682bcd0dad369818ddcd135d30a0fe11ff9"
}
~~~

## 呼び出し元

- [005fbd2c](../005fb/005fbd2c.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 876 bytes

~~~c

bool FUN_00afbac4(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb068 with catch @ 00afbac8 */
                    /* catch() { ... } // from try @ 00afb058 with catch @ 00afbacc */
                    /* catch() { ... } // from try @ 00afafe4 with catch @ 00afbad0 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afafd4 with catch @ 00afbae8 */
                    /* catch() { ... } // from try @ 00afb5f4 with catch @ 00afbb00 */
                    /* catch() { ... } // from try @ 00afb5c4 with catch @ 00afbb04
                       catch() { ... } // from try @ 00afb690 with catch @ 00afbb04 */
                    /* catch() { ... } // from try @ 00afb3e8 with catch @ 00afbb08 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a20) != 0;
}

~~~
