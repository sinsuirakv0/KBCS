# 009aabfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009aabfc",
  "name": "FUN_009aabfc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f186d04f189122da7d25a079603a8eb6615764a0a9553e4293ebed469ab32dbd",
  "source_text_sha256": "f186d04f189122da7d25a079603a8eb6615764a0a9553e4293ebed469ab32dbd"
}
~~~

## 呼び出し元

- [009b5ba4](../009b5/009b5ba4.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 113 bytes

~~~c

void FUN_009aabfc(long param_1,undefined1 param_2)

{
  *(undefined1 *)(param_1 + 0x35) = param_2;
  return;
}

~~~
