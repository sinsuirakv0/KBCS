# 007fafec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `007fafec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fafec.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "007fafec",
  "name": "FUN_007fafec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494",
  "source_text_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494"
}
~~~

## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)

## 呼び出し先

- [007faff8](../007fa/007faff8.md)

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007fafec(long param_1)

{
                    /* catch() { ... } // from try @ 007fa778 with catch @ 007faff0 */
  FUN_007faff8(param_1 + 0x18);
  return;
}

~~~
