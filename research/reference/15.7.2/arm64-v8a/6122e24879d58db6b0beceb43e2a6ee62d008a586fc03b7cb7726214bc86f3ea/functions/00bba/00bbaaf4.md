# 00bbaaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbac00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbaaf4",
  "name": "FUN_00bbaaf4",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a159dcdd11055ae0967db7cbc007dc55007530ea348a3bafab8ca96881ebc2d",
  "source_text_sha256": "1a159dcdd11055ae0967db7cbc007dc55007530ea348a3bafab8ca96881ebc2d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~

## 疑似コード / UTF-8 426 bytes

~~~c

void FUN_00bbaaf4(void)

{
                    /* catch() { ... } // from try @ 00bb7aec with catch @ 00bbaaf8 */
                    /* catch() { ... } // from try @ 00bb369c with catch @ 00bbaafc */
                    /* catch() { ... } // from try @ 00bb36a8 with catch @ 00bbab0c */
  PTR_s_uncaught_00c248a0 = s_unexpected_002a1122;
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
