# 00af2ffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af2ffc",
  "name": "FUN_00af2ffc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "144c9cf3795b678088dc5e79eb2743a57c2ca07190b138afcf2a9bde7c7696c7",
  "source_text_sha256": "144c9cf3795b678088dc5e79eb2743a57c2ca07190b138afcf2a9bde7c7696c7"
}
~~~

## 呼び出し元

- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 155 bytes

~~~c

undefined4 FUN_00af2ffc(int param_1)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + 0x84924);
}

~~~
