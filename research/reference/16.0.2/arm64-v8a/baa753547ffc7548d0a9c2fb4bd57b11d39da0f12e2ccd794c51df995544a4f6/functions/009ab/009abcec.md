# 009abcec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009abcec",
  "name": "FUN_009abcec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23e60a90b4f1c6a0620d6ab62a39833dac20885dd24e7ecd3e33eb733d25058e",
  "source_text_sha256": "23e60a90b4f1c6a0620d6ab62a39833dac20885dd24e7ecd3e33eb733d25058e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_009abcec(long param_1,long param_2)

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
