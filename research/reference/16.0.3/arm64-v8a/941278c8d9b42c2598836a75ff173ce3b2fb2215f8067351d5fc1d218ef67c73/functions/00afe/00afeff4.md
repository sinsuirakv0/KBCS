# 00afeff4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afeff4",
  "name": "FUN_00afeff4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91e47803c0dc6e275f138dd70fa138b844afc20b601379e854c7aad48684b348",
  "source_text_sha256": "91e47803c0dc6e275f138dd70fa138b844afc20b601379e854c7aad48684b348"
}
~~~

## 呼び出し元

- [00715908](../00715/00715908.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afeff4(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c90);
}

~~~
