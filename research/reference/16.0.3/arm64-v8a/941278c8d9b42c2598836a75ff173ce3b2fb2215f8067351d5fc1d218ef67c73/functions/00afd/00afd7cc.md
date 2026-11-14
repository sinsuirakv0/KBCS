# 00afd7cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afd7cc",
  "name": "FUN_00afd7cc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9697f89d686e5e4c999b5451779abc470a577e439b61e8d81c1e0568717109c5",
  "source_text_sha256": "9697f89d686e5e4c999b5451779abc470a577e439b61e8d81c1e0568717109c5"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 288 bytes

~~~c

undefined4 FUN_00afd7cc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afd7f4 to 00bfd817 has its CatchHandler @ 00afdb68 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b6c);
}

~~~
