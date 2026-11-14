# 00af5fbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af5fbc",
  "name": "FUN_00af5fbc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99e850e20718cb4c6003f594eb75af7ae077132578f80defb5467ee671e26adc",
  "source_text_sha256": "99e850e20718cb4c6003f594eb75af7ae077132578f80defb5467ee671e26adc"
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)
- [00715908](../00715/00715908.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af5fbc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ac4);
}

~~~
