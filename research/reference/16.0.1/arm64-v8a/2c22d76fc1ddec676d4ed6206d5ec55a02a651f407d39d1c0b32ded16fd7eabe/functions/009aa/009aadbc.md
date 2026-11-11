# 009aadbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009aadbc",
  "name": "FUN_009aadbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8610a3fe1d9e68e1183c1ed4e7a486e3c4dcf15d504acfffde30ea102793e510",
  "source_text_sha256": "8610a3fe1d9e68e1183c1ed4e7a486e3c4dcf15d504acfffde30ea102793e510"
}
~~~

## 呼び出し元

- [007644e4](../00764/007644e4.md)
- [009afea8](../009af/009afea8.md)
- [009b5d74](../009b5/009b5d74.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009aadbc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x4c);
  uVar1 = *(undefined4 *)(param_2 + 0x5c);
  param_1[1] = *(undefined8 *)(param_2 + 0x54);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~
