# 00bbaef4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbaef4",
  "name": "_ZNSt12out_of_rangeD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "746e92c5a788746dfe68eb99bec18041f680aaebb160a871bf2ad37adf5c2607",
  "source_text_sha256": "746e92c5a788746dfe68eb99bec18041f680aaebb160a871bf2ad37adf5c2607"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb150](../00bdb/00bdb150.md)

## 疑似コード / UTF-8 205 bytes

~~~c

void _ZNSt12out_of_rangeD0Ev(void *param_1)

{
                    /* try { // try from 00bbaf00 to 00cbaf13 has its CatchHandler @ 00bbb778 */
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
