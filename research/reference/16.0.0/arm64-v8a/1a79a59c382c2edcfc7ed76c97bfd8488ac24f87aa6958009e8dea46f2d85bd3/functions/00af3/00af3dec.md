# 00af3dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af3dec",
  "name": "FUN_00af3dec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "189650ce466002a521ca39087c4dac6ba3e2d4f348540d0281673a9c2c78e0ed",
  "source_text_sha256": "189650ce466002a521ca39087c4dac6ba3e2d4f348540d0281673a9c2c78e0ed"
}
~~~

## 呼び出し元

- [005f7900](../005f7/005f7900.md)
- [005f87e0](../005f8/005f87e0.md)
- [005f8e40](../005f8/005f8e40.md)
- [005f9670](../005f9/005f9670.md)
- [005fb400](../005fb/005fb400.md)
- [005fdc18](../005fd/005fdc18.md)
- [00700ab8](../00700/00700ab8.md)
- [00713318](../00713/00713318.md)
- [0071421c](../00714/0071421c.md)
- [00714f4c](../00714/00714f4c.md)
- [007154c0](../00715/007154c0.md)
- [00716b40](../00716/00716b40.md)
- [00716d50](../00716/00716d50.md)
- [00a51dcc](../00a51/00a51dcc.md)
- [00af2460](../00af2/00af2460.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af3dec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848d4);
}

~~~
