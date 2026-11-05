# 007fafbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007fafbc.md)

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
  "source_sha256": "e0ee84082b6242dc758203bc563b24808ef5bbd7554ebac142055c4d519511ac",
  "source_text_sha256": "e0ee84082b6242dc758203bc563b24808ef5bbd7554ebac142055c4d519511ac"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf50](../00bda/00bdaf50.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 592 bytes

~~~c

void FUN_007fafbc(undefined8 *param_1)

{
                    /* catch() { ... } // from try @ 007fae88 with catch @ 007fafc8
                       try { // try from 007fafc8 to 008fb12f has its CatchHandler @ 007fa6b0 */
                    /* catch() { ... } // from try @ 007fa800 with catch @ 007fafcc */
                    /* catch() { ... } // from try @ 007fa790 with catch @ 007fafd0 */
  *param_1 = &PTR_FUN_00c00348;
  _ZNSt6__ndk119__shared_weak_countD2Ev();
                    /* catch() { ... } // from try @ 007fa784 with catch @ 007fafe0 */
  _ZdlPv(param_1);
  return;
}

~~~
