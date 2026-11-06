# 00a1fddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00a1fddc",
  "name": "FUN_00a1fddc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30f2ec12622c65ed11ff02045166c03203e203384f489be57fb3f3e5f1eac526",
  "source_text_sha256": "30f2ec12622c65ed11ff02045166c03203e203384f489be57fb3f3e5f1eac526"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a1fddc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0c300;
  param_2[1] = uVar1;
  return;
}

~~~
