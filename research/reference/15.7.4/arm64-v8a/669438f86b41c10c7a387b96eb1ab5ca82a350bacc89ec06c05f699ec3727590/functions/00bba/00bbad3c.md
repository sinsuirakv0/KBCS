# 00bbad3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbad3c",
  "name": "_ZNSt9exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a69cc739bb19806e21f63ebb43917b0670c9bd383e65023cf9bccfee24461acd",
  "source_text_sha256": "a69cc739bb19806e21f63ebb43917b0670c9bd383e65023cf9bccfee24461acd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e40](../00be1/00be1e40.md)

## 疑似コード / UTF-8 1487 bytes

~~~c

void _ZNSt9exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb3a08 with catch @ 00bbad40 */
                    /* catch() { ... } // from try @ 00bb4204 with catch @ 00bbad44 */
                    /* catch() { ... } // from try @ 00bb3e18 with catch @ 00bbad48 */
                    /* catch() { ... } // from try @ 00bb39f8 with catch @ 00bbad4c */
                    /* catch() { ... } // from try @ 00bba2dc with catch @ 00bbad50
                       catch() { ... } // from try @ 00bba42c with catch @ 00bbad50 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bba2c4 with catch @ 00bbad54
                       catch() { ... } // from try @ 00bba414 with catch @ 00bbad54 */
                    /* catch() { ... } // from try @ 00bba2ac with catch @ 00bbad58
                       catch() { ... } // from try @ 00bba3fc with catch @ 00bbad58 */
                    /* catch() { ... } // from try @ 00bba294 with catch @ 00bbad5c
                       catch() { ... } // from try @ 00bba3e4 with catch @ 00bbad5c */
                    /* catch() { ... } // from try @ 00bba27c with catch @ 00bbad60
                       catch() { ... } // from try @ 00bba3cc with catch @ 00bbad60 */
                    /* catch() { ... } // from try @ 00bba264 with catch @ 00bbad64
                       catch() { ... } // from try @ 00bba3b4 with catch @ 00bbad64 */
  _ZdlPv(param_1);
  return;
}

~~~
