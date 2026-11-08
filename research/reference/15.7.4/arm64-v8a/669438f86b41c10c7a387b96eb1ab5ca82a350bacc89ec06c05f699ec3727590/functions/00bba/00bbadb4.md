# 00bbadb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbadb4",
  "name": "_ZNSt9bad_allocC2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125",
  "source_text_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125"
}
~~~

## 呼び出し元

- [00bdbbf0](../00bdb/00bdbbf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 551 bytes

~~~c

void _ZNSt9bad_allocC2Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb46f8 with catch @ 00bbadb8 */
                    /* catch() { ... } // from try @ 00bb76a0 with catch @ 00bbadbc */
                    /* catch() { ... } // from try @ 00bb76b8 with catch @ 00bbadc0 */
                    /* catch() { ... } // from try @ 00bb72f0 with catch @ 00bbadc4 */
  *param_1 = (long)(PTR__ZTVSt9bad_alloc_00c1c018 + 0x10);
                    /* catch() { ... } // from try @ 00bb7308 with catch @ 00bbadc8 */
  return;
}

~~~
