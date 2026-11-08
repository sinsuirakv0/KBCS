# 008edbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "008edbbc",
  "name": "FUN_008edbbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53904541a516b4ee9a7f128d3bbe6c52ae1b011c763ec3648c1e30e892d78ec9",
  "source_text_sha256": "53904541a516b4ee9a7f128d3bbe6c52ae1b011c763ec3648c1e30e892d78ec9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 198 bytes

~~~c

long FUN_008edbbc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication17NyankogatyaUpdateEvE3$_6") {
    param_1 = 0;
  }
  return param_1;
}

~~~
