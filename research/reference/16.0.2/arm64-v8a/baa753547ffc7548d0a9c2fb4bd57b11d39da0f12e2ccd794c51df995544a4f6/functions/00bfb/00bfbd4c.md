# 00bfbd4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbd4c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE10pubseekoffExNS_8ios_base7seekdirEj",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f81992cc2f22c2608c83bcd3a6200013fe6293e9a8d2cca5e14d0a50a6ef55",
  "source_text_sha256": "72f81992cc2f22c2608c83bcd3a6200013fe6293e9a8d2cca5e14d0a50a6ef55"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE10pubseekoffExNS_8ios_base7seekdirEj
               (long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfbd58. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x20))();
  return;
}

~~~
