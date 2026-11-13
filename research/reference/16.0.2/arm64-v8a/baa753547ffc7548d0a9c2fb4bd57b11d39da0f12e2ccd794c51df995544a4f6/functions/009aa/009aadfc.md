# 009aadfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009aadfc",
  "name": "FUN_009aadfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e37cd428056f67c48765ed97866d71edeede6a02ae66b09ed26f411cb3c16da0",
  "source_text_sha256": "e37cd428056f67c48765ed97866d71edeede6a02ae66b09ed26f411cb3c16da0"
}
~~~

## 呼び出し元

- [009afefc](../009af/009afefc.md)
- [009b5db8](../009b5/009b5db8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009aadfc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x38);
  uVar1 = *(undefined4 *)(param_2 + 0x48);
  param_1[1] = *(undefined8 *)(param_2 + 0x40);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~
