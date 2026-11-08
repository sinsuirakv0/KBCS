# 009dcecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d",
  "source_text_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d"
}
~~~

## 呼び出し元

- [009dcca0](../009dc/009dcca0.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 206 bytes

~~~c

void FUN_009dcecc(void)

{
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 009d9d58 with catch @ 009dcedc */
  FUN_00418c38("vector");
}

~~~
