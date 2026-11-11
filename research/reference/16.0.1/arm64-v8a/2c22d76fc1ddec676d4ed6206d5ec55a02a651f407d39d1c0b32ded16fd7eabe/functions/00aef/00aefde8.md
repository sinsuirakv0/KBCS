# 00aefde8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aefde8",
  "name": "FUN_00aefde8",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c93dae53c3dd045951cc8e5da7424abc04170af9ba2cb43c34e76f36ba9fd77",
  "source_text_sha256": "9c93dae53c3dd045951cc8e5da7424abc04170af9ba2cb43c34e76f36ba9fd77"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 614 bytes

~~~c

long FUN_00aefde8(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 00aeff9c with catch @ 00aefde8
                       catch() { ... } // from try @ 00af00cc with catch @ 00aefde8
                       catch() { ... } // from try @ 00af0280 with catch @ 00aefde8
                       catch() { ... } // from try @ 00af0434 with catch @ 00aefde8 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlP9NewDialogP9aGraphicsE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
