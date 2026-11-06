# 00bcfb8c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bcfb8c",
  "name": "FUN_00bcfb8c",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e142f13826626bb4872480e1d36b5c7d26c009852be543e491b4bd786783731",
  "source_text_sha256": "3e142f13826626bb4872480e1d36b5c7d26c009852be543e491b4bd786783731"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcfb8c(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcfb9c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x10) + 0x30))();
  return;
}

~~~
