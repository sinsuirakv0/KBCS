# 008abcdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008abcdc",
  "name": "FUN_008abcdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81ffe01f23a36b7a4c85ba732a44ca40c6a3bbf708f1b4b7c423ba43abb3d2b0",
  "source_text_sha256": "81ffe01f23a36b7a4c85ba732a44ca40c6a3bbf708f1b4b7c423ba43abb3d2b0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_008abcdc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c83630;
  param_2[1] = uVar1;
  return;
}

~~~
