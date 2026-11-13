# 00bbbfb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbbfb0",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc",
  "source_text_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a88](../00497/00497a88.md)
- [00c5b150](../00c5b/00c5b150.md)

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01126460 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbbfcc to 00cbbfef has its CatchHandler @ 00bbc808 */
    cVar1 = FUN_00497a88(uVar2,DAT_01126498,DAT_011263e0);
    return cVar1 != '\0';
  }
  return DAT_01126504 == 1;
}

~~~
