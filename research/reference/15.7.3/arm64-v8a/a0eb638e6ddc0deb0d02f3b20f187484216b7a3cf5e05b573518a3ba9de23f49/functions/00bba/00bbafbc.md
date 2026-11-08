# 00bbafbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbafbc",
  "name": "_ZNSt12out_of_rangeD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "595813dfd06b7b691e9da135fa51997e37e13bd0b2e5738f89fa7647d52d9dea",
  "source_text_sha256": "595813dfd06b7b691e9da135fa51997e37e13bd0b2e5738f89fa7647d52d9dea"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb200](../00bdb/00bdb200.md)

## 疑似コード / UTF-8 205 bytes

~~~c

void _ZNSt12out_of_rangeD0Ev(void *param_1)

{
                    /* try { // try from 00bbafc8 to 00cbafdb has its CatchHandler @ 00bbb840 */
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
