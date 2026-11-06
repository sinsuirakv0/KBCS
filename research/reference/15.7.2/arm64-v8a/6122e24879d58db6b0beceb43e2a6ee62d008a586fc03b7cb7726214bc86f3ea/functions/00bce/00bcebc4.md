# 00bcebc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "a5a1c7ed12050325e03e0594e8427b75bafa679bc224336cad4f7a85a61963cd",
  "source_text_sha256": "a5a1c7ed12050325e03e0594e8427b75bafa679bc224336cad4f7a85a61963cd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcebc4(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcebd4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
