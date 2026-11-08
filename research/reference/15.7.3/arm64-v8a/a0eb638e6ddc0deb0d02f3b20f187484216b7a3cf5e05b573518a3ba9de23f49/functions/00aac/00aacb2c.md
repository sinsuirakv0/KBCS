# 00aacb2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aacb2c",
  "name": "FUN_00aacb2c",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "206d3b5fbaf79bb2a75305980311706026c5b8fa38b49a8777fcb8b54550dc46",
  "source_text_sha256": "206d3b5fbaf79bb2a75305980311706026c5b8fa38b49a8777fcb8b54550dc46"
}
~~~

## 呼び出し元

- [00aac920](../00aac/00aac920.md)
- [00aacb54](../00aac/00aacb54.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00aacb2c(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
