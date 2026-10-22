# 00bcbdc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcbdc8.md)

## 関数情報

~~~json
{
  "address": "00bcbdc8",
  "name": "FUN_00bcbdc8",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cdc9b030229bc327c3089bb7b4eef3cd3f3224c571ddf5ab80ac6d7172489652",
  "source_text_sha256": "cdc9b030229bc327c3089bb7b4eef3cd3f3224c571ddf5ab80ac6d7172489652"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 276 bytes

~~~c

void FUN_00bcbdc8(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcbdd8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x10) + 0x28))();
  return;
}

~~~
