# 00a8deec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
  "source_sha256": "b64781a261838bec6215e143ccf34f8b9c6540ace7319fb3c0565326ca86d17e",
  "source_text_sha256": "b64781a261838bec6215e143ccf34f8b9c6540ace7319fb3c0565326ca86d17e"
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
  *param_2 = &PTR_FUN_00c0e108;
  param_2[1] = uVar1;
  return;
}

~~~
