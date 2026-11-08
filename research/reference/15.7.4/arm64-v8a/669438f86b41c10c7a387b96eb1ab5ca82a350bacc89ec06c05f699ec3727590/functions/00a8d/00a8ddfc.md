# 00a8ddfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a8ddfc",
  "name": "FUN_00a8ddfc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15a8d33b173f9cf34fbad81e7490ce3a101dbdcb4196be5eb8a612e712125d4d",
  "source_text_sha256": "15a8d33b173f9cf34fbad81e7490ce3a101dbdcb4196be5eb8a612e712125d4d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 416 bytes

~~~c

void FUN_00a8ddfc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_2 = &PTR_FUN_00c0e0d8;
                    /* try { // try from 00a8de08 to 00b8de6f has its CatchHandler @ 00a8fbd4 */
  uVar2 = *(undefined8 *)(param_1 + 0x10);
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[3] = *(undefined8 *)(param_1 + 0x18);
  param_2[2] = uVar2;
  param_2[1] = uVar1;
  return;
}

~~~
