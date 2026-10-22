# 00bcebc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcebc4.md)

## 関数情報

~~~json
{
  "address": "00bcebc4",
  "name": "FUN_00bcebc4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "376c42d8b9052575a7072a0010bf3a63d4bf5dbd81b09953c1d04ba357ab981b",
  "source_text_sha256": "376c42d8b9052575a7072a0010bf3a63d4bf5dbd81b09953c1d04ba357ab981b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 276 bytes

~~~c

void FUN_00bcebc4(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcebd4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
