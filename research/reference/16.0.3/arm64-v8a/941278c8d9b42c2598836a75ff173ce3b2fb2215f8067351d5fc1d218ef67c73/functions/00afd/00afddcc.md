# 00afddcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afddcc",
  "name": "FUN_00afddcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c123e9093b97f93f1e4060a41d34c5ecb2e4bc60c4343a8245e66a51815dd0f0",
  "source_text_sha256": "c123e9093b97f93f1e4060a41d34c5ecb2e4bc60c4343a8245e66a51815dd0f0"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)
- [0070ee64](../0070e/0070ee64.md)
- [00715908](../00715/00715908.md)
- [00717198](../00717/00717198.md)
- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afddcc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c34) = param_3 & 1;
  return;
}

~~~
