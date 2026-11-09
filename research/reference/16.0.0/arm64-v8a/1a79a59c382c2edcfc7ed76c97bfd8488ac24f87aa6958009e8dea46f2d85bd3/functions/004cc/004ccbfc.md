# 004ccbfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004ccbfc",
  "name": "FUN_004ccbfc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8b386ad60c7f7546b5eb0182565aa8c7da7dcb4f1e5358965cb4772a0bae476",
  "source_text_sha256": "b8b386ad60c7f7546b5eb0182565aa8c7da7dcb4f1e5358965cb4772a0bae476"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 263 bytes

~~~c

void FUN_004ccbfc(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x004ccc08. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)**(undefined8 **)(param_1 + 0x10))();
  return;
}

~~~
