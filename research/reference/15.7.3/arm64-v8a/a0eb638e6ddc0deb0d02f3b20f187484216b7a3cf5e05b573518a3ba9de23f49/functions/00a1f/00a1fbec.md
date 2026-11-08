# 00a1fbec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a1fbec",
  "name": "FUN_00a1fbec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b954bab20b24cb32410c4ed4a1000f66395e9b14d8911500dbcd8118defc3c5e",
  "source_text_sha256": "b954bab20b24cb32410c4ed4a1000f66395e9b14d8911500dbcd8118defc3c5e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a1fbec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0c2b0;
  param_2[1] = uVar1;
  return;
}

~~~
