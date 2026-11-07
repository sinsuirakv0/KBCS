# 00bbacfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbae08`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae08.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbacfc",
  "name": "_ZNSt20bad_array_new_lengthC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6196d8070b1d6bc29ba5e69f10645f5e8986372285e0e91f25b63e127945297f",
  "source_text_sha256": "6196d8070b1d6bc29ba5e69f10645f5e8986372285e0e91f25b63e127945297f"
}
~~~

## 呼び出し元

- [00bdb0e0](../00bdb/00bdb0e0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 575 bytes

~~~c

void _ZNSt20bad_array_new_lengthC1Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb4c88 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb4ca0 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb48c0 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bb48a8 with catch @ 00bbad0c */
  *param_1 = (long)(PTR__ZTVSt20bad_array_new_length_00c1bf20 + 0x10);
                    /* catch() { ... } // from try @ 00bb4500 with catch @ 00bbad10 */
  return;
}

~~~
