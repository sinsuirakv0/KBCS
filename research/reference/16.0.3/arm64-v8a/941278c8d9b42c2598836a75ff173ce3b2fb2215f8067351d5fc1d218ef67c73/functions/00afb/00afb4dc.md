# 00afb4dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afb4dc",
  "name": "FUN_00afb4dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b589130ba33e9555814d0b3e1feae45ae94a479a32ebbdda27dcfe358160e5d6",
  "source_text_sha256": "b589130ba33e9555814d0b3e1feae45ae94a479a32ebbdda27dcfe358160e5d6"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)
- [00af45e4](../00af4/00af45e4.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afb4dc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afb4e0 to 00bfb5c3 has its CatchHandler @ 00afaee0 */
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84be0) = param_3 & 1;
  return;
}

~~~
