# 00bfbeec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbeec",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8351987cf9ec4dbc7882cd9bdc1ac156b432fe42887cc4c2e3725d58919a203b",
  "source_text_sha256": "8351987cf9ec4dbc7882cd9bdc1ac156b432fe42887cc4c2e3725d58919a203b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 533 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sputcEc(long *param_1,byte param_2)

{
  byte *pbVar1;
  ulong uVar2;
  
  pbVar1 = (byte *)param_1[6];
  if (pbVar1 != (byte *)param_1[7]) {
    param_1[6] = (long)(pbVar1 + 1);
    *pbVar1 = param_2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbf24. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x68))(param_1,param_2);
  return uVar2;
}

~~~
