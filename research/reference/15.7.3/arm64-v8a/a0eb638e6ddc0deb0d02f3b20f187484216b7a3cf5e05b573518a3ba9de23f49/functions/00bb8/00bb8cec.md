# 00bb8cec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bb8cec",
  "name": "FUN_00bb8cec",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a763abbc6370dd054dbdf3fa2c7c945efe8a3cd03ef2ff880fc3f59f0f1fdfd",
  "source_text_sha256": "5a763abbc6370dd054dbdf3fa2c7c945efe8a3cd03ef2ff880fc3f59f0f1fdfd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1127 bytes

~~~c

void FUN_00bb8cec(void)

{
  if ((DAT_010a2d98 & 1) != 0) {
    _ZdlPv(DAT_010a2da8);
  }
  if ((DAT_010a2d80 & 1) != 0) {
    _ZdlPv(DAT_010a2d90);
  }
  if ((DAT_010a2d68 & 1) != 0) {
    _ZdlPv(DAT_010a2d78);
  }
  if ((DAT_010a2d50 & 1) != 0) {
    _ZdlPv(DAT_010a2d60);
  }
  if ((DAT_010a2d38 & 1) != 0) {
    _ZdlPv(DAT_010a2d48);
  }
  if ((DAT_010a2d20 & 1) != 0) {
                    /* try { // try from 00bb8d80 to 00cb8e57 has its CatchHandler @ 00bb3400 */
    _ZdlPv(DAT_010a2d30);
  }
  if ((DAT_010a2d08 & 1) != 0) {
    _ZdlPv(DAT_010a2d18);
  }
  if ((DAT_010a2cf0 & 1) != 0) {
    _ZdlPv(DAT_010a2d00);
  }
  if ((DAT_010a2cd8 & 1) != 0) {
    _ZdlPv(DAT_010a2ce8);
  }
  if ((DAT_010a2cc0 & 1) != 0) {
    _ZdlPv(DAT_010a2cd0);
  }
  if ((DAT_010a2ca8 & 1) != 0) {
    _ZdlPv(DAT_010a2cb8);
  }
  if ((DAT_010a2c90 & 1) != 0) {
    _ZdlPv(DAT_010a2ca0);
  }
  if ((DAT_010a2c78 & 1) != 0) {
    _ZdlPv(DAT_010a2c88);
  }
  if ((DAT_010a2c60 & 1) == 0) {
    return;
  }
                    /* try { // try from 00bb8e58 to 00cb8e5f has its CatchHandler @ 00bbac98 */
  _ZdlPv(DAT_010a2c70);
  return;
}

~~~
