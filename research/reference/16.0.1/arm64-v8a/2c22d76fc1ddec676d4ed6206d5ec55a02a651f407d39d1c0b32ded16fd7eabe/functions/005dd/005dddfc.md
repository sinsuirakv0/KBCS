# 005dddfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005dddfc",
  "name": "FUN_005dddfc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f110f6c4a6861f73df5ce236634b361ed0f0e91958eb6cc5916130c8aef86f59",
  "source_text_sha256": "f110f6c4a6861f73df5ce236634b361ed0f0e91958eb6cc5916130c8aef86f59"
}
~~~

## 呼び出し元

- [005eba70](../005eb/005eba70.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_005dddfc(undefined1 *param_1)

{
  *param_1 = 0;
  param_1[0x24] = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  param_1[0x30] = 0;
  *(undefined8 *)(param_1 + 0xc) = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 0x1c) = 0;
  *(undefined8 *)(param_1 + 0x14) = 0;
  *(undefined8 *)(param_1 + 0x34) = 0;
  *(undefined4 *)(param_1 + 0x3c) = 0xffffffff;
  return;
}

~~~
