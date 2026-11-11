# 00afdab8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afdab8",
  "name": "FUN_00afdab8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa7cafa80eb80c937228a639376bdca9758024d20bb5b0bc91eec2afddb4c307",
  "source_text_sha256": "fa7cafa80eb80c937228a639376bdca9758024d20bb5b0bc91eec2afddb4c307"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afdab8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b3c) = param_3;
  return;
}

~~~
