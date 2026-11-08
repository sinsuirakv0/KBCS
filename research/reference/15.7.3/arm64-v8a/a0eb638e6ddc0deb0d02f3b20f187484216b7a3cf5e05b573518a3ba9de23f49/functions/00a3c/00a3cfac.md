# 00a3cfac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a3cfac",
  "name": "FUN_00a3cfac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59aad4db65a1bc4e581e5a0221d6881045968126344f239a50da8d13f72b3664",
  "source_text_sha256": "59aad4db65a1bc4e581e5a0221d6881045968126344f239a50da8d13f72b3664"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a3cfac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0d578;
  param_2[1] = uVar1;
  return;
}

~~~
