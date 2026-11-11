# 00bfbdd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbdd8",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetnEPcl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d05968f5992e03ace654a072bd050c23e346c34dc6767bc6791a31b2c7fb35c",
  "source_text_sha256": "9d05968f5992e03ace654a072bd050c23e346c34dc6767bc6791a31b2c7fb35c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 298 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetnEPcl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfbde4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x40))();
  return;
}

~~~
