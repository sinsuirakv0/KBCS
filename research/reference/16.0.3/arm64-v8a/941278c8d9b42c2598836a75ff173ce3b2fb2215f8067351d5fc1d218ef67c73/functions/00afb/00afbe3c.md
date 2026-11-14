# 00afbe3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afbe3c",
  "name": "FUN_00afbe3c",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2add6f81c0b0de3a42f06737ea685f233c252cee298beae90b173cb0e75a238b",
  "source_text_sha256": "2add6f81c0b0de3a42f06737ea685f233c252cee298beae90b173cb0e75a238b"
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)
- [00700f00](../00700/00700f00.md)
- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afbe3c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a84) != 0;
}

~~~
