# 00afa1cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afa1cc",
  "name": "FUN_00afa1cc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5d0fafeeed1fe2260e0255f682123f785da5cadfbac93526f41b5d220e02e15",
  "source_text_sha256": "e5d0fafeeed1fe2260e0255f682123f785da5cadfbac93526f41b5d220e02e15"
}
~~~

## 呼び出し元

- [00713d24](../00713/00713d24.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 280 bytes

~~~c

bool FUN_00afa1cc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00afa1e4 to 00bfa243 has its CatchHandler @ 00afab54 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad8) != 0;
}

~~~
