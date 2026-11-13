# 00bfbd7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbd7c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8in_availEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5bd80a3bb8b6e28997a9860d15c2df43fb572034b1d8e02bebf23170bcf72b7",
  "source_text_sha256": "f5bd80a3bb8b6e28997a9860d15c2df43fb572034b1d8e02bebf23170bcf72b7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 417 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8in_availEv(long *param_1)

{
  long lVar1;
  
  if ((ulong)param_1[3] < (ulong)param_1[4]) {
    return param_1[4] - param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbd9c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  lVar1 = (**(code **)(*param_1 + 0x38))();
  return lVar1;
}

~~~
