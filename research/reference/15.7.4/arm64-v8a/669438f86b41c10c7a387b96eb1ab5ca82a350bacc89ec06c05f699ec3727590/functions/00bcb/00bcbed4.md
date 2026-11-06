# 00bcbed4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bcbed4",
  "name": "FUN_00bcbed4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82055a56c880bafcd1205b1203c83d25fa8682db8c5a7bff04a16c826e40d68e",
  "source_text_sha256": "82055a56c880bafcd1205b1203c83d25fa8682db8c5a7bff04a16c826e40d68e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcbed4(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcbee4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x10) + 0x28))();
  return;
}

~~~
