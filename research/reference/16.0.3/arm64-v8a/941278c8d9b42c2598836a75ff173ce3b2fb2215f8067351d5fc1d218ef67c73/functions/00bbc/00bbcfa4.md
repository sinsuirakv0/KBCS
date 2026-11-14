# 00bbcfa4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbcfa4",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69756d9228dc769cb36488bb4f810b262950e33dc635b50a27cfce17f69b34d1",
  "source_text_sha256": "69756d9228dc769cb36488bb4f810b262950e33dc635b50a27cfce17f69b34d1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497da8](../00497/00497da8.md)
- [00c5c120](../00c5c/00c5c120.md)

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01127420 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbcfc0 to 00cbcfe3 has its CatchHandler @ 00bbd7fc */
    cVar1 = FUN_00497da8(uVar2,DAT_01127458,DAT_011273a0);
    return cVar1 != '\0';
  }
  return DAT_011274c4 == 1;
}

~~~
