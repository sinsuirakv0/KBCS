# 00bba3dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bba3dc",
  "name": "_ZNSt6__ndk111regex_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f12ebbdbdda6c13cb9a8bf4918e468c60221e0a02afa788337b649383b599b65",
  "source_text_sha256": "f12ebbdbdda6c13cb9a8bf4918e468c60221e0a02afa788337b649383b599b65"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdd920](../00bdd/00bdd920.md)

## 疑似コード / UTF-8 315 bytes

~~~c

void _ZNSt6__ndk111regex_errorD0Ev(void *param_1)

{
                    /* try { // try from 00bba3e8 to 00cba3eb has its CatchHandler @ 00bbad0c */
  _ZNSt6__ndk111regex_errorD1Ev();
                    /* try { // try from 00bba400 to 00cba403 has its CatchHandler @ 00bbacd8 */
  _ZdlPv(param_1);
  return;
}

~~~
