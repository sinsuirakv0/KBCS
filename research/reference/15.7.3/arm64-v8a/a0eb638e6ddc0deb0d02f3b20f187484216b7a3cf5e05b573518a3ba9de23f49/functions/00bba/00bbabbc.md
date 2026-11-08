# 00bbabbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbabbc",
  "name": "FUN_00bbabbc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a",
  "source_text_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~

## 疑似コード / UTF-8 426 bytes

~~~c

void FUN_00bbabbc(void)

{
                    /* catch() { ... } // from try @ 00bb7bb4 with catch @ 00bbabc0 */
                    /* catch() { ... } // from try @ 00bb3764 with catch @ 00bbabc4 */
                    /* catch() { ... } // from try @ 00bb3770 with catch @ 00bbabd4 */
  PTR_s_uncaught_00c24950 = s_unexpected_002a11af;
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
