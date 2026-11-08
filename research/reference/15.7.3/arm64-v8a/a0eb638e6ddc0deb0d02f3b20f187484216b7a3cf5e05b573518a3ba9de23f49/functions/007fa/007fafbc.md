# 007fafbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "007fafbc",
  "name": "FUN_007fafbc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95a7e4cab9731fd3a3d2a975cd69432dfcd7afdc89c3016c32d561d438fc1332",
  "source_text_sha256": "95a7e4cab9731fd3a3d2a975cd69432dfcd7afdc89c3016c32d561d438fc1332"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb000](../00bdb/00bdb000.md)
- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 592 bytes

~~~c

void FUN_007fafbc(undefined8 *param_1)

{
                    /* catch() { ... } // from try @ 007fae88 with catch @ 007fafc8
                       try { // try from 007fafc8 to 008fb12f has its CatchHandler @ 007fa6b0 */
                    /* catch() { ... } // from try @ 007fa800 with catch @ 007fafcc */
                    /* catch() { ... } // from try @ 007fa790 with catch @ 007fafd0 */
  *param_1 = &PTR_FUN_00c003f8;
  _ZNSt6__ndk119__shared_weak_countD2Ev();
                    /* catch() { ... } // from try @ 007fa784 with catch @ 007fafe0 */
  _ZdlPv(param_1);
  return;
}

~~~
