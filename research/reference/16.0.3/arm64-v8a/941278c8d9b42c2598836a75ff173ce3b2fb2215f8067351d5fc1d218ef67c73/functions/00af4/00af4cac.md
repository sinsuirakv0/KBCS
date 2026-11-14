# 00af4cac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af4cac",
  "name": "FUN_00af4cac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41121f15681433f83c6e65eec7f77eb2b9be8aac356cde2d75516445634f401f",
  "source_text_sha256": "41121f15681433f83c6e65eec7f77eb2b9be8aac356cde2d75516445634f401f"
}
~~~

## 呼び出し元

- [005e0d90](../005e0/005e0d90.md)
- [005e49e8](../005e4/005e49e8.md)
- [005fbd2c](../005fb/005fbd2c.md)
- [006bc0a0](../006bc/006bc0a0.md)
- [00700f00](../00700/00700f00.md)
- [00707d34](../00707/00707d34.md)
- [007082e8](../00708/007082e8.md)
- [00713760](../00713/00713760.md)
- [00715908](../00715/00715908.md)
- [00716e98](../00716/00716e98.md)
- [00716f88](../00716/00716f88.md)
- [00717198](../00717/00717198.md)
- [00720498](../00720/00720498.md)
- [00a52c3c](../00a52/00a52c3c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af4cac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc);
}

~~~
