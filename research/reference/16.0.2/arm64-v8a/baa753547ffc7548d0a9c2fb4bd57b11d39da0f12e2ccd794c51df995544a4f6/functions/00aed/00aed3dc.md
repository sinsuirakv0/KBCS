# 00aed3dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aed3dc",
  "name": "FUN_00aed3dc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e",
  "source_text_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 383 bytes

~~~c

long FUN_00aed3dc(long param_1,long param_2)

{
                    /* try { // try from 00aed3e8 to 00bed3f3 has its CatchHandler @ 00aed5a4 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9pasteSlotEvE3$_0") {
    param_1 = 0;
  }
                    /* try { // try from 00aed3f4 to 00bed58b has its CatchHandler @ 00aed16c */
  return param_1;
}

~~~
