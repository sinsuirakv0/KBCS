# 00afcee8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcee8",
  "name": "FUN_00afcee8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3221770afb1ac11177f0385640f53e0bc1b55986b0a1d7bd57176e526f22b6b",
  "source_text_sha256": "c3221770afb1ac11177f0385640f53e0bc1b55986b0a1d7bd57176e526f22b6b"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 442 bytes

~~~c

void FUN_00afcee8(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00afcef0 to 00bfcef3 has its CatchHandler @ 00afdbb0 */
                    /* try { // try from 00afcef4 to 00bfd033 has its CatchHandler @ 00afc44c */
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x849f4) = *(int *)(lVar1 + 0x849f4) + param_3;
  return;
}

~~~
