# 00bbacc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbacc0",
  "name": "__cxa_pure_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85d08f10a64b2cedc1487154b603fe3620bc5830c317fc7dae07b37056e5a996",
  "source_text_sha256": "85d08f10a64b2cedc1487154b603fe3620bc5830c317fc7dae07b37056e5a996"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"Pure virtual function called!"
~~~

## 疑似コード / UTF-8 751 bytes

~~~c

void __cxa_pure_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb4ef0 with catch @ 00bbacc4 */
                    /* catch() { ... } // from try @ 00bb4b10 with catch @ 00bbacc8 */
                    /* catch() { ... } // from try @ 00bb4750 with catch @ 00bbaccc */
                    /* catch() { ... } // from try @ 00bba430 with catch @ 00bbacd0
                       catch() { ... } // from try @ 00bba478 with catch @ 00bbacd0 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bba418 with catch @ 00bbacd4
                       catch() { ... } // from try @ 00bba460 with catch @ 00bbacd4 */
  FUN_00bbb158("Pure virtual function called!");
}

~~~
