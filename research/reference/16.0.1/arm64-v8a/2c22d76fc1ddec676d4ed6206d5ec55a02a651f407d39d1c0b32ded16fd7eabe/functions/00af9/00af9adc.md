# 00af9adc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af9adc",
  "name": "FUN_00af9adc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "826d4998c96ade6bec67f8313afdeedcba50f01e652b16bd2293cfe24038ad59",
  "source_text_sha256": "826d4998c96ade6bec67f8313afdeedcba50f01e652b16bd2293cfe24038ad59"
}
~~~

## 呼び出し元

- [00713d24](../00713/00713d24.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af9adc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849a8);
}

~~~
