# 00afbdf0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbdf0",
  "name": "FUN_00afbdf0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9afb05e61b3bd6b16e27b546b4d2605b3ff72d53bb68de214b9eb8b14f119a3f",
  "source_text_sha256": "9afb05e61b3bd6b16e27b546b4d2605b3ff72d53bb68de214b9eb8b14f119a3f"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afbdf0(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbe0c to 00bfbf97 has its CatchHandler @ 00afbbcc */
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a34) = param_3 & 1;
  return;
}

~~~
