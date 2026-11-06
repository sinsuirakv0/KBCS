# 00bcecd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bcecd0",
  "name": "FUN_00bcecd0",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b72cf1868abfd5ee791525ebc5a396962c2da99d3cd6f1dbeadbc26ee11c0f70",
  "source_text_sha256": "b72cf1868abfd5ee791525ebc5a396962c2da99d3cd6f1dbeadbc26ee11c0f70"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcecd0(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcece0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
