# 00aeddc4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aeddc4",
  "name": "FUN_00aeddc4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "29a6cdec043c0b740125962c8299eeabee29f26935ebd78598dc1741b21ea108",
  "source_text_sha256": "29a6cdec043c0b740125962c8299eeabee29f26935ebd78598dc1741b21ea108"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00aeddc4(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c8dc68;
  param_2[1] = uVar1;
  return;
}

~~~
