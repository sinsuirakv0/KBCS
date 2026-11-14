# 00af5edc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af5edc",
  "name": "FUN_00af5edc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "686ae568dc8e39f2345fe4e1f99d6eed9430615f3b2eec34e3a14a049d39b0c9",
  "source_text_sha256": "686ae568dc8e39f2345fe4e1f99d6eed9430615f3b2eec34e3a14a049d39b0c9"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00af5edc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84a9c) = *(int *)(lVar1 + 0x84a9c) + param_3;
  return;
}

~~~
