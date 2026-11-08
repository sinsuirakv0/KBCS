# 00bcff1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bcff1c",
  "name": "FUN_00bcff1c",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e7d03f2016c2f579dd9401fdcc188370db70221ddfea760d4aa9f5fa0631e3a0",
  "source_text_sha256": "e7d03f2016c2f579dd9401fdcc188370db70221ddfea760d4aa9f5fa0631e3a0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcff1c(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcff2c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
