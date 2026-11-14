# 00af3aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af3aec",
  "name": "FUN_00af3aec",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95519c5e6fcfa9461e51514cc4f740852f06410117e033e8651900968ec1f2c2",
  "source_text_sha256": "95519c5e6fcfa9461e51514cc4f740852f06410117e033e8651900968ec1f2c2"
}
~~~

## 呼び出し元

- [005f7044](../005f7/005f7044.md)
- [005fe048](../005fe/005fe048.md)
- [00715908](../00715/00715908.md)
- [00a48f48](../00a48/00a48f48.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 155 bytes

~~~c

undefined4 FUN_00af3aec(int param_1)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x848f4);
}

~~~
