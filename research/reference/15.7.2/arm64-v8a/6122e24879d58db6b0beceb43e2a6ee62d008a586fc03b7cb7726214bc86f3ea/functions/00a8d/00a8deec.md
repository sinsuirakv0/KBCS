# 00a8deec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00a8deec",
  "name": "FUN_00a8deec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88190a846c3657b850d775ae74a32c1a2bd8f9052b960048555e8737c9d23530",
  "source_text_sha256": "88190a846c3657b850d775ae74a32c1a2bd8f9052b960048555e8737c9d23530"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_00a8deec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a8def4 to 00b8defb has its CatchHandler @ 00a8fafc */
  *param_2 = &PTR_FUN_00c0e058;
  param_2[1] = uVar1;
  return;
}

~~~
