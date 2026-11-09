# 00bbbaec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbbaec",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "673aef6f204e3647f264f76847b124ddede33a10b6be028dfd2fe297bc3e52ba",
  "source_text_sha256": "673aef6f204e3647f264f76847b124ddede33a10b6be028dfd2fe297bc3e52ba"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a08](../00497/00497a08.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01125f60 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
    cVar1 = FUN_00497a08(uVar2,DAT_01125f98,DAT_01125ee0);
                    /* try { // try from 00bbbb24 to 00cbbb2f has its CatchHandler @ 00bbc5b4 */
    return cVar1 != '\0';
  }
  return DAT_01126004 == 1;
}

~~~
