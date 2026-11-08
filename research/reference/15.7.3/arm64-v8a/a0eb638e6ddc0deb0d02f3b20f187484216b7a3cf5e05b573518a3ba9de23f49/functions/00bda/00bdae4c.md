# 00bdae4c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdae4c",
  "name": "FUN_00bdae4c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02d84d4528358711282c5873d2b61d8cafdcf15a664d5291d1dfa1f09806fd05",
  "source_text_sha256": "02d84d4528358711282c5873d2b61d8cafdcf15a664d5291d1dfa1f09806fd05"
}
~~~

## 呼び出し元

- [009613bc](../00961/009613bc.md)

## 呼び出し先

- [00963004](../00963/00963004.md)

## 疑似コード / UTF-8 146 bytes

~~~c

void FUN_00bdae4c(void)

{
                    /* catch() { ... } // from try @ 00bdadbc with catch @ 00bdae4c */
  FUN_00963004();
  return;
}

~~~
