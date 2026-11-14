# 00bbcff8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbcff8",
  "name": "_ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28da93111c5b057f822badcea7f6e619a4e3f224a9e7924d2a3ee3bcd188b6ba",
  "source_text_sha256": "28da93111c5b057f822badcea7f6e619a4e3f224a9e7924d2a3ee3bcd188b6ba"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0057504c](../00575/0057504c.md)
- [00c5c120](../00c5c/00c5c120.md)

## 疑似コード / UTF-8 454 bytes

~~~c

void _ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb(uint param_1)

{
  undefined8 uVar1;
  
  if (DAT_01127420 != 0) {
                    /* try { // try from 00bbd014 to 00cbd01f has its CatchHandler @ 00bbd7dc */
    uVar1 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01127420);
    FUN_0057504c(uVar1,DAT_01127458,DAT_011273a8,param_1 & 1);
    return;
  }
  DAT_011274c4 = 1;
  if ((param_1 & 1) == 0) {
    DAT_011274c4 = 2;
  }
  return;
}

~~~
