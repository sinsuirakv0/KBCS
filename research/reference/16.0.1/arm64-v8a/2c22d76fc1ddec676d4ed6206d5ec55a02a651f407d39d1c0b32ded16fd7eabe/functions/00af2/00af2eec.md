# 00af2eec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af2eec",
  "name": "FUN_00af2eec",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08b5b7d4a4fde2f2690bd9e6d317d33820ec21cdc83473befed0509f64446118",
  "source_text_sha256": "08b5b7d4a4fde2f2690bd9e6d317d33820ec21cdc83473befed0509f64446118"
}
~~~

## 呼び出し元

- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 181 bytes

~~~c

void FUN_00af2eec(int param_1,undefined4 param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x8491c) = param_2;
  return;
}

~~~
