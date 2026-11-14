# 00afce5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afce5c",
  "name": "FUN_00afce5c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "777338b8da47b69624b81a5b6ead772ed4e780f9686a7a563dbab475da03b876",
  "source_text_sha256": "777338b8da47b69624b81a5b6ead772ed4e780f9686a7a563dbab475da03b876"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [007082e8](../00708/007082e8.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)
- [00715908](../00715/00715908.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 288 bytes

~~~c

undefined4 FUN_00afce5c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afce74 to 00bfce87 has its CatchHandler @ 00afdc78 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f4);
}

~~~
