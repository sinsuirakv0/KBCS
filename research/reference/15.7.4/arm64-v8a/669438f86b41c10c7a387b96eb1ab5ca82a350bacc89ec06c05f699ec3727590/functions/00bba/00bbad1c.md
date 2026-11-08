# 00bbad1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbad1c",
  "name": "__cxa_deleted_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03a8ad0217ce692ad18acc6d177bb77bf95dbb6dbd995d3d3a721ebc429a2fe6",
  "source_text_sha256": "03a8ad0217ce692ad18acc6d177bb77bf95dbb6dbd995d3d3a721ebc429a2fe6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)

## 関連文字列（未確認候補）

~~~text
"Deleted virtual function called!"
~~~

## 疑似コード / UTF-8 589 bytes

~~~c

void __cxa_deleted_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb4318 with catch @ 00bbad20 */
                    /* catch() { ... } // from try @ 00bb3f2c with catch @ 00bbad24 */
                    /* catch() { ... } // from try @ 00bb3b0c with catch @ 00bbad28 */
                    /* catch() { ... } // from try @ 00bb422c with catch @ 00bbad2c */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb4214 with catch @ 00bbad30 */
  FUN_00bbb19c("Deleted virtual function called!");
}

~~~
