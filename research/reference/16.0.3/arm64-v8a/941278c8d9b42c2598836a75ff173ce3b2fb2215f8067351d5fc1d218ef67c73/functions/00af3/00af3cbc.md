# 00af3cbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af3cbc",
  "name": "FUN_00af3cbc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb327b379a09439848faad4b300ba65acc51747d888e72c618a9d58865b8fefa",
  "source_text_sha256": "eb327b379a09439848faad4b300ba65acc51747d888e72c618a9d58865b8fefa"
}
~~~

## 呼び出し元

- [00a48f48](../00a48/00a48f48.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 181 bytes

~~~c

void FUN_00af3cbc(int param_1,undefined4 param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x84908) = param_2;
  return;
}

~~~
