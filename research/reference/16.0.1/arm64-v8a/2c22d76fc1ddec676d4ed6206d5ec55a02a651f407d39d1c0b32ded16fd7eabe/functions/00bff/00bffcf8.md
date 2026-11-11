# 00bffcf8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bffcf8",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sputnEPKwl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8da7b1a7924e9e590e62ea5fe66b1ed6505ccd52d936e4fcc3c085b17dba5768",
  "source_text_sha256": "8da7b1a7924e9e590e62ea5fe66b1ed6505ccd52d936e4fcc3c085b17dba5768"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sputnEPKwl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bffd04. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x60))();
  return;
}

~~~
