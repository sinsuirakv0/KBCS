# 00bbacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbacd8",
  "name": "__cxa_deleted_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71",
  "source_text_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"Deleted virtual function called!"
~~~

## 疑似コード / UTF-8 589 bytes

~~~c

void __cxa_deleted_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb42d4 with catch @ 00bbacdc */
                    /* catch() { ... } // from try @ 00bb3ee8 with catch @ 00bbace0 */
                    /* catch() { ... } // from try @ 00bb3ac8 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb41e8 with catch @ 00bbace8 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb41d0 with catch @ 00bbacec */
  FUN_00bbb158("Deleted virtual function called!");
}

~~~
