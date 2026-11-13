# 00c4bbdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00c4bbdc",
  "name": "FUN_00c4bbdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6cb49a149e6f936581ac912c35a5f7ae1ac0269da7f4b0330c9e2cdf3bbbf6e",
  "source_text_sha256": "d6cb49a149e6f936581ac912c35a5f7ae1ac0269da7f4b0330c9e2cdf3bbbf6e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00c4bbdc(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00c4bbec. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~
