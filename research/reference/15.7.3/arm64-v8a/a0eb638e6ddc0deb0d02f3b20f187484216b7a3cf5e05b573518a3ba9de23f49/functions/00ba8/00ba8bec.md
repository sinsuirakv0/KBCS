# 00ba8bec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ba8bec",
  "name": "_ZNSt6__ndk114collate_bynameIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58a48254c836d1a87cb5c7aa54127d6313063da449632fac2646ee3dd1f4357e",
  "source_text_sha256": "58a48254c836d1a87cb5c7aa54127d6313063da449632fac2646ee3dd1f4357e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00be18f0](../00be1/00be18f0.md)

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIcED0Ev(void *param_1)

{
                    /* try { // try from 00ba8bf0 to 00ca8bf7 has its CatchHandler @ 00ba8d48 */
  _ZNSt6__ndk114collate_bynameIcED1Ev();
                    /* try { // try from 00ba8c0c to 00ca8c13 has its CatchHandler @ 00ba8db0 */
  _ZdlPv(param_1);
  return;
}

~~~
