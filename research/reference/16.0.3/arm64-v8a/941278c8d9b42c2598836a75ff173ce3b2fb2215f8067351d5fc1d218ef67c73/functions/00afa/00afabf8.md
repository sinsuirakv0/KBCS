# 00afabf8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afabf8",
  "name": "FUN_00afabf8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df16392aad6e90fa0a3dba46607e774faeadafc5cdb76828d015878603193f40",
  "source_text_sha256": "df16392aad6e90fa0a3dba46607e774faeadafc5cdb76828d015878603193f40"
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 548 bytes

~~~c

bool FUN_00afabf8(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afac14 to 00bfac1b has its CatchHandler @ 00afac48 */
                    /* catch() { ... } // from try @ 00afab58 with catch @ 00afac1c
                       try { // try from 00afac1c to 00bfad0f has its CatchHandler @ 00afa81c */
                    /* catch() { ... } // from try @ 00afa944 with catch @ 00afac34 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b4) != 0;
}

~~~
