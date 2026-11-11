# 00bfbe8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbe8c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputnEPKcl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc14827d0d2311e68e31cb70aa5666e8bcb69a57575d694031c44c6375dee480",
  "source_text_sha256": "bc14827d0d2311e68e31cb70aa5666e8bcb69a57575d694031c44c6375dee480"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputnEPKcl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfbe98. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x60))();
  return;
}

~~~
