# 00afcaf8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcaf8",
  "name": "FUN_00afcaf8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd9e072b5ee407f4107f4843769cd76b5063d8877449ab8efa042d750eec4788",
  "source_text_sha256": "fd9e072b5ee407f4107f4843769cd76b5063d8877449ab8efa042d750eec4788"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afcaf8(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x849bc) = *(int *)(lVar1 + 0x849bc) + param_3;
  return;
}

~~~
