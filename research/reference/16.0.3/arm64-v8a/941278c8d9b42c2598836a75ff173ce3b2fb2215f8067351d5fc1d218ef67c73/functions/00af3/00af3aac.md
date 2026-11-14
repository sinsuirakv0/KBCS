# 00af3aac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af3aac",
  "name": "FUN_00af3aac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0571b2e237cc00e3782d927324cae480f63e4321c00cca9fc92059129bcba2a7",
  "source_text_sha256": "0571b2e237cc00e3782d927324cae480f63e4321c00cca9fc92059129bcba2a7"
}
~~~

## 呼び出し元

- [00715908](../00715/00715908.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 212 bytes

~~~c

void FUN_00af3aac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  lVar1 = lVar1 + (long)param_1 * 0xc804;
  *(int *)(lVar1 + 0x848f0) = *(int *)(lVar1 + 0x848f0) + param_2;
  return;
}

~~~
