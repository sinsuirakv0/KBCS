# 008accec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008accec",
  "name": "FUN_008accec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4655213f95f1cd91f1a227dd8c6c78437a5f4c38cc2bff31b3a33b1ec467edb",
  "source_text_sha256": "c4655213f95f1cd91f1a227dd8c6c78437a5f4c38cc2bff31b3a33b1ec467edb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 287 bytes

~~~c

long FUN_008accec(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN17MyUtilityListener22miniBrowserLinkClickedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_6"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
