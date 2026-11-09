# 009abafc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009abafc",
  "name": "FUN_009abafc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d12a6ad084c10b5618f702b0cb284312a77bc4fd2a5ce59faf58a527863a99a5",
  "source_text_sha256": "d12a6ad084c10b5618f702b0cb284312a77bc4fd2a5ce59faf58a527863a99a5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_009abafc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN7Ranking10updateRankERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_1"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
