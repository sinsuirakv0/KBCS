# 00c4cbfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c4cbfc",
  "name": "FUN_00c4cbfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc5976c288f855237a67e94e4c843ec65499c8dfde61534d399a68b025e561de",
  "source_text_sha256": "cc5976c288f855237a67e94e4c843ec65499c8dfde61534d399a68b025e561de"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00c4cbfc(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00c4cc0c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
