# 00aefabc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aefabc",
  "name": "FUN_00aefabc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38dc9e03e2e3cb25486fc0f5d15b51bd8c05d89cb8f42bc03efb7a4fa45076a1",
  "source_text_sha256": "38dc9e03e2e3cb25486fc0f5d15b51bd8c05d89cb8f42bc03efb7a4fa45076a1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_00aefabc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00aefac8 to 00befacf has its CatchHandler @ 00aefdac */
  *param_2 = &PTR_FUN_00c8e168;
  param_2[1] = uVar1;
  return;
}

~~~
