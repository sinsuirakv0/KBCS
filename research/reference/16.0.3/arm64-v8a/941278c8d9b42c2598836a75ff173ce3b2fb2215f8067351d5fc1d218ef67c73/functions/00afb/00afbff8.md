# 00afbff8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbff8",
  "name": "FUN_00afbff8",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "592b529ab0e1aa02107ce37eb0f216899fa9340abb5a623ba32702280c976c58",
  "source_text_sha256": "592b529ab0e1aa02107ce37eb0f216899fa9340abb5a623ba32702280c976c58"
}
~~~

## 呼び出し元

- [005fbd2c](../005fb/005fbd2c.md)
- [00700f00](../00700/00700f00.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 288 bytes

~~~c

undefined4 FUN_00afbff8(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afbff8 to 00bfc057 has its CatchHandler @ 00afbbcc */
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad0);
}

~~~
