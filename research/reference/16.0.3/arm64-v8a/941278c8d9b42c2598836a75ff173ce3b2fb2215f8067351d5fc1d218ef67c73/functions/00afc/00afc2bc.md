# 00afc2bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afc2bc",
  "name": "FUN_00afc2bc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5dc38483fb630d5c72a87303befc9cc56270ebbac262e9cdebbf483310c3e71a",
  "source_text_sha256": "5dc38483fb630d5c72a87303befc9cc56270ebbac262e9cdebbf483310c3e71a"
}
~~~

## 呼び出し元

- [005f3e60](../005f3/005f3e60.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afc2bc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b68);
}

~~~
