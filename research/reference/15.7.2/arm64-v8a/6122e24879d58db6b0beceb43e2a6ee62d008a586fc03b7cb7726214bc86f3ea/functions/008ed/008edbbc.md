# 008edbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](008edbbc.md)

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
  "source_sha256": "29ca4c9ecc3c2207fca528487b420d5f30a99a3b9ba85e60a9425093f83f748f",
  "source_text_sha256": "29ca4c9ecc3c2207fca528487b420d5f30a99a3b9ba85e60a9425093f83f748f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 209 bytes

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
