# 00afccf0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afccf0",
  "name": "FUN_00afccf0",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3b9daa5775de6d6d1e0648486824d2222ef19c51ca114fe7ac4da7857c144389",
  "source_text_sha256": "3b9daa5775de6d6d1e0648486824d2222ef19c51ca114fe7ac4da7857c144389"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afccf0(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x849c0) = *(int *)(lVar1 + 0x849c0) + param_3;
  return;
}

~~~
