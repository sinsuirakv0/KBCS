# 008cfafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008cfafc",
  "name": "FUN_008cfafc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c95906e3a69de9781685d8465028be90a936b88cfe69c5d3e2f3d041796b55ff",
  "source_text_sha256": "c95906e3a69de9781685d8465028be90a936b88cfe69c5d3e2f3d041796b55ff"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 181 bytes

~~~c

long FUN_008cfafc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN9NyanCombo6updateEvE3$_2") {
    param_1 = 0;
  }
  return param_1;
}

~~~
