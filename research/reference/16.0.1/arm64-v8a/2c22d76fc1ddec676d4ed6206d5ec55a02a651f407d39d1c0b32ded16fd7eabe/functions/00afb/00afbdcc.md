# 00afbdcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afbdcc",
  "name": "FUN_00afbdcc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c02f2f6914ffd49f732d168f27f3c8453157e9e76e635ab765a0e3290e33730d",
  "source_text_sha256": "c02f2f6914ffd49f732d168f27f3c8453157e9e76e635ab765a0e3290e33730d"
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)
- [00707ee0](../00707/00707ee0.md)
- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)
- [00715500](../00715/00715500.md)
- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afbdcc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f4);
}

~~~
