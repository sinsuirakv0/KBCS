# 008eaecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008eaecc",
  "name": "FUN_008eaecc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a683201318bba6f005ed96c2dd9d61c9503d86ee34c21c90c8f105a4d2da0f5",
  "source_text_sha256": "4a683201318bba6f005ed96c2dd9d61c9503d86ee34c21c90c8f105a4d2da0f5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_008eaecc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c857d0;
  puVar1[1] = uVar2;
  return;
}

~~~
